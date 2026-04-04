# Source: https://scrapfly.io/web-scraping-tools/ja3-fingerprint

Title: | Scrapfly

URL Source: https://scrapfly.io/web-scraping-tools/ja3-fingerprint

Markdown Content:
JA3 is a method for creating TLS/SSL client fingerprints that are easy to produce and share. It collects decimal byte values from the Client Hello packet during the TLS handshake and creates a fingerprint by concatenating specific fields.

#### JA3 Components

*   **TLS Version:** The TLS protocol version requested by the client
*   **Cipher Suites:** List of encryption algorithms supported
*   **Extensions:** TLS extensions requested (SNI, ALPN, etc.)
*   **Supported Groups:** Elliptic curves supported for key exchange
*   **Point Formats:** EC point format preferences

The JA3 string concatenates these values separated by commas, then generates an MD5 hash. This hash uniquely identifies the TLS client implementation.

###### JA3 Instability Warning

**JA3 fingerprints are now considered unstable** due to TLS Extension Permutation. Modern browsers (Chrome 110+, Firefox 114+) randomize the order of TLS extensions in each connection to prevent fingerprinting. This means the same browser can produce different JA3 hashes across sessions.

**Solution:** Use **JA3N** (normalized) or **JA4** instead. JA3N sorts extensions alphabetically to produce stable fingerprints regardless of permutation. JA4 is the next-generation fingerprint that handles permutation natively and includes additional discriminating factors.

#### JA3 vs JA3N vs JA4 vs Scrapfly FP

*   **JA3:** Original algorithm, excludes GREASE and padding extensions - ⚠️ Unstable due to TLS permutation
*   **JA3N:** Normalized version that sorts extensions to produce stable fingerprints despite permutation
*   **JA4:** Next-generation fingerprint (FoxIO) - handles permutation natively, includes cipher/extension counts, ALPN, and signature algorithms
*   **Scrapfly FP:** Enhanced fingerprint with additional TLS parameters for higher accuracy

**JA4** is the next-generation TLS fingerprinting method developed by FoxIO (John Althouse, the creator of JA3). It was designed to address the limitations of JA3, particularly the instability caused by TLS extension permutation.

#### JA4 Format Structure

JA4 uses a three-part format: `a_b_c`

*   **Part A (Metadata):**`(protocol)(tls_version)(sni)(cipher_count)(ext_count)(alpn)`
    *   `t` = TCP, `q` = QUIC
    *   `13` = TLS 1.3, `12` = TLS 1.2
    *   `d` = domain SNI, `i` = IP-based
    *   2-digit cipher count, 2-digit extension count
    *   First ALPN protocol (h2, h1, h3)

*   **Part B (Ciphers):** SHA256 hash (first 12 chars) of sorted cipher suites in hex format
*   **Part C (Extensions + SigAlgs):** SHA256 hash of sorted extensions + signature algorithms

#### Example JA4 Fingerprint

`t13d1516h2_8daaf6152771_e5627efa2ab1`
This breaks down as:

*   `t` = TCP connection
*   `13` = TLS 1.3
*   `d` = Domain-based SNI (not IP)
*   `15` = 15 cipher suites offered
*   `16` = 16 extensions
*   `h2` = HTTP/2 as first ALPN
*   `8daaf6152771` = Truncated hash of sorted ciphers
*   `e5627efa2ab1` = Truncated hash of extensions + signature algorithms

#### Why JA4 is Better Than JA3

| Feature | JA3 | JA4 |
| --- | --- | --- |
| **TLS Permutation Resistant** | ❌ No | ✓ Yes (sorted) |
| **Human Readable** | ⚠️ Partially | ✓ Yes (metadata prefix) |
| **QUIC/HTTP3 Support** | ❌ No | ✓ Yes (q prefix) |
| **Signature Algorithms** | ❌ No | ✓ Included |
| **ALPN Information** | ❌ No | ✓ Included |

###### JA4+ Family

JA4 is part of the larger JA4+ fingerprint family which includes:

