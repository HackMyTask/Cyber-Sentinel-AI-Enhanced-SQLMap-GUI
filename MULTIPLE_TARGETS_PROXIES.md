# 🎯 Multiple Targets & Proxies - Mass Scanning

## Overview

Fitur **Multiple Targets & Proxies** memungkinkan kamu untuk:
- Scan banyak target sekaligus dari file
- Rotate proxies otomatis untuk bypass rate limiting
- Efficient mass vulnerability scanning

## 🚀 Multiple Targets

### Kenapa Penting?

✅ **Efisiensi**: Scan puluhan/ratusan target dalam satu session
✅ **Automation**: Set and forget - biarkan berjalan overnight
✅ **Consistency**: Semua target di-scan dengan parameter yang sama
✅ **Reporting**: Hasil tersimpan per-target untuk easy tracking

### Cara Menggunakan

#### Method 1: Manual File Creation

1. Buat file `targets.txt`:
```
http://example1.com/page?id=1
http://example2.com/product?pid=123
http://example3.com/user?uid=456
```

2. Di GUI, klik tombol **📁** di sebelah Target URL
3. Pilih file `targets.txt`
4. Start scan seperti biasa

#### Method 2: Use Example Template

1. Copy `targets.example.txt` ke `targets.txt`
2. Edit dan tambahkan target kamu
3. Load via file browser

### Format File

```txt
# Comments start with #
# One URL per line
# Blank lines are ignored

http://target1.com/page?id=1
http://target2.com/page?id=1
https://target3.com/api?param=value

# You can group targets with comments
# E-commerce sites
http://shop1.com/product?id=1
http://shop2.com/item?id=1
```

### Best Practices

**1. Group Similar Targets**
```txt
# Banking Apps
http://bank1.com/account?id=1
http://bank2.com/transfer?id=1

# E-commerce
http://shop1.com/product?id=1
http://shop2.com/cart?id=1
```

**2. Start Small, Scale Up**
```
First run: 5-10 targets
Monitor results
Scale to 50-100 targets
```

**3. Use Descriptive Comments**
```txt
# Client: ABC Corp - Production
http://abc.com/page?id=1

# Client: XYZ Inc - Staging
http://staging.xyz.com/page?id=1
```

## 🔄 Multiple Proxies

### Kenapa Penting?

✅ **Bypass Rate Limiting**: Rotate IP untuk avoid detection
✅ **Anonymity**: Hide your real IP address
✅ **Geo-Testing**: Test dari berbagai lokasi
✅ **WAF Evasion**: Distribute requests across IPs

### Cara Menggunakan

#### Method 1: Single Proxy

Masukkan langsung di field Proxy:
```
http://127.0.0.1:8080
```

#### Method 2: Multiple Proxies (Rotation)

1. Buat file `proxies.txt`:
```
http://proxy1.com:8080
http://proxy2.com:8080
http://proxy3.com:8080
socks5://proxy4.com:1080
```

2. Klik tombol **📁** di sebelah Proxy field
3. Pilih file `proxies.txt`
4. SQLMap akan rotate proxies otomatis

### Supported Proxy Types

| Type | Format | Example |
|------|--------|---------|
| HTTP | `http://ip:port` | `http://127.0.0.1:8080` |
| HTTPS | `https://ip:port` | `https://127.0.0.1:8443` |
| SOCKS4 | `socks4://ip:port` | `socks4://127.0.0.1:1080` |
| SOCKS5 | `socks5://ip:port` | `socks5://127.0.0.1:1080` |

### Proxy with Authentication

```txt
http://username:password@proxy.com:8080
socks5://user:pass@proxy.com:1080
```

### Format File Proxies

```txt
# HTTP Proxies
http://proxy1.com:8080
http://proxy2.com:8080

# SOCKS Proxies
socks5://proxy3.com:1080
socks5://proxy4.com:1080

# With Authentication
http://user:pass@proxy5.com:8080
```

## 🎮 Use Cases

### Case 1: Bug Bounty - Multiple Subdomains

**Scenario**: Testing 50 subdomains dari satu company

**Setup**:
```txt
# targets.txt
http://app1.company.com/page?id=1
http://app2.company.com/page?id=1
http://app3.company.com/page?id=1
... (47 more)
```

**Configuration**:
- Risk: 1
- Level: 1
- Batch: ✓
- Args: `--dbs --threads=3`

**Result**: Scan semua subdomain dalam beberapa jam

### Case 2: Pentest - Multiple Clients

**Scenario**: Monthly pentest untuk 10 clients

**Setup**:
```txt
# targets.txt
# Client A
http://clienta.com/page?id=1

# Client B  
http://clientb.com/page?id=1

# Client C
http://clientc.com/page?id=1
```

**Benefit**: Consistent testing methodology

### Case 3: WAF Bypass - Proxy Rotation

**Scenario**: Target dengan aggressive rate limiting

