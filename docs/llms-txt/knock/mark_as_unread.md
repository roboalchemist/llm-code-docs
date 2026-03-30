# Source: https://docs.knock.app/api-reference/messages/batch/mark_as_unread.md

# Source: https://docs.knock.app/api-reference/messages/mark_as_unread.md

### Mark message as unread

Marks a message as `unread`. This reverses the `read` state. Read more about message engagement statuses [here](/send-notifications/message-statuses#engagement-status).

#### Endpoint

`DELETE /v1/messages/{message_id}/read`

**Rate limit tier:** 2

#### Path parameters

- **message_id** (string) *required* - The unique identifier for the message.

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
    "seen"
  ],
  "id": "1jNaXzB2RZX3LY8wVQnfCKyPnv7",
  "inserted_at": "2021-01-01T00:00:00Z",
  "interacted_at": null,
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

