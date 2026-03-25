# Source: https://scrapfly.io/web-scraping-tools/http2-fingerprint

Title: | Scrapfly

URL Source: https://scrapfly.io/web-scraping-tools/http2-fingerprint

Markdown Content:
HTTP/2 Fingerprint - Detect Browser HTTP/2 Configuration
===============

[![Image 1: Scrapfly Logo](https://cdn.scrapfly.io/0.1.176/www/public/svg/logo.svg?version=0.1.176)Tools](https://scrapfly.io/web-scraping-tools)

Web Scraping API with anti-bot bypass[Start Free](https://scrapfly.io/signup)

FREE

#### Antibot Detector

Instantly detect what's blocking your scraper

16 Anti-bots

8 CAPTCHAs

21 Fingerprints

[Open Source](https://github.com/scrapfly/Antibot-Detector)[Add to Chrome](https://chromewebstore.google.com/detail/scrapfly/pdpakdgmjhkfimgaihlgaaiijlbilkca)Maybe later

Chrome Extension

*   [Antibot Detector](https://scrapfly.io/web-scraping-tools/antibot-detector "Antibot Detector Chrome Extension")

Browser Fingerprinting

*   [Browser](https://scrapfly.io/web-scraping-tools/browser-fingerprint "Comprehensive Browser Fingerprint Test")
*   [Canvas](https://scrapfly.io/web-scraping-tools/canvas-fingerprint "Canvas Fingerprint Test")
*   [GPU](https://scrapfly.io/web-scraping-tools/gpu-fingerprint "GPU & WebGL Fingerprint")
*   [WebGL](https://scrapfly.io/web-scraping-tools/webgl-fingerprint "WebGL Fingerprint Test")
*   [Audio](https://scrapfly.io/web-scraping-tools/audio-fingerprint "Audio Fingerprint Test")
*   [Screen](https://scrapfly.io/web-scraping-tools/screen-fingerprint "Screen & Display Fingerprint")
*   [Fonts](https://scrapfly.io/web-scraping-tools/fonts "Font Detection Test")
*   [Media Codecs](https://scrapfly.io/web-scraping-tools/media-codecs "Media Codec Detection")
*   [Voices](https://scrapfly.io/web-scraping-tools/speech-synthesis-voices "Speech Synthesis Voices")
*   [Math Engine](https://scrapfly.io/web-scraping-tools/math-engine "Math Engine Fingerprint")
*   [Timezone](https://scrapfly.io/web-scraping-tools/timezone-intl "Timezone & Locale Detection")
*   [Performance](https://scrapfly.io/web-scraping-tools/performance-inspector "Performance Inspector")
*   [Keyboard](https://scrapfly.io/web-scraping-tools/keyboard-layout "Keyboard Layout Detection")
*   [Battery](https://scrapfly.io/web-scraping-tools/battery-status "Battery Status API")
*   [DRM](https://scrapfly.io/web-scraping-tools/drm-capabilities "DRM Capabilities")

Network & Connection

*   [JA3/JA4 HTTP1/2](https://scrapfly.io/web-scraping-tools/ja3-fingerprint "JA3/JA4 TLS Fingerprint for HTTP/1.1 and HTTP/2")
*   [QUIC/HTTP3/JA4](https://scrapfly.io/web-scraping-tools/http3-quic-fingerprint "QUIC/HTTP3/JA4 Fingerprint")
*   [HTTP/2 Fingerprint](https://scrapfly.io/web-scraping-tools/http2-fingerprint "HTTP/2 Connection Fingerprint")
*   [IP Info](https://scrapfly.io/web-scraping-tools/ip-info "IP Address Information")
*   [Device Fingerprint](https://scrapfly.io/web-scraping-tools/device-fingerprint "TCP/IP & UDP/IP Device Fingerprint")
*   [WebRTC Leak](https://scrapfly.io/web-scraping-tools/webrtc-leak "WebRTC IP Leak Test")
*   [DNS Leak](https://scrapfly.io/web-scraping-tools/dns-leak "DNS Leak Test")

Scraping & Dev Tools

*   [CSS/XPath Tester](https://scrapfly.io/web-scraping-tools/css-xpath-tester "CSS & XPath Selector Tester")
*   [cURL to Python](https://scrapfly.io/web-scraping-tools/curl-python "Convert cURL to Python")
*   [Base64](https://scrapfly.io/web-scraping-tools/base64 "Base64 Encode/Decode")
*   [URL Encode](https://scrapfly.io/web-scraping-tools/urlencode "URL Encode/Decode")
*   [URL Prettier](https://scrapfly.io/web-scraping-tools/url-prettier "URL Beautifier & Parser")
*   [Cookie Parser](https://scrapfly.io/web-scraping-tools/cookie-parser "Cookie Parser & Analyzer")
*   [Patch Viewer](https://scrapfly.io/web-scraping-tools/patch-viewer "Git Patch Viewer")
*   [Text Diff](https://scrapfly.io/web-scraping-tools/text-diff "Text Diff Comparison")

#### Scrape Any Website

Web scraping API that handles the hard parts for you

*    Managed headless browsers
*    Anti-bot auto-bypass
*    Countless hours saved

[Start Free](https://scrapfly.io/signup)

HTTP/2 Fingerprint
==================

Test your browser's HTTP/2 fingerprint based on SETTINGS frames, WINDOW_UPDATE, priority, and pseudo-header order. Learn how HTTP/2 configuration is used to detect bots and block web scrapers.

### HTTP/2 Fingerprint

Fingerprint Hash (MD5)

52d84b11737d980aef856699f885ca86

Raw Fingerprint String

1:65536;2:0;4:6291456;6:262144|15663105|0|m,a,s,p

Curl Command Copy Command 

 curl 'https://tools.scrapfly.io/api/fp/akamai' 

Format: `[SETTINGS]|WINDOW_UPDATE|PRIORITY|Pseudo-Header-Order|HEADERS_FRAME|WINDOW_UPDATE`

HTTP/2 Fingerprint Ready

### Compare My Fingerprint

See how your HTTP/2 fingerprint matches against known browser profiles from our database.

Analyzing fingerprint...

#1

Chrome

94.2%

 154,320 samples 

#2

Firefox

4.1%

 8,921 samples 

#3

Edge

1.7%

 5,678 samples 

##### Unlock Real Fingerprint Analysis

Sign up for free to see how your actual HTTP/2 fingerprint compares against our database of real browser profiles.

[Sign Up Free](https://scrapfly.io/register)
Already have an account? [Log in](https://scrapfly.io/login)

### HTTP/2 Frame Timeline

SETTINGS

Frame 1

WINDOW_UPDATE

Frame 2

HEADERS

Frame 3

{
  "type": 4,
  "name": "SETTINGS",
  "settings_map": {
    "1": 65536,
    "2": 0,
    "4": 6291456,
    "6": 262144
  },
  "settings_order": [
    1,
    2,
    4,
    6
  ]
}

### SETTINGS Frame Parameters

HTTP/2 SETTINGS frame defines connection parameters that are unique to each browser implementation.

SETTINGS_HEADER_TABLE_SIZE

65536

Maximum size of the header compression table (HPACK)

SETTINGS_ENABLE_PUSH

0

Whether server push is enabled

SETTINGS_INITIAL_WINDOW_SIZE

6291456

Initial flow control window size

SETTINGS_MAX_HEADER_LIST_SIZE

262144

Maximum size of header list

### WINDOW_UPDATE Frame

Window Size Increment

15663105

### Stream Priority

Stream Dependency

1

Weight

N/A

Exclusive

N/A

### Pseudo-Header Order

The order of HTTP/2 pseudo-headers (:method, :authority, :scheme, :path) varies by browser and is part of the fingerprint.

1:method

2:authority

3:scheme

4:path

 What is HTTP/2 Fingerprinting?

HTTP/2 fingerprinting analyzes the configuration and behavior of HTTP/2 connections to identify the browser or HTTP client being used. Unlike HTTP/1.1, HTTP/2 introduces new frames and parameters that vary across implementations.

#### Key Fingerprinting Components

*   **SETTINGS Frame:** Parameters like header table size, max concurrent streams, initial window size
*   **WINDOW_UPDATE:** Flow control window size increments
*   **PRIORITY:** Stream dependency, weight, and exclusive flag
*   **Pseudo-Header Order:** Order of :method, :authority, :scheme, :path headers
*   **Frame Timing:** Sequence and timing of frame transmission

#### AKAMAI HTTP/2 Fingerprint Format

AKAMAI (a major CDN provider) uses this format for HTTP/2 fingerprinting:

`[SETTINGS params]|WINDOW_UPDATE|PRIORITY|Pseudo-Header-Order|...`

This captures the most distinctive aspects of an HTTP/2 connection in a compact string that can be hashed and compared.

#### Why HTTP/2?

HTTP/2 provides more fingerprinting data points than HTTP/1.1 because:

*   Binary framing protocol with configurable parameters
*   Multiple streams over single connection (multiplexing)
*   Flow control mechanisms with browser-specific defaults
*   Server push and priority handling varies by implementation

 How is HTTP/2 Fingerprinting Used for Bot Detection?

Websites and CDNs use HTTP/2 fingerprints to identify automated tools and scrapers:

#### Detection Techniques

*   **Blacklist Known Clients:** Block fingerprints from curl, Python requests, Go http client, etc.
*   **Inconsistency Detection:** Compare HTTP/2 fingerprint with User-Agent and TLS fingerprint
*   **Default Detection:** Flag connections using library defaults that differ from browsers
*   **Temporal Analysis:** Browsers update HTTP/2 configs with new versions - outdated configs are suspicious

#### Common Scraper Signatures

*   `curl` - Uses nghttp2 library with distinctive SETTINGS parameters
*   `Python httpx` - HTTP/2 support with h2 library defaults
*   `Go net/http` - golang.org/x/net/http2 implementation fingerprint
*   `Node.js http2` - Uses Node's built-in http2 module with specific defaults

#### Why It's Effective

HTTP/2 fingerprinting is particularly effective because:

*   Most HTTP libraries don't allow fine-grained HTTP/2 parameter control
*   Default SETTINGS values are hard-coded and rarely match browsers
*   Pseudo-header ordering is implementation-specific and hard to spoof
*   Combining with TLS fingerprinting creates very unique signatures

For example, Chrome sends SETTINGS with specific values for `HEADER_TABLE_SIZE=65536` and `MAX_CONCURRENT_STREAMS=1000`, while curl uses different defaults that immediately reveal it's not a browser.

 How to Avoid HTTP/2 Detection

Bypassing HTTP/2 fingerprinting requires matching the exact HTTP/2 configuration of a real browser:

#### Best Solutions

*   **Browser Automation:** Puppeteer, Playwright, Selenium - real browsers have perfect HTTP/2 fingerprints
*   **curl-impersonate:** Modified curl that mimics Chrome/Firefox HTTP/2 behavior
*   **curl_cffi (Python):** Python wrapper around curl-impersonate with HTTP/2 support
*   **Scrapfly API:** Automatically handles HTTP/2 fingerprinting with ASP (Anti-Scraping Protection)

#### Manual Configuration (Advanced)

Some HTTP/2 libraries allow manual configuration, but it's complex:

*   Set SETTINGS frame parameters to match target browser exactly
*   Configure WINDOW_UPDATE increment values
*   Set stream priority parameters (dependency, weight, exclusive)
*   Order pseudo-headers correctly (:method, :authority, :scheme, :path)
*   Match frame transmission timing and sequence

#### Example: Matching Chrome's HTTP/2 Config

```yaml
SETTINGS:
  HEADER_TABLE_SIZE: 65536
  ENABLE_PUSH: 1
  MAX_CONCURRENT_STREAMS: 1000
  INITIAL_WINDOW_SIZE: 6291456
  MAX_FRAME_SIZE: 16384
  MAX_HEADER_LIST_SIZE: 262144

WINDOW_UPDATE: 15663105
PRIORITY: stream_dep=0, weight=255, exclusive=true
PSEUDO_HEADERS: :method, :authority, :scheme, :path
```

**Note:** Manual HTTP/2 configuration is extremely fragile and breaks with browser updates. Use browser automation or specialized tools for reliable results.

Learn more about HTTP/2 fingerprinting and bypassing: [Scrapfly Blog - Web Scraping Blocking Techniques](https://scrapfly.io/blog/tags/blocking/)

 Programmatic Access

You can access your HTTP/2 fingerprint programmatically via our API:

#### API Endpoint

```ruby
GET https://tools.scrapfly.io/api/fp/akamai
```

#### Response Format (JSON)

```bash
{
  "http2_fingerprint": "[SETTINGS]|...",
  "http2_digest": "abc123...",
  "http2_frames": [
    {
      "name": "SETTINGS",
      "settings": {
        "SETTINGS_HEADER_TABLE_SIZE": 65536,
        "SETTINGS_MAX_CONCURRENT_STREAMS": 1000,
        ...
      }
    },
    {
      "name": "WINDOW_UPDATE",
      "window_size_increment": 15663105
    },
    {
      "name": "HEADERS",
      "pseudo_header_order": [":method", ":authority", ":scheme", ":path"],
      "stream_dependency": 0,
      "weight": 255,
      "exclusive": true
    }
  ]
}
```

#### JavaScript Example

```javascript
fetch('https://tools.scrapfly.io/api/fp/akamai')
  .then(r => r.json())
  .then(data => {
    console.log('HTTP/2 Hash:', data.http2_digest);
    console.log('Settings:', data.http2_frames[0].settings);
  });
```

The fingerprint data is also available in the browser console via `window.fingerprint`.

How to bypass web scraping bot detection
----------------------------------------

[![Image 2: Web Scraping With Node-Unblocker](https://cdn.scrapfly.io/static/blog/posts/how-to-scrape-without-getting-blocked-tutorial/feature-light.svg) Tutorial on how to avoid web scraper blocking. What is javascript and TLS (JA3) fingerprinting and what role request headers play in blocking.](https://scrapfly.io/blog/posts/how-to-scrape-without-getting-blocked-tutorial/ "How to Scrape Without Getting Blocked Tutorial")

[![Image 3: How to Avoid Web Scraping Blocking: Headers Guide](https://cdn.scrapfly.io/static/blog/posts/how-to-avoid-web-scraping-blocking-headers/feature-light.svg) Introduction to web scraping headers - what do they mean, how to configure them in web scrapers and how to avoid being blocked.](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-headers/ "How to Avoid Web Scraping Blocking: Headers Guide")

[![Image 4: How to Avoid Web Scraping Blocking: Javascript](https://cdn.scrapfly.io/static/blog/posts/how-to-avoid-web-scraping-blocking-javascript/feature-light.svg) Introduction to how javascript is used to detect web scrapers. What's in javascript fingerprint and how to correctly spoof it for web scraping.](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-javascript/ "How to Avoid Web Scraping Blocking")

![Image 5: Scrapfly Logo](https://cdn.scrapfly.io/0.1.176/www/public/svg/logo.svg?version=0.1.176)
The ultimate data collection APIs for developers. Scrape, capture, and extract web data with battle-tested tools that scale.

[](https://github.com/scrapfly)[](https://www.linkedin.com/company/scrapfly)[](https://www.youtube.com/@scrapfly)[](https://x.com/Scrapfly_dev)

### Company

*   [Careers](https://scrapfly.io/jobs)
*   [Why Scrapfly?](https://scrapfly.io/why-choose-scrapfly)
*   [Pricing](https://scrapfly.io/pricing)
*   [Status](https://scrapfly.statuspage.io/)

### Resources

*   [API Docs](https://scrapfly.io/docs)
*   [Academy](https://scrapfly.io/academy)
*   [Blog](https://scrapfly.io/blog/)
*   [Tools](https://scrapfly.io/web-scraping-tools)
*   [FAQ](https://scrapfly.io/faq)
*   [Alternatives](https://scrapfly.io/compare)

### Legal

*   [Terms of Service](https://scrapfly.io/terms-of-service)
*   [Privacy Policy](https://scrapfly.io/privacy-policy)
*   [DPA](https://scrapfly.io/data-processing-agreement)
*   [KYC](https://scrapfly.io/kyc-and-safety)

#### Integrations

*   [Zapier](https://scrapfly.io/integration/zapier)
*   [Make](https://scrapfly.io/integration/make)
*   [N8n](https://scrapfly.io/integration/n8n)
*   [LlamaIndex](https://scrapfly.io/integration/llamaindex)
*   [LangChain](https://scrapfly.io/integration/langchain)
*   [CrewAI](https://scrapfly.io/integration/crewai)

#### Learn Web Scraping

*   [Python](https://scrapfly.io/blog/posts/everything-to-know-about-web-scraping-python/)
*   [NodeJS](https://scrapfly.io/blog/posts/web-scraping-with-nodejs/)
*   [PHP](https://scrapfly.io/blog/posts/web-scraping-with-php-101/)
*   [Ruby](https://scrapfly.io/blog/posts/web-scraping-with-ruby/)
*   [Scrapy](https://scrapfly.io/blog/posts/web-scraping-with-scrapy/)
*   [Puppeteer](https://scrapfly.io/blog/posts/web-scraping-with-puppeteer-and-nodejs/)

#### Use Cases

*   [AI Training](https://scrapfly.io/use-case/ai-training-web-scraping)
*   [eCommerce](https://scrapfly.io/use-case/ecommerce-web-scraping)
*   [Real Estate](https://scrapfly.io/use-case/real-estate-web-scraping)
*   [Finance](https://scrapfly.io/use-case/finance-web-scraping)
*   [SERP & SEO](https://scrapfly.io/use-case/seo-and-serp-web-scraping)
*   [Travel](https://scrapfly.io/use-case/travel-web-scraping)

#### Popular Tools

*   [cURL to Python](https://scrapfly.io/web-scraping-tools/curl-python)
*   [JA3 Fingerprint](https://scrapfly.io/web-scraping-tools/ja3-fingerprint)
*   [HTTP2 Fingerprint](https://scrapfly.io/web-scraping-tools/http2-fingerprint)
*   [Selector Tester](https://scrapfly.io/web-scraping-tools/css-xpath-tester)
*   [Antibot Detector](https://scrapfly.io/antibot-detector)
*   [Unblocker](https://scrapfly.io/unblocker)

#### Anti-Bot Bypass

*   [Cloudflare](https://scrapfly.io/bypass/cloudflare)
*   [Akamai](https://scrapfly.io/bypass/akamai)
*   [DataDome](https://scrapfly.io/bypass/datadome)
*   [Incapsula](https://scrapfly.io/bypass/incapsula)
*   [PerimeterX](https://scrapfly.io/bypass/perimeterx)
*   [View All](https://scrapfly.io/bypass)

© 2026 Scrapfly. The Best Web Scraping API For Developers.

[Is Web Scraping Legal?](https://scrapfly.io/is-web-scraping-legal)•[Open Source Scrapers](https://github.com/scrapfly/scrapfly-scrapers)
