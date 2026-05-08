"""
Cyber-Sentinel: AI-Enhanced SQLMap GUI
Main Entry Point

Author: AI-Generated
Description: Premium dark luxury interface for SQLMap with AI-powered analysis
"""

import sys
import os

# Add current directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from ui import CyberSentinelUI


def main():
    """Main entry point"""
    print("=" * 60)
    print("⚡ CYBER-SENTINEL - AI-Enhanced SQLMap GUI")
    print("=" * 60)
    print("\n🚀 Starting application...")
    print("\n📋 Prerequisites:")
    print("   1. SQLMap must be installed and in PATH")
    print("   2. For AI features, set API key:")
    print("      - OPENAI_API_KEY (for OpenAI)")
    print("      - ANTHROPIC_API_KEY (for Anthropic)")
    print("\n💡 Tips:")
    print("   - Use batch mode to avoid interactive prompts")
    print("   - Start with Risk=1, Level=1 for initial testing")
    print("   - Click 'ANALYZE OUTPUT' to get AI insights")
    print("\n" + "=" * 60 + "\n")
    
    try:
        # Create and run the application
        app = CyberSentinelUI()
        app.run()
    
    except KeyboardInterrupt:
        print("\n\n🛑 Application interrupted by user")
        sys.exit(0)
    
    except Exception as e:
        print(f"\n\n❌ Fatal Error: {str(e)}")
        print("\nPlease ensure all dependencies are installed:")
        print("   pip install -r requirements.txt")
        sys.exit(1)


if __name__ == "__main__":
    main()
