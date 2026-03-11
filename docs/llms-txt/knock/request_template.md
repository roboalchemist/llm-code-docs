# Source: https://docs.knock.app/mapi-reference/templates/schemas/request_template.md

### RequestTemplate

A request template for a fetch function step.

#### Attributes

- **body** (string) - The body of the request. Only used for POST or PUT requests.
- **headers** (object) - The headers of the request. Can be a template string or a list of key-value pairs.
- **method** (string) *required* - The HTTP method of the request.
- **query_params** (object) - The query params of the request. Can be a template string or a list of key-value pairs.
- **url** (string) *required* - The URL of the request.

#### Example

```json
{
  "body": null,
  "headers": [
    {
      "key": "X-API-Key",
      "value": "1234567890"
    }
  ],
  "method": "get",
  "query_params": [
    {
      "key": "key",
      "value": "value"
    }
  ],
  "url": "https://example.com"
}
```

