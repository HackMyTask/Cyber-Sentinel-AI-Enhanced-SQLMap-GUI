"""
Configuration file for Cyber-Sentinel SQLMap GUI
"""

# Theme Colors - "Obsidian Night" Dark Luxury
COLORS = {
    'bg_primary': '#0B0B0B',
    'bg_secondary': '#1a1a1a',
    'bg_tertiary': '#252525',
    'accent_cyan': '#00F2FF',
    'accent_gold': '#FFD700',
    'text_primary': '#FFFFFF',
    'text_secondary': '#B0B0B0',
    'success': '#00FF88',
    'warning': '#FFA500',
    'error': '#FF4444',
    'border': '#00F2FF',
}

# UI Settings
UI_SETTINGS = {
    'window_title': 'Cyber-Sentinel | AI-Enhanced SQLMap',
    'window_size': '1400x900',
    'corner_radius': 10,
    'font_family': 'Cascadia Code',
    'font_size_normal': 12,
    'font_size_header': 16,
    'font_size_terminal': 11,
}

# SQLMap Settings
SQLMAP_SETTINGS = {
    'default_risk': 1,
    'default_level': 1,
    'tamper_scripts': [
        'None',
        'space2comment',
        'between',
        'charencode',
        'charunicodeencode',
        'equaltolike',
        'greatest',
        'ifnull2ifisnull',
        'multiplespaces',
        'percentage',
        'randomcase',
        'space2plus',
        'space2randomblank',
        'unionalltounion',
        'unmagicquotes',
    ],
}

# AI Settings
AI_SETTINGS = {
    'provider': 'openai',  # 'openai' or 'anthropic'
    'default_model': 'gpt-4',
    'max_tokens': 500,
    'temperature': 0.7,
    'system_message': """You are an intelligent assistant for penetration testers. 
Your task is to analyze SQLMap scan logs and provide concise technical advice to:
1. Identify detected vulnerabilities in plain English
2. Suggest optimal tamper scripts to bypass WAF/IDS
3. Recommend next steps for exploitation
4. Explain any errors or issues encountered

Keep responses brief, technical, and actionable."""
}

# Available AI Models
AI_MODELS = {
    'OpenAI': {
        'gpt-4': 'GPT-4 (Most Capable)',
        'gpt-4-turbo': 'GPT-4 Turbo (Fast & Smart)',
        'gpt-3.5-turbo': 'GPT-3.5 Turbo (Fast & Cheap)',
    },
    'Anthropic': {
        'claude-3-opus-20240229': 'Claude 3 Opus (Most Capable)',
        'claude-3-sonnet-20240229': 'Claude 3 Sonnet (Balanced)',
        'claude-3-haiku-20240307': 'Claude 3 Haiku (Fast)',
    }
}

# API Keys (User should set these as environment variables)
API_KEYS = {
    'openai': '',  # Set via environment variable OPENAI_API_KEY
    'anthropic': '',  # Set via environment variable ANTHROPIC_API_KEY
}
