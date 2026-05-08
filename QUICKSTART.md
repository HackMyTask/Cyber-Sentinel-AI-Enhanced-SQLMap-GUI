# 🚀 Quick Start Guide - Cyber-Sentinel

## Installation (5 minutes)

### Step 1: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 2: Install SQLMap (if not already installed)
```bash
pip install sqlmap
```

### Step 3: (Optional) Configure AI
If you want AI analysis features:

1. Copy `.env.example` to `.env`
2. Add your API key:
   ```
   OPENAI_API_KEY=sk-your-key-here
   ```

### Step 4: Run the Application
```bash
python main.py
```

## First Scan (2 minutes)

### Test with a Vulnerable Site
Use this intentionally vulnerable test site:

**Target URL:**
```
http://testphp.vulnweb.com/artists.php?artist=1
```

**Configuration:**
- Risk: 1
- Level: 1
- Random Agent: ✓
- Batch Mode: ✓
- Additional Args: `--dbs`

**Steps:**
1. Paste the URL in "Target URL" field
2. Keep default settings (Risk=1, Level=1)
3. Click "🚀 START SCAN"
4. Watch the terminal output in real-time
5. When scan completes, click "🔍 ANALYZE OUTPUT" for AI insights

## Common Use Cases

### 1. Basic Vulnerability Check
```
Target: http://example.com/page?id=1
Risk: 1
Level: 1
Args: --batch
```

### 2. Database Enumeration
```
Target: http://example.com/page?id=1
Risk: 1
Level: 1
Args: --dbs --batch
```

### 3. Extract Specific Database
```
Target: http://example.com/page?id=1
Risk: 1
Level: 1
Args: -D database_name --tables --batch
```

### 4. WAF Bypass Attempt
```
Target: http://example.com/page?id=1
Risk: 2
Level: 3
Tamper: space2comment
Random Agent: ✓
Args: --batch
```

### 5. Full Dump
```
Target: http://example.com/page?id=1
Risk: 1
Level: 1
Args: -D dbname -T tablename --dump --batch
```

## Keyboard Shortcuts

- **Ctrl+C** in terminal: Stop scan
- **Clear button**: Clear terminal output
- **Stop button**: Terminate running scan

## Troubleshooting

### "SQLMap not found"
```bash
# Install SQLMap
pip install sqlmap

# Or add to PATH if installed manually
set PATH=%PATH%;C:\path\to\sqlmap
```

### "AI Analysis unavailable"
- Set your API key in environment variables
- Or create a `.env` file with your key

### GUI doesn't start
```bash
# Reinstall CustomTkinter
pip install --upgrade customtkinter
```

## Tips for Best Results

1. **Start Conservative**: Use Risk=1, Level=1 first
2. **Use Batch Mode**: Prevents interactive prompts
3. **Test Legally**: Only scan systems you own or have permission to test
4. **Read Output**: SQLMap provides detailed information in terminal
5. **Use AI Analysis**: Get plain English explanations of findings

## Next Steps

- Read the full [README.md](README.md) for detailed documentation
- Customize colors in `config.py`
- Explore different tamper scripts for WAF bypass
- Check SQLMap documentation for advanced flags

---

**⚠️ Legal Notice**: Only use this tool on systems you own or have explicit permission to test. Unauthorized testing is illegal.
