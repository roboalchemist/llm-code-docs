# Source: https://docs.linkup.so/pages/changelog/fetch-endpoint.md

> ## Documentation Index
> Fetch the complete documentation index at: https://docs.linkup.so/llms.txt
> Use this file to discover all available pages before exploring further.

# Fetch Endpoint

> _Released: September 12, 2025_

We're excited to introduce the new **`/fetch`** endpoint, which allows you to retrieve the raw HTML or markdown content of any webpage with optional JavaScript rendering capabilities.

### How to Use

The `/fetch` endpoint accepts a URL and returns the webpage content in your preferred format. You can choose whether to render JavaScript or retrieve the static HTML.

**Example Request**

```shell curl theme={null}
curl --request POST \
  --url https://api.linkup.so/v1/fetch \
  --header 'Authorization: Bearer <token>' \
  --header 'Content-Type: application/json' \
  --data '{
  "url": "https://example.com/page",
  "outputFormat": "html",
  "renderJS": false
}'
```

**Example Response**

```json json theme={null}
{
  "url": "https://example.com/page",
  "content": "<html><head><title>Example Page</title></head><body><h1>Example Domain</h1><p>This domain is for use in illustrative examples in documents...</p></body></html>",
  "outputFormat": "html",
  "timestamp": "2025-09-12T10:30:00Z"
}
```

### Key Features

* **Flexible Content Retrieval**: Get webpage content as raw HTML or clean markdown
* **JavaScript Rendering**: Optional JavaScript execution for dynamic content
* **Direct URL Access**: Fetch content from any publicly accessible webpage
* **Clean Output**: Structured response with metadata and content

This endpoint is perfect for content extraction, web scraping, and building applications that need to process webpage data programmatically.


Built with [Mintlify](https://mintlify.com).