**Setup**:
```txt
# proxies.txt
http://proxy1.com:8080
http://proxy2.com:8080
http://proxy3.com:8080
http://proxy4.com:8080
http://proxy5.com:8080
```

**Configuration**:
- Single target
- Multiple proxies
- Random Agent: ✓
- Tamper: space2comment

**Result**: Bypass rate limiting dengan IP rotation

### Case 4: Geo-Distributed Testing

**Scenario**: Test dari berbagai negara

**Setup**:
```txt
# proxies.txt
http://us-proxy.com:8080      # USA
http://uk-proxy.com:8080      # UK
http://sg-proxy.com:8080      # Singapore
http://jp-proxy.com:8080      # Japan
```

**Benefit**: Detect geo-specific vulnerabilities

## 💡 Pro Tips

### 1. Combine Multiple Targets + Multiple Proxies

```
Targets: 50 URLs
Proxies: 10 IPs
Result: Distributed load, harder to detect
```

### 2. Use Threads Wisely

```python
# For multiple targets
Args: --threads=5

# Balance between speed and stealth
Too many threads = easier detection
Too few threads = slow scan
```

### 3. Monitor Progress

SQLMap akan show progress untuk each target:
```
[INFO] testing URL 'http://target1.com/page?id=1'
[INFO] testing URL 'http://target2.com/page?id=1'
```

### 4. Save Results Per Target

SQLMap automatically saves results:
```
~/.sqlmap/output/target1.com/
~/.sqlmap/output/target2.com/
~/.sqlmap/output/target3.com/
```

### 5. Proxy Testing

Test proxy sebelum use:
```bash
curl -x http://proxy.com:8080 http://ipinfo.io
```

## 🛠️ Advanced Configurations

### Scenario: Mass Scan with AI Analysis

```
1. Load 100 targets from file
2. Use 5 rotating proxies
3. Risk=1, Level=1 for speed
4. Let it run overnight
5. Next morning: Analyze results with AI
6. AI identifies most critical findings
7. Deep dive on high-priority targets
```

### Scenario: Stealth Mode

```
Targets: targets.txt (10 URLs)
Proxies: proxies.txt (20 IPs)
Random Agent: ✓
Tamper: randomcase
Threads: 2 (slow but stealthy)
Args: --delay=3 --randomize=User-Agent
```

### Scenario: Speed Mode

```
Targets: targets.txt (5 URLs)
Proxies: None (direct connection)
Risk: 3
Level: 5
Threads: 10
Args: --threads=10 --batch
```

## 📊 Performance Metrics

| Targets | Proxies | Threads | Est. Time |
|---------|---------|---------|-----------|
| 10 | 0 | 3 | 30-60 min |
| 50 | 5 | 5 | 3-5 hours |
| 100 | 10 | 5 | 6-10 hours |
| 500 | 20 | 10 | 24-48 hours |

*Times vary based on target response time and complexity*

## ⚠️ Important Notes

### Legal Considerations

- Only scan targets you have permission to test
- Multiple targets = multiple permissions needed
- Document authorization for each target

### Rate Limiting

- Even with proxies, respect rate limits
- Use `--delay` flag for slower requests
- Monitor for IP bans

### Proxy Quality

- Free proxies are often unreliable
- Use paid/private proxies for serious work
- Test proxies before mass scanning

### Resource Usage

- Multiple targets = high CPU/memory usage
- Monitor system resources
- Consider running on dedicated server

## 🔧 Troubleshooting

### Issue: "Proxy connection failed"

**Solution**:
```
1. Test proxy manually
2. Check proxy format
3. Verify proxy is online
4. Try different proxy
```

### Issue: "Too many targets, slow performance"

**Solution**:
```
1. Reduce thread count
2. Split targets into batches
3. Use more powerful machine
4. Run multiple instances
```

### Issue: "Some targets skipped"

**Solution**:
```
1. Check target URL format
2. Verify targets are accessible
3. Review SQLMap logs
4. Remove invalid URLs from file
```

## 📚 Example Workflows

### Workflow 1: Daily Bug Bounty Routine

```bash
# Morning: Load fresh targets
targets.txt: 20 new subdomains found

# Afternoon: Run scan
Risk: 1, Level: 1, Proxies: 5 IPs

# Evening: AI Analysis
Analyze results, prioritize findings

# Night: Deep dive
Manual testing on promising targets
```

### Workflow 2: Monthly Pentest

```bash
# Week 1: Reconnaissance
Gather all client URLs

# Week 2: Mass Scan
Load all targets, run comprehensive scan

# Week 3: Analysis
Review results, verify findings

# Week 4: Reporting
Generate reports per client
```

## 🎯 Summary

**Multiple Targets** = Efficiency & Scale
**Multiple Proxies** = Stealth & Bypass

**Combined** = Professional-grade mass vulnerability scanning!

---

**💡 Remember**: With great power comes great responsibility. Always get proper authorization!
