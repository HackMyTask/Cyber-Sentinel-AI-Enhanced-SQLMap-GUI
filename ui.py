"""
Main UI Module - Dark Luxury Interface
Built with CustomTkinter for modern aesthetics
"""

import customtkinter as ctk
from tkinter import scrolledtext
import threading
from typing import Optional

from config import COLORS, UI_SETTINGS, SQLMAP_SETTINGS, AI_SETTINGS, AI_MODELS
from logic import SQLMapWrapper
from ai_analyzer import AIAnalyzer


class CyberSentinelUI:
    """Main GUI Application"""
    
    def __init__(self):
        """Initialize the UI"""
        # Set appearance mode and color theme
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("blue")
        
        # Create main window
        self.root = ctk.CTk()
        self.root.title(UI_SETTINGS['window_title'])
        self.root.geometry(UI_SETTINGS['window_size'])
        self.root.configure(fg_color=COLORS['bg_primary'])
        
        # Initialize components
        self.sqlmap = SQLMapWrapper(self.append_output)
        self.ai_analyzer = AIAnalyzer(provider=AI_SETTINGS['provider'])
        
        # Build UI
        self._build_ui()
        
    def _build_ui(self):
        """Build the complete UI"""
        # Main container with padding
        main_container = ctk.CTkFrame(self.root, fg_color=COLORS['bg_primary'])
        main_container.pack(fill='both', expand=True, padx=10, pady=10)
        
        # Header
        self._build_header(main_container)
        
        # Content area (split into left and right)
        content_frame = ctk.CTkFrame(main_container, fg_color=COLORS['bg_primary'])
        content_frame.pack(fill='both', expand=True, pady=(10, 0))
        
        # Left panel (Configuration + Terminal)
        left_panel = ctk.CTkFrame(content_frame, fg_color=COLORS['bg_primary'])
        left_panel.pack(side='left', fill='both', expand=True, padx=(0, 5))
        
        self._build_config_panel(left_panel)
        self._build_terminal(left_panel)
        
        # Right panel (AI Insights)
        right_panel = ctk.CTkFrame(content_frame, fg_color=COLORS['bg_primary'], width=400)
        right_panel.pack(side='right', fill='both', padx=(5, 0))
        right_panel.pack_propagate(False)
        
        self._build_ai_panel(right_panel)
        
    def _build_header(self, parent):
        """Build header section"""
        header = ctk.CTkFrame(parent, fg_color=COLORS['bg_secondary'], 
                             corner_radius=UI_SETTINGS['corner_radius'],
                             border_width=2, border_color=COLORS['border'])
        header.pack(fill='x', pady=(0, 10))
        
        # Title with gradient effect (simulated with colors)
        title_label = ctk.CTkLabel(
            header,
            text="⚡ CYBER-SENTINEL",
            font=(UI_SETTINGS['font_family'], 24, 'bold'),
            text_color=COLORS['accent_cyan']
        )
        title_label.pack(side='left', padx=20, pady=15)
        
        subtitle_label = ctk.CTkLabel(
            header,
            text="AI-Enhanced SQLMap Interface",
            font=(UI_SETTINGS['font_family'], 12),
            text_color=COLORS['text_secondary']
        )
        subtitle_label.pack(side='left', padx=(0, 20), pady=15)
        
        # Status indicator
        self.status_label = ctk.CTkLabel(
            header,
            text="● READY",
            font=(UI_SETTINGS['font_family'], 12, 'bold'),
            text_color=COLORS['success']
        )
        self.status_label.pack(side='right', padx=20, pady=15)
        
    def _build_config_panel(self, parent):
        """Build configuration panel"""
        config_frame = ctk.CTkFrame(parent, fg_color=COLORS['bg_secondary'],
                                   corner_radius=UI_SETTINGS['corner_radius'],
                                   border_width=2, border_color=COLORS['border'])
        config_frame.pack(fill='x', pady=(0, 10))
        
        # Title
        title = ctk.CTkLabel(
            config_frame,
            text="🎯 SCAN CONFIGURATION",
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_header'], 'bold'),
            text_color=COLORS['accent_gold']
        )
        title.pack(pady=(15, 10), padx=15, anchor='w')
        
        # Target URL with file selector
        url_frame = ctk.CTkFrame(config_frame, fg_color='transparent')
        url_frame.pack(fill='x', padx=15, pady=5)
        
        url_label_frame = ctk.CTkFrame(url_frame, fg_color='transparent')
        url_label_frame.pack(fill='x')
        
        ctk.CTkLabel(url_label_frame, text="Target URL:", 
                    font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal']),
                    text_color=COLORS['text_primary']).pack(side='left')
        
        ctk.CTkLabel(url_label_frame, text="(or .txt file for multiple targets)", 
                    font=(UI_SETTINGS['font_family'], 9),
                    text_color=COLORS['text_secondary']).pack(side='left', padx=(5, 0))
        
        url_input_frame = ctk.CTkFrame(url_frame, fg_color='transparent')
        url_input_frame.pack(fill='x', pady=(5, 0))
        
        self.url_entry = ctk.CTkEntry(
            url_input_frame,
            placeholder_text="https://example.com/page?id=1 or C:\\targets.txt",
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal']),
            fg_color=COLORS['bg_tertiary'],
            border_color=COLORS['accent_cyan'],
            border_width=2,
            corner_radius=UI_SETTINGS['corner_radius']
        )
        self.url_entry.pack(side='left', fill='x', expand=True, padx=(0, 5))
        
        self.browse_targets_btn = ctk.CTkButton(
            url_input_frame,
            text="📁",
            command=self.browse_targets,
            width=40,
            font=(UI_SETTINGS['font_family'], 14),
            fg_color=COLORS['bg_tertiary'],
            hover_color=COLORS['accent_cyan'],
            corner_radius=UI_SETTINGS['corner_radius']
        )
        self.browse_targets_btn.pack(side='left')
        
        # Options row
        options_frame = ctk.CTkFrame(config_frame, fg_color='transparent')
        options_frame.pack(fill='x', padx=15, pady=10)
        
        # Risk
        risk_frame = ctk.CTkFrame(options_frame, fg_color='transparent')
        risk_frame.pack(side='left', expand=True, fill='x', padx=(0, 5))
        
        ctk.CTkLabel(risk_frame, text="Risk Level:",
                    font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal']),
                    text_color=COLORS['text_primary']).pack(anchor='w')
        
        self.risk_var = ctk.StringVar(value="1")
        self.risk_menu = ctk.CTkOptionMenu(
            risk_frame,
            values=["1", "2", "3"],
            variable=self.risk_var,
            fg_color=COLORS['bg_tertiary'],
            button_color=COLORS['accent_cyan'],
            button_hover_color=COLORS['accent_gold'],
            corner_radius=UI_SETTINGS['corner_radius']
        )
        self.risk_menu.pack(fill='x', pady=(5, 0))
        
        # Level
        level_frame = ctk.CTkFrame(options_frame, fg_color='transparent')
        level_frame.pack(side='left', expand=True, fill='x', padx=5)
        
        ctk.CTkLabel(level_frame, text="Level:",
                    font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal']),
                    text_color=COLORS['text_primary']).pack(anchor='w')
        
        self.level_var = ctk.StringVar(value="1")
        self.level_menu = ctk.CTkOptionMenu(
            level_frame,
            values=["1", "2", "3", "4", "5"],
            variable=self.level_var,
            fg_color=COLORS['bg_tertiary'],
            button_color=COLORS['accent_cyan'],
            button_hover_color=COLORS['accent_gold'],
            corner_radius=UI_SETTINGS['corner_radius']
        )
        self.level_menu.pack(fill='x', pady=(5, 0))
        
        # Tamper
        tamper_frame = ctk.CTkFrame(options_frame, fg_color='transparent')
        tamper_frame.pack(side='left', expand=True, fill='x', padx=(5, 0))
        
        ctk.CTkLabel(tamper_frame, text="Tamper Script:",
                    font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal']),
                    text_color=COLORS['text_primary']).pack(anchor='w')
        
        self.tamper_var = ctk.StringVar(value="None")
        self.tamper_menu = ctk.CTkOptionMenu(
            tamper_frame,
            values=SQLMAP_SETTINGS['tamper_scripts'],
            variable=self.tamper_var,
            fg_color=COLORS['bg_tertiary'],
            button_color=COLORS['accent_cyan'],
            button_hover_color=COLORS['accent_gold'],
            corner_radius=UI_SETTINGS['corner_radius']
        )
        self.tamper_menu.pack(fill='x', pady=(5, 0))
        
        # Toggles
        toggles_frame = ctk.CTkFrame(config_frame, fg_color='transparent')
        toggles_frame.pack(fill='x', padx=15, pady=5)
        
        self.random_agent_var = ctk.BooleanVar(value=True)
        self.random_agent_check = ctk.CTkCheckBox(
            toggles_frame,
            text="Random User-Agent",
            variable=self.random_agent_var,
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal']),
            fg_color=COLORS['accent_cyan'],
            hover_color=COLORS['accent_gold'],
            corner_radius=UI_SETTINGS['corner_radius']
        )
        self.random_agent_check.pack(side='left', padx=(0, 15))
        
        self.batch_var = ctk.BooleanVar(value=True)
        self.batch_check = ctk.CTkCheckBox(
            toggles_frame,
            text="Batch Mode (No Prompts)",
            variable=self.batch_var,
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal']),
            fg_color=COLORS['accent_cyan'],
            hover_color=COLORS['accent_gold'],
            corner_radius=UI_SETTINGS['corner_radius']
        )
        self.batch_check.pack(side='left')
        
        # Proxy configuration
        proxy_frame = ctk.CTkFrame(config_frame, fg_color='transparent')
        proxy_frame.pack(fill='x', padx=15, pady=5)
        
        proxy_label_frame = ctk.CTkFrame(proxy_frame, fg_color='transparent')
        proxy_label_frame.pack(fill='x')
        
        ctk.CTkLabel(proxy_label_frame, text="Proxy (Optional):", 
                    font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal']),
                    text_color=COLORS['text_primary']).pack(side='left')
        
        ctk.CTkLabel(proxy_label_frame, text="(or .txt file for multiple proxies)", 
                    font=(UI_SETTINGS['font_family'], 9),
                    text_color=COLORS['text_secondary']).pack(side='left', padx=(5, 0))
        
        proxy_input_frame = ctk.CTkFrame(proxy_frame, fg_color='transparent')
        proxy_input_frame.pack(fill='x', pady=(5, 0))
        
        self.proxy_entry = ctk.CTkEntry(
            proxy_input_frame,
            placeholder_text="http://127.0.0.1:8080 or C:\\proxies.txt",
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal']),
            fg_color=COLORS['bg_tertiary'],
            border_color=COLORS['accent_cyan'],
            border_width=2,
            corner_radius=UI_SETTINGS['corner_radius']
        )
        self.proxy_entry.pack(side='left', fill='x', expand=True, padx=(0, 5))
        
        self.browse_proxies_btn = ctk.CTkButton(
            proxy_input_frame,
            text="📁",
            command=self.browse_proxies,
            width=40,
            font=(UI_SETTINGS['font_family'], 14),
            fg_color=COLORS['bg_tertiary'],
            hover_color=COLORS['accent_cyan'],
            corner_radius=UI_SETTINGS['corner_radius']
        )
        self.browse_proxies_btn.pack(side='left')
        
        # Additional arguments
        args_frame = ctk.CTkFrame(config_frame, fg_color='transparent')
        args_frame.pack(fill='x', padx=15, pady=5)
        
        ctk.CTkLabel(args_frame, text="Additional Arguments:",
                    font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal']),
                    text_color=COLORS['text_primary']).pack(anchor='w')
        
        self.args_entry = ctk.CTkEntry(
            args_frame,
            placeholder_text="--dbs --threads=5",
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal']),
            fg_color=COLORS['bg_tertiary'],
            border_color=COLORS['accent_cyan'],
            border_width=2,
            corner_radius=UI_SETTINGS['corner_radius']
        )
        self.args_entry.pack(fill='x', pady=(5, 0))
        
        # Action buttons
        buttons_frame = ctk.CTkFrame(config_frame, fg_color='transparent')
        buttons_frame.pack(fill='x', padx=15, pady=15)
        
        self.start_button = ctk.CTkButton(
            buttons_frame,
            text="🚀 START SCAN",
            command=self.start_scan,
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal'], 'bold'),
            fg_color=COLORS['success'],
            hover_color=COLORS['accent_cyan'],
            corner_radius=UI_SETTINGS['corner_radius'],
            height=40
        )
        self.start_button.pack(side='left', expand=True, fill='x', padx=(0, 5))
        
        self.stop_button = ctk.CTkButton(
            buttons_frame,
            text="🛑 STOP",
            command=self.stop_scan,
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal'], 'bold'),
            fg_color=COLORS['error'],
            hover_color=COLORS['warning'],
            corner_radius=UI_SETTINGS['corner_radius'],
            height=40
        )
        self.stop_button.pack(side='left', expand=True, fill='x', padx=5)
        
        self.clear_button = ctk.CTkButton(
            buttons_frame,
            text="🗑️ CLEAR",
            command=self.clear_terminal,
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal'], 'bold'),
            fg_color=COLORS['bg_tertiary'],
            hover_color=COLORS['accent_gold'],
            corner_radius=UI_SETTINGS['corner_radius'],
            height=40
        )
        self.clear_button.pack(side='left', expand=True, fill='x', padx=(5, 0))
        
    def _build_terminal(self, parent):
        """Build terminal output section"""
        terminal_frame = ctk.CTkFrame(parent, fg_color=COLORS['bg_secondary'],
                                     corner_radius=UI_SETTINGS['corner_radius'],
                                     border_width=2, border_color=COLORS['border'])
        terminal_frame.pack(fill='both', expand=True)
        
        # Title
        title = ctk.CTkLabel(
            terminal_frame,
            text="💻 TERMINAL OUTPUT",
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_header'], 'bold'),
            text_color=COLORS['accent_gold']
        )
        title.pack(pady=(15, 10), padx=15, anchor='w')
        
        # Terminal text widget (using tkinter's Text for better control)
        import tkinter as tk
        self.terminal = tk.Text(
            terminal_frame,
            bg=COLORS['bg_primary'],
            fg=COLORS['text_primary'],
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_terminal']),
            insertbackground=COLORS['accent_cyan'],
            selectbackground=COLORS['accent_cyan'],
            selectforeground=COLORS['bg_primary'],
            relief='flat',
            wrap='word',
            state='disabled'
        )
        self.terminal.pack(fill='both', expand=True, padx=15, pady=(0, 15))
        
        # Configure tags for colored output
        self.terminal.tag_config('success', foreground=COLORS['success'])
        self.terminal.tag_config('error', foreground=COLORS['error'])
        self.terminal.tag_config('warning', foreground=COLORS['warning'])
        self.terminal.tag_config('info', foreground=COLORS['accent_cyan'])
        
    def _build_ai_panel(self, parent):
        """Build AI insights panel"""
        ai_frame = ctk.CTkFrame(parent, fg_color=COLORS['bg_secondary'],
                               corner_radius=UI_SETTINGS['corner_radius'],
                               border_width=2, border_color=COLORS['accent_gold'])
        ai_frame.pack(fill='both', expand=True)
        
        # Title
        title = ctk.CTkLabel(
            ai_frame,
            text="🤖 AI ANALYST",
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_header'], 'bold'),
            text_color=COLORS['accent_gold']
        )
        title.pack(pady=(15, 10), padx=15, anchor='w')
        
        # Model Selector Section
        model_frame = ctk.CTkFrame(ai_frame, fg_color='transparent')
        model_frame.pack(fill='x', padx=15, pady=(0, 10))
        
        # Provider selector
        provider_frame = ctk.CTkFrame(model_frame, fg_color='transparent')
        provider_frame.pack(side='left', expand=True, fill='x', padx=(0, 5))
        
        ctk.CTkLabel(
            provider_frame,
            text="Provider:",
            font=(UI_SETTINGS['font_family'], 10),
            text_color=COLORS['text_secondary']
        ).pack(anchor='w')
        
        self.ai_provider_var = ctk.StringVar(value="OpenAI")
        self.provider_menu = ctk.CTkOptionMenu(
            provider_frame,
            values=["OpenAI", "Anthropic"],
            variable=self.ai_provider_var,
            command=self.on_provider_change,
            fg_color=COLORS['bg_tertiary'],
            button_color=COLORS['accent_gold'],
            button_hover_color=COLORS['accent_cyan'],
            corner_radius=UI_SETTINGS['corner_radius'],
            font=(UI_SETTINGS['font_family'], 10)
        )
        self.provider_menu.pack(fill='x', pady=(3, 0))
        
        # Model selector
        model_selector_frame = ctk.CTkFrame(model_frame, fg_color='transparent')
        model_selector_frame.pack(side='left', expand=True, fill='x', padx=(5, 0))
        
        ctk.CTkLabel(
            model_selector_frame,
            text="Model:",
            font=(UI_SETTINGS['font_family'], 10),
            text_color=COLORS['text_secondary']
        ).pack(anchor='w')
        
        # Initialize with OpenAI models
        openai_models = list(AI_MODELS['OpenAI'].values())
        self.ai_model_var = ctk.StringVar(value=openai_models[0])
        self.model_menu = ctk.CTkOptionMenu(
            model_selector_frame,
            values=openai_models,
            variable=self.ai_model_var,
            command=self.on_model_change,
            fg_color=COLORS['bg_tertiary'],
            button_color=COLORS['accent_gold'],
            button_hover_color=COLORS['accent_cyan'],
            corner_radius=UI_SETTINGS['corner_radius'],
            font=(UI_SETTINGS['font_family'], 10)
        )
        self.model_menu.pack(fill='x', pady=(3, 0))
        
        # Store model mappings
        self.model_id_map = {}
        for provider, models in AI_MODELS.items():
            for model_id, model_name in models.items():
                self.model_id_map[model_name] = model_id
        
        # AI output
        import tkinter as tk
        self.ai_output = tk.Text(
            ai_frame,
            bg=COLORS['bg_primary'],
            fg=COLORS['text_primary'],
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal']),
            relief='flat',
            wrap='word',
            state='disabled'
        )
        self.ai_output.pack(fill='both', expand=True, padx=15, pady=(0, 10))
        
        # Analyze button
        self.analyze_button = ctk.CTkButton(
            ai_frame,
            text="🔍 ANALYZE OUTPUT",
            command=self.analyze_with_ai,
            font=(UI_SETTINGS['font_family'], UI_SETTINGS['font_size_normal'], 'bold'),
            fg_color=COLORS['accent_gold'],
            hover_color=COLORS['accent_cyan'],
            corner_radius=UI_SETTINGS['corner_radius'],
            height=40
        )
        self.analyze_button.pack(fill='x', padx=15, pady=(0, 15))
        
    def append_output(self, text: str):
        """Append text to terminal output"""
        self.terminal.configure(state='normal')
        
        # Apply color tags based on content
        if '✅' in text or 'success' in text.lower():
            self.terminal.insert('end', text, 'success')
        elif '❌' in text or 'error' in text.lower():
            self.terminal.insert('end', text, 'error')
        elif '⚠️' in text or 'warning' in text.lower():
            self.terminal.insert('end', text, 'warning')
        elif '🚀' in text or 'executing' in text.lower():
            self.terminal.insert('end', text, 'info')
        else:
            self.terminal.insert('end', text)
        
        self.terminal.see('end')
        self.terminal.configure(state='disabled')
        
    def clear_terminal(self):
        """Clear terminal output"""
        self.terminal.configure(state='normal')
        self.terminal.delete('1.0', 'end')
        self.terminal.configure(state='disabled')
        
    def update_ai_output(self, text: str):
        """Update AI output panel"""
        self.ai_output.configure(state='normal')
        self.ai_output.delete('1.0', 'end')
        self.ai_output.insert('1.0', text)
        self.ai_output.configure(state='disabled')
        
    def browse_targets(self):
        """Open file dialog to select targets file"""
        from tkinter import filedialog
        filename = filedialog.askopenfilename(
            title="Select Targets File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            self.url_entry.delete(0, 'end')
            self.url_entry.insert(0, filename)
            self.append_output(f"📁 Loaded targets file: {filename}\n")
    
    def browse_proxies(self):
        """Open file dialog to select proxies file"""
        from tkinter import filedialog
        filename = filedialog.askopenfilename(
            title="Select Proxies File",
            filetypes=[("Text files", "*.txt"), ("All files", "*.*")]
        )
        if filename:
            self.proxy_entry.delete(0, 'end')
            self.proxy_entry.insert(0, filename)
            self.append_output(f"📁 Loaded proxies file: {filename}\n")
    
    def start_scan(self):
        """Start SQLMap scan"""
        target_url = self.url_entry.get().strip()
        
        if not target_url:
            self.append_output("❌ Please enter a target URL or targets file\n")
            return
        
        # Check if multiple targets
        if target_url.endswith('.txt'):
            self.append_output(f"📋 Multiple targets mode: {target_url}\n")
        
        # Get proxy
        proxy = self.proxy_entry.get().strip()
        if proxy:
            if proxy.endswith('.txt'):
                self.append_output(f"🔄 Multiple proxies mode: {proxy}\n")
            else:
                self.append_output(f"🔒 Using proxy: {proxy}\n")
        
        # Update status
        self.status_label.configure(text="● SCANNING", text_color=COLORS['warning'])
        
        # Build command
        command = self.sqlmap.build_command(
            target_url=target_url,
            risk=int(self.risk_var.get()),
            level=int(self.level_var.get()),
            random_agent=self.random_agent_var.get(),
            batch=self.batch_var.get(),
            tamper=self.tamper_var.get(),
            proxy=proxy,
            additional_args=self.args_entry.get()
        )
        
        # Start scan
        self.sqlmap.start_scan(command)
        
    def stop_scan(self):
        """Stop running scan"""
        self.sqlmap.stop_scan()
        self.status_label.configure(text="● READY", text_color=COLORS['success'])
        
    def on_provider_change(self, provider: str):
        """Handle AI provider change"""
        # Update model dropdown based on provider
        if provider == "OpenAI":
            models = list(AI_MODELS['OpenAI'].values())
            self.ai_analyzer.set_provider('openai')
        else:  # Anthropic
            models = list(AI_MODELS['Anthropic'].values())
            self.ai_analyzer.set_provider('anthropic')
        
        # Update model menu
        self.model_menu.configure(values=models)
        self.ai_model_var.set(models[0])
        
        # Update analyzer with first model
        model_id = self.model_id_map[models[0]]
        self.ai_analyzer.set_model(model_id)
        
        # Update AI output
        self.update_ai_output(f"✅ Switched to {provider}\nModel: {models[0]}\n\nReady to analyze SQLMap output.")
    
    def on_model_change(self, model_name: str):
        """Handle AI model change"""
        # Get model ID from name
        model_id = self.model_id_map.get(model_name)
        if model_id:
            self.ai_analyzer.set_model(model_id)
            self.update_ai_output(f"✅ Model changed to:\n{model_name}\n\nReady to analyze SQLMap output.")
    
    def analyze_with_ai(self):
        """Analyze output with AI"""
        current_model = self.ai_model_var.get()
        self.update_ai_output(f"🔄 Analyzing with {current_model}...\n\nPlease wait...")
        
        # Run analysis in thread to avoid blocking UI
        def analyze():
            recent_output = self.sqlmap.get_recent_output(20)
            analysis = self.ai_analyzer.analyze_output(recent_output)
            self.root.after(0, lambda: self.update_ai_output(analysis))
        
        thread = threading.Thread(target=analyze)
        thread.daemon = True
        thread.start()
        
    def run(self):
        """Start the application"""
        self.root.mainloop()