*   **JA4:** TLS Client fingerprint (this page)
*   **JA4S:** TLS Server fingerprint
*   **JA4H:** HTTP Client fingerprint (headers, cookies)
*   **JA4X:** X.509 Certificate fingerprint
*   **JA4T:** TCP fingerprint
*   **JA4SSH:** SSH fingerprint

Websites and security systems use JA3 fingerprints to identify and block automated tools:

#### Detection Methods

*   **Blacklist Known Bots:** Block JA3 hashes from known scraping libraries (curl, requests, etc.)
*   **Inconsistency Detection:** Compare JA3 with User-Agent string - mismatch indicates spoofing
*   **Rate by Fingerprint:** Apply stricter rate limits to suspicious JA3 hashes
*   **Browser Verification:** Real browsers have consistent JA3 signatures per version

#### Common Problematic Fingerprints

*   `curl/7.x` - Distinctive TLS configuration easily identified
*   `Python requests` - Uses urllib3 with unique cipher suite order
*   `Go http.Client` - Different extension set than browsers
*   `Node.js https` - OpenSSL defaults differ from browser TLS

To avoid detection, scrapers must match the exact JA3 fingerprint of the target browser, including cipher suite order, extension set, and TLS version.

To bypass JA3 fingerprinting, you need to match the exact TLS configuration of a real browser:

#### Solutions for Web Scraping

*   **Browser Automation:** Use Puppeteer, Playwright, or Selenium - they use real browser engines with matching JA3
*   **curl-impersonate:** Modified curl that mimics Chrome/Firefox TLS handshakes
*   **curl_cffi (Python):** Python bindings for curl-impersonate
*   **tls-client (Go):** Go library that can mimic browser TLS fingerprints
*   **Scrapfly API:** Automatically handles JA3 fingerprinting with our ASP (Anti-Scraping Protection)

#### Manual Configuration (Advanced)

You can manually configure your HTTP client to match browser TLS settings:

*   Set exact cipher suite order from target browser
*   Include all required TLS extensions in correct order
*   Match TLS version and supported groups
*   Handle GREASE values properly

**Note:** Manual configuration is complex and fragile. Browser automation or specialized libraries are recommended for reliable JA3 bypass.

Learn more in our comprehensive guide: [How to Avoid Web Scraping Blocking: TLS Fingerprinting](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-tls/)

Major CDN and anti-bot providers extensively use JA3 fingerprinting to identify and block automated traffic. Understanding their techniques is essential for effective web scraping.

#### Cloudflare Bot Management

Cloudflare maintains a massive database of JA3 fingerprints from known bots, scrapers, and automation tools:

*   **Blocklist Database:** Instant blocking of known bot JA3 hashes (curl, Python requests, old browsers)
*   **User-Agent Correlation:** Validates JA3 matches claimed browser in User-Agent 
    *   Example: User-Agent claims "Chrome 120" but JA3 matches Python requests → **Block**

*   **HTTP/2 Integration:** Combines JA3 with HTTP/2 SETTINGS frame fingerprinting (Akamai-style)
*   **Challenge Pages:** JavaScript challenges verify TLS consistency across multiple requests
*   **Reputation Scoring:** JA3 hashes with high bot activity get lower trust scores

###### Real Blocking Example

**Scenario:** Python `requests` library (urllib3) has JA3: `771,49200-49196-...`

This fingerprint is in Cloudflare's bot database → **403 Forbidden or Captcha challenge**

**Solution:** Use `curl_cffi` for static sites (no JS rendering) or Scrapfly ASP for full browser emulation with JS support

#### Akamai Bot Manager

Akamai pioneered TLS fingerprinting and uses an enhanced version beyond basic JA3:

*   **Enhanced JA3:** Includes additional TLS parameters not in original JA3 spec
*   **HTTP/2 Fingerprinting:** SETTINGS frames, WINDOW_UPDATE values, stream priority
*   **Timing Analysis:** Measures TLS handshake duration and connection setup speed
*   **Certificate Validation:** Checks client certificate handling patterns
*   **Cross-Request Consistency:** Ensures JA3 remains stable across multiple requests

###### Akamai HTTP/2 Fingerprint Format

Akamai combines TLS and HTTP/2 fingerprinting:

