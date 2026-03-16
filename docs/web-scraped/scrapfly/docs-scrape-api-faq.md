# Source: https://scrapfly.io/docs/scrape-api/faq

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/faq

Markdown Content:
FAQ
---

Here are some of the most common issues and questions that come up when using Scrapfly API. See the tag filter on the right for more.

> **Using Scrapfly with AI models?**Check out the [MCP Server FAQ](https://scrapfly.io/docs/mcp/faq)for questions about using Scrapfly through the Model Context Protocol with Claude Desktop, Cursor, and other AI clients.

[How to send a POST-type requests?](https://scrapfly.io/docs/scrape-api/faq#post-requests)
------------------------------------------------------------------------------------------

#POST#Requests

This can be done by calling scrapfly API through `POST` HTTP requests instead of the default `GET`. Scrapfly uses the same request type for scraping as it's called with. See the [request method customization](https://scrapfly.io/docs/scrape-api/custom#method) page for more info.

For Scrapfly Typescript and Python SDKs the `method="POST"` parameter can be used instead.

[Why are URL parameters missing in my Scrapfly requests?](https://scrapfly.io/docs/scrape-api/faq#missing-parameter)
--------------------------------------------------------------------------------------------------------------------

#Requests

If your Scrapfly scrape requests end up missing URL parameters it's likely that you are not url encoding the URL properly as `url` parameter has to be [url encoded](https://scrapfly.io/web-scraping-tools/urlencode)

*   Valid: `url=https%3A%2F%2Fhttpbin.org%2Fget%3Ffoo%3D1%26bar%3D2`
*   **Invalid:**`url=https://httpbin.org/get?foo=1&bar=2`; Here, the `bar=2` will be interpreted as Scrapfly parameter not scrape URL parameter. 

[Why is my scraped HTML result missing data?](https://scrapfly.io/docs/scrape-api/faq#missing-content)
------------------------------------------------------------------------------------------------------

#Scraping#Anti-Bot#Headless Browsers#Proxies

There are many reasons why Scrapfly scraper might see results differently compared to your test web browser. Here are the main points.

The website could be **dynamically loaded** through browser javascript. If you're scraping without [render_js](https://scrapfly.io/docs/scrape-api/getting-started#api_param_render_js) parameter Scrapfly is not executing javascript which can cause the said data difference. If you are using `render_js` then ensure the scraper is waiting for the website to fully load using the [wait_for_selector](https://scrapfly.io/docs/scrape-api/getting-started#api_param_wait_for_selector) or [rendering_wait](https://scrapfly.io/docs/scrape-api/getting-started#api_param_rendering_wait) parameters. See this [Dynamic Scraping Academy](https://scrapfly.io/academy/dynamic-scraping) tutorial for more on dynamic pages.

Another cause could be **anti-bot** measures which are designed to block scrapers. For this, make sure [Anti Scraping Protection bypass](https://scrapfly.io/docs/scrape-api/anti-scraping-protection) is enabled.

Finally, data could be missing because of a different **proxy country**. Try changing the proxy [country](https://scrapfly.io/docs/scrape-api/getting-started#api_param_country) parameter to match your region.

[Why does ASP fail to bypass protection?](https://scrapfly.io/docs/scrape-api/faq#asp-failing)
----------------------------------------------------------------------------------------------

#Scraping#Anti-Bot

Scrapfly's [Anti Scraping Protection bypass](https://scrapfly.io/docs/scrape-api/anti-scraping-protection) is a powerful but not a silver bullet for all cases. However, there are a few things you can do to ensure ASP has the best chance at bypassing anti-bot systems:

The first step is to ensure send **headers and URL parameters** match what the website expects. Scrapfly does manage fingerprint and all-natural headers but websites can set custom values through javascript or other scripting. For some examples, refer to our Scrapeground [CSRF](https://scrapfly.io/scrapeground/headers/csrf) and [CSRF](https://scrapfly.io/scrapeground/headers/referer) exercise tutorials.

When scraping with `POST` ensure that the request body also matches the expected formatting and data values.

See the [Anti Scraping Protection bypass](https://scrapfly.io/docs/scrape-api/anti-scraping-protection) page for more.

[What does HTTP status code 400 mean?](https://scrapfly.io/docs/scrape-api/faq#status-400)
------------------------------------------------------------------------------------------

#Requests#Error

Response status code 400 means that the request made to Scrapfly API is malformed. Ensure that the request parameters match the expected values and formatting described in the [API specification](https://scrapfly.io/docs/scrape-api/getting-started#spec). For more see the [Errors](https://scrapfly.io/docs/scrape-api/errors#web_scraping_api_error) page for all applicable error codes related to status code 400.

To debug this see response json content which describes what parameter is configured incorrectly.

### Examples

Missing required `url` parameter:

```
{
                    "error_id": "26490351-0ff4-4b13-b885-3fbf115e2a89",
                    "http_code": 400,
                    "links": null,
                    "message": "Missing mandatory `url` parameter e.g: url=https://google.com",
                    "reason": "Bad Request"
                    }
```

Invalid protocol in the `url` parameter:

```
{
                    "error_id": "c318989d-6928-48e8-be4f-07a3da549e3d",
                    "http_code": 400,
                    "links": null,
                    "message": "Invalid uri protocol `url` parameter must begin with http:// or https://, given httpz://httpbin.dev/get",
                    "reason": "Bad Request"
                    }
```

[What does HTTP status code 401 mean?](https://scrapfly.io/docs/scrape-api/faq#status-401)
------------------------------------------------------------------------------------------

#Requests#Error

Response status code 401 means authorization error. You most likely forgot to add `key` parameter to Scrapfly API calls. For more see the [Errors](https://scrapfly.io/docs/scrape-api/errors#web_scraping_api_error) page for all applicable error codes related to status code 401.

### Examples

```
{
                "status": "error",
                "http_code": 401,
                "reason": "Unauthorized",
                "error_id": "301e2d9e-b4f5-4289-85ea-e452143338df",
                "message": "Invalid API key"
                }
```

[Why am I getting Read Timeout errors?](https://scrapfly.io/docs/scrape-api/faq#read-timeout-error)
---------------------------------------------------------------------------------------------------

#Requests#Error

As complex scraping operations can take a long time to execute Scrapfly sets read timeout to 155 seconds. Most HTTP clients have lower defaults of 30 seconds or less. To prevent read timeout set your HTTP client's read timeout to at least 155 seconds.

[How do I know how many API credits my scrapes use?](https://scrapfly.io/docs/scrape-api/faq#billing-cost)
----------------------------------------------------------------------------------------------------------

#Billing

The credit use is calculated based on scraping details and enabled features.

*   From the API response: The results are available in the `X-Scrapfly-Api-Cost` API response header and `context.cost` data field. Alternatively, cost breakdown can also be found in the [Monitoring](https://scrapfly.io/docs/monitoring) dashboard under `cost` field. 
*   From the dashboard: The cost per call and the overview is available in the [dashboard monitoring section](https://scrapfly.io/dashboard/monitoring), then you can inspect the cost of each scrape. On each scrape log, you can see the cost breakdown on the right side under the `cost` tab. 

[What is concurrency?](https://scrapfly.io/docs/scrape-api/faq#concurrency)
---------------------------------------------------------------------------

#Concurrency

Concurrency measures the number of requests that are currently in flight through Scrapfly. Each Scrapfly plan has a different concurrency quota and exceeding it will result in failed scrape requests.

Concurrency is decreased by 1 for each scheduled scrape and reset as soon as the scrape request finishes.

**Related Error:**[ERR::SCRAPE::TOO_MANY_CONCURRENT_REQUEST](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::TOO_MANY_CONCURRENT_REQUEST)

> If you're having trouble with concurrency usage decreasing ensure that your HTTP client's read timeout is set to 155 seconds.

[How to check concurrency use?](https://scrapfly.io/docs/scrape-api/faq#concurrency-use)
----------------------------------------------------------------------------------------

#Concurrency

To program with concurrency in mind, you can check the following API response headers:

*   `X-Scrapfly-Account-Concurrent-Usage` Indicate the current number of requests in flight (scrape is waiting for the response). Global, applied to current Scrapfly account. 
*   `X-Scrapfly-Account-Remaining-Concurrent-Usage` Indicates the remaining concurrency limit. Global, applied to current Scrapfly account. 
*   `X-Scrapfly-Project-Concurrent-Usage` Indicate the current number of requests in flight (scrape is waiting for the response). Scoped, applied to the selected [Scrapfly project](https://scrapfly.io/docs/project). 
*   `X-Scrapfly-Project-Remaining-Concurrent-Usage` Indicates the remaining concurrency limit. Scoped, applied to the selected [Scrapfly project](https://scrapfly.io/docs/project). 

**Related Error:**[ERR::SCRAPE::TOO_MANY_CONCURRENT_REQUEST](https://scrapfly.io/docs/scrape-api/error/ERR::SCRAPE::TOO_MANY_CONCURRENT_REQUEST)

[What is asynchronous programming?](https://scrapfly.io/docs/scrape-api/faq#async)
----------------------------------------------------------------------------------

#Concurrency

Languages like Javascript, Python, etc. support asynchronous programming which allows easy asynchronous connections. This is one of the easiest ways to handle web scraper scaling and both Scrapfly [Python SDK](https://scrapfly.io/docs/sdk/python) and [Typescript SDK](https://scrapfly.io/docs/sdk/typescript) support easy concurrency through async.

#Billing

Scrapfly PAG allows you to continue scraping beyond the subscription credit limit to prevent scrapers from breaking and potentially losing data. Note that PAG usage are generally more expensive than subscription credits so it's best to avoid it if it's possible to predict the scraping load. see the [Billing page](https://scrapfly.io/docs/billing#extra_usage) for more info.

> In case of upgrade or downgrade, any ongoing PAGusage is billed at the plan rate they have been recorded with and are not refundable.

#Billing

From PRO plan, you can go over your quota and be billed on PAG model. You can completely disable PAG per project basis:

1.   In your dashboard, in the left menu, click on project
2.   Select a project
3.   Unselect "Allow PAG"
4.   Click update

> **By default, all account include a hard limit for Pay As You Go to avoid any major issue. The Pay As You Go usage is capped to 125% of your monthly quota.**You will receive a notification when you reach 100% of your quota to warn you. 
> Example: You have 1,000,000 API Credits per month, you can use up to 1,250,000 API Credits on PAG, so a total of 2,250,000 credits.
> 
> 
> If you have ongoing operation that will reach this limit, you can [contact us](https://scrapfly.io/docs/support) to increase the limit exceptionally. If you are reaching this limit on your ENTERPRISE plan, you can [contact us](https://scrapfly.io/docs/support) to create a custom plan.

[How to estimate API Credit cost of a scrape?](https://scrapfly.io/docs/scrape-api/faq#billing-calculation)
-----------------------------------------------------------------------------------------------------------

#Billing

Scrapfly API credit cost is calculated based on the scrape details and enabled features. For that refer to the [Billing Table](https://scrapfly.io/docs/scrape-api/getting-started#billing) page.

However, the easiest way to estimate scrape cost is to try it in our [Web API Player](https://scrapfly.io/dashboard/playground/web-scraper), on the right side, we display the estimation for a given configuration. 

 Each scrape request made in the web player also shows up in monitoring dashboard where [scrape cost breakdown](https://scrapfly.io/docs/scrape-api/faq#billing-cost) can be found.

[How to cancel Scrapfly subscription?](https://scrapfly.io/docs/scrape-api/faq#cancel)
--------------------------------------------------------------------------------------

#Billing

You can cancel your subscription from your dashboard: click on the account setting located on the right side of the top bar, then billing and then on the right side, the "plan" card, there is a cancel button. Alternatively, here's the direct link to [the dashboard billing](https://scrapfly.io/dashboard/billing) page. Cancellation keep your current subscription until the renewal date and downgrade to free.

[How to control Scrapfly credit spending?](https://scrapfly.io/docs/scrape-api/faq#spending)
--------------------------------------------------------------------------------------------

#Billing

*   [Project](https://scrapfly.io/docs/project#quote) can be configured with spending, concurrency and PAG use limits. 
*   [Throttling](https://scrapfly.io/docs/throttling#budget_limit) can be customized to define a budget limit per hour, day, week or month. Note that too low a budget can block all scraping so ensure a proper minimum is set. 
*   [cost_budget](https://scrapfly.io/docs/scrape-api/getting-started#api_param_cost_budget) parameter can be used to define the maximum budget per scrape. Note that too low a budget can block all scraping so ensure a proper minimum is set. 

[How to set Scrapfly proxy country?](https://scrapfly.io/docs/scrape-api/faq#proxy-set-country)
-----------------------------------------------------------------------------------------------

#Features#Proxies

The [country](https://scrapfly.io/docs/scrape-api/getting-started#api_param_country) can be set to set proxy country for Scrapfly scrape requests. This parameter can also take a list of countries (separated by a comma) and Scrapfly will choose a random proxy from the list for each scraper. If the parameter is not set Scrapfly will choose a semi-random proxy from all available countries. For more see the [proxy documentation page](https://scrapfly.io/docs/scrape-api/proxy#geo).

[Can I use Scrapfly as a HTTP Proxy?](https://scrapfly.io/docs/scrape-api/faq#scrapfly-as-proxy)
------------------------------------------------------------------------------------------------

#Features

No, the HTTP proxy protocol does not offer enough capability to enable Scrapfly features however [proxified_response feature](https://scrapfly.io/docs/scrape-api/faq#proxified-response) can be used that imitates HTTP proxy behavior.

[Where can I see history of my scrape requests?](https://scrapfly.io/docs/scrape-api/faq#scrape-history)
--------------------------------------------------------------------------------------------------------

#Features#Dashboard

Scrapfly provides a [Monitoring](https://scrapfly.io/docs/monitoring) dashboard where all scrape requests are logged.

**Privacy Protection:** Scrapfly automatically filters sensitive data from logs. Passwords, tokens, API keys, emails, and other credentials matching common patterns (e.g., `password`, `token`, `secret`, `auth`) are automatically redacted and replaced with `<SECRET>` in stored logs.

[Can I cache Scrapfly scrape requests?](https://scrapfly.io/docs/scrape-api/faq#cache)
--------------------------------------------------------------------------------------

#Features#Cache

Yes, Scrapfly supports [Cache](https://scrapfly.io/docs/scrape-api/cache) which can cache scrape results on Scrapfly servers. Any subsequent scrape requests will be served from the cache for a set amount of time or until the cache is explicitly cleared. In short, see the [cache](https://scrapfly.io/docs/scrape-api/getting-started#api_param_cache) and [cache_ttl](https://scrapfly.io/docs/scrape-api/getting-started#api_param_cache) parameters.
