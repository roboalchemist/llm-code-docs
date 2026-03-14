# Source: https://docs.nimbleway.io/nimble-sdk/search-api/extract-api-quick-start.md

# Extract API Quick Start

Extract and parse content from specific URLs with advanced rendering and parsing capabilities.

### **Sample Request**

```bash
curl -X POST https://nimble-retriever.webit.live/extract \
  -H "Authorization: Bearer YOUR_API_KEY" \
  -H "Content-Type: application/json" \
  -d '{
    "links": [
      "https://example.com/article-1",
      "https://example.com/article-2"
    ],
    "output_format": "markdown",
    "driver": "vx10-pro",
    "wait": 2000
  }'
```

### **Sample Response**

```json
{
  "message": "Request processed successfully",
  "body": [
    {
      "page_content": "# Article Title\n\nClean, parsed content in markdown format...",
      "metadata": {
        "url": "https://example.com/article-1",
        "entity_type": "HtmlContent",
        "country": null,
        "locale": null
      }
    },
    {
      "page_content": "# Another Article\n\nMore parsed content...",
      "metadata": {
        "url": "https://example.com/article-2",
        "entity_type": "HtmlContent",
        "country": null,
        "locale": null
      }
    }
  ]
}
```

***

### **Request Body Parameters**

| Parameter       | Type           | Required | Default    | Description                                                         |
| --------------- | -------------- | -------- | ---------- | ------------------------------------------------------------------- |
| `links`         | array\[string] | Yes      | -          | List of URLs to extract content from (max: 20)                      |
| `output_format` | enum           | No       | `markdown` | Output format. Options: `plain_text`, `markdown`, `simplified_html` |
| `locale`        | string         | No       | -          | Locale for content extraction                                       |
| `country`       | string         | No       | -          | Country code for content extraction                                 |
| `driver`        | enum           | No       | -          | Browser driver version to use                                       |
| `wait`          | integer        | No       | null       | Wait time in milliseconds before extracting content                 |