`tls_version|settings_frame|window_update|priority|pseudo_headers`
Example: `13|3:100;4:10485760;6:262144|15663105|1:0:0:201|m,a,s,p`

This makes spoofing significantly harder than JA3 alone.

#### Common Bot JA3 Signatures

| Tool/Library | JA3 Hash | Detection Rate |
| --- | --- | --- |
| **Python requests** | `599ccb0563b...` | 100% |
| **cURL 7.x** | `e7d705a3286...` | 100% |
| **Go http.Client** | `b32309a26951...` | 95% |
| **Node.js https** | `8f1c5a3428db...` | 85% |
| **curl_cffi** | `579ccef312d1...` (Chrome-like) | 5% |
| **Scrapfly ASP** | _Rotates real browser fingerprints_ | 0.1% |

#### DataDome & PerimeterX

Other major anti-bot systems also rely on JA3:

*   **DataDome:** Combines JA3 with canvas fingerprinting and behavioral analysis
*   **PerimeterX:** Uses JA3 as part of their bot sensor suite, integrates with cookie tracking
*   **Kasada:** Enhanced TLS fingerprinting beyond JA3, includes cipher selection timing

Learn how to test and compare JA3 fingerprints across different HTTP libraries and tools:

#### Python Library Comparison

###### 1. Testing with `requests` (urllib3)

```
import requests

# Standard requests - WILL BE BLOCKED
response = requests.get('https://tools.scrapfly.io/api/fp/ja3')
ja3_hash = response.json().get('ja3_hash')
print(f"requests JA3: {ja3_hash}")
# Output: 599ccb0563b7bbae9962ca7e634cc462 (Known bot signature)
```

###### 2. Testing with `curl_cffi` (Recommended)

```
from curl_cffi import requests

# Impersonate Chrome 120
session = requests.Session(impersonate="chrome120")
response = session.get('https://tools.scrapfly.io/api/fp/ja3')
ja3_hash = response.json().get('ja3_hash')
print(f"curl_cffi JA3: {ja3_hash}")
# Output: 579ccef312d18482fc42e2b822ca2430 (Matches real Chrome!)
```

###### 3. Testing with `httpx`

```
import httpx

# httpx with HTTP/2 support
async with httpx.AsyncClient(http2=True) as client:
    response = await client.get('https://tools.scrapfly.io/api/fp/ja3')
    ja3_hash = response.json().get('ja3_hash')
    print(f"httpx JA3: {ja3_hash}")
    # Still detectable, but better than requests
```

###### 4. Testing with Scrapfly

```
from scrapfly import ScrapflyClient, ScrapeConfig

client = ScrapflyClient(key='YOUR_API_KEY')

# Automatic TLS fingerprint matching
result = client.scrape(ScrapeConfig(
    url='https://tools.scrapfly.io/api/fp/ja3',
    asp=True,  # Anti-Scraping Protection
    country='US'
))

# Scrapfly rotates real browser fingerprints
print("JA3 matches real Chrome/Firefox")
print(result.content)
```

#### Node.js/JavaScript Testing

###### 1. Testing with native `https` module

```
const https = require('https');

https.get('https://tools.scrapfly.io/api/fp/ja3', (res) => {
    let data = '';
    res.on('data', chunk => data += chunk);
    res.on('end', () => {
        const ja3 = JSON.parse(data).ja3_hash;
        console.log('Node.js https JA3:', ja3);
        // Detectable as Node.js
    });
});
```

###### 2. Testing with Puppeteer (Real Browser)

```
const puppeteer = require('puppeteer');

(async () => {
    const browser = await puppeteer.launch();
    const page = await browser.newPage();

    await page.goto('https://tools.scrapfly.io/api/fp/ja3');
    const ja3 = await page.evaluate(() => {
        return JSON.parse(document.body.innerText).ja3_hash;
    });

    console.log('Puppeteer JA3:', ja3);
    // Matches real Chrome! (but navigator.webdriver present)

    await browser.close();
})();
```

#### Command Line Testing

