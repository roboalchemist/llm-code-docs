# Source: https://scrapfly.io/docs/release-notes

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/release-notes

Markdown Content:
Scrapfly Product Release Notes
------------------------------

[Subscribe to RSS Feed](https://scrapfly.io/docs/release-notes/feed.xml)

Filter by product:

[2026-02-20](https://scrapfly.io/docs/release-notes#date-2026-02-20)
--------------------------------------------------------------------

#### [Web Scraping API](https://scrapfly.io/docs/release-notes#p-2026-02-20-web-scraping-api)

FEATURE

**New `select` JavaScript Scenario action.** Select options from dropdown menus as part of your browser automation scenarios. Supports both native HTML `<select>` elements and custom dropdown widgets (React Select, Material UI, etc.) with real human-like interaction.

**Supported selection methods:**

*   **Native `<select>` by value** — `{"select": {"selector": "select#country", "value": "US"}}`
*   **Custom dropdown by CSS attribute** — `{"select": {"selector": ".dropdown", "option_selector": ".option[value='US']"}}`
*   **Custom dropdown by visible text** — `{"select": {"selector": ".dropdown", "option_selector": ".item", "text": "Germany"}}`
*   **Custom dropdown by index** — `{"select": {"selector": ".dropdown", "option_selector": "[role='option']", "index": 2}}`

[See the JavaScript Scenario documentation](https://scrapfly.io/docs/scrape-api/javascript-scenario)

[2026-02-18](https://scrapfly.io/docs/release-notes#date-2026-02-18)
--------------------------------------------------------------------

#### [Scrapium Browser](https://scrapfly.io/docs/release-notes#p-2026-02-18-scrapium-browser)

RELEASE

**Scrapium Browser v145 released (Chromium 145).** This version introduces a new Antibot CDP domain for browser automation and human simulation, delivering improved stealth and significantly fewer errors during automation operations.

**Key improvements:**

*   **New Antibot CDP Domain** — A new way to automate and simulate human interactions directly within the browser process, enabling lower-latency and more reliable execution
*   **Cross-Frame Support** — Automation commands now work seamlessly across iframes and nested frames, eliminating common errors when interacting with cross-origin content
*   **Better Humanization** — Improved human simulation with more natural mouse movements, clicks, scrolling, and keyboard input
*   **Multi-Brand Browser Spoofing (Private Beta)** — Spoof browser identity as Brave, Microsoft Edge, or Opera in addition to Chrome for enhanced fingerprint diversity

**Automatically available on all services** — No configuration required:

*   Web Scraping API
*   Screenshot API
*   Crawler API
*   Cloud Browser Service

[2026-02-14](https://scrapfly.io/docs/release-notes#date-2026-02-14)
--------------------------------------------------------------------

#### [Web Scraping API](https://scrapfly.io/docs/release-notes#p-2026-02-14-web-scraping-api)

FEATURE

**Proxy Mode now available.** Use Scrapfly as a standard HTTP/HTTPS forward proxy with any third-party tool that supports proxy configuration — SEO crawlers (Screaming Frog), automation platforms (Apify, Crawlee), monitoring tools, and data pipelines.

**Key features:**

*   **Drop-in proxy URL** — Configure any tool's proxy settings with Scrapfly's endpoint, no SDK needed
*   **Options in username** — Encode scraping options (country, ASP, JS rendering, etc.) as dash-separated key-value pairs in the proxy username
*   **Rich API options** — JavaScript rendering, anti-bot protection, proxy rotation, caching, extraction, and more
*   **HTTP and HTTP/2 transport** — Supports both HTTP/1.1 and HTTP/2 as proxy transport protocols
*   **Standard HTTP proxy protocol** — Works with HTTP and HTTPS CONNECT methods
*   **Response metadata** — `X-Scrapfly-*` headers provide cost, timing, and error details alongside the target response
*   **API Player integration** — Generate proxy URLs directly from the dashboard

[See the Proxy Mode documentation](https://scrapfly.io/docs/scrape-api/proxy-mode)

[2026-01-19](https://scrapfly.io/docs/release-notes#date-2026-01-19)
--------------------------------------------------------------------

#### [Scrapium Browser](https://scrapfly.io/docs/release-notes#p-2026-01-19-scrapium-browser)

RELEASE

**Scrapium Browser v144 released with HTTP/3, QUIC, and UDP support.** This version matches Chromium 144 and introduces next-generation protocol support for enhanced stealth and fingerprint accuracy.

**Key improvements:**

*   **HTTP/3 Protocol Support** - Modern web protocol over QUIC for improved performance and stealth
*   **QUIC Transport Layer** - Low-latency multiplexed connections with better congestion control
*   **UDP Proxy Support** - Full support for HTTP/3/QUIC/UDP proxy connections

HTTP/3 and QUIC provide significant advantages for web scraping by matching real browser fingerprints more accurately. Modern browsers like Chrome, Firefox, and Safari all support HTTP/3, making it essential for avoiding detection on HTTP/3-enabled websites.

**Automatically available on all services** - No configuration required:

*   Web Scraping API
*   Screenshot API
*   Crawler API
*   Cloud Browser Service

#### [Web Scraping API](https://scrapfly.io/docs/release-notes#p-2026-01-19-web-scraping-api)

FEATURE

**HTTP/3, QUIC, and UDP protocols now automatically enabled.** Our infrastructure has been upgraded to support next-generation web protocols for enhanced fingerprint accuracy and stealth.

**What's new:**

*   **Curlium HTTP/3 Support** - HTTP client library upgraded with HTTP/3, QUIC, and UDP protocol support
*   **Proxy Network HTTP/3** - Residential, datacenter, and mobile proxies now support HTTP/3/QUIC/UDP
*   **Automatic Protocol Negotiation** - Seamless fallback to HTTP/2 or HTTP/1.1 when needed
*   **Zero Configuration** - Available automatically on Web Scraping API, Screenshot API, Crawler API, and Cloud Browser Service

**Why HTTP/3 matters for stealth:**

HTTP/3 and QUIC enable better fingerprint matching with real browsers and improved performance through reduced latency and connection overhead. Since HTTP/3 is increasingly adopted by major websites and CDNs, using these protocols helps your requests blend in with legitimate traffic, reducing the risk of detection on websites that analyze protocol-level fingerprints.

All proxy types now support these protocols without any additional configuration.

[2026-01-07](https://scrapfly.io/docs/release-notes#date-2026-01-07)
--------------------------------------------------------------------

#### [Python SDK](https://scrapfly.io/docs/release-notes#p-2026-01-07-python-sdk)

RELEASE

[2026-01-04](https://scrapfly.io/docs/release-notes#date-2026-01-04)
--------------------------------------------------------------------

#### [Antibot Detector](https://scrapfly.io/docs/release-notes#p-2026-01-04-antibot-detector)

RELEASE

**Antibot Detector 2.4 released.**

*   **Fix badge/popup desync** - Popup now correctly shows detection results when badge displays count
*   Root cause: Badge updates early (in processDetectionData), but cache write happens later (in finalizeDetection)
*   Fix: Check badge count and use `state.mainData` directly without waiting for `state.expiry`
*   **Fix "Extension context invalidated" errors** - Logger now gracefully handles extension reload
*   **Fix memory leaks** - Clean up `finalizationDebounce` and `batchProcessingFlags` Maps on tab close/URL change

The Chrome extension for detecting antibot protection has been updated.

[View release on GitHub](https://github.com/scrapfly/Antibot-Detector/releases/tag/v2.4)

[See the Antibot Detector documentation](https://scrapfly.io/docs/tools/antibot-detector)

[2025-12-22](https://scrapfly.io/docs/release-notes#date-2025-12-22)
--------------------------------------------------------------------

#### [Screenshot API](https://scrapfly.io/docs/release-notes#p-2025-12-22-screenshot-api)

FEATURE

**Vision Deficiency Simulation now available for accessibility testing.** Capture screenshots that simulate how web pages appear to users with various visual impairments, enabling WCAG, ADA, and Section 508 compliance testing.

**Supported vision deficiency types:**

*   **Deuteranopia** - Red-green color blindness (green-blind), affects ~6% of males
*   **Protanopia** - Red-green color blindness (red-blind), affects ~2% of males
*   **Tritanopia** - Blue-yellow color blindness
*   **Achromatopsia** - Complete color blindness (monochromacy)
*   **Blurred Vision** - Simulates uncorrected refractive errors

Use the `vision_deficiency` parameter to test your pages for accessibility compliance.

[Learn more about accessibility testing](https://scrapfly.io/docs/screenshot-api/accessibility)

#### [Dashboard](https://scrapfly.io/docs/release-notes#p-2025-12-22-dashboard)

FEATURE

**Screenshot API Visual Player now available.** A dedicated interactive playground for the Screenshot API, allowing you to configure, test, and preview screenshot captures directly in your browser.

**Key features:**

*   **Live Preview** - See screenshot results instantly with full-size image preview
*   **All Parameters** - Configure capture mode (fullpage, viewport, element selector), resolution, format (JPG, PNG, WebP, GIF), and rendering options
*   **Visual Options** - Dark mode, banner blocking, print media format, and image loading controls
*   **Cost Estimation** - Real-time API credit cost estimation with bandwidth warnings
*   **Code Snippets** - Auto-generated code snippets for Python, TypeScript, Go, and cURL
*   **Webhook Support** - Test asynchronous screenshot requests with webhook integration
*   **Log Replay** - Replay previous screenshot requests directly from the monitoring log

[Try the Screenshot API Player](https://scrapfly.io/dashboard/playground/screenshot)

[2025-12-19](https://scrapfly.io/docs/release-notes#date-2025-12-19)
--------------------------------------------------------------------

IMPROVEMENT

**Enhanced AI Extraction with Structured Output.** Our AI-powered extraction engine has been significantly upgraded to deliver more accurate and reliable structured data.

**Key improvements:**

*   **Guaranteed Schema Compliance** - Extracted data now strictly adheres to the defined schema structure, eliminating malformed outputs
*   **Smarter Computed Fields** - Enhanced intelligence for derived fields like sentiment analysis, date formatting, and currency normalization
*   **Automatic Currency Detection** - Currency symbols are now automatically converted to ISO3 codes (e.g., $ → USD, € → EUR, £ → GBP)
*   **Intelligent Date Parsing** - Raw dates in any format are automatically normalized to standard YYYY-MM-DD format
*   **Improved Sentiment Analysis** - More accurate sentiment detection with confidence scores for review extraction

These improvements apply to all extraction schemas including Product, Article, Review, Real Estate, Job Posting, and more.

[Explore the Extraction API documentation](https://scrapfly.io/docs/extraction-api/getting-started)

[2025-12-16](https://scrapfly.io/docs/release-notes#date-2025-12-16)
--------------------------------------------------------------------

#### [MCP Server](https://scrapfly.io/docs/release-notes#p-2025-12-16-mcp-server)

RELEASE

**MCP Server 1.0.9 released.**

The Scrapfly MCP (Model Context Protocol) server has been updated.

[View release on GitHub](https://github.com/scrapfly/scrapfly-mcp/releases/tag/v1.0.9)

[2025-12-13](https://scrapfly.io/docs/release-notes#date-2025-12-13)
--------------------------------------------------------------------

#### [Scrapium Browser](https://scrapfly.io/docs/release-notes#p-2025-12-13-scrapium-browser)

RELEASE

Scrapium Browser v143 released. This version match with Chromium 143 and continue to improve antibot detection and scraping capabilities.

Following services are automatically upgraded:

*   Cloud Browser Service
*   Web Scraping API
*   Screenshot API

[2025-12-10](https://scrapfly.io/docs/release-notes#date-2025-12-10)
--------------------------------------------------------------------

#### [MCP Server](https://scrapfly.io/docs/release-notes#p-2025-12-10-mcp-server)

ANNOUNCEMENT

**Scrapfly MCP Server now available for self-hosting.** You can now run the Scrapfly MCP (Model Context Protocol) server on your own infrastructure for enhanced privacy and control.

The self-hosted MCP server provides the same powerful web scraping capabilities through a standardized protocol, allowing seamless integration with AI assistants and automation tools.

**Key features:**

*   Full control over your scraping infrastructure
*   Compatible with Claude, GPT, and other MCP-enabled AI assistants
*   Easy Docker deployment
*   All Scrapfly API features available

[View the MCP Server repository on GitHub](https://github.com/scrapfly/scrapfly-mcp)

#### [Go SDK](https://scrapfly.io/docs/release-notes#p-2025-12-10-go-sdk)

RELEASE

**Go SDK officially released.** Scrapfly now offers a native Go SDK for seamless integration with your Go applications.

The Go SDK provides a clean, idiomatic API for accessing all Scrapfly services including Web Scraping API, Screenshot API, and Extraction API.

**Key features:**

*   Full Web Scraping API support
*   Screenshot API integration
*   Extraction API support
*   Async and concurrent scraping
*   Comprehensive error handling
*   Well-documented with examples

Install with `go get github.com/scrapfly/go-scrapfly`

[See the Go SDK documentation](https://scrapfly.io/docs/sdk/golang)

[2025-11-27](https://scrapfly.io/docs/release-notes#date-2025-11-27)
--------------------------------------------------------------------

#### [Web Scraping API](https://scrapfly.io/docs/release-notes#p-2025-11-27-web-scraping-api)

FEATURE

**Proxified Response now transparently handles CLOB and BLOB content.** When using `proxified_response=true`, large content (over 5MB) that would normally be stored as CLOB (text) or BLOB (binary) is now streamed directly to you without any additional API calls.

Previously, large responses required a separate request to retrieve the content. Now the API automatically streams the content transparently, making integration simpler for large files like PDFs, images, and datasets.

Learn more in the [Web Scraping API documentation](https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxified_response).

#### [Dashboard](https://scrapfly.io/docs/release-notes#p-2025-11-27-dashboard)

FEATURE

**Proxified Response mode available in API Player.** Test the `proxified_response` parameter directly in the dashboard.

[2025-11-26](https://scrapfly.io/docs/release-notes#date-2025-11-26)
--------------------------------------------------------------------

#### [Go SDK](https://scrapfly.io/docs/release-notes#p-2025-11-26-go-sdk)

RELEASE

[2025-11-17](https://scrapfly.io/docs/release-notes#date-2025-11-17)
--------------------------------------------------------------------

#### [Crawler API](https://scrapfly.io/docs/release-notes#p-2025-11-17-crawler-api)

ANNOUNCEMENT

**Crawler API released in EARLY ACCESS.** This powerful API allows you to crawl entire websites with advanced configuration options.

The Crawler API is perfect for discovering and scraping content at scale across multiple pages, with intelligent depth control and filtering capabilities.

**Key features:**

*   Configurable crawl depth and page limits
*   URL filtering with include/exclude path patterns
*   Automatic sitemap and robots.txt processing
*   Multiple content format support (HTML, Markdown, Text, Clean HTML)
*   Built-in extraction rules for structured data
*   Real-time webhook notifications
*   Content caching and TTL configuration
*   Batch content retrieval with multipart responses
*   Export and import crawler configurations

Discover the [Crawler API documentation](https://scrapfly.io/docs/crawler-api/getting-started) and start crawling in your [dashboard](https://scrapfly.io/dashboard/playground/crawler).

#### [Dashboard](https://scrapfly.io/docs/release-notes#p-2025-11-17-dashboard)

FEATURE

**Extraction API Player added to Dashboard.** Test and debug extraction rules on already-scraped content directly in your browser.

The Extraction API Player is perfect for replaying extraction on cached content, data lake documents, or previously scraped pages without re-scraping the target website.

**Key features:**

*   Test extraction on custom HTML/text content
*   Try all extraction methods (AI Model, LLM Prompt, Manual Template)
*   Pre-configured examples for quick start
*   Live preview of extracted data
*   Code snippets in multiple languages
*   Load content directly from crawler results
*   Export and share extraction configurations

Access the [Extraction API Player](https://scrapfly.io/dashboard/playground/extraction) and learn more in the [Extraction API documentation](https://scrapfly.io/docs/extraction-api/getting-started).

[2025-11-05](https://scrapfly.io/docs/release-notes#date-2025-11-05)
--------------------------------------------------------------------

#### [Web Scraping API](https://scrapfly.io/docs/release-notes#p-2025-11-05-web-scraping-api)

FEATURE

**Browser Downloads & File Attachments now supported.** When Javascript Rendering is enabled, Scrapfly browsers now automatically capture files downloaded during browser interactions.

This powerful feature allows you to retrieve documents, PDFs, spreadsheets, and other file attachments that are triggered by button clicks, form submissions, or other browser interactions.

Downloaded files are automatically captured and stored on Scrapfly's servers, with metadata and download URLs available in the API response under `result.browser_data.attachments`.

**Key features:**

*   Automatic capture of all browser downloads
*   Support for all file types (PDFs, spreadsheets, documents, archives, etc.)
*   Authenticated download URLs with API key
*   Automatic duplicate filename handling
*   Visible in monitoring dashboard Attachments tab

Learn more in the [Browser Downloads documentation](https://scrapfly.io/docs/scrape-api/javascript-rendering#browser_downloads).

[2025-11-04](https://scrapfly.io/docs/release-notes#date-2025-11-04)
--------------------------------------------------------------------

#### [N8N Integration](https://scrapfly.io/docs/release-notes#p-2025-11-04-n8n-integration)

RELEASE

[2025-11-01](https://scrapfly.io/docs/release-notes#date-2025-11-01)
--------------------------------------------------------------------

#### [Scrapium Browser](https://scrapfly.io/docs/release-notes#p-2025-11-01-scrapium-browser)

RELEASE

Scrapium Browser v142 released. This version match with Chromium 142 and continue to improve antibot detection and scraping capabilities.

Following services are automatically upgraded:

*   Cloud Browser Service
*   Web Scraping API
*   Screenshot API

[2025-10-15](https://scrapfly.io/docs/release-notes#date-2025-10-15)
--------------------------------------------------------------------

#### [Scrapium Browser](https://scrapfly.io/docs/release-notes#p-2025-10-15-scrapium-browser)

RELEASE

Scrapium Browser v141 released. This version match with Chromium 141 and continue to improve antibot detection and scraping capabilities.

Following services are automatically upgraded:

*   Cloud Browser Service
*   Web Scraping API
*   Screenshot API

[2025-09-21](https://scrapfly.io/docs/release-notes#date-2025-09-21)
--------------------------------------------------------------------

#### [Dashboard](https://scrapfly.io/docs/release-notes#p-2025-09-21-dashboard)

FEATURE

Multi factor authentication (MFA) is now available for all users to improve the security of your account. It works for individual and team accounts. You can now enable it from your [dashboard security settings](https://scrapfly.io/dashboard/settings).

[2025-05-20](https://scrapfly.io/docs/release-notes#date-2025-05-20)
--------------------------------------------------------------------

#### [Scrapium Browser](https://scrapfly.io/docs/release-notes#p-2025-05-20-scrapium-browser)

RELEASE

Scrapium Browser v137 released. This version match with Chromium 137 and continue to improve antibot detection and scraping capabilities.

Following services are automatically upgraded:

*   Cloud Browser Service
*   Web Scraping API
*   Screenshot API

[2025-04-29](https://scrapfly.io/docs/release-notes#date-2025-04-29)
--------------------------------------------------------------------

#### [Python SDK](https://scrapfly.io/docs/release-notes#p-2025-04-29-python-sdk)

RELEASE

[2025-04-20](https://scrapfly.io/docs/release-notes#date-2025-04-20)
--------------------------------------------------------------------

#### [Proxy Saver](https://scrapfly.io/docs/release-notes#p-2025-04-20-proxy-saver)

ANNOUNCEMENT

**Proxy Saver** is now available in public beta. Proxy saver allows you to cut cost on proxy provider by reducing the bandwidth usage and leverage distributed http cache, reuse connection and more. (Compatible with any proxy provider on the market and private proxies).

*   [See the Proxy Saver documentation](https://scrapfly.io/docs/proxy-saver/getting-started)
*   [Acces Proxy Saver Dasbhoard](https://scrapfly.io/dashboard/proxy-saver)

[2024-12-28](https://scrapfly.io/docs/release-notes#date-2024-12-28)
--------------------------------------------------------------------

#### [Dashboard](https://scrapfly.io/docs/release-notes#p-2024-12-28-dashboard)

FEATURE

Team feature is now available in the dashboard. You can now invite your team members to collaborate on your projects and configure their access rights.

You can see the [documentation](https://scrapfly.io/docs/workspace-and-team), and discover it in your [dashboard](https://scrapfly.io/dashboard/team).

[2024-11-09](https://scrapfly.io/docs/release-notes#date-2024-11-09)
--------------------------------------------------------------------

#### [TypeScript SDK](https://scrapfly.io/docs/release-notes#p-2024-11-09-typescript-sdk)

RELEASE

**TypeScript SDK 0.6.9 released.**

*   change Extraction API parameters names to match API parameter names:
*   `ephemeral_template` ->`extraction_ehphemeral_template`
*   `template` ->`extraction_template`
*   old parameter names are still available with a deprecation warning

**Update instructions:**

*   npm: `npm install scrapfly-sdk@0.6.9`
*   JSR: `jsr add @scrapfly/scrapfly-sdk@0.6.9`

[View release on GitHub](https://github.com/scrapfly/typescript-scrapfly/releases/tag/v0.6.9)

[See the TypeScript SDK documentation](https://scrapfly.io/docs/sdk/typescript)

[2024-06-10](https://scrapfly.io/docs/release-notes#date-2024-06-10)
--------------------------------------------------------------------

#### [Web Scraping API](https://scrapfly.io/docs/release-notes#p-2024-06-10-web-scraping-api)

CHANGED

**Web Scraping API now announce the debug replay url**, when you are using the `debug` parameter in the Web Scraping API, the response will now contain a `content_replay_url` in `context.debug` to replay a scrape against the exact same content.

This URL need to be authenticated with the same API key used to perform the scrape.

```
context {
      debug: {
        screenshot_url: "https://api.scrapfly.io/11cd6abe-5061-4dce-8d37-5d50e667a071/scrape/screenshot/ee8484c6-ee5f-4775-a665-0a2b57631c1c/debug",
        response_url: "https://api.scrapfly.io/scrape/debug/ee8484c6-ee5f-4775-a665-0a2b57631c1c",
        content_replay_url: "https://api.scrapfly.io/scrape/debug/ee8484c6-ee5f-4775-a665-0a2b57631c1c/replay",
      }
    }
```

For more information, refer to the [Web Scraping API documentation](https://scrapfly.io/docs/scrape-api/debug)

[2024-06-04](https://scrapfly.io/docs/release-notes#date-2024-06-04)
--------------------------------------------------------------------

#### [Screenshot API](https://scrapfly.io/docs/release-notes#p-2024-06-04-screenshot-api)

ANNOUNCEMENT

**Screenshot API released.** This API allows you to take screenshots of web pages, much simpler than the Web Scraping API and all preset pre configured (Image load, High quality, Rendering wait)

**Screenshot API provide some unique features:**

*   Multiple image format (jpg, png, webp, gif)
*   Multiple capture mode (custom viewport, fullpage, vertical, elements)
*   Custom resolution
*   Caching
*   Page options (Dark mode, block banners, block ads, print format)

You can now discover the [Screenshot API in the API documentation](https://scrapfly.io/docs/screenshot-api/getting-started).

ANNOUNCEMENT

**Extraction API released in BETA.** This API allows you to extract structured data from web pages. It comes with 3 modes of extraction:

*   **Custom rules with extraction template:** define your own extraction rules, formatters, and filters
*   **LLM Prompt Extraction:** Extract or ask question about the document using our pre-trained LLM model dedicated to web scraping
*   **Automatic extraction:** Choose a model of extraction based on the type of page (product, job, article, etc.) and retrieved the structured data and metadata information to evaluate the quality of the extraction

You can now discover the [Extraction API in the API documentation](https://scrapfly.io/docs/extraction-api/getting-started).

#### [Web Scraping API](https://scrapfly.io/docs/release-notes#p-2024-06-04-web-scraping-api)

FEATURE

FIXED

Fixed an issue where the Web Scraping API screenshot return the image with an invalid IANA content type `image/jpg` instead of `image/jpeg`

CHANGED

The `proxified_response` parameter, when using `extraction_template` or `extraction_prompt` or `extraction_model`, now return the `content-type` of the extracted data instead of the original response content-type.

More information about the `proxified_response` parameter in the [Web Scraping API documentation](https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxified_response)

CHANGED

The `format` parameter now accept options to **configure the output format** of the scraped page.

Markdown format now allow to:

*   Disable images `no_links` and use the alt text instead
*   Disable links `no_images` and use the anchor instead

By using the following notation: `markdown:no_links,no_images` - `{format}:{option1},{optionN}`

To lean more about those formats, refer to the [Web Scraping API documentation](https://scrapfly.io/docs/scrape-api/getting-started#api_param_format)

[2024-04-24](https://scrapfly.io/docs/release-notes#date-2024-04-24)
--------------------------------------------------------------------

#### [Python SDK](https://scrapfly.io/docs/release-notes#p-2024-04-24-python-sdk)

RELEASE

**Python SDK 0.8.17 released.** This version introduce the support of:

*   Web Scraping API `format` parameter
*   Web Scraping API `screenshot_flags` parameter

You can now install the new version with `pip install scrapfly-sdk==0.8.17` or upgrade with `pip install --upgrade scrapfly-sdk`

[See the Python SDK documentation](https://github.com/scrapfly/python-scrapfly)[PyPi package](https://pypi.org/project/scrapfly-sdk/)

#### [Javascript SDK](https://scrapfly.io/docs/release-notes#p-2024-04-24-javascript-sdk)

RELEASE

**Javascript SDK 0.5.0 released.** This version introduce the support of:

*   Web Scraping API `format` parameter
*   Web Scraping API `screenshot_flags` parameter

You can now install the new version with `npm install scrapfly-sdk@0.5.0` or upgrade with `npm install scrapfly-sdk@latest`

[See the Javascript SDK documentation](https://github.com/scrapfly/typescript-scrapfly)[NPM package](https://www.npmjs.com/package/scrapfly-sdk)

[2024-04-22](https://scrapfly.io/docs/release-notes#date-2024-04-22)
--------------------------------------------------------------------

#### [Python SDK](https://scrapfly.io/docs/release-notes#p-2024-04-22-python-sdk)

ANNOUNCEMENT

ANNOUNCEMENT

#### [Web Scraping API](https://scrapfly.io/docs/release-notes#p-2024-04-22-web-scraping-api)

FEATURE

**Introduce a new parameter `format`** to the Web Scraping API to allow you to convert the scraped page to a specific format. With the rise of LLM usage, you can now convert into friendly LLM format and more.

You can now convert the scraped page to:

*   `markdown`
*   `text`
*   `json` (auto parse)
*   `clean_html`

If you are using `proxified_response` to directly retrieve the content, the announced `content-type` will follow the format you choose.

To lean more about those formats, refer to the [Web Scraping API documentation](https://scrapfly.io/docs/scrape-api/getting-started#api_param_format)

FEATURE

You can now pass flags to **configure screenshot** options directly from the Web Scraping API.

Available flags:

*   `load_images`
*   `dark_mode`
*   `block_banners`
*   `high_quality`
*   `print_media_format`

To lean more about those flags, refer to the [Web Scraping API documentation](https://scrapfly.io/docs/scrape-api/getting-started#api_param_screenshot_flags)
