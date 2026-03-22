# Source: https://scrapfly.io/docs/scrape-api/anti-scraping-protection

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/scrape-api/anti-scraping-protection

Markdown Content:
Anti Scraping Protection (ASP)
------------------------------

Service Level Agreenment (SLA) and Service Interruption

**Service interruptions may occasionally occur** independent of Scrapfly's control. As anti scraping protection technology is constantly evolving Scrapfly engineers are working hard to keep up with the latest changes. This may take hours to days to weeks to implement as a reliable production-grade remedy. It is essential to bear this in mind and develop your software accordingly when utilizing this feature.

Please note that

*    We can't provide ETA regarding service restoration due to the R&D, however with the volume we handle and the number of corporates account we have, most of incidents are resolved 1 business days on well known anti bot, on average around from 3 to 7 business days. 
*    The API Credit cost may fluctuate, if a website introduce new protection(s) or migrate to another anti bot server. The underlying resources required to handle it can change (residential network, browser usage, custom solution) 
*    SLA plan are available from a minimum commitment of **$50k/Month**

Scrapfly's Anti-Scraping Protection is designed to unblock protected websites that are inaccessible to bots. We accomplish this by incorporating various concepts that help maintain a coherent fingerprint, making it as close to that of a real user as possible when scraping a website.