```
# curl (standard) - DETECTABLE
curl https://tools.scrapfly.io/api/fp/ja3
# JA3: e7d705a3286e19ea42f587b344ee6865

# curl-impersonate (Chrome) - UNDETECTABLE
curl_chrome116 https://tools.scrapfly.io/api/fp/ja3
# JA3: Matches Chrome 116

# wget - DETECTABLE
wget -qO- https://tools.scrapfly.io/api/fp/ja3
# JA3: Different from browsers
```

#### Comparison Table

| Library/Tool | HTTP/2 Support | Browser-like JA3 | Cloudflare Pass Rate |
| --- | --- | --- | --- |
| **requests (urllib3)** | ❌ No | ❌ No | ~2% |
| **httpx** | ✓ Yes | ❌ No | ~15% |
| **curl_cffi** | ✓ Yes | ✓ Yes | ~85%** |
| **Selenium/Puppeteer** | ✓ Yes | ✓ Yes | ~60%* |
| **Scrapfly ASP** | ✓ Yes | ✓ Yes | 99.9% |

* Selenium/Puppeteer have correct JA3 but fail other checks (navigator.webdriver, canvas fingerprinting)

** curl_cffi has correct JA3 but lacks JavaScript rendering - sites requiring JS execution will still block. Use Scrapfly for JS-heavy sites.

###### Pro Tip: Compare Side-by-Side

To verify your scraper's JA3 fingerprint:

1.   Visit this tool with your target browser (Chrome, Firefox, Safari)
2.   Note the JA3 hash displayed
3.   Run your scraping code against `https://tools.scrapfly.io/api/fp/ja3`
4.   Compare the JA3 hashes - they should match exactly

If hashes differ, anti-bot systems will detect your automation tool.

Comprehensive guide to bypassing JA3 detection across different scenarios and requirements:

#### Recommended Solution: Scrapfly ASP

**Why Scrapfly ASP is the best solution:**

*   ✅ **Real browser TLS fingerprints** from Chrome, Firefox, Safari, Edge
*   ✅ **Automatic rotation** across hundreds of unique fingerprints
*   ✅ **Perfect HTTP/2 support** including Akamai-style fingerprinting
*   ✅ **Zero configuration** - just enable `asp=True`
*   ✅ **99.9% success rate** against Cloudflare, Akamai, DataDome
*   ✅ **Consistent with all signals** - JA3, canvas, WebGL, fonts all match

###### Quick Example:

```
from scrapfly import ScrapflyClient, ScrapeConfig

client = ScrapflyClient(key='YOUR_API_KEY')

# Automatic JA3 + HTTP/2 + Canvas + WebGL handling
result = client.scrape(ScrapeConfig(
    url='https://protected-site.com',
    asp=True,  # Enable Anti-Scraping Protection
    render_js=True,  # Enable browser rendering if needed
    country='US'
))

print(result.content)  # Successfully bypassed all fingerprinting!
```

#### DIY Solutions (For Learning)

###### 1. curl_cffi (Python - Best DIY Option)

```
# Install: pip install curl_cffi
from curl_cffi import requests

# Impersonate specific browser
session = requests.Session(impersonate="chrome120")

response = session.get('https://protected-site.com')
print(response.text)

# Available impersonations:
# chrome99, chrome100, chrome101, ... chrome120
# edge99, edge101
# safari15_3, safari15_5
```

**Pros:** ✅ Exact Chrome JA3, ✅ HTTP/2 support, ✅ Fast

**Cons:** ⚠️ Requires curl-impersonate binary, ⚠️ Limited browser versions, ❌ No JavaScript rendering, ❌ No canvas/WebGL matching

###### 2. tls-client (Go)

```
package main

import (
    "fmt"
    tls_client "github.com/bogdanfinn/tls-client"
)

func main() {
    options := []tls_client.HttpClientOption{
        tls_client.WithClientProfile(tls_client.Chrome_120),
    }

    client, _ := tls_client.NewHttpClient(tls_client.NewNoopLogger(), options...)
    response, _ := client.Get("https://protected-site.com")

    fmt.Println(response.Status)
}
```

**Pros:** ✅ Multiple browser profiles, ✅ HTTP/2

**Cons:** ⚠️ Go only, ⚠️ Complex setup, ❌ No browser fingerprint matching

###### 3. Puppeteer/Playwright (Browser Automation)

