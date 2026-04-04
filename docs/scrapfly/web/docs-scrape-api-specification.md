# Source: https://scrapfly.io/docs/scrape-api/specification

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/specification

Markdown Content:
Getting Started with Scrapfly
-----------------------------

Discover how to use Scrapfly API - the basics, available parameters and features, error handling and other information related to the API use.

Minimal API call is a GET, POST, PUT, PATCH or HEAD request with `url` and `key` parameters:

`https://api.scrapfly.io/scrape?url=&key=`

[On Steroids](https://scrapfly.io/docs/scrape-api/getting-started#onste)
------------------------------------------------------------------------

*    Smart defaults - **scrape without being blocked**. Scrapfly pre-configures user-agent and other request headers. 
*   [Anti Scraping Protection](https://scrapfly.io/docs/scrape-api/anti-scraping-protection) feature bypasses all anti-scraping systems. 
*    By default, the API responds in JSON. Though, a more efficient `msgpack` format is also available by setting the accept: application/msgpack header. 
*    Text content is returned as utf-8 while binary is encoded in base64, so you can scrape any kind of data (pdf, zip, etc) 
*    Gzip compression is available through content-encoding: gzip header. 
*    Ability to [debug and replay scrape requests](https://scrapfly.io/docs/scrape-api/debug) from the dashboard log page and API. 
*   [Handle large payload](https://scrapfly.io/docs/scrape-api/specification#handle_large_object), large text response greater than 5MB are called "CLOB" (Character Large Object) and binary are called "BLOB" (Binary Large Object) and can be downloaded separately with streaming support. 

[Quality of Life](https://scrapfly.io/docs/scrape-api/getting-started#qol)
--------------------------------------------------------------------------

*    All scrape requests and metadata are automatically tracked on a [Web Dashboard](https://scrapfly.io/docs/monitoring)
*    Multi project/scraper support through [Project Management](https://scrapfly.io/docs/project)
*    Experiment with the [Visual API playground](https://scrapfly.io/dashboard/playground/web-scraper)
*   [Status page](https://scrapfly.statuspage.io/) with notification subscription. 
*    Full API transparency through useful meta headers: 
    *   **X-Scrapfly-Api-Cost** API Cost billed 
    *   **X-Scrapfly-Remaining-Api-Credit** Remaining Api Credit, if 0, billed in extra credit 
    *   **X-Scrapfly-Account-Concurrent-Usage** You current concurrency usage of your account 
    *   **X-Scrapfly-Account-Remaining-Concurrent-Usage** Maximum concurrency allowed by the account 
    *   **X-Scrapfly-Project-Concurrent-Usage** Concurrency usage of the project 
    *   **X-Scrapfly-Project-Remaining-Concurrent-Usage** If the concurrency limit is set on the project otherwise equal to the account concurrency 

Concurrency is defined by your subscription

[Billing](https://scrapfly.io/docs/scrape-api/getting-started#billing)
----------------------------------------------------------------------

Scrapfly uses a credit system to bill scrape API requests where each scrape request has a variable cost based on:

*   Enabled scrape features and options (browser rendering, blocking bypass etc.).
*   Response body type (binary vs text results).
*   [ASP](https://scrapfly.io/docs/scrape-api/anti-scraping-protection) feature can override scrape config details to bypass blocking which can alter the overall cost. 

For more information see [scrape API billing breakdown](https://scrapfly.io/docs/scrape-api/billing#billing).

Billing is reported in every scrape response and the monitoring dashboard and can be controlled through Scrapfly budget settings. For more see [Web Scraper Billing](https://scrapfly.io/docs/scrape-api/billing).

[Handle Large Object](https://scrapfly.io/docs/scrape-api/getting-started#handle_large_object)
----------------------------------------------------------------------------------------------

Large object `CLOB` for text and `BLOB` are offloaded from the API response to prevent any CPU/RAM issue with your JSON/MSGPACK decoder and increase the efficiency of your scrapers.

Instead of the actual content in `response.result.content`, you get an URL to download the large object. The URL is valid until the log expire.

*   `response.result.format` indicate whether it's a large object by checking if it's `blob` or `clob`
*   `response.result.content` contains the url to download the content. This url need to be authenticated with your API Key (Must be the API key that belong to project/env)
*   `BLOB` is not base64 encoded like `binary` format, you directly retrieve the binary data and the `Content-Type` header announce the actual type

[Errors](https://scrapfly.io/docs/scrape-api/getting-started#error_handling)
----------------------------------------------------------------------------

Scrapfly uses conventional HTTP response codes to indicate the success or failure of an API request.

**Codes in the 2xx** range indicate success.

**Codes in the 4xx** range indicate an error that failed given the information provided (e.g., a required parameter was omitted, not permitted, max concurrency reached, etc.).

**Codes in the 5xx** range indicate an error with Scrapfly's servers.

* * *

**HTTP 422 - Request Failed** provide extra headers in order to help as much as possible:

*   **X-Scrapfly-Reject-Code:** Error Code 
*   **X-Scrapfly-Reject-Description:** URL to the related documentation 
*   **X-Scrapfly-Reject-Retryable:** Indicate if the scrape is retryable 

> It is important to properly handle HTTP client errors in order to access the error headers and body. These details contain valuable information for troubleshooting, resolving the issue or reaching the support.

### HTTP Status Code Summary

| 200 - OK | Everything worked as expected. |
| --- |
| 400 - Bad Request | The request was unacceptable, often due to missing a required parameter or a bad value or a bad format. |
| 401 - Unauthorized | No valid API key provided. |
| 402 - Payment Required | A payment issue occur and need to be resolved |
| 403 - Forbidden | The API key doesn't have permissions to perform the request. |
| 422 - Request Failed | The parameters were valid but the request failed. |
| 429 - Too Many Requests | All free quota used or max allowed concurrency or domain throttled |
| 500, 502, 503 - Server Errors | Something went wrong on Scrapfly's end. |
| 504 - Timeout | The scrape have timeout |
| You can check out the [full error list](https://scrapfly.io/docs/scrape-api/errors) to learn more. |

* * *

[Specification](https://scrapfly.io/docs/scrape-api/getting-started#spec)
-------------------------------------------------------------------------

Scrapfly has loads of features and the best way to discover them is through the specification docs below.

If you have any questions you can check out the [Frequently asked question section](https://scrapfly.io/docs/scrape-api/faq) or see the [support chat](https://scrapfly.io/docs/support).

> **By default, the API has a read timeout of 155 seconds.**To avoid read timeout errors, you must configure your HTTP client to set the read timeout to 155 seconds. If you need a different timeout value, please refer to the documentation for information on [how to control the timeout.](https://scrapfly.io/docs/scrape-api/understand-timeout)

Try out the API directly in your terminal using `curl`:

*   [GET](https://scrapfly.io/docs/scrape-api/specification#GET)
*   [POST](https://scrapfly.io/docs/scrape-api/specification#POST)
*   [PUT](https://scrapfly.io/docs/scrape-api/specification#PUT)
*   [PATCH](https://scrapfly.io/docs/scrape-api/specification#PATCH)
*   [HEAD](https://scrapfly.io/docs/scrape-api/specification#HEAD)
*   [OPTIONS](https://scrapfly.io/docs/scrape-api/specification#OPTIONS)

`curl -X GET https://api.scrapfly.io/scrape?url=https://httpbin.dev/anything?q=I%20want%20to%20Scrape%20this&country=us&render_js=true&key=`

`curl -X POST https://api.scrapfly.io/scrape?url=https://httpbin.dev/anything?q=I%20want%20to%20Scrape%20this&country=us&render_js=true&key= -H content-type: text/json --data-raw "{\"test\": \"example\"}"`

`curl -X PUT https://api.scrapfly.io/scrape?url=https://httpbin.dev/anything?q=I%20want%20to%20Scrape%20this&country=us&render_js=true&key= -H content-type: text/json --data-raw "{\"test\": \"example\"}"`

`curl -X PATCH https://api.scrapfly.io/scrape?url=https://httpbin.dev/anything?q=I%20want%20to%20Scrape%20this&country=us&render_js=true&key= -H content-type: text/json --data-raw "{\"test\": \"example\"}"`

`curl -X OPTIONS https://api.scrapfly.io/scrape?url=https://httpbin.dev/anything&country=us&render_js=true&key= -H content-type: text/json --data-raw "{\"test\": \"example\"}"`

`curl -I https://api.scrapfly.io/scrape?url=https://httpbin.dev/anything?q=I%20want%20to%20Scrape%20this&country=us&render_js=true&key=`

Want to try out the API without coding? Check out our visual API player and test/generate code to use our API.

[Checkout The Web Player](https://scrapfly.io/dashboard/playground/web-scraper)

The default response format is JSON, and the scraped content is available in `result.content`. Your scrape configuration is present in `config`, and other activated feature information is available in `context`. To get the HTML page directly, refer to the [`proxified_response`](https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxified_response) parameter.

Required Parameters

`https://httpbin.dev/anything?q=test`

API Key for authentication. Find your key on [dashboard](https://scrapfly.io/docs/project#api-keys)

`scp-live-xxx...`

Proxy & Location

Select proxy pool. See [proxy dashboard](https://scrapfly.io/dashboard/proxy) for available pools and pricing

`public_datacenter_pool``public_residential_pool`

Proxy country (ISO 3166-1 alpha-2). Supports exclusions (`-gb`) and weighted distribution (`us:10,gb:5`)

`us``us,ca,mx``-gb`

 More details

**Country selection modes:**

*   **Single country:**`country=us`
*   **Multiple countries:**`country=us,ca,mx` (random selection)
*   **Exclusions:**`country=-gb` (exclude UK)
*   **Weighted:**`country=us:10,gb:5` (2x more US than UK)

Page language (sets `Accept-Language` header). Defaults to proxy location language

`en``fr-FR,en`

 More details

**How it works:**

*   Sets the `Accept-Language` HTTP header automatically
*   The `Accept-Language` header cannot be set manually via `headers` parameter
*   Multiple languages can be listed in priority order

**Examples:**

*   `lang=en` - English content
*   `lang=fr-FR,en` - French (France) preferred, English fallback
*   `lang=en-IN,en-US` - English (India) preferred, US English fallback

When supported by the target website, the returned content will be in the specified language.

Operating System. Cannot be set with custom `User-Agent` header

`win11``mac``linux`

Request Configuration

`30000``120000`

Retry on failure (network errors, HTTP 5xx). Has impact on timeout

`true``false`

Response Format

Output format: `raw`, `clean_html`, `json`, `markdown`, `text`. Markdown/text support `:no_links,no_images,only_content` options

`raw``markdown``text`

 More details

**Available formats:**

*   `raw` - Original HTML as-is
*   `clean_html` - Cleaned and sanitized HTML
*   `json` - Attempt to parse as JSON
*   `markdown` - Convert to Markdown
*   `text` - Extract plain text

**Format options (markdown/text only):**

*   `format=markdown:no_links` - Remove links
*   `format=text:no_images` - Remove image references
*   `format=markdown:only_content` - Extract main content only

Combine options: `format=markdown:no_links,no_images,only_content`

Return scraped content directly as response body (instead of JSON wrapper). Large objects (CLOB/BLOB) are auto-streamed

`true``false`

 More details

**When enabled:**

*   Page content becomes the response body directly
*   Actual HTTP status codes and headers from target are returned
*   Works with custom `format` options (JSON, markdown, etc.)
*   Large objects (CLOB/BLOB) are streamed automatically

**Available Scrapfly headers:**

*   `X-Scrapfly-Content-Format` - Data type (text or binary)
*   `X-Scrapfly-Log` - Log ID for debugging
*   `X-Scrapfly-Api-Cost` - Credits charged
*   `X-Scrapfly-Remaining-Api-Credit` - Remaining credits
*   `X-Scrapfly-Reject-Code` - Error code (on failures)

When using data extraction, extracted data is available in `result.extracted_data` with corresponding content-type.

Debugging & Tracking

Store API result and take screenshot (if render_js enabled). Enable when contacting support

`true``false`

`e3ba784cde0d`

Query and retrieve target DNS information

`true``false`

Pull remote SSL certificate and TLS info. Only for `https://` targets

`true``false`

Queue request and redirect response to webhook. Create webhooks in [dashboard](https://scrapfly.io/dashboard/webhook)

`my-webhook-name`

Data Extraction

Anti Scraping Protection

`true``false`

 More details

**Anti Scraping Protection** automatically handles:

*   CAPTCHA challenges and bot detection
*   JavaScript challenges (Cloudflare, PerimeterX, etc.)
*   Browser fingerprinting and TLS fingerprints
*   Rate limiting and access restrictions

ASP dynamically upgrades parameters (proxy_pool, browser) to bypass protection, which can increase API cost. Use `cost_budget` to limit spending.

Limit ASP retry cost. ASP upgrades params dynamically; set budget to control spending. Min value needed to pass target

`25``55`

 More details

When `asp=true`, the system may retry with different configurations (residential proxies, browser rendering) which increases cost. Set a budget to:

*   Control maximum spending per request
*   Fail fast if target requires expensive bypass
*   Make costs more predictable

Set the minimum budget needed for your target. If budget is too low, the request will be rejected without attempting bypass.

Headless Browser / Javascript Rendering

Enable browser rendering to execute JavaScript and render dynamic content

`true``false`

Delay in milliseconds after page load. Only for HTML pages

`1000``5000`

Wait until CSS/XPath selector or XHR pattern visible. Use `xhr:` prefix for XHR patterns

`body``#content``//button``xhr:/api/*`

 More details

**Supported selector types:**

*   **CSS Selector** - Standard CSS selectors like `body`, `input[type="submit"]`
*   **XPath Selector** - XPath expressions like `//button[contains(text(),"Go")]`
*   **XHR Pattern** - Network request patterns prefixed with `xhr:`

**XHR Pattern matching:**

*   Prefix matching: `xhr:/page/reviews`
*   Wildcard matching: `xhr:/page/*`

Only executed on `HTML` pages. If the selector is not found, the scrape will timeout.

JavaScript to execute (base64 encoded, max 16KB). [Encode here](https://scrapfly.io/web-scraping-tools/base64)

`cmV0dXJuIG5hdmlnYXRvci51c2VyQWdlbnQ`

 More details

**Execution behavior:**

*   If `wait_for_selector` is defined, the script executes **after** the selector is found
*   Use JavaScript `await` to prevent early return when waiting for data
*   Return values are available in the API response

Only executed on `HTML` pages. Maximum script size is 16KB before base64 encoding.

Capture screenshots of fullpage or specific elements. Key=name, value=selector or `fullpage`

`screenshots[page]=fullpage``screenshots[price]=#price`

 More details

**Capture options:**

*   `fullpage` - Captures the entire page including scrolled content
*   **CSS selector** - Captures only the matching element (e.g., `#price`)
*   **XPath selector** - Captures element by XPath expression

**Multiple screenshots:** You can take multiple screenshots of different areas by specifying different names:

*   `screenshots[page]=fullpage`
*   `screenshots[price]=#product-price`
*   `screenshots[reviews]=.reviews-section`

Screenshot options: `load_images`, `dark_mode`, `block_banners`, `high_quality`, `print_media_format`

`load_images``block_banners,high_quality`

 More details

**Available flags:**

*   `load_images` - Load images (extra bandwidth cost applies)
*   `dark_mode` - Enable dark mode display
*   `block_banners` - Block cookie banners and overlays
*   `high_quality` - No compression on output image
*   `print_media_format` - Render page in print mode

Combine multiple flags with commas: `screenshot_flags=load_images,block_banners,high_quality`

`eydjbGljayc6IHsnc2VsZWN0b3InOiAnI3N1Ym1pdCd9fQ`

 More details

**Available scenario actions:**

*   `click` - Click on elements
*   `fill` - Fill input fields with text
*   `wait` - Wait for specified milliseconds
*   `scroll` - Scroll the page or element
*   `execute` - Execute custom JavaScript
*   `wait_for_selector` - Wait for element to appear
*   `wait_for_navigation` - Wait for page navigation

**Example scenario (before base64):**

`[{"click": {"selector": "#login-btn"}}, {"fill": {"selector": "#username", "value": "test"}}]`

Spoof browser geolocation. Format: `latitude,longitude`

`48.856614,2.3522219``40.712784,-74.005941`

Page load stage to wait for. Use `domcontentloaded` for faster scrapes

`complete``domcontentloaded`

Caching Options

Enable caching. Returns cached content if HIT, otherwise scrapes and caches

`true``false`

Cache time-to-live in seconds. Expired cache triggers fresh scrape

`60``3600``86400`

Force cache refresh on this request

`true``false`

Session Management

Session name to persist cookies, fingerprint, and proxy across scrapes. Alphanumeric, max 255 chars

`my-session-123`

 More details

**Session automatically persists:**

*   **Cookies** - Login sessions, preferences, cart data
*   **Browser fingerprint** - Consistent identity across requests
*   **Proxy IP** - Same IP when possible (see `session_sticky_proxy`)

**Use cases:**

*   Multi-step authentication flows
*   Shopping cart persistence
*   Pagination with session-based state

Session name must be alphanumeric, maximum 255 characters. Sessions are automatically cleaned after inactivity.

Best effort to reuse same proxy IP within session

`true``false`

 More details

When enabled, the system attempts to use the same proxy IP address for all requests within a session. This is useful for:

*   Websites that track IP consistency
*   Rate-limited sites that count per-IP
*   Session-based authentication tied to IP

This is a best effort feature. The same IP is not guaranteed if the proxy becomes unavailable.
