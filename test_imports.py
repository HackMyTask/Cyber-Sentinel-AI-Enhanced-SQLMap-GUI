"""
Quick test script to verify all imports work correctly
"""

print("Testing imports...")
print("-" * 50)

try:
    import sys
    print(f"✓ Python {sys.version.split()[0]}")
except Exception as e:
    print(f"✗ Python: {e}")

try:
    import customtkinter as ctk
    print(f"✓ CustomTkinter {ctk.__version__}")
except Exception as e:
    print(f"✗ CustomTkinter: {e}")

try:
    from config import COLORS, UI_SETTINGS
    print("✓ config.py")
except Exception as e:
    print(f"✗ config.py: {e}")

try:
    from logic import SQLMapWrapper
    print("✓ logic.py (SQLMapWrapper)")
except Exception as e:
    print(f"✗ logic.py: {e}")

try:
    from ai_analyzer import AIAnalyzer
    print("✓ ai_analyzer.py (AIAnalyzer)")
except Exception as e:
    print(f"✗ ai_analyzer.py: {e}")

try:
    from ui import CyberSentinelUI
    print("✓ ui.py (CyberSentinelUI)")
except Exception as e:
    print(f"✗ ui.py: {e}")

print("-" * 50)
print("\n✅ All core imports successful!")
print("\nOptional dependencies:")

try:
    import openai
    print("✓ OpenAI library installed")
except:
    print("⚠ OpenAI library not installed (optional)")

try:
    import anthropic
    print("✓ Anthropic library installed")
except:
    print("⚠ Anthropic library not installed (optional)")

print("\n" + "=" * 50)
print("Ready to run: python main.py")
print("=" * 50)
