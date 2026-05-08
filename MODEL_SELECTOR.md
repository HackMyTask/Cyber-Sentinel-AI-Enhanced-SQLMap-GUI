# 🧠 AI Model Selector - Dynamic Intelligence

## Overview

Fitur **Model Selector** memungkinkan kamu untuk mengganti AI model secara real-time tanpa restart aplikasi. Ini sangat berguna ketika menghadapi WAF yang berbeda-beda tingkat kesulitannya.

## 🎯 Kenapa Fitur Ini Penting?

### Skenario Penggunaan

1. **WAF Ringan** → Gunakan model cepat & murah (GPT-3.5 Turbo / Claude Haiku)
2. **WAF Sedang** → Gunakan model balanced (Claude Sonnet)
3. **WAF Berat** → Gunakan model paling pintar (GPT-4 / Claude Opus)

### Keuntungan

✅ **Hemat Biaya**: Tidak perlu pakai GPT-4 untuk analisis sederhana
✅ **Fleksibilitas**: Switch model sesuai kompleksitas target
✅ **Kecepatan**: Model ringan lebih cepat untuk quick analysis
✅ **Akurasi**: Model premium untuk kasus sulit

## 🔧 Cara Menggunakan

### 1. Pilih Provider

Di panel **AI ANALYST**, kamu akan melihat 2 dropdown:

**Provider Dropdown:**
- OpenAI (GPT models)
- Anthropic (Claude models)

### 2. Pilih Model

Setelah pilih provider, dropdown **Model** akan update otomatis:

#### OpenAI Models:
- **GPT-4 (Most Capable)** - Paling pintar, tapi paling mahal
- **GPT-4 Turbo (Fast & Smart)** - Balance antara speed & intelligence
- **GPT-3.5 Turbo (Fast & Cheap)** - Cepat dan murah untuk analisis basic

#### Anthropic Models:
- **Claude 3 Opus (Most Capable)** - Setara GPT-4, sangat detail
- **Claude 3 Sonnet (Balanced)** - Sweet spot untuk most cases
- **Claude 3 Haiku (Fast)** - Super cepat untuk quick insights

### 3. Real-time Switching

Kamu bisa ganti model **kapan saja**, bahkan di tengah-tengah scan:

```
1. Scan dimulai dengan GPT-3.5 Turbo
2. Ketemu WAF yang kompleks
3. Switch ke GPT-4 untuk analisis lebih dalam
4. Dapat rekomendasi tamper script yang lebih akurat
```

## 💡 Best Practices

### Strategi Penggunaan Model

#### Fase 1: Initial Reconnaissance
```
Model: GPT-3.5 Turbo / Claude Haiku
Tujuan: Quick scan untuk identifikasi basic vulnerabilities
Cost: Rendah
```

#### Fase 2: WAF Detection
```
Model: Claude Sonnet / GPT-4 Turbo
Tujuan: Analisis WAF pattern dan suggest bypass
Cost: Medium
```

#### Fase 3: Advanced Exploitation
```
Model: GPT-4 / Claude Opus
Tujuan: Deep analysis untuk complex injection scenarios
Cost: Tinggi (tapi worth it!)
```

## 🎮 Contoh Workflow

### Scenario: Testing E-commerce Site

**Step 1: Basic Check**
```
Provider: OpenAI
Model: GPT-3.5 Turbo
Action: Analyze initial scan output
Result: "Basic SQL injection detected, no WAF"
```

**Step 2: WAF Detected**
```
Provider: Anthropic
Model: Claude Sonnet
Action: Analyze WAF behavior
Result: "Cloudflare WAF detected, suggest: space2comment + randomcase"
```

**Step 3: Bypass Failed**
```
Provider: OpenAI
Model: GPT-4
Action: Deep analysis of failed attempts
Result: "Try combination: charencode + between + custom payload timing"
```

## 📊 Model Comparison

| Model | Speed | Cost | Best For |
|-------|-------|------|----------|
| GPT-3.5 Turbo | ⚡⚡⚡ | 💰 | Quick scans, basic analysis |
| GPT-4 Turbo | ⚡⚡ | 💰💰 | Balanced performance |
| GPT-4 | ⚡ | 💰💰💰 | Complex WAF bypass |
| Claude Haiku | ⚡⚡⚡ | 💰 | Fast insights |
| Claude Sonnet | ⚡⚡ | 💰💰 | Most use cases |
| Claude Opus | ⚡ | 💰💰💰 | Maximum accuracy |

## 🔥 Pro Tips

### 1. Cost Optimization
```python
# Start cheap, scale up only when needed
Initial scan → GPT-3.5 Turbo
WAF detected → Claude Sonnet
Complex bypass → GPT-4
```

### 2. Speed vs Accuracy
```python
# Time-sensitive testing
Use: Claude Haiku or GPT-3.5 Turbo

# Critical production testing
Use: GPT-4 or Claude Opus
```

### 3. Provider Switching
```python
# OpenAI rate limited?
Switch to: Anthropic (Claude)

# Need different perspective?
Try: Both providers for same output
```

## 🛠️ Technical Details

### Model IDs (Internal)

**OpenAI:**
- `gpt-4` - GPT-4 base model
- `gpt-4-turbo` - GPT-4 Turbo
- `gpt-3.5-turbo` - GPT-3.5 Turbo

**Anthropic:**
- `claude-3-opus-20240229` - Claude 3 Opus
- `claude-3-sonnet-20240229` - Claude 3 Sonnet
- `claude-3-haiku-20240307` - Claude 3 Haiku

### API Configuration

Models dikonfigurasi di `config.py`:
```python
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
```

## 🎯 Real-World Examples

### Example 1: Budget-Conscious Testing
```
Target: Small business website
Budget: Limited
Strategy:
  1. Use GPT-3.5 Turbo for all basic scans
  2. Only upgrade to GPT-4 if stuck
  3. Estimated cost: $0.50 per full test
```

### Example 2: Enterprise Pentest
```
Target: Banking application
Budget: No limit
Strategy:
  1. Start with Claude Opus for thorough analysis
  2. Cross-verify with GPT-4
  3. Use both models for critical findings
  4. Estimated cost: $5-10 per full test
```

### Example 3: Bug Bounty Hunting
```
Target: Multiple targets
Budget: Medium
Strategy:
  1. Quick scan all targets with Claude Haiku
  2. Deep dive promising targets with Sonnet
  3. Final exploitation with GPT-4
  4. Estimated cost: $2-3 per target
```

## 🚀 Future Enhancements

Planned features:
- [ ] Auto-select model based on WAF complexity
- [ ] Cost tracking per session
- [ ] Model performance comparison
- [ ] Custom model fine-tuning
- [ ] Local LLM support (Llama, Mistral)

## 📞 Support

Jika ada pertanyaan tentang model selection:
1. Check API key configuration
2. Verify internet connection
3. Monitor API rate limits
4. Review cost usage in provider dashboard

---

**💡 Remember**: The right model at the right time = Maximum efficiency!
