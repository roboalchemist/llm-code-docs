# Crawl4AI Cloud API - Complete Reference

> Crawl4AI Cloud is a managed web crawling and data extraction API.
> Base URL: https://api.crawl4ai.com
> All requests require `X-API-Key` header for authentication.

---

## Authentication

All API requests require an API key in the header:
```
X-API-Key: YOUR_API_KEY
```

Get your API key from [https://api.crawl4ai.com/dashboard](https://api.crawl4ai.com/dashboard)

---

## API Endpoints

### Crawl API

#### POST /v1/crawl - Sync Crawl
Crawl a single URL synchronously. Blocks until complete.

```bash
curl -X POST https://api.crawl4ai.com/v1/crawl \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{"url": "https://example.com"}'
```

**Parameters:**
- `url` (required): URL to crawl
- `strategy`: "browser" (default) or "http" (faster, no JS)
- `browser_config`: Browser settings (viewport, headers, cookies)
- `crawler_config`: Crawl settings (screenshot, extraction_strategy, wait_until)
- `proxy`: Proxy configuration
- `bypass_cache`: Skip cache (default: false)

**Response:**
```json
{
  "url": "https://example.com",
  "success": true,
  "html": "<html>...</html>",
  "markdown": {"raw_markdown": "# Page Title..."},
  "extracted_content": "...",
  "screenshot": "base64...",
  "status_code": 200,
  "duration_ms": 1250,
  "crawl_strategy": "browser"
}
```

#### POST /v1/crawl/batch - Batch Crawl
Crawl multiple URLs (max 10) sequentially.

```bash
curl -X POST https://api.crawl4ai.com/v1/crawl/batch \
  -H "X-API-Key: YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "urls": ["https://example.com", "https://example.org"],
    "strategy": "http"
  }'
```

**Response:**
```json
{
  "results": [
    {"url": "https://example.com", "success": true, "status_code": 200},
    {"url": "https://example.org", "success": true, "status_code": 200}
  ],
  "total_duration_ms": 2500
}
```

#### POST /v1/crawl/async - Async Crawl
Create async job for up to 100 URLs. Returns job ID for polling.

```bash
curl -X POST https://api.crawl4ai.com/v1/crawl/async \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{"urls": ["https://example.com"], "webhook_url": "https://your-server.com/webhook"}'
```

**Response:**
```json
{"job_id": "async-abc123", "status": "pending", "urls_count": 1}
```

#### GET /v1/crawl/jobs/{job_id} - Get Job Status
```bash
curl https://api.crawl4ai.com/v1/crawl/jobs/async-abc123 \
  -H "X-API-Key: YOUR_API_KEY"
```

#### GET /v1/crawl/jobs - List Jobs

#### DELETE /v1/crawl/jobs/{job_id} - Cancel Job

#### GET /v1/crawl/jobs/{job_id}/download - Get Download URL

---

### Deep Crawl API

#### POST /v1/deep-crawl - Multi-page Discovery
Crawl entire websites with URL discovery.

```bash
curl -X POST https://api.crawl4ai.com/v1/deep-crawl \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{
    "url": "https://docs.example.com",
    "max_depth": 3,
    "max_urls": 100,
    "strategy_type": "bfs"
  }'
```

**Parameters:**
- `url`: Starting URL
- `max_depth`: Maximum link depth (1-10)
- `max_urls`: Maximum URLs to crawl
- `strategy_type`: "bfs" (breadth-first), "dfs" (depth-first), "best_first"
- `url_filters`: Filter patterns for URLs
- `scorers`: Score URLs for best-first strategy
- `scan_only`: Discover URLs without extracting content

**Response:**
```json
{
  "job_id": "deep-xyz789",
  "status": "running",
  "discovered_urls": 50,
  "crawled_urls": 25
}
```

---

### Extraction Strategies

Include in `crawler_config.extraction_strategy`:

#### CSS Extraction
```json
{
  "type": "json_css",
  "schema": {
    "baseSelector": ".article",
    "fields": [
      {"name": "title", "selector": "h1", "type": "text"},
      {"name": "link", "selector": "a", "type": "attribute", "attribute": "href"}
    ]
  }
}
```

#### XPath Extraction
```json
{
  "type": "json_xpath",
  "schema": {
    "baseSelector": "//article",
    "fields": [
      {"name": "title", "xpath": ".//h1/text()"},
      {"name": "link", "xpath": ".//a/@href"}
    ]
  }
}
```

#### LLM Extraction
```json
{
  "type": "llm",
  "instruction": "Extract product name, price, and description",
  "schema": {
    "type": "object",
    "properties": {
      "product_name": {"type": "string"},
      "price": {"type": "number"},
      "description": {"type": "string"}
    }
  }
}
```

---

### Proxy Configuration

```json
{
  "proxy": {
    "mode": "residential",
    "country": "US"
  }
}
```

**Modes:** "none", "datacenter", "residential"  
**Countries:** "US", "UK", "DE", etc.

---

### Session API

#### POST /v1/sessions - Create Browser Session
```bash
curl -X POST https://api.crawl4ai.com/v1/sessions \
  -H "X-API-Key: YOUR_API_KEY" \
  -d '{"timeout": 300}'
```

**Response:**
```json
{
  "session_id": "sess_abc123",
  "ws_url": "wss://api.crawl4ai.com/v1/cdp/sess_abc123",
  "expires_at": "2025-12-28T12:05:00Z"
}
```

Connect via Puppeteer/Playwright using the `ws_url`.

#### GET /v1/sessions - List Sessions
#### DELETE /v1/sessions/{session_id} - Delete Session

---

### Storage API

#### GET /v1/crawl/storage - Check Storage Usage
```json
{"used_mb": 250.0, "max_mb": 1000, "percent_used": 25.0}
```

---

## Python SDK

```bash
pip install crawl4ai-cloud
```

```python
import asyncio
from crawl4ai_cloud import AsyncWebCrawler, CrawlerRunConfig

async def main():
    async with AsyncWebCrawler(api_key="YOUR_API_KEY") as crawler:
        # Single crawl
        result = await crawler.run("https://example.com")
        print(result.markdown.raw_md)

        # With options
        result = await crawler.run(
            "https://example.com",
            strategy="browser",
            config=CrawlerRunConfig(screenshot=True)
        )

        # Multiple URLs (auto-selects batch or async)
        results = await crawler.run_many(urls, wait=True)

        # Deep crawl
        result = await crawler.deep_crawl(
            "https://docs.example.com",
            strategy="bfs",
            max_urls=50,
            wait=True
        )

asyncio.run(main())
```

---

## JavaScript/TypeScript SDK

```bash
npm install crawl4ai-cloud
```

```typescript
import { AsyncWebCrawler } from 'crawl4ai-cloud';

const crawler = new AsyncWebCrawler({ apiKey: 'YOUR_API_KEY' });

// Single crawl
const result = await crawler.run('https://example.com', null);
console.log(result.markdown?.rawMarkdown);

// With options
const result = await crawler.run('https://example.com', {
  strategy: 'browser',
  config: { screenshot: true }
});

// Multiple URLs
const results = await crawler.runMany(urls, { wait: true });

// Deep crawl
const deepResult = await crawler.deepCrawl('https://docs.example.com', {
  strategy: 'bfs',
  maxUrls: 50,
  wait: true,
});
```

---

## Go SDK

```bash
go get github.com/unclecode/crawl4ai-cloud-sdk/go
```

```go
import "github.com/unclecode/crawl4ai-cloud-sdk/go/pkg/crawl4ai"

crawler, _ := crawl4ai.NewAsyncWebCrawler(crawl4ai.CrawlerOptions{
    APIKey: "YOUR_API_KEY",
})
defer crawler.Close()

// Single crawl
result, _ := crawler.Run("https://example.com", nil)
fmt.Println(result.Markdown.RawMarkdown)

// Deep crawl
deepResult, _ := crawler.DeepCrawl("https://docs.example.com", &crawl4ai.DeepCrawlOptions{
    Strategy: "bfs",
    MaxURLs:  50,
    Wait:     true,
})
```

---

## Rate Limits

| Plan | Requests/min | Daily Crawls | Concurrent |
|------|--------------|--------------|------------|
| Free | 10 | 50 | 1 |
| Starter | 30 | 500 | 2 |
| Pro | 60 | 5,000 | 5 |

Headers returned: `X-RateLimit-Limit`, `X-RateLimit-Remaining`, `X-RateLimit-Reset`

---

## Error Codes

| Status | Meaning |
|--------|---------|
| 400 | Invalid parameters |
| 401 | Invalid/missing API key |
| 429 | Rate limit exceeded |
| 503 | No workers available |
| 504 | Crawl timeout |

---

## Documentation Links

- Full docs: [https://api.crawl4ai.com/docs](https://api.crawl4ai.com/docs)
- Quickstart: [https://api.crawl4ai.com/docs/getting-started/quickstart.md](https://api.crawl4ai.com/docs/getting-started/quickstart.md)
- Authentication: [https://api.crawl4ai.com/docs/getting-started/authentication.md](https://api.crawl4ai.com/docs/getting-started/authentication.md)
- Sync Crawl: [https://api.crawl4ai.com/docs/crawl-api/sync-crawl.md](https://api.crawl4ai.com/docs/crawl-api/sync-crawl.md)
- Batch Crawl: [https://api.crawl4ai.com/docs/crawl-api/batch-crawl.md](https://api.crawl4ai.com/docs/crawl-api/batch-crawl.md)
- Async Crawl: [https://api.crawl4ai.com/docs/crawl-api/async-crawl.md](https://api.crawl4ai.com/docs/crawl-api/async-crawl.md)
- Deep Crawl: [https://api.crawl4ai.com/docs/deep-crawl/overview.md](https://api.crawl4ai.com/docs/deep-crawl/overview.md)
- CSS Extraction: [https://api.crawl4ai.com/docs/extraction/css-extraction.md](https://api.crawl4ai.com/docs/extraction/css-extraction.md)
- LLM Extraction: [https://api.crawl4ai.com/docs/extraction/llm-extraction.md](https://api.crawl4ai.com/docs/extraction/llm-extraction.md)
- Proxy: [https://api.crawl4ai.com/docs/proxy/configuration.md](https://api.crawl4ai.com/docs/proxy/configuration.md)
- Sessions: [https://api.crawl4ai.com/docs/sessions/browser-sessions.md](https://api.crawl4ai.com/docs/sessions/browser-sessions.md)
- Python SDK: [https://api.crawl4ai.com/docs/sdk/python.md](https://api.crawl4ai.com/docs/sdk/python.md)
- JavaScript SDK: [https://api.crawl4ai.com/docs/sdk/javascript.md](https://api.crawl4ai.com/docs/sdk/javascript.md)
- All Endpoints: [https://api.crawl4ai.com/docs/reference/endpoints.md](https://api.crawl4ai.com/docs/reference/endpoints.md)
- Models: [https://api.crawl4ai.com/docs/reference/models.md](https://api.crawl4ai.com/docs/reference/models.md)