# Source: https://docs.knock.app/api-reference/objects/bulk/add_subscriptions.md

# Source: https://docs.knock.app/api-reference/objects/add_subscriptions.md

### Add subscriptions

Add subscriptions for an object. If a subscription already exists, it will be updated. This endpoint also handles [inline identifications](/managing-recipients/identifying-recipients#inline-identifying-recipients) for the `recipient`.

#### Endpoint

`POST /v1/objects/{collection}/{object_id}/subscriptions`

**Rate limit tier:** 3

#### Path parameters

- **object_id** (string) *required* - Unique identifier for the object.
- **collection** (string) *required* - The collection this object belongs to.

#### Request body

A request to upsert subscriptions for a set of recipients.

##### Example

```json
{
  "properties": {
    "key": "value"
  },
  "recipients": [
    "user_1",
    "user_2"
  ]
}
```

#### Responses

##### 200

OK

###### Example

```json
[
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
]
```

