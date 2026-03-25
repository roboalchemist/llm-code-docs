# Source: https://docs.knock.app/mapi-reference/templates/schemas/webhook_template.md

### WebhookTemplate

A webhook template. By default, a webhook step will use the request settings you configured in your webhook channel. You can override this as you see fit on a per-step basis.

#### Attributes

- **body** (string) - The body of the request. Only used for POST or PUT requests.
- **headers** (array) - A list of key-value pairs for the request headers. Each object should contain key and value fields with string values.
- **method** (string) *required* - The HTTP method of the webhook.
- **query_params** (array) - A list of key-value pairs for the request query params. Each object should contain key and value fields with string values.
- **url** (string) *required* - The URL of the webhook.

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

