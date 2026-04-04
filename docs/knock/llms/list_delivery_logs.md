# Source: https://docs.knock.app/api-reference/messages/list_delivery_logs.md

### List delivery logs

Returns a paginated list of delivery logs for the specified message.

#### Endpoint

`GET /v1/messages/{message_id}/delivery_logs`

**Rate limit tier:** 3

#### Path parameters

- **message_id** (string) *required* - The ID of the message to fetch delivery logs for.

#### Query parameters

- **after** (string) - The cursor to fetch entries after.
- **before** (string) - The cursor to fetch entries before.
- **page_size** (integer) - The number of items per page (defaults to 50).

#### Responses

##### 200

OK

###### Example

```json
{
  "items": [
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
  ],
  "page_info": {
    "__typename": "PageInfo",
    "after": null,
    "before": null,
    "page_size": 25
  }
}
```

