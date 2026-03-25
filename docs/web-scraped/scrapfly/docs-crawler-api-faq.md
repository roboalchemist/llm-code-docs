# Source: https://scrapfly.io/docs/crawler-api/faq

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/crawler-api/faq

Markdown Content:
FAQ
---

Here are some of the most common issues and questions that come up when using Scrapfly Crawler API. See the tag filter on the right for more.

[What is the Crawler API?](https://scrapfly.io/docs/crawler-api/faq#what-is-crawler-api)
----------------------------------------------------------------------------------------

#Crawler#Basics

The Scrapfly Crawler API enables recursive website crawling at scale. Unlike the Web Scraping API which scrapes individual URLs, the Crawler API can automatically discover and scrape entire websites following links and applying URL filtering rules.

Results are delivered as industry-standard artifacts like [WARC Format](https://scrapfly.io/docs/crawler-api/warc-format), Parquet, and HAR formats for easy integration with data pipelines. See [Crawler API Getting Started](https://scrapfly.io/docs/crawler-api/getting-started) for more details.

[How do I start a crawl?](https://scrapfly.io/docs/crawler-api/faq#how-to-start-crawl)
--------------------------------------------------------------------------------------

#Crawler#Configuration

To start a crawl, send a POST request to the `/crawl` endpoint with your configuration:

*   **Seed URLs:** Starting points for the crawl (e.g., homepage, category pages)
*   **URL Rules:** Patterns to include/exclude URLs (regex or glob patterns)
*   **Limits:** Maximum pages, crawl depth, time limits
*   **Scrape Config:** Web Scraping API parameters (ASP, proxies, JavaScript rendering, etc.)

The API returns a crawler UUID which you use to check status and retrieve results. See [Crawler API Getting Started](https://scrapfly.io/docs/crawler-api/getting-started) for detailed examples.

[How do I control which URLs get crawled?](https://scrapfly.io/docs/crawler-api/faq#url-filtering)
--------------------------------------------------------------------------------------------------

#Crawler#Configuration

Use URL filtering rules to include or exclude specific URL patterns:

*   **Include rules:** Only crawl URLs matching these patterns (e.g., `/products/*`)
*   **Exclude rules:** Skip URLs matching these patterns (e.g., `/login`, `/cart`)
*   **Domain restrictions:** Stay within specific domains or subdomains

Rules support both glob patterns (`*.html`) and regex patterns for maximum flexibility. See [Crawler API Getting Started](https://scrapfly.io/docs/crawler-api/getting-started) for configuration details.

[How do I limit the size of my crawl?](https://scrapfly.io/docs/crawler-api/faq#crawl-limits)
---------------------------------------------------------------------------------------------

#Crawler#Configuration#Limits

Configure limits to control crawl scope and prevent runaway costs:

*   **max_pages:** Maximum number of pages to crawl
*   **max_depth:** Maximum link depth from seed URLs
*   **max_duration:** Maximum crawl time in seconds
*   **cost_budget:** Maximum API credits to spend

The crawl stops when any limit is reached. Always set appropriate limits to avoid unexpected costs.

[How do I check the status of my crawl?](https://scrapfly.io/docs/crawler-api/faq#check-crawl-status)
-----------------------------------------------------------------------------------------------------

#Crawler#Workflow#Polling

Use the `GET /crawl/{crawler_uuid}` endpoint to check crawl status. The response includes:

*   **status:**`running`, `completed`, `failed`, or `cancelled`
*   **progress:** Number of pages crawled, pending URLs, etc.
*   **cost:** Total API credits consumed so far
*   **artifacts:** Available result artifacts (WARC, Parquet, HAR)

Poll this endpoint periodically until the status changes to `completed` or `failed`. See [Crawler API Getting Started](https://scrapfly.io/docs/crawler-api/getting-started) for workflow details.

[Can I get notified when my crawl completes?](https://scrapfly.io/docs/crawler-api/faq#webhooks)
------------------------------------------------------------------------------------------------

#Crawler#Workflow#Webhooks

Yes! Configure a webhook URL when creating the crawl. Scrapfly will send a POST request to your webhook when:

*   The crawl completes successfully
*   The crawl fails or is cancelled
*   Each page is crawled (optional)

Webhooks eliminate the need for polling and provide real-time notifications. See [Crawler API Webhook](https://scrapfly.io/docs/crawler-api/webhook) for configuration and examples.

[How do I retrieve crawl results?](https://scrapfly.io/docs/crawler-api/faq#get-results)
----------------------------------------------------------------------------------------

#Crawler#Results#Artifacts

Results are available as downloadable artifacts in multiple formats:

*   **WARC:** Industry-standard web archive format (gzipped)
*   **Parquet:** Columnar format optimized for analytics and big data
*   **HAR:** HTTP Archive format for request/response inspection

Use the `GET /crawl/{crawler_uuid}/artifacts/{format}` endpoint to download results. See [Crawler API Results](https://scrapfly.io/docs/crawler-api/results) for detailed format specifications.

[Which artifact format should I use?](https://scrapfly.io/docs/crawler-api/faq#artifact-formats)
------------------------------------------------------------------------------------------------

#Crawler#Results#Artifacts

Choose based on your use case:

*   **WARC:** Best for archival, compliance, and reprocessing. Standard format used by Internet Archive and libraries.
*   **Parquet:** Best for data analytics, machine learning, and integration with data warehouses (BigQuery, Snowflake, Databricks).
*   **HAR:** Best for debugging, request inspection, and replaying requests in browser dev tools.

All formats contain the same data - choose what works best for your workflow. See [WARC Format](https://scrapfly.io/docs/crawler-api/warc-format) and [Crawler API Results](https://scrapfly.io/docs/crawler-api/results) for format details.

#Crawler#Extraction

Yes! Configure extraction rules to extract structured data from crawled pages simultaneously. The Crawler API supports:

*   **AI extraction models:** Automatic extraction using predefined models (products, articles, reviews, etc.)
*   **LLM prompts:** Custom extraction using AI prompts
*   **Template-based:** Define JSON templates with CSS/XPath selectors

Extracted data is included in the result artifacts alongside raw HTML content. See [Crawler API Extraction Rules](https://scrapfly.io/docs/crawler-api/extraction-rules) for configuration examples.

[How is Crawler API billing calculated?](https://scrapfly.io/docs/crawler-api/faq#billing-cost)
-----------------------------------------------------------------------------------------------

#Billing

Crawler API billing is simple: **total cost = sum of all Web Scraping API calls made during the crawl**.

Each page crawled is billed as a Web Scraping API request based on your enabled features (ASP, JavaScript rendering, proxies, screenshots, etc.). The total cost is shown in the crawl status response.

See [Crawler API Billing](https://scrapfly.io/docs/crawler-api/billing) for detailed cost calculation and examples.

[How do I estimate the cost of a crawl before running it?](https://scrapfly.io/docs/crawler-api/faq#estimate-cost)
------------------------------------------------------------------------------------------------------------------

#Billing

To estimate costs:

1.   Estimate the number of pages that will be crawled (use `max_pages` as upper bound)
2.   Check the cost per page in [Crawler API Billing](https://scrapfly.io/docs/crawler-api/billing) based on your scrape configuration
3.   Multiply: `estimated_pages × cost_per_page = total_cost`

Start with a small crawl (low `max_pages`) to test your configuration and measure actual cost per page. You can also set `cost_budget` to automatically stop the crawl when reaching a credit limit.

[How do I prevent unexpected crawl costs?](https://scrapfly.io/docs/crawler-api/faq#prevent-overages)
-----------------------------------------------------------------------------------------------------

#Billing#Limits

Always configure crawl limits to prevent runaway costs:

*   Set `max_pages` to limit total pages crawled
*   Set `cost_budget` to cap total API credits spent
*   Set `max_duration` to limit crawl time
*   Configure [project limits](https://scrapfly.io/docs/project) for additional spending controls

The crawl automatically stops when any limit is reached, preventing unexpected charges.

[Why did my crawl not find any URLs?](https://scrapfly.io/docs/crawler-api/faq#no-urls-crawled)
-----------------------------------------------------------------------------------------------

#Error#Troubleshooting

This usually happens due to:

*   **Too restrictive URL rules:** Include rules don't match any links on the seed pages
*   **JavaScript-loaded links:** Enable `render_js: true` in scrape config to render JavaScript
*   **Wrong seed URLs:** Seed pages don't contain links to follow
*   **Cross-domain restrictions:** Links point to different domains and same-domain crawling is enforced

Test your URL rules on a small sample first and check the HAR artifact to inspect discovered links.

[Does Crawler API support anti-bot bypass?](https://scrapfly.io/docs/crawler-api/faq#bypass-anti-bot)
-----------------------------------------------------------------------------------------------------

#Features#Anti-Bot

Yes! Enable [Anti Scraping Protection bypass](https://scrapfly.io/docs/scrape-api/anti-scraping-protection) in the scrape configuration when creating the crawl. ASP is applied to every page crawled, bypassing protections like Cloudflare, PerimeterX, DataDome, etc.

All Web Scraping API features work with the Crawler API including proxies, JavaScript rendering, sessions, and screenshots.

[Does Crawler API rotate proxies automatically?](https://scrapfly.io/docs/crawler-api/faq#proxy-rotation)
---------------------------------------------------------------------------------------------------------

#Features#Proxies

Yes! The Crawler API automatically rotates proxies between pages to avoid rate limiting and IP blocks. Configure proxy settings in the scrape configuration:

*   **proxy_pool:** Choose datacenter or residential proxies
*   **country:** Specify proxy country or list of countries

See [Proxy documentation](https://scrapfly.io/docs/scrape-api/proxy) for all available proxy options.

[Can Crawler API handle JavaScript-rendered websites?](https://scrapfly.io/docs/crawler-api/faq#javascript-rendering)
---------------------------------------------------------------------------------------------------------------------

#Features#JavaScript

Yes! Enable `render_js: true` in the scrape configuration. The crawler will use headless browsers to execute JavaScript on every page, making it ideal for modern SPAs and dynamic websites.

You can also use [JavaScript scenarios](https://scrapfly.io/docs/scrape-api/javascript-scenario) to automate interactions like clicking buttons, scrolling, filling forms, etc. before extracting content.

[How fast does the Crawler API crawl?](https://scrapfly.io/docs/crawler-api/faq#crawl-speed)
--------------------------------------------------------------------------------------------

#Features#Concurrency

Crawl speed depends on your account's concurrency limit. The crawler uses your available concurrency to fetch multiple pages in parallel, significantly speeding up large crawls.

For example, with 100 concurrent requests, the crawler can fetch 100 pages simultaneously. Configure [throttling rules](https://scrapfly.io/docs/throttling) if you need to slow down crawling for specific domains.

[Does Crawler API support sessions?](https://scrapfly.io/docs/crawler-api/faq#sessions)
---------------------------------------------------------------------------------------

#Features#Sessions

Yes! Configure a session in the scrape configuration to maintain cookies and context across crawled pages. This is useful for:

*   Crawling authenticated areas (after login)
*   Maintaining shopping cart state
*   Preserving user preferences across pages

See [Session](https://scrapfly.io/docs/scrape-api/session) for session configuration details.

[Can I monitor crawl progress in real-time?](https://scrapfly.io/docs/crawler-api/faq#monitor-progress)
-------------------------------------------------------------------------------------------------------

#Workflow#Monitoring

Yes! The crawl status endpoint provides real-time progress metrics:

*   **Pages crawled:** Total pages successfully scraped
*   **Pages pending:** URLs queued for crawling
*   **Pages failed:** URLs that failed to scrape
*   **Current depth:** Current crawl depth from seed URLs
*   **Credits used:** API credits consumed so far

Additionally, all crawled pages appear in the [Monitoring dashboard](https://scrapfly.io/docs/monitoring) for detailed inspection.

[Can I cancel a running crawl?](https://scrapfly.io/docs/crawler-api/faq#cancel-crawl)
--------------------------------------------------------------------------------------

#Workflow

Yes! Send a `DELETE` request to `/crawl/{crawler_uuid}` to cancel a running crawl. The crawler will stop immediately and you can still retrieve artifacts for pages that were already crawled.

You are only charged for pages successfully crawled before cancellation.

[Can I resume a failed or cancelled crawl?](https://scrapfly.io/docs/crawler-api/faq#resume-crawl)
--------------------------------------------------------------------------------------------------

#Workflow

Currently, crawls cannot be resumed. If a crawl fails or is cancelled, you need to create a new crawl. However, you can retrieve partial results (artifacts) from incomplete crawls for pages that were successfully scraped.

[How long are crawl artifacts stored?](https://scrapfly.io/docs/crawler-api/faq#artifact-retention)
---------------------------------------------------------------------------------------------------

#Limits#Retention

Crawl artifacts are stored according to your plan's log retention policy, typically 7-90 days depending on your subscription. Download artifacts before they expire if you need long-term storage.

Check your [project settings](https://scrapfly.io/docs/project) for your specific retention period.

[Can I schedule recurring crawls?](https://scrapfly.io/docs/crawler-api/faq#schedule-crawls)
--------------------------------------------------------------------------------------------

#Workflow#Scheduling

The Crawler API doesn't have built-in scheduling, but you can use external tools:

*   **Cron jobs:** Schedule crawls using cron on your server
*   **Cloud schedulers:** Use AWS EventBridge, GCP Cloud Scheduler, or Azure Logic Apps
*   **Workflow automation:** Use tools like Airflow, Prefect, or n8n

Simply trigger the `POST /crawl` endpoint on your desired schedule.

#Features#Extraction

Yes! Define custom extraction rules using CSS or XPath selectors to extract specific data fields from crawled pages. You can also use AI models or LLM prompts for intelligent extraction.

See [Crawler API Extraction Rules](https://scrapfly.io/docs/crawler-api/extraction-rules) for template syntax and examples.

[Why is my crawl running slowly?](https://scrapfly.io/docs/crawler-api/faq#slow-crawl)
--------------------------------------------------------------------------------------

#Troubleshooting#Performance

Common reasons for slow crawls:

*   **Low concurrency:** Upgrade your plan for higher concurrency limits
*   **JavaScript rendering:** Headless browsers are slower than HTTP requests - only enable if needed
*   **Slow target website:** Some websites respond slowly or throttle requests
*   **Throttling rules:** Check if you have [throttling](https://scrapfly.io/docs/throttling) configured

Disable `render_js` for static pages and increase concurrency for faster crawls.

[Why did my crawl stop before completing?](https://scrapfly.io/docs/crawler-api/faq#crawl-stopped-early)
--------------------------------------------------------------------------------------------------------

#Troubleshooting#Limits

Check which limit was reached in the crawl status response:

*   **max_pages:** Maximum page limit reached
*   **max_depth:** Maximum depth limit reached
*   **max_duration:** Time limit exceeded
*   **cost_budget:** Credit budget exhausted
*   **No more URLs:** All discoverable URLs within rules have been crawled

Increase the relevant limit if you want to crawl more pages.

[How do I integrate Crawler API with my data pipeline?](https://scrapfly.io/docs/crawler-api/faq#integrate-data-pipeline)
-------------------------------------------------------------------------------------------------------------------------

#Integration

The Crawler API is designed for easy integration:

*   **Webhooks:** Get notified when crawls complete and trigger downstream processing
*   **Parquet artifacts:** Load directly into BigQuery, Snowflake, Databricks, or Pandas
*   **WARC artifacts:** Standard format supported by archival and ETL tools
*   **REST API:** Easy integration with any programming language or workflow tool

Use webhooks + Parquet for the most streamlined integration with modern data stacks.

[When should I use Crawler API vs Web Scraping API?](https://scrapfly.io/docs/crawler-api/faq#when-use-crawler)
---------------------------------------------------------------------------------------------------------------

#Comparison

Use **Crawler API** when:

*   You need to scrape entire websites or large sections
*   You want automatic URL discovery by following links
*   You need archival-quality artifacts (WARC)
*   You're building a search engine, data lake, or compliance archive

Use **Web Scraping API** when:

*   You have a specific list of URLs to scrape
*   You need real-time scraping with immediate results
*   You're building application features (price monitoring, product data, etc.)
*   You want maximum control over scraping order and logic
