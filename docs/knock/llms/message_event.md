# Source: https://docs.knock.app/api-reference/messages/schemas/message_event.md

### MessageEvent

A message event. Occurs when a message [delivery or engagement status](/send-notifications/message-statuses) changes.

#### Attributes

- **__typename** (string) *required* - The typename of the schema.
- **data** (object) - The data associated with the message event. Only present for some event types.
- **id** (string) *required* - The unique identifier for the message event.
- **inserted_at** (string) *required* - Timestamp when the event was created.
- **recipient** (unknown) *required* - A reference to a recipient, either a user identifier (string) or an object reference (ID, collection).
- **type** (string) *required* - The type of event that occurred.

#### Example

```json
{
  "__typename": "MessageEvent",
  "data": null,
  "id": "2FVHPWxRqNuXQ9krvNP5A6Z4qXe",
  "inserted_at": "2021-01-01T00:00:00Z",
  "recipient": "user_123",
  "type": "message.sent"
}
```

