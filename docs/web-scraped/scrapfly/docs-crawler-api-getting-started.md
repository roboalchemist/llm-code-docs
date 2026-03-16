# Source: https://scrapfly.io/docs/crawler-api/getting-started

Title: | Scrapfly

URL Source: https://scrapfly.io/docs/crawler-api/getting-started

Markdown Content:
Getting Started with Scrapfly Crawler API
-----------------------------------------

The **Scrapfly Crawler API** enables recursive website crawling at scale. We leverage [WARC](https://scrapfly.io/docs/crawler-api/warc-format), Parquet format for large scale scraping and you can easily visualize using HAR artifact. Crawl entire websites with configurable limits, extract content in multiple formats simultaneously, and retrieve results as industry-standard artifacts.

[Quick Start: Choose Your Workflow](https://scrapfly.io/docs/crawler-api/getting-started#quick-start)
-----------------------------------------------------------------------------------------------------

The Crawler API supports two integration patterns. Choose the approach that best fits your use case:

### Polling Workflow

Schedule a crawl, poll the status endpoint to monitor progress, and retrieve results when complete. **Best for batch processing, testing, and simple integrations.**

1.   **Schedule Crawl**
Create a crawler with a single API call. The API returns immediately with a crawler UUID:

```
curl -X POST "https://api.scrapfly.io/crawl?key=" \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://web-scraping.dev",
    "page_limit": 5
  }'
``` 
Response includes crawler UUID and status:

`{"uuid": "550e8400-e29b-41d4-a716-446655440000", "status": "PENDING"}` 
2.   **Monitor Progress**
Poll the status endpoint to track crawl progress:

`curl https://api.scrapfly.io/crawl/{crawler_uuid}/status?key=` 
Status response shows real-time progress:

```
{
  "crawler_uuid": "550e8400-e29b-41d4-a716-446655440000",
  "status": "RUNNING",
  "is_finished": false,
  "is_success": null,
  "state": {
    "urls_visited": 847,
    "urls_extracted": 1523,
    "urls_failed": 12,
    "urls_skipped": 34,
    "urls_to_crawl": 676,
    "api_credit_used": 8470,
    "duration": 145,
    "stop_reason": null
  }
}
``` 
#### Understanding the Status Response

| Field | Values | Description |
| --- | --- | --- |
| `status` | `PENDING` `RUNNING` `DONE` `CANCELLED` | Current crawler state - actively running or completed |
| `is_finished` | `true` / `false` | Whether crawler has stopped (regardless of success/failure) |
| `is_success` | `true` - Success `false` - Failed `null` - Running | Outcome of the crawl (only set when finished) |
| `stop_reason` | See table below | Why the crawler stopped (only set when finished) |

**Stop Reasons:**

| Stop Reason | Description |
| --- | --- |
| `no_more_urls` | All discovered URLs have been crawled - **normal completion** |
| `page_limit` | Reached the configured `page_limit` |
| `max_duration` | Exceeded the `max_duration` time limit |
| `max_api_credit` | Reached the `max_api_credit` limit |
| `seed_url_failed` | The starting URL failed to crawl - **no URLs visited** |
| `user_cancelled` | User manually cancelled the crawl via API |
| `crawler_error` | Internal crawler error occurred |
| `no_api_credit_left` | Account ran out of API credits during crawl |
| `storage_error` | An error occurred while saving the content |
3.   **Retrieve Results**
Once `is_finished: true`, download artifacts or query content:

```
# Download WARC artifact (recommended for large crawls)
curl https://api.scrapfly.io/crawl/{crawler_uuid}/artifact?key=&type=warc -o crawl.warc.gz

# Query specific URL content
curl https://api.scrapfly.io/crawl/{crawler_uuid}/contents?key=&url=https://web-scraping.dev/page&format=markdown

# Or batch retrieve multiple URLs (max 100 per request)
curl -X POST https://api.scrapfly.io/crawl/{crawler_uuid}/contents/batch?key=&formats=markdown \
  -H 'Content-Type: text/plain' \
  -d 'https://web-scraping.dev/page1
https://web-scraping.dev/page2
https://web-scraping.dev/page3'
``` 
For comprehensive retrieval options, see [Retrieving Crawler Results](https://scrapfly.io/docs/crawler-api/results).

### Real-Time Webhook Workflow

Schedule a crawl with webhook configuration, receive instant HTTP callbacks as events occur, and process results in real-time. **Best for real-time data ingestion, streaming pipelines, and event-driven architectures.**

1.   **Schedule Crawl with Webhook**
Create a crawler and specify the webhook name configured in your dashboard:

```
curl -X POST "https://api.scrapfly.io/crawl?key=" \
  -H 'Content-Type: application/json' \
  -d '{
    "url": "https://web-scraping.dev",
    "page_limit": 5,
    "webhook_name": "my-crawler-webhook",
    "webhook_events": [
      "crawler_started",
      "crawler_url_visited",
      "crawler_finished"
    ]
  }'
``` 
Response includes crawler UUID:

`{"uuid": "550e8400-e29b-41d4-a716-446655440000", "status": "PENDING"}` 
2.   **Receive Real-Time Webhooks**
Your endpoint receives HTTP POST callbacks as events occur during the crawl:

```
{
  "event": "crawler_url_visited",
  "payload": {
    "crawler_uuid": "550e8400-e29b-41d4-a716-446655440000",
    "url": "https://web-scraping.dev/page",
    "status_code": 200,
    "depth": 1,
    "state": {
      "urls_visited": 42,
      "urls_to_crawl": 158,
      "api_credit_used": 420
    }
  }
}
``` 
**Webhook Headers:**

| Header | Purpose |
| --- | --- |
| `X-Scrapfly-Crawl-Event-Name` | Event type (e.g., `crawler_url_visited`) for fast routing |
| `X-Scrapfly-Webhook-Job-Id` | Crawler UUID for tracking |
| `X-Scrapfly-Webhook-Signature` | HMAC-SHA256 signature for verification |
3.   **Process Events in Real-Time**
Handle webhook callbacks to stream data to your database, trigger pipelines, or process results:

```
# Example: Python webhook handler
@app.post('/webhooks/crawler')
def handle_crawler_webhook(request):
    event = request.headers['X-Scrapfly-Crawl-Event-Name']
    payload = request.json()['payload']

    if event == 'crawler_url_visited':
        # Stream scraped content to database
        save_to_database(payload['url'], payload['content'])

    elif event == 'crawler_finished':
        # Trigger downstream processing
        trigger_data_pipeline(payload['crawler_uuid'])

    return {'status': 'ok'}
``` 

For detailed webhook documentation and all available events, see [Crawler Webhook Documentation](https://scrapfly.io/docs/crawler-api/webhook).

[Error Handling](https://scrapfly.io/docs/crawler-api/getting-started#errors)
-----------------------------------------------------------------------------

Crawler API uses standard HTTP response codes and provides detailed error information:

| `200` - OK | Request successful |
| --- |
| `201` - Created | Crawler job created successfully |
| `400` - Bad Request | Invalid parameters or configuration |
| `401` - Unauthorized | Invalid or missing API key |
| `404` - Not Found | Crawler job not found |
| `429` - Too Many Requests | Rate limit or concurrency limit exceeded |
| `500` - Server Error | Internal server error |
| See the [full error list](https://scrapfly.io/docs/crawler-api/errors) for more details. |

* * *

[API Specification](https://scrapfly.io/docs/crawler-api/getting-started#spec)
------------------------------------------------------------------------------

Authentication (Query Parameter)

API Key for authentication. Must be passed as URL query parameter (`?key=...`), not in request body.

`scp-live-xxx...`

Crawl Configuration

Starting URL for the crawl. Must be a valid HTTP/HTTPS URL. [Must be URL encoded](https://scrapfly.io/web-scraping-tools/urlencode)

`https://web-scraping.dev``https://example.com/blog`

Maximum pages to crawl. Set to `0` for unlimited (subject to subscription limits)

`100``1000``0`

Maximum link depth from starting URL. Depth 0 is the starting URL, depth 1 is links from it

`2``5``0`

Exclude URLs matching these path patterns. Supports wildcards (`*`). Max 100 paths

`["/admin/*"]``["*/login"]`

Only crawl URLs matching these patterns. Supports wildcards (`*`). Max 100 paths. Mutually exclusive with `exclude_paths`

`["/blog/*"]``["/products/*"]`

Advanced Configuration

By default, crawler stays within the starting URL's base path. Enable to crawl any path on the same domain

`true``false`

Allow crawler to follow links to external domains. External pages are scraped but their links are not followed

`true``false`

Whitelist of external domains when `follow_external_links=true`. Max 250 domains. Supports wildcards (`*`)

`["*.web-scraping.dev"]``["cdn.site.com"]`

Allow crawler to follow links to subdomains of the starting domain.

`true` (default): all subdomains are followed. Use `allowed_internal_subdomains` to restrict to specific ones.

`false`: only the seed URL's exact hostname is crawled, no subdomains at all.

`true``false`

Restrict crawling to specific subdomains when `follow_internal_subdomains=true`.

**If empty (default): all subdomains are allowed.**

If set: only the seed hostname and the listed subdomains are crawled.

Each pattern must be a subdomain of the seed URL's domain. Supports wildcard patterns (`*`). Maximum 250 entries.

Ignored when `follow_internal_subdomains=false`.

`["blog.web-scraping.dev"]``["*.cdn.web-scraping.dev"]`

Wait time in ms after page load before extraction. Set `0` to disable browser rendering. Range: 0-25000ms

`0``2000``5000`

Maximum concurrent scrape requests. Limited by your account's concurrency limit. Set `0` for account default

`5``10``0`

Delay between requests in milliseconds. Range: 0-15000ms. Be polite to target servers

`"1000"``"5000"`

Custom User-Agent string. Ignored when `asp=true` (ASP manages User-Agent automatically)

`MyBot/1.0 (+https://example.com/bot)`

Use sitemap.xml for URL discovery if available

`true``false`

Respect robots.txt rules and `Disallow` directives

`true``false`

Caching Options

Enable cache layer for crawled pages. Cached versions are used instead of re-crawling

`true``false`

Cache time-to-live in seconds. Range: 0-604800 (max 7 days). Only applies when `cache=true`

`3600``86400``604800`

Force refresh of cached pages. All pages will be re-crawled even if valid cache exists

`true``false`

Ignore `rel="nofollow"` attributes on links. Crawl all links regardless of nofollow

`true``false`

Content & Extraction

Content formats to extract: `html`, `clean_html`, `markdown`, `text`, `json`, `extracted_data`, `page_metadata`

`["markdown"]``["html", "text"]`

 More details

**Available formats:**

*   `html` - Original HTML content
*   `clean_html` - Cleaned and sanitized HTML
*   `markdown` - LLM-ready markdown format
*   `text` - Plain text extraction
*   `json` - Parse as JSON (for API responses)
*   `extracted_data` - Structured data from extraction rules
*   `page_metadata` - Page title, description, etc.

Multiple formats can be extracted simultaneously from each page. Markdown format is ideal for LLM processing.

Maximum crawl duration in seconds. Range: 15-10800 (15s to 3 hours). Crawler stops when reached

`900``3600``10800`

Maximum API credits to spend. Set `0` for no limit. Useful for controlling costs

`1000``5000``0`

Webhooks

Name of webhook configured in [dashboard](https://scrapfly.io/dashboard/webhook). Not a URL - references webhook by name

`my-crawler-webhook`

Events to subscribe: `crawler_started`, `crawler_finished`, `crawler_url_visited`, `crawler_url_failed`, etc.

`["crawler_finished"]``["crawler_url_visited"]`

 More details

**Available events:**

*   `crawler_started` - Crawl job has begun
*   `crawler_url_visited` - Page successfully scraped
*   `crawler_url_skipped` - Page skipped (cached, excluded, etc.)
*   `crawler_url_discovered` - New URL found
*   `crawler_url_failed` - Page scrape failed
*   `crawler_stopped` - Crawl stopped (limits reached)
*   `crawler_cancelled` - Crawl manually cancelled
*   `crawler_finished` - Crawl completed

If `webhook_name` is set without specifying events, basic events are used by default.

Proxy & Protection

Select proxy pool. See [proxy dashboard](https://scrapfly.io/dashboard/proxy) for available pools and pricing

`public_datacenter_pool``public_residential_pool`

Proxy country (ISO 3166-1 alpha-2). Supports exclusions (`-gb`) and weighted distribution (`us:10,gb:5`)

`us``us,ca,mx``-gb`

[Anti Scraping Protection](https://scrapfly.io/docs/scrape-api/anti-scraping-protection) - Enable advanced anti-bot bypass with browser rendering and fingerprinting. Ignores custom `user_agent`

`true``false`

[Get Crawler Status](https://scrapfly.io/docs/crawler-api/getting-started#get-status)
-------------------------------------------------------------------------------------

Retrieve the current status and progress of a crawler job. Use this endpoint to poll for updates while the crawler is running.

GET`https://api.scrapfly.io/crawl/{crawler_uuid}/status`

`curl "https://api.scrapfly.io/crawl/{crawler_uuid}/status?key="`

**Response includes:**

*   `status` - Current status (PENDING, RUNNING, COMPLETED, FAILED, CANCELLED)
*   `state.urls_discovered` - Total URLs discovered
*   `state.urls_crawled` - URLs successfully crawled
*   `state.urls_pending` - URLs waiting to be crawled
*   `state.urls_failed` - URLs that failed to crawl
*   `state.api_credits_used` - Total API credits consumed

[Get Crawled URLs](https://scrapfly.io/docs/crawler-api/getting-started#get-urls)
---------------------------------------------------------------------------------

Retrieve a list of all URLs discovered and crawled during the job, with metadata about each URL.

GET`https://api.scrapfly.io/crawl/{crawler_uuid}/urls`

```
# Get all visited URLs
curl "https://api.scrapfly.io/crawl/{crawler_uuid}/urls?key=&status=visited"

# Get failed URLs with pagination
curl "https://api.scrapfly.io/crawl/{crawler_uuid}/urls?key=&status=failed&page=1&per_page=100"
```

**Query Parameters:**

*   `key` - Your API key (required)
*   `status` - Filter by URL status: `visited`, `pending`, `failed`
*   `page` - Page number for pagination (default: 1)
*   `per_page` - Results per page (default: 100, max: 1000)

[Get Content](https://scrapfly.io/docs/crawler-api/getting-started#get-content)
-------------------------------------------------------------------------------

Retrieve extracted content from crawled pages in the format(s) specified in your crawl configuration.

### Single URL or All Pages (GET)

GET`https://api.scrapfly.io/crawl/{crawler_uuid}/contents`

```
# Get all content in markdown format
curl "https://api.scrapfly.io/crawl/{crawler_uuid}/contents?key=&format=markdown"

# Get content for a specific URL
curl "https://api.scrapfly.io/crawl/{crawler_uuid}/contents?key=&format=html&url=https://web-scraping.dev/page"
```

**Query Parameters:**

*   `key` - Your API key (required)
*   `format` - Content format to retrieve (must be one of the formats specified in crawl config)
*   `url` - Optional: Retrieve content for a specific URL only

### Batch Content Retrieval (POST)

POST`https://api.scrapfly.io/crawl/{crawler_uuid}/contents/batch`

Retrieve content for multiple specific URLs in a single request. More efficient than making individual GET requests for each URL. **Maximum 100 URLs per request.**

```
# Batch retrieve content for multiple URLs
curl -X POST "https://api.scrapfly.io/crawl/{crawler_uuid}/contents/batch?key=&formats=markdown,text" \
  -H "Content-Type: text/plain" \
  -d "https://web-scraping.dev/page1
https://web-scraping.dev/page2
https://web-scraping.dev/page3"
```

**Query Parameters:**

*   `key` - Your API key (required)
*   `formats` - Comma-separated list of formats (e.g., `markdown,text,html`)

**Request Body:**

*   `Content-Type: text/plain` - Plain text with URLs separated by newlines
*   **Maximum 100 URLs per request**

**Response Format:**

*   `Content-Type: multipart/related` - Standard HTTP multipart format (RFC 2387)
*   `X-Scrapfly-Requested-URLs` header - Number of URLs in the request
*   `X-Scrapfly-Found-URLs` header - Number of URLs found in the crawl results
*   Each part contains `Content-Type` and `Content-Location` headers identifying the format and URL

[Download Artifact](https://scrapfly.io/docs/crawler-api/getting-started#get-artifact)
--------------------------------------------------------------------------------------

Download industry-standard archive files containing all crawled data, including HTTP requests, responses, headers, and extracted content. Perfect for storing bulk crawl results offline or in object storage (S3, Google Cloud Storage).

GET`https://api.scrapfly.io/crawl/{crawler_uuid}/artifact`

```
# Download WARC artifact (gzip compressed, recommended for large crawls)
curl "https://api.scrapfly.io/crawl/{crawler_uuid}/artifact?key=&type=warc" -o crawl.warc.gz

# Download HAR artifact (JSON format)
curl "https://api.scrapfly.io/crawl/{crawler_uuid}/artifact?key=&type=har" -o crawl.har
```

**Query Parameters:**

*   `key` - Your API key (required)
*   `type` - Artifact type: 
    *   `warc` - Web ARChive format (gzip compressed, industry standard)
    *   `har` - HTTP Archive format (JSON, browser-compatible)

[Billing](https://scrapfly.io/docs/crawler-api/getting-started#billing)
-----------------------------------------------------------------------

Crawler API billing is simple: **the cost equals the sum of all Web Scraping API calls** made during the crawl. Each page crawled consumes credits based on enabled features (browser rendering, anti-scraping protection, proxy type, etc.).

For detailed billing information, see [Crawler API Billing](https://scrapfly.io/docs/crawler-api/billing).
