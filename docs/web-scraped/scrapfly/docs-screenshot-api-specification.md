# Source: https://scrapfly.io/docs/screenshot-api/specification

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/screenshot-api/specification

Markdown Content:
Scrapfly Screenshot API
-----------------------

The Screenshot API allows capturing screenshots of any web page or specific parts of the web page. This API comes with many convenience features like blocking bypass, viewport settings, full page capture auto scroll, banner blocking and much more!

> If you need advanced scraping capabilities for screenshot capture like browser interaction, cookies, headers, etc. Use the [full Web Scraping API to take screenshot instead](https://scrapfly.io/docs/scrape-api/screenshot). Screenshot API is a simplified version suited for more general screenshot capture.

This API is designed to be as simple as possible while maintaining the flexibility to capture any web page and is fully controlled through GET requests and URL parameters making it accessible in any environment.

Minimal API call is a GET request with `url` and `key` parameters:

`https://api.scrapfly.io/screenshot?url=https%3A%2F%2Fweb-scraping.dev%2Fproduct%2F1&key=`

[Intro Video](https://scrapfly.io/docs/screenshot-api/getting-started#video)
----------------------------------------------------------------------------

[On Steroids](https://scrapfly.io/docs/screenshot-api/getting-started#onste)
----------------------------------------------------------------------------

*    Automatically unblock websites without extra configuration . 
*    Gzip compression is available through the accept-encoding: gzip header. 
*    Direct screenshot results as `jpg, png, webp, gif` using [format](https://scrapfly.io/docs/screenshot-api/specification#api_param_format). 
*    Block ads, pop-ups, modals and banners with [options=block_banners](https://scrapfly.io/docs/screenshot-api/specification#api_param_options). 
*    Auto scroll to the bottom of the page to load all page details with [auto_scroll](https://scrapfly.io/docs/screenshot-api/specification#api_param_auto_scroll). 
*    Execute JavaScript code on the page before taking the screenshot using the [js parameter](https://scrapfly.io/docs/screenshot-api/specification#api_param_js). 

[Quality of Life](https://scrapfly.io/docs/screenshot-api/getting-started#qol)
------------------------------------------------------------------------------

*    All screenshot requests and metadata are automatically tracked on a [Web Dashboard](https://scrapfly.io/docs/monitoring). 
*    Multi project/scraper support through [Project Management](https://scrapfly.io/docs/project). 
*    Ability to debug and replay scrape requests from the dashboard log page. 
*    API [Status page](https://scrapfly.statuspage.io/) with a notification subscription. 
*    Full API transparency through meta HTTP headers: 
    *   **X-Scrapfly-Api-Cost** - API cost billed 
    *   **X-Scrapfly-Remaining-Api-Credit** Remaining Api credit. If 0, billed in extra credits 
    *   **X-Scrapfly-Account-Concurrent-Usage** You current concurrency usage of your account 
    *   **X-Scrapfly-Account-Remaining-Concurrent-Usage** Maximum concurrency allowed by the account 
    *   **X-Scrapfly-Project-Concurrent-Usage** Concurrency usage of the project 
    *   **X-Scrapfly-Project-Remaining-Concurrent-Usage** If the concurrency limit is set on the project otherwise equal to the account concurrency 
    *   **X-Scrapfly-Screenshot-Url** URL for the screenshot store on Scrapfly's servers for later retrieval. 

Concurrency is defined by your subscription

[Billing](https://scrapfly.io/docs/screenshot-api/getting-started#billing)
--------------------------------------------------------------------------

Scrapfly uses a credit system to bill Screenshot API requests.

Billing is reported in every scrape response through the `X-Scrapfly-API-Cost` header and the monitoring dashboard and can be controlled through Scrapfly budget settings.

For more see [Screenshot Billing](https://scrapfly.io/docs/screenshot-api/billing).

[Errors](https://scrapfly.io/docs/screenshot-api/getting-started#error_handling)
--------------------------------------------------------------------------------

Scrapfly uses conventional HTTP response codes to indicate the success or failure of an API request.

**Codes in the 2xx** range indicate success.

**Codes in the 4xx** range indicate an error that failed given the information provided (e.g., a required parameter was omitted, not permitted, max concurrency reached, etc.).

**Codes in the 5xx** range indicate an error with Scrapfly's servers.

* * *

**HTTP 422 - Request Failed** provide extra headers in order to help as much as possible:

*   **X-Scrapfly-Reject-Code:** Error Code 
*   **X-Scrapfly-Reject-Description:** URL to the related documentation 
*   **X-Scrapfly-Reject-Retryable:** Indicate if the screenshot is retryable 

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
| 504 - Timeout | The screenshot have timeout |
| You can check out the [full error list](https://scrapfly.io/docs/screenshot-api/errors) to learn more. |

* * *

[Specification](https://scrapfly.io/docs/screenshot-api/getting-started#spec)
-----------------------------------------------------------------------------

Scrapfly has loads of features and the best way to discover them is through the specification docs below.

The following **headers are available** with the screenshot response:

*   **X-Scrapfly-Upstream-Http-Code:** The Status code the page
*   **X-Scrapfly-Upstream-Url:** The actual url of the screenshot after potential redirection
*   **X-Scrapfly-Screenshot-Url:** Screenshot storage URL on scrapfly servers. Use `?key=YOUR-SCRAPFLY-KEY` for retrieval

To start, you can try out the API directly using your browser:

`https://api.scrapfly.io/screenshot?url=https%3A%2F%2Fweb-scraping.dev%2Fproduct%2F1&key=`

Or by using curl in your terminal:

```
$ curl -G \
--request "GET" \
--url "https://api.scrapfly.io/screenshot" \
--data-urlencode "key=" \
--data-urlencode "url=https://web-scraping.dev/product/1" -o screenshot.jpg
```

Command Explanation
*   **`curl -G`**: 
    *   `curl` is a command-line tool for transferring data with URLs.
    *   `-G` specifies that the request should be a GET request and appends the data specified with `--data-urlencode` as query parameters.

*   **`--request "GET"`**: 
    *   `--request "GET"` explicitly sets the request method to GET. This is redundant since `-G` already indicates a GET request.

*   **URL**: 
    *   The URL of the API endpoint being accessed: `https://api.scrapfly.io/screenshot`.

*   **`--data-urlencode "key=__API_KEY__"`**: 
    *   `--data-urlencode` encodes data as a URL parameter.
    *   `"key=__API_KEY__"` is the API key used for authentication.

*   **`--data-urlencode "url=https://web-scraping.dev/product/1"`**: 
    *   `--data-urlencode` encodes data as a URL parameter.
    *   `"url=https://web-scraping.dev/product/1"` is the URL of the web page to be screenshotted, URL-encoded.

*   **`--data-urlencode "options=load_images"`**: 
    *   `--data-urlencode` encodes data as a URL parameter.
    *   `"options=load_images"` specifies that images should be loaded in the screenshot.

*   **`-o screenshot.jpg`**: 
    *   `-o` specifies the output file for the response.
    *   `screenshot.jpg` is the name of the file where the screenshot will be saved.

This will save the results to `screenshot.jpg` in the current directory:

`open screenshot.jpg`

> **Only documents of content-type `text/*` are eligible**for screenshot, otherwise the error [ERR::SCREENSHOT::INVALID_CONTENT_TYPE](https://scrapfly.io/docs/screenshot-api/error/ERR::SCREENSHOT::INVALID_CONTENT_TYPE)will be returned.

With that in mind, now you can explore the API specification to see all features that are available through URL parameters:

`https://example.com/page`

API Key to authenticate the call

`scp-live-xxx...`

Format of the screenshot image

`jpg``png``webp``gif`

Area to capture: viewport, full page, or CSS selector/XPath for specific element

`viewport``fullpage``#header``//div/img`

 More details

**Capture modes:**

*   `viewport` - Visible screen area only
*   `fullpage` - Entire page including scrolled content
*   `vertical` - Vertical section of page
*   **CSS Selector:**`#header`, `.product-image`
*   **XPath:**`//div/img[1]`

When using selectors, only the matching element is captured. Useful for extracting specific page components.

Screen resolution (width x height)

`1920x1080``375x812`

 More details

**Common resolutions:**

*   `1920x1080` - Desktop Full HD (default)
*   `1440x900` - Desktop standard
*   `375x812` - iPhone X/11/12
*   `320x860` - Mobile portrait
*   `768x1024` - iPad portrait

Use mobile resolutions to capture responsive/mobile versions of websites.

Proxy country location (ISO 3166 alpha-2). Supports multiple, weighted, or exclusions

`us``us,ca,mx``-gb`

 More details

**Country selection modes:**

*   **Single country:**`country=us`
*   **Multiple countries:**`country=us,ca,mx` (random selection)
*   **Exclusions:**`country=-gb` (exclude UK)
*   **Weighted:**`country=us:10,gb:5`

Maximum time allowed in milliseconds (min: 60000, max: 120000)

`60000``120000`

Rendering Options

Delay in milliseconds to wait after page load

`2000``5000`

Wait until CSS selector or XPath is visible before capturing

`body``#content``//button`

Screenshot flags: `dark_mode`, `block_banners`, `print_media_format`

`block_banners``dark_mode`

 More details

**Available options:**

*   `dark_mode` - Enable dark theme rendering
*   `block_banners` - Remove cookie banners and overlays
*   `print_media_format` - Render page in print mode

**Combining options:** Use comma-separated values:

`options=block_banners,dark_mode`

Options can significantly improve screenshot quality by removing distracting elements.

JavaScript to execute (base64 encoded, max 16KB). [Encode here](https://scrapfly.io/web-scraping-tools/base64)

`ZG9jdW1lbnQuYm9keS5zdHls...`

Caching Options

Enable caching for repeated screenshots of same URL

`true``false`

Cache time-to-live in seconds

`60``3600``86400`

Force cache refresh on this request

`true``false`

Accessibility Testing

Simulate vision deficiency for accessibility testing (WCAG compliance)

`deuteranopia``protanopia``tritanopia`

 More details

**Available vision deficiency types:**

*   `none` - Normal vision (default)
*   `deuteranopia` - Red-green color blindness (green-blind), affects ~6% of males
*   `protanopia` - Red-green color blindness (red-blind), affects ~2% of males
*   `tritanopia` - Blue-yellow color blindness, affects ~0.01%
*   `achromatopsia` - Complete color blindness (monochromacy), affects ~0.003%
*   `blurredVision` - Blurred/unfocused vision, affects ~2.2B globally

Use this for WCAG 2.2, Section 508, ADA, and European Accessibility Act compliance testing. See [Accessibility Testing Guide](https://scrapfly.io/docs/screenshot-api/accessibility).

[Using HEAD Requests](https://scrapfly.io/docs/screenshot-api/getting-started#head)
-----------------------------------------------------------------------------------

Screenshot API also support `HEAD` type requests for operations that do not need an immediate data stream. This approach can **save significant amounts of bandwidth** and increase capture speeds as no response body is returned just a URL to the screenshot.

Scrapfly stores all of your screenshots on our servers so you can download them later in your integrations by storing the screenshot storage URL from `X-Scrapfly-Screenshot-Url` header.

```
$ curl -G \
    --head
    --url "https://api.scrapfly.io/screenshot" \
    --data-urlencode "key=" \
    --data-urlencode "url=https://web-scraping.dev/product/1"

HTTP/2 200
content-type: image/jpeg
date: Tue, 18 Feb 2025 07:05:29 GMT
vary: Accept-Encoding
x-request-id: 20a07b29-a1d1-4e50-9f64-a39766aee488
x-scrapfly-account-concurrent-usage: 1
x-scrapfly-account-remaining-concurrent-usage: 9
x-scrapfly-api-cost: 60
x-scrapfly-project-concurrent-usage: 1
x-scrapfly-project-remaining-concurrent-usage: 9
x-scrapfly-remaining-api-credit: 526904
x-scrapfly-response-time: 8.510000
x-scrapfly-screenshot-url:
https://api.scrapfly.io/scrape/screenshot/01JMBY09ETZSH1ZB6NAHFR8WJP/main
# ^^^ screenshot url avaiable in the headers. Attach `?key=YOUR-SCRAPFLY-KEY` to retrieve the image at any time.
x-scrapfly-upstream-http-code: 200
x-scrapfly-upstream-url: https://web-scraping.dev/product/1
content-length: 340684
```

Command Explanation
*   **`curl -G`**: 
    *   `curl` is a command-line tool for transferring data with URLs.
    *   `-G` specifies that the request should be a GET request and appends the data specified with `--data-urlencode` as query parameters.

*   **`--head`**: 
    *   `--head` makes a HEAD request instead of a GET request. This retrieves headers only, without the response body.

*   **URL**: 
    *   The URL of the API endpoint being accessed: `https://api.scrapfly.io/screenshot`.

*   **`--data-urlencode "key=__API_KEY__"`**: 
    *   `--data-urlencode` encodes data as a URL parameter.
    *   `"key=__API_KEY__"` is the API key used for authentication.

*   **`--data-urlencode "url=https://web-scraping.dev/product/1"`**: 
    *   `--data-urlencode` encodes data as a URL parameter.
    *   `"url=https://web-scraping.dev/product/1"` is the URL of the web page to be screenshotted, URL-encoded.

Note that screenshot store **duration depends on your plan's [log retention policy](https://scrapfly.io/docs/monitoring)**which varies between 1 to 4 weeks.

> All scrapfly store URLs still **require authentication**which can be done by attaching `?key`parameter with your API key. i.e. `https://api.scrapfly.io/screenshot/01JMBY09ETZSH1ZB6NAHFR8WJP/main?key=YOUR-SCRAPFLY-KEY`

All related errors are listed below. You can see full description and example of error response on the [Errors section](https://scrapfly.io/docs/extraction-api/errors).

*   [ERR::SCREENSHOT::INVALID_CONTENT_TYPE](https://scrapfly.io/docs/extraction-api/error/ERR::SCREENSHOT::INVALID_CONTENT_TYPE) - Only content type text/html is supported for screenshot
*   [ERR::SCREENSHOT::UNABLE_TO_TAKE_SCREENSHOT](https://scrapfly.io/docs/extraction-api/error/ERR::SCREENSHOT::UNABLE_TO_TAKE_SCREENSHOT) - For some reason we were unable to take the screenshot

[FAQ](https://scrapfly.io/docs/screenshot-api/getting-started#faq)
------------------------------------------------------------------

### [Why are some images missing in my screenshot?](https://scrapfly.io/docs/screenshot-api/getting-started#missing-images)

Some images can be loaded dynamically and render slowly. Try setting `rendering_wait` parameter to a few seconds (e.g. `3000`) or wait for elements to load explicitly using `wait_for_selector` parameter.

Some images only load when scrolled into viewport so you can try increasing the `viewport` parameter to bigger values than the default `1920x1080`. You can also use `auto_scroll` to have Scrapfly scroll to the very bottom of the page to force image loading.

Finally, some images can be blocked from loading by modals and banners. Use the `block_banners` flag in the `options` parameter to close any pop-ups, modals or banners i.e. `options=block_banners`.