To use ASP just enable [asp parameter](https://scrapfly.io/docs/scrape-api/getting-started#api_param_asp) in your API call.

Scrapfly is capable of identifying and resolving obstacles posed by commonly used anti-scraping measures. Our platform also provides support for custom anti-scraping measures implemented by popular websites. Scrapfly ASP bypass does not require any extra input from you, and **you will receive successful responses automatically**.

* * *

If you are interested in understanding the technical aspects of how we achieve this undetectability, we have published a series of articles on the subject available in the [learning resources section](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#learning_resources) below.

Usage and Abuse Limitation

To summarize our [TOS](https://scrapfly.io/terms-of-service), following usage are prohibited:

*   Automated Online Payment
*   Account Creation
*   Spam Posts
*   Vote Falsification
*   Credit Card Testing
*   Login Brute Force
*   Referral / Gifting systems
*   Ads fraud
*   Banks
*   Ticketing (Automated Buying System)
*   Betting, Casino, Gambling

The use of ASP can be authorized for use by cybersecurity firms (red teams) after obtaining approval from the relevant parties for the specific domains they wish to test.

[Usage](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#usage)
---------------------------------------------------------------------------

When **ASP** is enabled, anti-bot solution vendor are automatically detected and everything is managed to bypass it.

```
curl -G \
--request "GET" \
--url "https://api.scrapfly.io/scrape" \
--data-urlencode "asp=true" \
--data-urlencode "key=__API_KEY__" \
--data-urlencode "url=https://httpbin.dev/anything"
```

`https://api.scrapfly.io/scrape?asp=true&key=&url=https%3A%2F%2Fhttpbin.dev%2Fanything`

**ASP will fine-tune some parameters regardless of user configuration. Some examples are listed below:**

These adjustments can increase the request credit price and for that check the [pricing section for more details](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#pricing).

*   **[Proxy Pool:](https://scrapfly.io/docs/scrape-api/proxy)** ASP can access exclusive private proxy pools specific to scraped targets or upgrade to a better general proxy pool.
*   **[Browser Usage:](https://scrapfly.io/docs/scrape-api/javascript-rendering)** ASP might enable it to bypass pages that require javascript.
*   **[Headers:](https://scrapfly.io/docs/scrape-api/custom)** Some browser headers set by you might be ignored or modified. Headers based on resource type (image, file, html etc) and referer can be fine-tuned as well. We can also add custom headers if the target require or challenge method require them. 
    *   `referer` is auto generated if not present, you can pass `none` as header value to no pass any `referer` header to the target website
    *   `cookie` ASP auto handle session usage and reuse challenge cookies for faster result
    *   `accept` can be changed regarding the type of resources (images, script, json, xhr, etc)
    *   `content-type` based on request body and website target format
    *   `user-agent`: Make sure to set a custom user-agent only when required by the target website, as the user agent is already managed by ASP for optimal bypass. 
        *   Chrome based user agent are ignored and will be replaced by the one provided for the fingerprint
        *   Non-Chrome user agent are left untouched

*   **[Country:](https://scrapfly.io/docs/scrape-api/proxy)** Base on target website location and usual traffic, ASP might fine-tune the proxy country. If you set [country](https://scrapfly.io/docs/scrape-api/getting-started#api_param_country) explicitly the ASP will respect this.
*   **[OS:](https://scrapfly.io/docs/scrape-api/custom)** To align fingerprint for optimal bypass we may change the OS and related headers based on the exit proxy hardware.
*   **Body:** JSON are re-encoded to produce the same serialized output as a real web browser.

[ASP Limitations](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#limitation)
------------------------------------------------------------------------------------------

While popular anti-bot vendors can be bypassed without any additional effort, there are still some areas that require manual configuration of calls.

For best results, it's important to understand how the target websites work and replicate their behavior in scraping calls. ASP bypass handles bot detection, and it's up to the user to configure last mile settings to avoid identification through use patterns.

### [How to avoid anti bot detection on POST request](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#avoid-anti-bot)

Avoiding anti-bot detection on a POST request can be tricky, but there are some key areas to focus on:

1.   Mimic a real user's behavior: Anti-bot systems often check for unusual behavior that may indicate a bot, such as a high number of requests from the same IP address or at the same time. You can mimic a real user's behavior by visiting some pages to retrieve navigation cookies/referers urls.

2.   Handling CSRF: Cross-Site Request Forgery (CSRF) is a common anti-bot measure used by websites.

For more, see these tutorials and resources:

    *   [CSRF header tutorial](https://scrapfly.io/scrapeground/headers/csrf) on Scrapfly's Scrapeground.
    *   [introduction to headers in scraper blocking](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-headers/) blog post.

3.   Use realistic headers: Anti-bot systems can detect bots by looking at the headers of the requests. You should try to replicate the headers of a real user's request as closely as possible. This includes the `Accept`, `Content-Type`, `Referer` and `Origin` headers. Make sure to configure correctly the value of `Accept` and `Content-Type` regarding the content you expect (json, html).

For more, see these tutorials and resources:

    *   [Referer](https://scrapfly.io/scrapeground/headers/referer) header tutorial on Scrapfly's Scrapeground.
    *   [introduction to headers in scraper blocking](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-headers/) blog post.

4.   Authentication: If the website requires authentication, make sure you include the correct credentials in your request. This might involve logging in to the website first, then including the session cookie or token in your POST request. If the API/Website requires it, ASP is not able to manage this, you must handle it on your side.

For more, see these tutorials and resources:

    *   [Cookies authentication](https://scrapfly.io/scrapeground/cookies) tutorial on Scrapfly's Scrapeground.

Overall, the key to bypassing anti-bot measures on a POST request is to replicate the headers, cookies, and authentication of a regular browser request as closely as possible. This requires careful inspection of the website's code and network traffic to identify the required elements.

### [Website with Private/Hidden API](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#hidden-apis)

Scraping a private API can be a bit more challenging than scraping public APIs. Here are some recommendations to follow:

1.    Make sure you have permission: Before scraping any private API, make sure you have the necessary permission from the website owner or API provider. Scraping a private API without permission can result in legal consequences. 
2.    Mimic a real user: When scraping a private API, it's important to mimic a real user as closely as possible. This means sending the same headers and parameters that a real user would send when accessing the API. 
3.    Use authentication: Most private APIs require some form of authentication, such as a token or API key. Make sure you obtain the necessary credentials and use them in your requests. 
4.    Monitor for changes: Private APIs can change over time, so it's important to monitor for any changes in the API's structure or authentication requirements. If you notice any changes, update your scraping code accordingly. 

Overall, scraping private APIs requires more attention to detail and careful configuration of requests. Following these recommendations can help ensure a successful and ethical scraping process.

[Maximize Your Success Rate](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#maximize_success_rate)
----------------------------------------------------------------------------------------------------------------

#### [Network Quality](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#network-quality)

In many cases, datacenter IPs are sufficient. However, anti-bot vendors may check the origin of the IP when protecting websites, to determine if the traffic comes from a datacenter or a regular connection. In such cases, residential networks can provide a better IP reputation, as they are registered under a regular ASN that helps control the origin of the IP.

*   [Introduction To Proxies in Web Scraping](https://scrapfly.io/blog/posts/introduction-to-proxies-in-web-scraping/)
*   [How to Avoid Web Scraping Blocking: IP Address Guide](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-ip-addresses/)
*   [Learn how to change the network type](https://scrapfly.io/docs/scrape-api/proxy#api)

> **API Usage:**`proxy_pool=public_residential_pool`, [checkout the related documentation](https://scrapfly.io/docs/scrape-api/getting-started#api_param_proxy_pool "Select Residential Proxy via HTTP API")

#### [Use a Browser](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#use-browser)

Most anti bots check the browser fingerprint and javascript engine to generate detection metrics.

> **API Usage:**`render_js=true`, [checkout the related documentation](https://scrapfly.io/docs/scrape-api/getting-started#api_param_render_js "Enable browser rendering via HTTP API")

#### [Verify Cookies and Headers](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#verify-cookies)

Observe headers/cookies of regular calls that are successful; you can figure out if you need to add extra headers or retrieve specific cookies to authenticate. You can use [the dev tool and inspect the network activity](https://developer.chrome.com/docs/devtools/network/).

*   [What are Chrome Devtools?](https://scrapfly.io/blog/answers/browser-developer-tools-in-web-scraping/)
*   [How to Avoid Web Scraping Blocking: Headers Guide](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-headers/)

> **API Usage:**`headers[referer]=https%3A%2F%2Fweb-scraping.dev`(value is [url encoded](https://scrapfly.io/web-scraping-tools/urlencode "URL encode")), [checkout the related documentation](https://scrapfly.io/docs/scrape-api/getting-started#api_param_headers "Customize API headers")

#### [Navigation Coherence](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#nav-coherence)

To ensure navigation coherence when scraping unofficial APIs, you may need to obtain cookies from your navigation. One way to do this is by enabling session and rendering JavaScript during the initial scraping to retrieve cookies. Once the cookies are stored in your session, you can continue scraping without rendering JavaScript while still applying the previously obtained cookies for consistency. The following Scrapfly features you must take a look to achieve that:

*   [Using Session (sticky proxy - keep same ip, Cookies memory)](https://scrapfly.io/docs/scrape-api/session)
*   [Javascript Rendering - Headless browser](https://scrapfly.io/docs/scrape-api/javascript-rendering)

> **API Usage:**`session=my-unique-session-name`, [checkout the related documentation](https://scrapfly.io/docs/scrape-api/getting-started#api_param_session "Session Usage")

> **API Usage:**`render_js=true`, [checkout the related documentation](https://scrapfly.io/docs/scrape-api/getting-started#api_param_render_js "Javascript Rendering - Headless browser")

#### [Geo Blocking](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#geo-blocking)

When browsing certain websites, users may encounter blocks based on their IP location. Scrapfly can bypass this issue by default, as it selects a random country from its pool. However, specifying the country based on the location of the website can be a helpful way to avoid geo-blocking.

> **API Usage:**`country=us`, [checkout the related documentation](https://scrapfly.io/docs/scrape-api/getting-started#api_param_country "Select country via HTTP API")

[Pricing](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#pricing)
-------------------------------------------------------------------------------

Our Anti-Scraping Protection (ASP) solution is a sophisticated tool that provides advanced protection against scraping attempts. It is designed to adapt to various anti-scraping measures implemented on different websites. To achieve this, the ASP dynamically fine-tune your configuration parameters based on the target and the anti-scraping solution in place, and this can have an impact on pricing.

The main impact on the API Cost are:

*   Browser Usage
*   Proxy Pool
*   Target/Shield

You will find the [pricing grid](https://scrapfly.io/docs/scrape-api/billing#billing) for browser usage and proxy network type. Specific target/shield have fees and are not publicly documented, only very specific one have fees otherwise there is no additional cost (Those fees are displayed in the cost section on your log). To get the full detail of the cost, you can the [dedicated troubleshooting section](https://scrapfly.io/docs/scrape-api/troubleshoot#cost)

To ensure predictability and control of your spending, we recommend creating an account and gradually monitoring the usage costs as you increase your volume. You can also the [use api budget](https://scrapfly.io/docs/scrape-api/getting-started#api_param_cost_budget) on scrape call `cost_budget=25` Once you have determined the actual cost, you can check our [set of tools](https://scrapfly.io/docs/scrape-api/getting-started#billing) to make it more predictable and ensure staying within budget.

> It's totally free on non-blocked scrape
> If you scrape various websites, and you don't know which is protected or not, just keep it enabled, no extra cost is applied on non-protected traffic.
> 
> 
> Furthermore, when ASP is enabled, a lot of things are automatically handled with [the fine-tuning of parameters](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#usage) to prevent detection which result in saving.

[Integration](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#integration)
---------------------------------------------------------------------------------------

*   [ASP example with Python SDK](https://scrapfly.io/docs/onboarding#asp)

All related errors are listed below. You can see full description and example of error response on the [Errors section](https://scrapfly.io/docs/scrape-api/errors#proxy). You can also check the [troubleshooting section](https://scrapfly.io/docs/scrape-api/troubleshoot) if you have timeout issue with ASP.

*   [ERR::ASP::CAPTCHA_ERROR](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::CAPTCHA_ERROR) - Something wrong happened with the captcha. We will figure out to fix the problem as soon as possible
*   [ERR::ASP::CAPTCHA_TIMEOUT](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::CAPTCHA_TIMEOUT) - The budgeted time to solve the captcha is reached
*   [ERR::ASP::SHIELD_ERROR](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::SHIELD_ERROR) - The ASP encounter an unexpected problem. We will fix it as soon as possible. Our team has been alerted
*   [ERR::ASP::SHIELD_EXPIRED](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::SHIELD_EXPIRED) - The ASP shield previously set is expired, you must retry.
*   [ERR::ASP::SHIELD_NOT_ELIGIBLE](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::SHIELD_NOT_ELIGIBLE) - The feature requested is not eligible while using the ASP for the given protection/target
*   [ERR::ASP::SHIELD_PROTECTION_FAILED](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::SHIELD_PROTECTION_FAILED) - The ASP shield failed to solve the challenge against the anti scrapping protection
*   [ERR::ASP::TIMEOUT](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::TIMEOUT) - The ASP made too much time to solve or respond
*   [ERR::ASP::UNABLE_TO_SOLVE_CAPTCHA](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::UNABLE_TO_SOLVE_CAPTCHA) - Despite our effort, we were unable to solve the captcha. It can happened sporadically, please retry
*   [ERR::ASP::UPSTREAM_UNEXPECTED_RESPONSE](https://scrapfly.io/docs/scrape-api/error/ERR::ASP::UPSTREAM_UNEXPECTED_RESPONSE) - The response given by the upstream after challenge resolution is not expected. Our team has been alerted

[Learning Resources](https://scrapfly.io/docs/scrape-api/anti-scraping-protection#learning_resources)
-----------------------------------------------------------------------------------------------------

*   [How to Scrape Without Getting Blocked? In-Depth Tutorial](https://scrapfly.io/blog/posts/how-to-scrape-without-getting-blocked-tutorial/)
*   [How to Avoid Web Scraper IP Blocking?](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-ip-addresses/)
*   [How TLS Fingerprint is Used to Block Web Scrapers?](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-tls/)
*   [How Javascript is Used to Block Web Scrapers? In-Depth Guide](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-javascript/)
*   [How to Scrape Dynamic Websites Using Headless Web Browsers](https://scrapfly.io/blog/posts/scraping-using-browsers/)
