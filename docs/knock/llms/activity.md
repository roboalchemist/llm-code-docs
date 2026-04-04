# Source: https://docs.knock.app/api-reference/messages/schemas/activity.md

### Activity

An activity associated with a workflow trigger request. Messages produced after a [batch step](/designing-workflows/batch-function) can be associated with one or more activities. Non-batched messages will always be associated with a single activity.

#### Attributes

- **__typename** (string) - The typename of the schema.
- **actor** (object) - The actor who performed the activity.
- **data** (object) - The workflow trigger `data` payload associated with the activity.
- **id** (string) - Unique identifier for the activity.
- **inserted_at** (string) - Timestamp when the activity was created.
- **recipient** (object) - A recipient of a notification, which is either a user or an object.
- **updated_at** (string) - Timestamp when the activity was last updated.

#### Example

```json
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
```

