# Source: https://docs.knock.app/api-reference/messages/batch/mark_as_interacted.md

# Source: https://docs.knock.app/api-reference/messages/mark_as_interacted.md

### Mark message as interacted

Marks a message as `interacted` with by the user. This can include any user action on the message, with optional metadata about the specific interaction. Cannot include more than 5 key-value pairs, must not contain nested data. Read more about message engagement statuses [here](/send-notifications/message-statuses#engagement-status).

#### Endpoint

`PUT /v1/messages/{message_id}/interacted`

**Rate limit tier:** 2

#### Path parameters

- **message_id** (string) *required* - The unique identifier for the message.

#### Request body

A request to mark a message as interacted with.

##### Example

```json
{
  "metadata": {
    "key": "value"
  }
}
```

#### Responses

##### 200

OK

###### Example

```json
{
  "__typename": "Message",
  "actors": [
    "user_123"
  ],
  "archived_at": null,
  "channel_id": "123e4567-e89b-12d3-a456-426614174000",
  "clicked_at": null,
  "data": {
    "foo": "bar"
  },
  "engagement_statuses": [
    "seen",
    "interacted"
  ],
  "id": "1jNaXzB2RZX3LY8wVQnfCKyPnv7",
  "inserted_at": "2021-01-01T00:00:00Z",
  "interacted_at": "2025-01-01T00:03:00Z",
  "link_clicked_at": null,
  "metadata": {
    "external_id": "123e4567-e89b-12d3-a456-426614174000"
  },
  "read_at": null,
  "recipient": "user_123",
  "scheduled_at": null,
  "seen_at": "2025-01-01T00:01:00Z",
  "source": {
    "__typename": "NotificationSource",
    "categories": [
      "collaboration"
    ],
    "key": "comment-created",
    "step_ref": "email_step_1",
    "version_id": "123e4567-e89b-12d3-a456-426614174000"
  },
  "status": "sent",
  "tenant": "tenant_123",
  "updated_at": "2021-01-01T00:00:00Z",
  "workflow": "comment-created"
}
```

