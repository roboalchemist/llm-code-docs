# Source: https://scrapfly.io/docs/scrape-api/proxy-mode

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/proxy-mode

Markdown Content:
Proxy Mode
----------

Scrapfly's **Proxy Mode** lets you use the Scrapfly scraping API as a standard HTTP/HTTPS forward proxy. Instead of making REST API calls to `/scrape`, you configure your third-party tool to use Scrapfly as a proxy server. Scraping options are encoded in the proxy username, and your API key is used as the password.

This is designed for **third-party tools and services** that only support the proxy protocol format and cannot integrate with the Scrapfly API directly — such as SEO platforms (Screaming Frog, Ahrefs), crawling platforms (Apify, Crawlee), monitoring tools, data pipelines, and other software that only accept a proxy URL as configuration.

> **Not for custom code**— If you are writing your own scraping code, use the [REST API](https://scrapfly.io/docs/scrape-api/getting-started)or one of the [Scrapfly SDKs](https://scrapfly.io/docs/sdk/python)instead. Proxy Mode is for tools that **only**accept a proxy URL as their configuration and cannot call the API directly.

[How It Works](https://scrapfly.io/docs/scrape-api/proxy-mode#how-it-works)
---------------------------------------------------------------------------

100%

Drag to pan, Ctrl/Cmd+scroll to zoom, double-click for fullscreen

1.   **3rd-Party Tool**: Sends requests through Scrapfly's proxy endpoint. You configure the proxy URL in the tool's settings.
2.   **Scrapfly Proxy**: Authenticates your API key, extracts scraping options from the proxy username, and converts the request to an internal scrape API call.
3.   **Scrapfly API**: Processes the request with JavaScript rendering, anti-bot protection (ASP), proxy rotation, and other features.
4.   **Target Website**: The Scrapfly API fetches the content from the target and returns it to the tool.

The response includes the target website's content along with `X-Scrapfly-*` headers containing metadata about the scrape (cost, timing, quotas, screenshot URLs, etc.).

[Quick Start](https://scrapfly.io/docs/scrape-api/proxy-mode#quick-start)
-------------------------------------------------------------------------

Configure your third-party tool's proxy settings with the following details:

**Proxy Host**`proxy.scrapfly.io:7777`
**Username**Scraping options as dash-separated key-value pairs (e.g., `country-us`)
**Password**Your Scrapfly API key

Or as a single proxy URL:

`http://OPTIONS:API_KEY@proxy.scrapfly.io:7777`

You can verify the setup with cURL:

```
# Test with a simple request
curl -x http://country-us:YOUR_API_KEY@proxy.scrapfly.io:7777 \
    https://httpbin.dev/anything

# Test with JavaScript rendering and anti-bot protection
curl -x http://renderJs-true-asp-true-country-us:YOUR_API_KEY@proxy.scrapfly.io:7777 \
    https://web-scraping.dev/products
```

[SSL / Certificate Verification](https://scrapfly.io/docs/scrape-api/proxy-mode#ssl-certificate)
------------------------------------------------------------------------------------------------

When proxying HTTPS requests, the Scrapfly proxy intercepts TLS connections to route them through the scraping pipeline. Your tool's HTTP client will see the Scrapfly proxy certificate instead of the target website's certificate, which causes certificate verification errors by default.

*   [Disable Verification (Recommended)](https://scrapfly.io/docs/scrape-api/proxy-mode#ssl-disable)
*   [Install CA Certificate](https://scrapfly.io/docs/scrape-api/proxy-mode#ssl-install-ca)

The simplest approach is to disable SSL certificate verification in your tool. This is safe because the connection between your tool and the Scrapfly proxy is authenticated via your API key.

Most third-party tools have a similar option in their proxy or network settings (e.g., “Ignore SSL errors”, “Skip certificate check”).

*   [cURL](https://scrapfly.io/docs/scrape-api/proxy-mode#ssl-disable-curl)
*   [Python](https://scrapfly.io/docs/scrape-api/proxy-mode#ssl-disable-python)
*   [Node.js](https://scrapfly.io/docs/scrape-api/proxy-mode#ssl-disable-nodejs)
*   [wget](https://scrapfly.io/docs/scrape-api/proxy-mode#ssl-disable-wget)

```
# Use the -k flag to skip certificate verification
curl -k -x http://country-us:YOUR_API_KEY@proxy.scrapfly.io:7777 \
    https://httpbin.dev/anything
```

```
import requests

proxies = {
    "http": "http://scrape:YOUR_API_KEY@proxy.scrapfly.io:7777",
    "https": "http://scrape:YOUR_API_KEY@proxy.scrapfly.io:7777",
}
# Set verify=False to skip certificate verification
response = requests.get("https://httpbin.dev/anything", proxies=proxies, verify=False)
```

```
// Set this environment variable before running your script
// NODE_TLS_REJECT_UNAUTHORIZED=0 node my_script.js

// Or set it programmatically (before any HTTPS requests)
process.env.NODE_TLS_REJECT_UNAUTHORIZED = "0";
```

```
# Use --no-check-certificate to skip certificate verification
wget --no-check-certificate -e use_proxy=yes \
    -e http_proxy="http://scrape:YOUR_API_KEY@proxy.scrapfly.io:7777" \
    https://httpbin.dev/anything
```

If your tool does not support disabling certificate verification, you can install the Scrapfly proxy CA certificate so your system trusts the proxy's TLS connections.

#### Automatic Install (Recommended)

Run this one-liner to automatically install the certificate for your OS (Linux, macOS, WSL):

`curl -sL https://scrapfly.io/install-ca.sh | sh`

#### Manual Install

**1. Download the certificate:**

`curl -o scrapfly-proxy-ca.crt https://scrapfly.io/ca.crt`

**2. Install it in your system or tool's trust store:**

*   [Linux](https://scrapfly.io/docs/scrape-api/proxy-mode#ssl-install-linux)
*   [macOS](https://scrapfly.io/docs/scrape-api/proxy-mode#ssl-install-macos)
*   [Windows](https://scrapfly.io/docs/scrape-api/proxy-mode#ssl-install-windows)
*   [Python](https://scrapfly.io/docs/scrape-api/proxy-mode#ssl-install-python)
*   [Node.js](https://scrapfly.io/docs/scrape-api/proxy-mode#ssl-install-nodejs)

```
# Debian / Ubuntu
sudo cp scrapfly-proxy-ca.crt /usr/local/share/ca-certificates/
sudo update-ca-certificates
```

```
sudo security add-trusted-cert -d -r trustRoot \
    -k /Library/Keychains/System.keychain scrapfly-proxy-ca.crt
```

```
# PowerShell (run as Administrator)
certutil -addstore -f "ROOT" scrapfly-proxy-ca.crt
```

```
# For requests / httpx: set REQUESTS_CA_BUNDLE
export REQUESTS_CA_BUNDLE=/path/to/scrapfly-proxy-ca.crt

# Or pass it directly
response = requests.get(url, proxies=proxies, verify="/path/to/scrapfly-proxy-ca.crt")
```

```
# Set NODE_EXTRA_CA_CERTS environment variable
export NODE_EXTRA_CA_CERTS=/path/to/scrapfly-proxy-ca.crt
node my_script.js
```

[Username Format](https://scrapfly.io/docs/scrape-api/proxy-mode#username-format)
---------------------------------------------------------------------------------

Options are encoded as dash-separated key-value pairs. Keys are **case-insensitive**. Boolean options use `true` / `false` values.

```
# Format: key1-value1-key2-value2-...
# Example:
country-us-renderJs-true-asp-true-proxyPool-public_residential_pool
```

If no options are specified, you can use any non-empty string as the username (e.g., `scrape`). Default settings will be applied.

> **No options needed?**If you don't want to pass any scraping options, use `scrapfly`as the username placeholder. Default settings (JavaScript rendering + anti-bot protection) will be applied automatically. E.g., `http://scrapfly:YOUR_API_KEY@proxy.scrapfly.io:7777`

> **Escaping dashes in values:**Since dashes (`-`) are used as separators, values that contain literal dashes must escape them with a backslash (`\-`). This is common with CSS selectors used in `waitForSelector`. E.g., `div.my-class`becomes `waitForSelector-div.my\-class`.

[Supported Options](https://scrapfly.io/docs/scrape-api/proxy-mode#options)
---------------------------------------------------------------------------

Proxy Mode supports a subset of the [Web Scraping API](https://scrapfly.io/docs/scrape-api/getting-started) options. All options are optional — defaults are used when not specified.

| Option Key | Type | Default | Description |
| --- | --- | --- | --- |
| `proxyPool` | string | `public_datacenter_pool` | [Proxy pool](https://scrapfly.io/docs/scrape-api/proxy) to use. E.g., `public_residential_pool`. |
| `country` | string | _auto_ | [Country code](https://scrapfly.io/docs/scrape-api/proxy#country) (ISO 3166-1 alpha-2). E.g., `us`, `fr`, `de`. |
| `renderJs` | boolean | `true` | Enable [JavaScript rendering](https://scrapfly.io/docs/scrape-api/javascript-rendering) via headless browser. Enabled by default in proxy mode. |
| `asp` / `unblocker` | boolean | `true` | Enable [Anti Scraping Protection](https://scrapfly.io/docs/scrape-api/anti-scraping-protection) bypass. Enabled by default in proxy mode. `unblocker` is an alias for `asp`. |
| `format` | string | `raw` | Response format. Values: `raw`, `json`, `text`, `markdown`, `no_images`. |
| `session` | string | _none_ | [Session](https://scrapfly.io/docs/scrape-api/session) identifier to share cookies and navigation context across requests. |
| `timeout` | integer | `60` | Request timeout in seconds (max 300). |
| `cache` | boolean | `false` | Enable [response caching](https://scrapfly.io/docs/scrape-api/cache). |
| `cacheTtl` | integer | _default_ | Cache TTL in seconds. |
| `cacheClear` | boolean | `false` | Clear cached response and fetch fresh content. |
| `tags` | string | _none_ | Comma-separated tags for request labeling (e.g., `tag1,tag2`). |
| `dns` | boolean | `false` | Enable [DNS data](https://scrapfly.io/docs/scrape-api/dns) collection. |
| `ssl` | boolean | `false` | Enable [SSL certificate](https://scrapfly.io/docs/scrape-api/ssl) data collection. |
| `debug` | boolean | `false` | Enable [debug mode](https://scrapfly.io/docs/scrape-api/debug) for detailed logging. |
| `retry` | boolean | `true` | Enable automatic retry on failure. |
| `cost` | integer | _auto_ | Set maximum API credit cost budget for the request. |
| `renderingWait` | integer | _none_ | Wait time in milliseconds after page load (requires `renderJs=true`). See [JavaScript rendering](https://scrapfly.io/docs/scrape-api/javascript-rendering). |
| `webhook` | string | _none_ | [Webhook](https://scrapfly.io/docs/scrape-api/webhook) name to receive scrape results asynchronously. |
| `lang` | string | _none_ | Comma-separated language codes (e.g., `en,fr`). Sets the `Accept-Language` header. |
| `correlationId` | string | _none_ | Custom identifier for grouping and tracking related requests. |
| `extractionModel` | string | _none_ | [Extraction model](https://scrapfly.io/docs/scrape-api/extraction) for AI-powered data extraction (e.g., `product`, `article`). |
| `screenshot` | boolean | `false` | Capture a fullpage [screenshot](https://scrapfly.io/docs/scrape-api/screenshot) (requires `renderJs=true`). |
| `waitForSelector` | string | _none_ | CSS selector to wait for before returning the response (requires `renderJs=true`). Escape literal dashes with `\-` (e.g., `div.my\-class`). See [JavaScript rendering](https://scrapfly.io/docs/scrape-api/javascript-rendering). |
| `forwardHeaders` | boolean | `true` | Forward client HTTP headers (e.g., `Cookie`, `Accept`) to the target website. Scrapfly already manages standard headers automatically — only set custom headers on your proxied request when you need specific ones like `Cookie` or custom headers. Set to `false` to let Scrapfly handle all headers. |

> **Tip:**Options `renderJs`and `asp`default to `true`in proxy mode, unlike the REST API where they default to `false`. This ensures the best scraping results out of the box. Set `renderJs-false`or `asp-false`explicitly to disable them.

> **forwardHeaders:**In most cases, you should set `forwardHeaders-false`in the proxy username to let Scrapfly fully manage request headers (User-Agent, Accept, etc.) for optimal anti-bot evasion. Only enable header forwarding (`forwardHeaders-true`, the default) if your tool needs to send specific headers like `Cookie`or custom authentication headers to the target website.

Proxy Mode responses include `X-Scrapfly-*` headers alongside the target website's response headers. These headers provide metadata about the scrape request — cost, quotas, timing, and error details.

| Header | Description |
| --- | --- |
| `X-Scrapfly-Api-Cost` | API credits consumed by this request. |
| `X-Scrapfly-Response-Time` | Scrape duration in seconds. |
| `X-Scrapfly-Remaining-Api-Credit` | Remaining API credits on your account. |
| `X-Scrapfly-Account-Concurrent-Usage` | Current concurrent request usage at the account level. |
| `X-Scrapfly-Account-Remaining-Concurrent-Usage` | Remaining concurrent request slots at the account level. |
| `X-Scrapfly-Log` | Scrape log UUID — use this to look up the request in the [Dashboard Monitoring](https://scrapfly.io/dashboard/monitoring). |
| `X-Scrapfly-Content-Format` | Response content format (`text` or `binary`). |
| `X-Scrapfly-Reject-Code` | Error code when the scrape fails (see [Error Reference](https://scrapfly.io/docs/scrape-api/errors)). |
| `X-Scrapfly-Reject-Description` | Human-readable error description. |
| `X-Scrapfly-Reject-Retryable` | `true` if the request can be retried. |
| `X-Scrapfly-Screenshot-{name}` | Screenshot download URL (one header per screenshot). E.g., `X-Scrapfly-Screenshot-fullpage`. Requires `screenshot-true` option. |

```
# Example: inspect response headers with curl
curl -v -x http://country-us:YOUR_API_KEY@proxy.scrapfly.io:7777 \
    https://httpbin.dev/html 2>&1 | grep -i "x-scrapfly"

# Output:
# < X-Scrapfly-Api-Cost: 5
# < X-Scrapfly-Response-Time: 1.234000
# < X-Scrapfly-Remaining-Api-Credit: 99995
# < X-Scrapfly-Log: 550e8400-e29b-41d4-a716-446655440000
```

[Error Handling](https://scrapfly.io/docs/scrape-api/proxy-mode#error-handling)
-------------------------------------------------------------------------------

Proxy Mode uses standard HTTP proxy error codes for connection-level failures. Once the proxy connection is established, the Scrapfly API handles the request and responds with its standard error format — the same error codes and response body as the [REST API error reference](https://scrapfly.io/docs/scrape-api/errors).

### Proxy-Level Errors

These errors occur **before** the request reaches the Scrapfly API:

| Status Code | Meaning |
| --- | --- |
| `407` | Proxy Authentication Required — missing or invalid API key. |
| `400` | Bad Request — invalid proxy username format or unknown option. |
| `502` | Bad Gateway — proxy could not reach the Scrapfly API. |

### API-Level Errors

Once the proxy successfully connects to the Scrapfly API, the API processes the request and responds with its usual error codes. These are returned as-is through the proxy with the `X-Scrapfly-Reject-Code` and `X-Scrapfly-Reject-Description` headers. See the full [Error Reference](https://scrapfly.io/docs/scrape-api/errors) for details.

[Proxy Mode vs REST API](https://scrapfly.io/docs/scrape-api/proxy-mode#proxy-mode-vs-rest-api)
-----------------------------------------------------------------------------------------------

Choose the right integration method for your use case:

| Feature | Proxy Mode | REST API |
| --- | --- | --- |
| **Integration effort** | Drop-in proxy URL configuration | SDK or custom HTTP client code |
| **Best for** | 3rd-party tools (Screaming Frog, Apify, etc.) | Custom scrapers, application code |
| **JavaScript scenarios** | Not available | Full support |
| **Response format** | Raw HTML + X-Scrapfly headers | Full JSON with metadata |
| **Screenshots** | Fullpage only (via headers) | Multiple types, custom viewports |

[Differences from REST API](https://scrapfly.io/docs/scrape-api/proxy-mode#differences-from-rest-api)
-----------------------------------------------------------------------------------------------------

Proxy Mode is optimized for drop-in compatibility with existing tools and services. This design means some REST API features are not available or work differently:

*   Only a subset of scraping options is available (see [Supported Options](https://scrapfly.io/docs/scrape-api/proxy-mode#options)).
*   Response metadata is provided via [`X-Scrapfly-*` headers](https://scrapfly.io/docs/scrape-api/proxy-mode#response-headers) instead of a JSON envelope.
*   [JavaScript Scenarios](https://scrapfly.io/docs/scrape-api/javascript-scenario) are not supported (use the REST API for complex browser interactions). 
*   Screenshots are limited to fullpage capture only. For custom viewports or multiple screenshots, use the REST API.
*   Client headers are forwarded automatically (disable with `forwardHeaders-false`). Scrapfly manages most headers — only set specific ones like `Cookie` on your request.

> **When to use REST API:**If you are writing custom scraping code, use the [REST API](https://scrapfly.io/docs/scrape-api/getting-started)or [Scrapfly SDKs](https://scrapfly.io/docs/sdk/python)instead. Proxy Mode is specifically for third-party tools that only accept a proxy URL.

[Tool Integration Guides](https://scrapfly.io/docs/scrape-api/proxy-mode#tool-integrations)
-------------------------------------------------------------------------------------------

Step-by-step configuration guides for popular tools:

*   [**Screaming Frog SEO Spider**](https://scrapfly.io/docs/scrape-api/proxy-mode/screaming-frog) — SEO auditing and site crawling
*   [**Apify**](https://scrapfly.io/docs/scrape-api/proxy-mode/apify) — cloud scraping and automation platform
