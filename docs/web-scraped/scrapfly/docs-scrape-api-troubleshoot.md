# Source: https://scrapfly.io/docs/scrape-api/troubleshoot

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/troubleshoot

Markdown Content:
Troubleshooting
---------------

Troubleshooting Scrapfly scrapers is relatively easy as Scrapfly provides extensive logging. Let's take a look at some examples.

To start the [Monitoring](https://scrapfly.io/docs/monitoring) dashboard displays all scrape requests and their details. Inspecting the scrape monitoring dashboard is the first step to troubleshooting and we'll cover this extensively in the following sections.

For additional details make sure to enable the [debug](https://scrapfly.io/docs/scrape-api/getting-started#api_param_debug) parameter which will provide more details about the scrape requests and even capture screenshots when [render_js](https://scrapfly.io/docs/scrape-api/getting-started#api_param_render_js) is enabled.

[Replicating with Player](https://scrapfly.io/docs/scrape-api/troubleshoot#unexpected-results)
----------------------------------------------------------------------------------------------

The first step to figuring out why a scrape request is not working as expected is to replicate the [Web Player](https://scrapfly.io/dashboard/playground/web-scraper) which allow easy and reliable scrape configuration

👉

If the [Web Player](https://scrapfly.io/dashboard/playground/web-scraper) works as expected, then the issue is likely related to the API call configuration. Ensure that the API call is configured as per [API Specification](https://scrapfly.io/docs/scrape-api/getting-started#spec). In particular, note that some API parameters need to be [url encoded](https://scrapfly.io/web-scraping-tools/urlencode).

[Timeout](https://scrapfly.io/docs/scrape-api/troubleshoot#scrape-config)
-------------------------------------------------------------------------

If you receive a lot of [`ERR::SCRAPE::OPERATION_TIMEOUT`](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::OPERATION_TIMEOUT) errors, inspect the following:

*   If `retry=false` is set, you can increase the `timeout` parameter
*   If `asp=true` and `retry=false` are set you can increase `timeout=60000` even `timeout=90000`
*   If the url you hit is redirected (like url ending with `/` or `wwww`) try to avoid unnecessary redirects and scrape the final urls to speed up scraping.
*    If you use `asp=true` you can replicate ASP fine-tuning as default scrape parameters. For example, ASP can upgrade requests to residential proxies and you can set this upgrade as default to save execution time. You can see ASP upgrades in the monitoring logs. 

You can the find [full documentation about timeout mechanism](https://scrapfly.io/docs/scrape-api/understand-timeout)

[Confirming Scrape Instructions](https://scrapfly.io/docs/scrape-api/troubleshoot#scrape-config)
------------------------------------------------------------------------------------------------

Another way to troubleshoot this is to check the [Monitoring](https://scrapfly.io/docs/monitoring) dashboard and validate that Scrapfly received the same scrape instructions as you intended.

👈

If there's a mismatch, it's likely that the API call was incorrectly configured. If that's not the case then let's proceed further and take a look at potential causes.

> Note that Scrapfly can alter parts of scrape details to bypass scraper blocking when [Anti Scraping Protection bypass](https://scrapfly.io/docs/scrape-api/anti-scraping-protection)is enabled.

[Unexpected Results](https://scrapfly.io/docs/scrape-api/troubleshoot#unexpected-result)
----------------------------------------------------------------------------------------

The results you see in your browser are not always easy to replicate in a scraper. Here are the main causes that could explain **missing or different data**:

#### [Status Code Overview](https://scrapfly.io/docs/scrape-api/troubleshoot#response-statuses)

The first step is to ensure that the scrape request resulted in a **successful response**. To do this the `result.status_code`:

```
{
    [...]
    "result": {
    "status": "DONE",
    "status_code": 203,
    "success": true,
    "url": "https://httpbin.dev/status/203"
    [...]
    }
```

Here's a quick summary of the most common status codes and what are common causes for each:

##### [200](https://scrapfly.io/docs/scrape-api/troubleshoot#status-code-200)

All 200 range codes (200, 201, 202 etc.) are considered success. If that's the case skip to the [Missing Scrape Details](https://scrapfly.io/docs/scrape-api/troubleshoot#missing-req-data) section below.

##### [400](https://scrapfly.io/docs/scrape-api/troubleshoot#status-code-400)

This error stands for client error and this likely means the scrape request is misconfigured:

*   Check the scrape URL
*   Check the scrape request headers
*   Check the scrape request body if it's a POST or PUT type request
*   See the [Missing Scrape Details](https://scrapfly.io/docs/scrape-api/troubleshoot#missing-req-data) section below

##### [404](https://scrapfly.io/docs/scrape-api/troubleshoot#status-code-410)

The page is **not found** and this likely means the scrape URL is invalid. Typo in the URL is most likely cause though alternatively, this can also mean request misconfiguration. See the [Missing Scrape Details](https://scrapfly.io/docs/scrape-api/troubleshoot#missing-req-data) section below.

##### [410](https://scrapfly.io/docs/scrape-api/troubleshoot#status-code-410)

The page is **gone** and this likely means the scrape URL has become invalid. This is common when scraping pages with an expiration date like second hand listings or advertisements.

##### [405](https://scrapfly.io/docs/scrape-api/troubleshoot#status-code-405)

The page doesn't accept current HTTP method. This can be caused by sending POST-type request to GET endpoints and vice versa.

##### [406](https://scrapfly.io/docs/scrape-api/troubleshoot#status-code-406)

The page doesn't accept current content type. This can be caused by sending JSON-type request to HTML endpoints and vice versa or setting invalid `Accept` header.

#### [Missing Scrape Details](https://scrapfly.io/docs/scrape-api/troubleshoot#missing-req-data)

The most common reason for missing data is that the scraper is missing configuration details that are required to fully load the page.

When replicating requests from web browser in Scrapfly it's important to match all request details.

##### [URL Parameters](https://scrapfly.io/docs/scrape-api/troubleshoot#req-parameters)

URL parameters are everything after the `?` symbol and optimally this should match what we see in the browser.

For example in the URL `https://web-scraping.dev/product/2?variant=one&COLOR=dark%20blue` we should keep both `variant=one` and `COLOR=dark%20blue` parameters in the scrape request as they appear in the URL including:

*   Parameter order. Here, "variant" then "COLOR"
*   Parameter name spelling and case. Here, "COLOR" is uppercase
*   Parameter value encoding and formatting (if any). Here, the color value is url encoded as "dark%20blue"

Some non-functional parameters like analytics tracking parameters should be ignored. These parameters often appear as non-sensical IDs (like `?tid=cfa44df`) and can be easily confirmed if the website functionality remains the same when they are removed.

While Scrapfly configures all headers related to fingerprinting and blocking it cannot predict all custom headers for all websites.

This is particularly important when websites use customer headers that are usually identified with `X-` prefix - these should be replicated and included in scrape requests.

##### [Cookies](https://scrapfly.io/docs/scrape-api/troubleshoot#req-cookies)

Some pages can be cookie-locked and require cookies set from previous requests. The easiest way to handle this is to use Scrapfly [Session](https://scrapfly.io/docs/scrape-api/session) and request the pages in the required order.

#### [Dynamic Websites](https://scrapfly.io/docs/scrape-api/troubleshoot#dynamic-websites)

The website could be **dynamically loaded** through browser javascript. If you're scraping without [render_js](https://scrapfly.io/docs/scrape-api/getting-started#api_param_render_js) parameter Scrapfly is not executing javascript which can cause the said data difference. If you are using `render_js` then ensure the scraper is waiting for the website to fully load using the [wait_for_selector](https://scrapfly.io/docs/scrape-api/getting-started#api_param_wait_for_selector) or [rendering_wait](https://scrapfly.io/docs/scrape-api/getting-started#api_param_rendering_wait) parameters.

#### [Geo Location](https://scrapfly.io/docs/scrape-api/troubleshoot#geo-location)

Data could be different or missing because of a different **proxy country**. By default, Scrapfly selects a fitting proxy randomly which might not always match the desired scrape region. Try changing the proxy [country](https://scrapfly.io/docs/scrape-api/getting-started#api_param_country) parameter to match your region, e.g. `country=us`.

#### [Scraper Blocking](https://scrapfly.io/docs/scrape-api/troubleshoot#scraper-blocking)

Another cause could be **anti-bot** measures which are designed to block scrapers. For this, make sure [Anti Scraping Protection bypass](https://scrapfly.io/docs/scrape-api/anti-scraping-protection) is enabled.

Additionally, you can improve success chances by:

*    Enabling browser usage by default `render_js=true`[](https://scrapfly.io/docs/scrape-api/javascript-rendering)
*    Enabling residential proxy network `proxy_pool=public_residential_pool`[](https://scrapfly.io/docs/scrape-api/proxy#api)
*    Ensuring the scrape config matches web browser requests as closely as possible - request headers, POST content etc. For more see the related FAQ entries. 👉

[Errors](https://scrapfly.io/docs/scrape-api/troubleshoot#errors)
-----------------------------------------------------------------

Scrapfly uses a comprehensive error code status system that indicates exactly what went wrong with a scrape request and error details can be accessed through Scrapfly response `result.error` field:

```
{
    "config": { ... },
    "context": { ... },
    "result": {
    [...],
    "status": "DONE",
    "success": false,
    "reason": null,
    "error": {
    "http_code": 429,
    "code": "ERR::THROTTLE::MAX_REQUEST_RATE_EXCEEDED",
    "description": "Your scrape request as been throttle. Too much request during the last minute. If it's not expected, please check your throttle configuration for the given project and env",
    "error_id": "9993a546-b899-4927-b788-04f5c4e473d5",
    "message": "Max request rate exceeded",
    "scrape_id": "7c61352c-f1a7-4ea6-a0b8-198d7ac6fe1a",
    "retryable": false,
    "doc_url": "https://scrapfly.io/docs/scrape-api/error/ERR::THROTTLE::MAX_REQUEST_RATE_EXCEEDED"
    },
    [...],
    }
    }
```

This field contains all of the information needed to troubleshoot the error. In particular, error `code` and `http_code` can be used to troubleshoot any error page.

The http and error codes are defined in the **[Errors](https://scrapfly.io/docs/scrape-api/errors)** documentation or can be looked up through using the command.

For example, will look up all errors related to http status code `422` and will look up all pages related to this error.

[Scraping Costs](https://scrapfly.io/docs/scrape-api/troubleshoot#cost)
-----------------------------------------------------------------------

To troubleshoot billing issues, first check the `cost` field in the [Monitoring](https://scrapfly.io/docs/monitoring) dashboard. This field breaks down all the credit costs used for this scrape request.

👈

Note that scrape cost can vary for each scrape request depending on the scrape details. Many costs like [Anti Scraping Protection bypass](https://scrapfly.io/docs/scrape-api/anti-scraping-protection) are only billed when use is required and tech is reused when possible with reduced charge.
