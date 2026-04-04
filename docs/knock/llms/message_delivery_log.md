# Source: https://docs.knock.app/api-reference/messages/schemas/message_delivery_log.md

### MessageDeliveryLog

A message delivery log contains a `request` from Knock to a downstream provider and the `response` that was returned.

#### Attributes

- **__typename** (string) *required* - The typename of the schema.
- **environment_id** (string) *required* - The ID of the environment in which the message delivery occurred.
- **id** (string) *required* - The unique identifier for the message delivery log.
- **inserted_at** (string) *required* - Timestamp when the message delivery log was created.
- **request** (object) *required* - A message delivery log request.
- **response** (object) *required* - A message delivery log response.
- **service_name** (string) *required* - The name of the service that processed the delivery.

#### Example

```json
{
  "__typename": "MessageDeliveryLog",
  "environment_id": "123e4567-e89b-12d3-a456-426614174000",
  "id": "2FVHPWxRqNuXQ9krvNP5A6Z4qXe",
  "inserted_at": "2021-01-01T00:00:00Z",
  "request": {
    "body": {
      "html_content": "<html></html>"
    },
    "headers": {
      "Content-Type": "application/json"
    },
    "host": "localhost",
    "method": "GET",
    "path": "/",
    "query": "?foo=bar"
  },
  "response": {
    "body": {
      "success": true
    },
    "headers": {
      "Content-Type": "application/json"
    },
    "status": 200
  },
  "service_name": "Postmark"
}
```

