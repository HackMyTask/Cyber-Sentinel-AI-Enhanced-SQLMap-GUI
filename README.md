# ⚡ Cyber-Sentinel: AI-Enhanced SQLMap GUI

A premium, dark luxury GUI for SQLMap with integrated AI analysis capabilities. Built with Python and CustomTkinter for a modern, sleek interface.

![Theme: Obsidian Night](https://img.shields.io/badge/Theme-Obsidian%20Night-00F2FF?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![License](https://img.shields.io/badge/License-MIT-gold?style=for-the-badge)

## 🎯 Features

### Core Functionality
- **Real-time Terminal Output**: Live streaming of SQLMap execution with syntax highlighting
- **Visual Configuration**: Intuitive controls for all SQLMap parameters
- **Non-blocking Execution**: Threaded subprocess management keeps UI responsive
- **AI-Powered Analysis**: Integrated OpenAI/Anthropic for intelligent vulnerability analysis

### AI Analyst Panel
- **Real-time Model Selector**: Switch between AI providers and models on-the-fly
- **Multiple AI Models**: Support for GPT-4, GPT-3.5, Claude 3 Opus, Sonnet, and Haiku
- Analyzes SQLMap output in plain English
- Suggests optimal tamper scripts for detected WAFs
- Provides actionable recommendations for exploitation
- Explains errors and issues encountered

### Dark Luxury Design
- **Theme**: "Obsidian Night" - Deep matte black with neon cyan accents
- **Typography**: Monospace fonts (Cascadia Code/JetBrains Mono)
- **Components**: Rounded corners, semi-transparent overlays, animated elements
- **Colors**: 
  - Background: `#0B0B0B` (Primary), `#1a1a1a` (Secondary)
  - Accents: `#00F2FF` (Cyan), `#FFD700` (Gold)

## 📋 Prerequisites

### Required
- **Python 3.8+**
- **SQLMap**: Must be installed and accessible in PATH
  ```bash
  # Install via pip
  pip install sqlmap
  
  # Or clone from GitHub
  git clone https://github.com/sqlmapproject/sqlmap.git
  ```

### Optional (for AI features)
- **OpenAI API Key** or **Anthropic API Key**

## 🚀 Installation

1. **Clone or download this repository**
   ```bash
   cd "sqlmap gui"
   ```

2. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Set up API keys (optional)**
   
   Create a `.env` file or set environment variables:
   ```bash
   # For OpenAI
   set OPENAI_API_KEY=your_openai_api_key_here
   
   # For Anthropic
   set ANTHROPIC_API_KEY=your_anthropic_api_key_here
   ```

4. **Run the application**
   ```bash
   python main.py
   ```

## 🎮 Usage

### Basic Workflow

1. **Enter Target URL**
   - Input the vulnerable URL with parameter (e.g., `http://example.com/page?id=1`)

2. **Configure Scan Parameters**
   - **Risk Level** (1-3): Higher risk = more aggressive tests
   - **Level** (1-5): Higher level = more extensive tests
   - **Tamper Script**: Select evasion technique for WAF bypass
   - **Random User-Agent**: Randomize HTTP User-Agent header
   - **Batch Mode**: Automatically answer prompts (recommended)

3. **Additional Arguments**
   - Add custom SQLMap flags (e.g., `--dbs --threads=5`)

4. **Start Scan**
   - Click "🚀 START SCAN" to begin
   - Monitor real-time output in terminal
   - Stop anytime with "🛑 STOP" button

5. **AI Analysis**
   - Click "🔍 ANALYZE OUTPUT" to get AI insights
   - Receive vulnerability explanations and recommendations

### Example Configurations

#### Basic Database Enumeration
```
Target: http://testphp.vulnweb.com/artists.php?artist=1
Risk: 1
Level: 1
Additional Args: --dbs --batch
```

#### WAF Bypass Attempt
```
Target: http://example.com/page?id=1
Risk: 2
Level: 3
Tamper: space2comment
Random Agent: ✓
Additional Args: --random-agent --batch
```

#### Full Database Dump
```
Target: http://example.com/page?id=1
Risk: 1
Level: 1
Additional Args: -D database_name --dump --batch
```

## 🏗️ Architecture

### Project Structure
```
sqlmap gui/
├── main.py           # Entry point
├── ui.py             # GUI implementation (CustomTkinter)
├── logic.py          # SQLMap wrapper & subprocess management
├── ai_analyzer.py    # AI integration (OpenAI/Anthropic)
├── config.py         # Configuration & theme settings
├── requirements.txt  # Python dependencies
└── README.md         # Documentation
```

### Key Components

#### SQLMapWrapper (`logic.py`)
- Manages subprocess execution
- Streams output in real-time
- Handles command building and process lifecycle

#### AIAnalyzer (`ai_analyzer.py`)
- Integrates with OpenAI or Anthropic APIs
- Analyzes scan output for vulnerabilities
- Suggests tamper scripts for WAF bypass

#### CyberSentinelUI (`ui.py`)
- Modern dark-themed interface
- Real-time terminal with syntax highlighting
- Responsive controls and status indicators

## ⚙️ Configuration

### Customizing Theme
Edit `config.py` to modify colors and UI settings:

```python
COLORS = {
    'bg_primary': '#0B0B0B',      # Main background
    'accent_cyan': '#00F2FF',      # Primary accent
    'accent_gold': '#FFD700',      # Secondary accent
    # ... more colors
}
```

### Changing AI Provider
In `config.py`:
```python
AI_SETTINGS = {
    'provider': 'openai',  # or 'anthropic'
    'openai_model': 'gpt-4',
    'anthropic_model': 'claude-3-sonnet-20240229',
}
```

### SQLMap Path
If SQLMap is not in PATH, modify `logic.py`:
```python
def _find_sqlmap(self) -> str:
    return 'C:\\path\\to\\sqlmap.py'  # Your SQLMap path
```

## 🔒 Security Notes

⚠️ **Important**: This tool is for authorized security testing only.

- Only test systems you have permission to assess
- Unauthorized testing may be illegal in your jurisdiction
- Use responsibly and ethically
- Keep API keys secure and never commit them to version control

## 🐛 Troubleshooting

### SQLMap Not Found
```
❌ ERROR: SQLMap not found!
```
**Solution**: Install SQLMap or add it to your PATH
```bash
pip install sqlmap
# or
set PATH=%PATH%;C:\path\to\sqlmap
```

### AI Analysis Unavailable
```
⚠️ AI Analysis unavailable. Please configure API key.
```
**Solution**: Set environment variable for your chosen provider
```bash
set OPENAI_API_KEY=your_key_here
```

### GUI Not Displaying Correctly
**Solution**: Ensure CustomTkinter is properly installed
```bash
pip install --upgrade customtkinter
```

### Font Not Found
**Solution**: The app will fall back to system default if Cascadia Code is unavailable. To install:
- Windows: Download from [Microsoft](https://github.com/microsoft/cascadia-code)
- Linux: `sudo apt install fonts-cascadia-code`

## 🎨 Screenshots

### Main Interface
- Dark luxury theme with neon cyan accents
- Real-time terminal output with color coding
- Intuitive configuration panel

### AI Analyst Panel
- Intelligent vulnerability analysis
- Plain English explanations
- Actionable recommendations

## 📝 License

This project is provided as-is for educational and authorized security testing purposes.

## 🤝 Contributing

Contributions are welcome! Areas for improvement:
- Database tree view visualization
- Export scan results to JSON/XML
- Scan history and session management
- Additional AI providers
- Custom tamper script editor

## 📚 Resources

- [SQLMap Documentation](https://github.com/sqlmapproject/sqlmap/wiki)
- [CustomTkinter Docs](https://customtkinter.tomschimansky.com/)
- [OpenAI API](https://platform.openai.com/docs)
- [Anthropic API](https://docs.anthropic.com/)

## 🙏 Acknowledgments

- SQLMap team for the amazing tool
- CustomTkinter for the modern UI framework
- OpenAI & Anthropic for AI capabilities

---

**Made with ⚡ by AI | For Ethical Hackers & Security Researchers**
