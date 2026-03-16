# Source: https://scrapfly.io/academy

Title: | Scrapfly

URL Source: https://scrapfly.io/academy

Markdown Content:
Scrapfly Web Scraping Academy
-----------------------------

Learn _Everything_ about Web Scraping!
--------------------------------------

Scrapfly Academy covers modern web scraping issues and their solutions walking you through them step-by-step.

Web scraping can be hard and confusing at times, and we know it! We have been doing it for years and we have been through all the issues you can imagine. We have built Scrapfly to make web scraping easy and accessible and here we are sharing everything we know! (well almost 😉)

![Image 1: Developer hub docs](https://cdn.scrapfly.io/0.1.176/www/public/svg/academy/academy.svg?version=0.1.176)

[Web Scraping Roadmap](https://scrapfly.io/academy#mindmap)
-----------------------------------------------------------

![Image 2: mindmap icon](https://cdn.scrapfly.io/0.1.176/www/public/svg/academy/mindmap-icon.svg?version=0.1.176)

For a quick overview of all web scraping topics, challenges and everything that makes web scraping such a fascinating subject see our interactive academy **mindmap** 👇

HTML Parsing
------------

HTML is designed to be machine parsable which means extracting content when web scraping is easy even for very complex pages. For this usually XPath or CSS Selectors are used.

[Read More](https://scrapfly.io/academy/html-parsing)

JSON Parsing
------------

JSON is a key-to-value data format used by Javascript but adopted by other languages as well. It's often encountered on the web and the the documents can be big and complex requiring parsing.

JSON documents most commonly are encountered in [Hidden API](https://scrapfly.io/academy/hidden-api-scraping) and [Hidden Web](https://scrapfly.io/academy/hidden-web-data) scraping.

[Read More](https://scrapfly.io/academy/html-parsing)

Static Page Scraping
--------------------

Static HTML pages are the easiest and simplest form pages encountered in web scraping. Easy way to confirm whether the page is static or not is to disable javascript in your browser and confirm whether the data is still present.

An example of a static HTML page would be [web-scraping.dev/products](https://web-scraping.dev/products) page which lists a page of products without using any javascript. On the other hand, [web-scraping.dev/testimonials](https://web-scraping.dev/testimonials) is a dynamic page which does use javascript to load pages as the user scrolls down.

[Read More](https://scrapfly.io/academy/static-scraping)

Dynamic Page Scraping
---------------------

Dynamic Pages are very different from classic static HTML pages as the page rendering is done client side, by the web browser. This becomes an issue in web scraping as web scrapers are not web browsers, well, not usually.

An example of a dynamic page would be [web-scraping.dev/testimonials](https://web-scraping.dev/testimonials) where more testimonials are being loaded as the user scrolls down the page.

[Read More](https://scrapfly.io/academy/dynamic-scraping)

Headless Browsers
-----------------

Headless browsers are special version of web browsers that contain no UI elements and run in the background. This makes them ideal for web automation and web scraping dynamic pages.

Scraping using headless browsers has some clear advantages and disadvantages:

*   Easier to scrape dynamic pages as scrapers see everything the browser sees.
*   Can help with scraper blocking.

*   Extremely resource intense. Browsers use significantly more sources from processing and memory to bandwidth use.
*   Prone to bugs as browsers are very complicated.

[Read More](https://scrapfly.io/academy/headless-browsers)

Hidden API Scraping
-------------------

When web pages need to load data on demand background requests to hidden data APIs are often used. These hidden APIs can be scraped directly.

[Read More](https://scrapfly.io/academy/hidden-api-scraping)

Hidden Web Data Scraping
------------------------

Some data can be hidden in the invisible parts of HTML pages. Often this data is in hidden `<script>` tags in JSON format that can be conveniently extracted as whole datasets.

[Read More](https://scrapfly.io/academy/hidden-web-data)

Reverse Engineering Websites
----------------------------

Understanding how websites work can help to scrape them or even discover hidden APIs and data. This is called reverse engineering and there are tools that can assist with this.

[Read More](https://scrapfly.io/academy/reverse-engineering)

HTTP Secrets
------------

Pages can require secret HTTP attributes to load successfully. This details need to be discovered and included in web scrapers which can done through browser developer tools through reverse engineering.

For an example, see this [Referer-lock](https://scrapfly.io/scrapeground/headers/referer) Scrapeground exercise - loads page only when correct `Referer` is provided.

[More on Reverse Engineering](https://scrapfly.io/academy/reverse-engineering)

Javascript Tokens
-----------------

Pages can require secret tokens to load successfully. This details need to be discovered and included in web scrapers which can done through browser developer tools through reverse engineering.

For an example, see this [CSRF-lock](https://scrapfly.io/scrapeground/headers/csrf) Scrapeground exercise where page only loads when correct secret token is provided.

[More on Reverse Engineering](https://scrapfly.io/academy/reverse-engineering)

Fingerprinting
--------------

Web scraper connections can be fingerprinted through various means which can lead to web scraper blocking or even feeding scrapers with false data.

[Read More](https://scrapfly.io/academy/scraper-blocking)

Javascript Fingerprinting
-------------------------

Javascript can reveal a lot about the user's machine which leads to scraper identification and blocking. For this scrapers that use headless browsers need to be extra diligent. See [intro to javascript fingerprinting](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-javascript/).

> Scrapfly automatically bypasses Javascript fingerprint when [javascript rendering](https://scrapfly.io/docs/scrape-api/javascript-rendering)feature is used.

[Read More](https://scrapfly.io/academy/scraper-blocking)

TLS Fingerprinting
------------------

TLS handshake is the first step to every `https` (secure) connection and it can be fingerprinted. This fingerprint is used to track and identify web scrapers. See [intro to TLS fingerprinting](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-tls/).

> Scrapfly automatically bypasses TLS fingerprint.

[More on Scraper Blocking](https://scrapfly.io/academy/scraper-blocking)

HTTP2 Fingerprinting
--------------------

HTTP v2 is complex enough of a protocol that it can be fingerprinted to track and identify web scrapers.

> Scrapfly automatically bypasses http2 fingerprint.

[More on Scraper Blocking](https://scrapfly.io/academy/scraper-blocking)

HTTP Headers
------------

HTTP request headers provide metadata about outgoing requests. Scrapers that are sending headers that are different compared to the real web browser users can be easily identified and blocked. For more see [Introduction to request headers](https://scrapfly.io/blog/posts/how-to-avoid-web-scraping-blocking-headers/) for more.

[More on Scraper Blocking](https://scrapfly.io/academy/scraper-blocking)

Anti-Bot Services
-----------------

There are many software as a service tools that try to identify and block web scrapers. These tools use all fingerprinting and IP tracking techniques to identify web scrapers.

Here's a list of the most popular ones and introduction articles on how they work and what can be done to bypass them:

*   [Akamai](https://scrapfly.io/blog/posts/how-to-bypass-akamai-anti-scraping/)
*   [Cloudflare](https://scrapfly.io/blog/posts/how-to-bypass-cloudflare-anti-scraping/)
*   [Datadome](https://scrapfly.io/blog/posts/how-to-bypass-datadome-anti-scraping/)
*   [Imperva / Incapsula](https://scrapfly.io/blog/posts/how-to-bypass-imperva-incapsula-anti-scraping/)
*   [PerimerterX / Human](https://scrapfly.io/blog/posts/how-to-bypass-perimeterx-human-anti-scraping/)

> Scrapfly automatically bypasses anti scraping services when [ASP](https://scrapfly.io/docs/scrape-api/anti-scraping-protection)feature is used.

[More on Scraper Blocking](https://scrapfly.io/academy/scraper-blocking)

Proxy Types
-----------

There are 3 primary proxy types:

*   Datacenter - IP addresses given out to datacenter corporations (AWS, Google etc.)
*   Residential - IP addresses given out to residential homes.
*   Mobile - IP addresses given out to mobile 3/4/5G towers

Datacenter proxies are easy to identify and block while residential and mobile appear as natural traffic thus better for web scraping.

> Scrapfly offers millions of residential [proxies](https://scrapfly.io/docs/scrape-api/proxy)from 50+ countries.

[More on Proxies](https://scrapfly.io/academy/proxies)

Proxy Rotation
--------------

To fully take advantage of proxies the addresses need to be rotated for each scraping request. Rotation logic can impact overall scraper blocking when scraping targets that use behavior analysis for scraper blocking.

For an example, see our [intro to proxy rotation](https://scrapfly.io/blog/posts/how-to-rotate-proxies-in-web-scraping/) article.

> Scrapfly automatically rotates [proxies](https://scrapfly.io/docs/scrape-api/proxy)for you from over 50+ countries of your choice.

[More on Proxies](https://scrapfly.io/academy/proxies)

Proxy Analysis
--------------

Proxy IP addresses are tracked and analyzed globally which can lead to scraper blocking. Proxies are being identified by subnet, ASN (owner number), country, city, ISP and more.

> Scrapfly has millions of [proxies](https://scrapfly.io/docs/scrape-api/proxy)that are specifically made for web scraping.

[More on Proxies](https://scrapfly.io/academy/proxies)

Geographically Locked Content
-----------------------------

Some websites can only be accessed in specific countries which means proxies are needed to scrape this content. Scraping from the natural country of the target website can also drastically reduce scraper blocking rate.

> Scrapfly has millions of [proxies](https://scrapfly.io/docs/scrape-api/proxy)from 50+ countries.

[More on Proxies](https://scrapfly.io/academy/proxies)

Scraped Data Parsing
--------------------

The web is full of different data formats: HTML, XML, JSON just to name a few. These data formats need to be parsed using robust parsing techniques like Xpath, CSS selectors and JMESPath.

[Read More](https://scrapfly.io/academy/data-processing)

Scraped Data Validation
-----------------------

For long-term web scraping projects data output validation tests are a great way to keep an eye on scraper performance. Static data models can instantly capture any changes but are fragile while schema-based validators are more flexible.

Read more about [data validation techniques in web scraping](https://scrapfly.io/blog/posts/how-to-ensure-web-scrapped-data-quality/).

[More on Data Processing](https://scrapfly.io/academy/data-processing)

Data Cleanup
------------

As scrapers are collecting unknown data from the internet data-cleanup process is an important step of the delivery process. This involves natural language parsing, data normalization and so on.

[Read More](https://scrapfly.io/academy/data-processing)

Multi Processing
----------------

Scraping tasks can be processing intensive, especially when it comes to data parsing. Multi-processing allows distributing of scrape tasks through multiple processes that can take advantage of multiple CPU cores.

See the [Multi Processing Section](https://scrapfly.io/blog/posts/web-scraping-speed/#multi-process-parsing) of this tutorial.

HTTP Cache
----------

HTTP caching is an important scraper optimization step especially when it comes to repeated scraping, testing and debugging.

> Scrapfly can store and manage web scraping cache using the [cache](https://scrapfly.io/docs/scrape-api/cache)feature.

Asynchronous Code
-----------------

As web scraping relies on IO-bound operations (HTTP requests) asynchronous programming can speed up scrapers hundreds to thousands of times. For more see [intro to asynchronous requests in scraping](https://scrapfly.io/blog/posts/web-scraping-speed/#async-requests) article.

Services
--------

Separating scraper performance into different services is the most common way of scaling up web scrapers. Using full web scraping services like Scrapfly is an option but it's also possible to host parts of web scraping tasks as services yourself. Here are some examples:

*   [Scraping with Selenium Grid](https://scrapfly.io/blog/posts/intro-to-web-scraping-using-selenium-grid/)

* * *

Powered by Tools Built for Web Scraping!
----------------------------------------

Aside from being an awesome web scraping API that does everything for you Scrapfly also hosts a platitude of web scraping tools that are also used by Scrapfly Academy.

* * *
