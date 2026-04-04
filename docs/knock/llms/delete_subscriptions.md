# Source: https://docs.knock.app/api-reference/objects/bulk/delete_subscriptions.md

# Source: https://docs.knock.app/api-reference/objects/delete_subscriptions.md

### Delete subscriptions

Delete subscriptions for the specified recipients from an object. Returns the list of deleted subscriptions.

#### Endpoint

`DELETE /v1/objects/{collection}/{object_id}/subscriptions`

**Rate limit tier:** 3

#### Path parameters

- **object_id** (string) *required* - Unique identifier for the object.
- **collection** (string) *required* - The collection this object belongs to.

#### Request body

A request to delete subscriptions for a set of recipients.

##### Example

```json
{
  "recipients": [
    "user_123"
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

