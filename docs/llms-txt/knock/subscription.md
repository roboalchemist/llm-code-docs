# Source: https://docs.knock.app/api-reference/recipients/subscriptions/schemas/subscription.md

### Subscription

A subscription object.

#### Attributes

- **__typename** (string) *required* - The typename of the schema.
- **inserted_at** (string) *required* - Timestamp when the resource was created.
- **object** (object) *required* - A custom [Object](/concepts/objects) entity which belongs to a collection.
- **properties** (object) - The custom properties associated with the subscription relationship.
- **recipient** (object) *required* - A recipient of a notification, which is either a user or an object.
- **updated_at** (string) *required* - The timestamp when the resource was last updated.

#### Example

```json
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
```

