# Source: https://docs.knock.app/api-reference/objects/list_subscriptions.md

# Source: https://docs.knock.app/api-reference/users/list_subscriptions.md

### List user subscriptions

Retrieves a paginated list of subscriptions for a specific user, in descending order.

#### Endpoint

`GET /v1/users/{user_id}/subscriptions`

**Rate limit tier:** 4

#### Path parameters

- **user_id** (string) *required* - The user ID to list subscriptions for.

#### Query parameters

- **include[]** (array) - Associated resources to include in the response.
- **objects[]** (array) - Only returns subscriptions for the specified object references.
- **after** (string) - The cursor to fetch entries after.
- **before** (string) - The cursor to fetch entries before.
- **page_size** (integer) - The number of items per page (defaults to 50).

#### Responses

##### 200

OK

###### Example

```json
{
  "entries": [
    {
      "__typename": "Subscription",
      "inserted_at": "2021-01-01T00:00:00Z",
      "object": {
        "__typename": "Object",
        "collection": "assets",
        "created_at": null,
        "id": "specimen_25",
        "properties": {
          "classification": "Theropod",
          "config": {
            "biz": "baz",
            "foo": "bar"
          },
          "name": "Velociraptor",
          "status": "contained"
        },
        "updated_at": "2024-05-22T12:00:00Z"
      },
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
      "updated_at": "2021-01-01T00:00:00Z"
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

