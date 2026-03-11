# Source: https://docs.knock.app/api-reference/messages/list_events.md

### List events

Returns a paginated list of events for the specified message.

#### Endpoint

`GET /v1/messages/{message_id}/events`

**Rate limit tier:** 3

#### Path parameters

- **message_id** (string) *required* - The ID of the message to fetch events for.

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
      "__typename": "MessageEvent",
      "data": null,
      "id": "2FVHPWxRqNuXQ9krvNP5A6Z4qXe",
      "inserted_at": "2021-01-01T00:00:00Z",
      "recipient": "user_123",
      "type": "message.sent"
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

