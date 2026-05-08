"""
AI Analyzer Module for SQLMap Output
Integrates with OpenAI or Anthropic to provide intelligent analysis
"""

import os
from typing import Optional
from config import AI_SETTINGS, API_KEYS


class AIAnalyzer:
    """Handles AI-powered analysis of SQLMap output"""
    
    def __init__(self, provider: str = 'openai', model: str = None):
        """
        Initialize AI Analyzer
        
        Args:
            provider: 'openai' or 'anthropic'
            model: Specific model to use (optional)
        """
        self.provider = provider
        self.current_model = model
        self.client = None
        self._initialize_client()
    
    def _initialize_client(self):
        """Initialize the AI client based on provider"""
        try:
            if self.provider == 'openai':
                import openai
                api_key = os.getenv('OPENAI_API_KEY', API_KEYS.get('openai', ''))
                if api_key:
                    self.client = openai.OpenAI(api_key=api_key)
                else:
                    print("Warning: OpenAI API key not found")
            
            elif self.provider == 'anthropic':
                import anthropic
                api_key = os.getenv('ANTHROPIC_API_KEY', API_KEYS.get('anthropic', ''))
                if api_key:
                    self.client = anthropic.Anthropic(api_key=api_key)
                else:
                    print("Warning: Anthropic API key not found")
        
        except ImportError as e:
            print(f"Error importing AI library: {e}")
            self.client = None
    
    def analyze_output(self, sqlmap_output: str) -> str:
        """
        Analyze SQLMap output and provide insights
        
        Args:
            sqlmap_output: Recent SQLMap terminal output
            
        Returns:
            AI-generated analysis and recommendations
        """
        if not self.client:
            return "⚠️ AI Analysis unavailable. Please configure API key.\n\nSet environment variable:\n- OPENAI_API_KEY for OpenAI\n- ANTHROPIC_API_KEY for Anthropic"
        
        if not sqlmap_output or len(sqlmap_output.strip()) < 10:
            return "⏳ Waiting for SQLMap output to analyze..."
        
        try:
            if self.provider == 'openai':
                return self._analyze_with_openai(sqlmap_output)
            elif self.provider == 'anthropic':
                return self._analyze_with_anthropic(sqlmap_output)
        
        except Exception as e:
            return f"❌ AI Analysis Error: {str(e)}\n\nPlease check your API key and internet connection."
    
    def set_model(self, model: str):
        """
        Change the current AI model
        
        Args:
            model: Model identifier to use
        """
        self.current_model = model
    
    def set_provider(self, provider: str):
        """
        Change the AI provider and reinitialize client
        
        Args:
            provider: 'openai' or 'anthropic'
        """
        self.provider = provider
        self._initialize_client()
    
    def _analyze_with_openai(self, output: str) -> str:
        """Analyze using OpenAI API"""
        try:
            # Use current model or fall back to default
            model = self.current_model if self.current_model else AI_SETTINGS['default_model']
            
            response = self.client.chat.completions.create(
                model=model,
                messages=[
                    {"role": "system", "content": AI_SETTINGS['system_message']},
                    {"role": "user", "content": f"Analyze this SQLMap output:\n\n{output}"}
                ],
                max_tokens=AI_SETTINGS['max_tokens'],
                temperature=AI_SETTINGS['temperature']
            )
            
            return f"🤖 AI Analysis ({model}):\n\n" + response.choices[0].message.content
        
        except Exception as e:
            return f"❌ OpenAI Error: {str(e)}"
    
    def _analyze_with_anthropic(self, output: str) -> str:
        """Analyze using Anthropic API"""
        try:
            # Use current model or fall back to default
            model = self.current_model if self.current_model else 'claude-3-sonnet-20240229'
            
            response = self.client.messages.create(
                model=model,
                max_tokens=AI_SETTINGS['max_tokens'],
                temperature=AI_SETTINGS['temperature'],
                system=AI_SETTINGS['system_message'],
                messages=[
                    {"role": "user", "content": f"Analyze this SQLMap output:\n\n{output}"}
                ]
            )
            
            return f"🤖 AI Analysis ({model}):\n\n" + response.content[0].text
        
        except Exception as e:
            return f"❌ Anthropic Error: {str(e)}"
    
    def suggest_tamper(self, waf_detected: str) -> str:
        """
        Suggest tamper scripts based on detected WAF
        
        Args:
            waf_detected: Name of detected WAF/IDS
            
        Returns:
            Recommended tamper scripts
        """
        if not self.client:
            return "AI unavailable for tamper suggestions"
        
        prompt = f"A {waf_detected} WAF/IDS was detected. Suggest the best SQLMap tamper scripts to bypass it. Be specific and brief."
        
        try:
            if self.provider == 'openai':
                response = self.client.chat.completions.create(
                    model=AI_SETTINGS['openai_model'],
                    messages=[
                        {"role": "system", "content": AI_SETTINGS['system_message']},
                        {"role": "user", "content": prompt}
                    ],
                    max_tokens=200,
                    temperature=0.5
                )
                return response.choices[0].message.content
            
            elif self.provider == 'anthropic':
                response = self.client.messages.create(
                    model=AI_SETTINGS['anthropic_model'],
                    max_tokens=200,
                    temperature=0.5,
                    system=AI_SETTINGS['system_message'],
                    messages=[{"role": "user", "content": prompt}]
                )
                return response.content[0].text
        
        except Exception as e:
            return f"Error getting tamper suggestion: {str(e)}"