```
const puppeteer = require('puppeteer-extra');
const StealthPlugin = require('puppeteer-extra-plugin-stealth');
puppeteer.use(StealthPlugin());

(async () => {
    const browser = await puppeteer.launch({ headless: true });
    const page = await browser.newPage();

    await page.goto('https://protected-site.com');
    const content = await page.content();

    console.log(content);
    await browser.close();
})();
```

**Pros:** ✅ Perfect JA3, ✅ Real browser rendering, ✅ Handles JavaScript

**Cons:** ⚠️ Slow (2-5 seconds per page), ⚠️ High memory usage, ⚠️ Still detectable via navigator.webdriver

###### 4. curl-impersonate (Command Line)

```
# Install curl-impersonate
curl_chrome116 https://protected-site.com

# Or with specific options
curl_chrome116 -H "User-Agent: Mozilla/5.0..." \
    https://protected-site.com
```

**Pros:** ✅ Perfect Chrome JA3, ✅ Fast

**Cons:** ⚠️ Command-line only, ⚠️ No JavaScript support, ⚠️ Limited to curl features

#### Methods That DON'T Work

###### 1. Manually Configuring OpenSSL/urllib3

```
# ❌ This approach FAILS
import urllib3

# Trying to manually set cipher order
urllib3.util.ssl_.DEFAULT_CIPHERS = 'ECDHE-RSA-AES128-GCM-SHA256:...'
# Problem: Can't control all TLS parameters needed for JA3 match
```

**Why it fails:** Python's ssl module doesn't expose low-level TLS handshake control. You can't set extension order, GREASE values, or elliptic curves properly.

###### 2. Proxying Through Real Browsers

**Why it fails:** TLS handshake happens between your client and the server. Proxying through a browser doesn't change YOUR client's JA3 fingerprint.

###### 3. User-Agent Spoofing Alone

```
# ❌ This is NOT enough
headers = {'User-Agent': 'Mozilla/5.0 (Chrome/120.0)'}
requests.get(url, headers=headers)
# Still has Python requests JA3 fingerprint!
```

**Why it fails:** Anti-bot systems check if User-Agent matches JA3. Mismatch = instant detection.

#### Success Rate Comparison

| Method | Setup Complexity | Speed | Success vs Cloudflare | Success vs Akamai |
| --- | --- | --- | --- | --- |
| **Scrapfly ASP** | None | Fast (500ms) | 99.9% | 99.8% |
| **curl_cffi** | Medium | Fast (300ms) | 85% | 60% |
| **Puppeteer + Stealth** | Medium | Slow (3s) | 60% | 50% |
| **tls-client (Go)** | High | Fast (400ms) | 80% | 55% |
| **Manual OpenSSL Config** | Very High | Fast | 10% | 5% |

##### Q: What's the difference between JA3, JA3N, and JA3S?

**A:**

*   **JA3:** Original client fingerprinting algorithm (Client Hello packet)
*   **JA3N:** Normalized version that handles edge cases and GREASE values more consistently
*   **JA3S:** Server fingerprinting (Server Hello packet) - identifies the server's TLS configuration
*   **Scrapfly FP:** Enhanced fingerprint with additional TLS parameters for higher accuracy

For web scraping, you primarily care about JA3 (client fingerprint) since that's what identifies your tool.

##### Q: Can I manually configure my HTTP client to match a browser JA3?

**A:** Extremely difficult and not recommended. You'd need to control:

*   Exact cipher suite order (20-30 ciphers)
*   TLS extension order (15+ extensions)
*   GREASE value generation and placement
*   Elliptic curve preferences
*   EC point format preferences

Most standard libraries (Python ssl, Java JSSE, Node.js tls) don't expose these low-level controls. Use specialized libraries like curl_cffi or services like Scrapfly instead.

##### Q: Does HTTPS proxy affect JA3 fingerprinting?

**A:** No, if using CONNECT method (standard HTTPS proxy). The TLS handshake happens end-to-end between your client and the target server. The proxy only tunnels encrypted traffic.

**Exception:** If proxy performs SSL/TLS termination (man-in-the-middle), the target server sees the proxy's JA3, not yours. This is rare for standard proxies.

