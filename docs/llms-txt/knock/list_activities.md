# Source: https://docs.knock.app/api-reference/messages/list_activities.md

### List activities

Returns a paginated list of activities for the specified message.

#### Endpoint

`GET /v1/messages/{message_id}/activities`

**Rate limit tier:** 4

#### Path parameters

- **message_id** (string) *required* - The ID of the message to fetch activities for.

#### Query parameters

- **trigger_data** (string) - The trigger data to filter activities by.
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
      "__typename": "Activity",
      "actor": null,
      "data": {
        "foo": "bar"
      },
      "id": "2FVHPWxRqNuXQ9krvNP5A6Z4qXe",
      "inserted_at": "2024-01-01T00:00:00Z",
      "recipient": {
        "__typename": "User",
        "avatar": null,
        "created_at": null,
        "email": "jane@ingen.net",
        "id": "jane",
        "name": "Jane Doe",
        "phone_number": null,
        "timezone": null,
        "updated_at": "2024-05-22T12:00:00Z"
      },
      "updated_at": "2024-01-01T00:00:00Z"
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