##### Q: How often do browser JA3 signatures change?

**A:** Browser JA3 fingerprints change with:

*   **Major browser updates:** Every 6-12 months (e.g., Chrome 119 → 120)
*   **TLS protocol updates:** When new TLS 1.3 extensions are added
*   **Cipher suite changes:** When browsers deprecate old ciphers or add new ones

**Impact on scraping:** You need to update your impersonation target periodically. Scrapfly ASP automatically updates to match latest browsers.

##### Q: Can JA3 fingerprinting work with HTTP/1.1?

**A:** Yes! JA3 is TLS-layer fingerprinting, independent of HTTP version. Works with HTTP/1.1, HTTP/2, and HTTP/3 (QUIC).

**However:** Anti-bot systems often combine JA3 (TLS) with HTTP/2 fingerprinting (SETTINGS frames, priority) for stronger detection. Using HTTP/1.1 on a site that expects HTTP/2 is itself suspicious.

##### Q: Is JA3 fingerprinting legal to bypass?

**A:** Yes, bypassing JA3 fingerprinting is legal in most jurisdictions. JA3 is a technical fingerprinting method, not a legal barrier. However:

*   ✅ **Legal:** Using curl_cffi, Scrapfly, or browser automation for legitimate data collection
*   ✅ **Legal:** Testing your own infrastructure's anti-bot defenses
*   ⚠️ **Check ToS:** Some websites prohibit scraping in their Terms of Service
*   ❌ **Illegal:** Bypassing authentication, stealing data, or causing harm

Always respect robots.txt, rate limit yourself, and only collect publicly available data.

##### Q: Why does my Selenium/Puppeteer still get blocked if JA3 matches?

**A:** JA3 is just ONE signal. Anti-bot systems check:

*   **Canvas fingerprinting:** Selenium often has detectable canvas hash
*   **navigator.webdriver:** Set to `true` in Selenium/Puppeteer
*   **Chrome DevTools Protocol:** Detectable via timing analysis
*   **Behavioral patterns:** Bots click/scroll differently than humans
*   **WebGL:** Headless browsers use software rendering (SwiftShader)

Perfect JA3 match + other bot signals = still blocked. You need consistency across ALL fingerprints.

##### Q: Can I rotate JA3 fingerprints to avoid detection?

**A:** Yes, but with caveats:

*   ✅ **Rotate between real browser JA3s:** Chrome 119, Chrome 120, Firefox 121 (looks natural)
*   ⚠️ **Don't mix:** Chrome JA3 + Firefox User-Agent = instant detection
*   ⚠️ **Session consistency:** Keep same JA3 within a session (cookies, logins)
*   ✅ **Scrapfly approach:** Assigns consistent fingerprint profile per session, rotates between sessions

Random JA3 rotation without matching other signals (User-Agent, canvas, WebGL) will trigger inconsistency detection.

You can access your TLS fingerprint programmatically via our API:

#### API Endpoint

`GET https://tools.scrapfly.io/api/fp/ja3`
#### Response Format (JSON)

```
{
  "ja3": "771,4865-4866-4867...",
  "ja3_digest": "579ccef312d18482fc42e2b822ca2430",
  "ja3n": "771,4865-4866-4867...",
  "ja3n_digest": "...",
  "ja4": "t13d1516h2_8daaf6152771_...",
  "ja4_r": "t13d1516h2_002f,009c,..._0005,000a,...",
  "ja4_hash": "8daaf615277...",
  "scrapfly_fp": "...",
  "scrapfly_fp_digest": "...",
  "tls": {
    "version": "TLS 1.3",
    "ciphers": [...],
    "extensions": [...],
    "curves": [...],
    "points": [...],
    "versions": [...],
    "protocols": [...]
  }
}
```

#### JavaScript Example

```
fetch('https://tools.scrapfly.io/api/fp/ja3')
  .then(r => r.json())
  .then(data => {
    console.log('JA3 Hash:', data.ja3_digest);
    console.log('TLS Version:', data.tls.version);
  });
```

The fingerprint data is also available in the browser console via `window.fingerprint`.
