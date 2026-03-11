# Source: https://docs.knock.app/mapi-reference/guides/archive.md

# Source: https://docs.knock.app/api-reference/messages/batch/archive.md

# Source: https://docs.knock.app/api-reference/messages/archive.md

### Archive message

Archives a message for the user. Archived messages are hidden from the default message list in the feed but can still be accessed and unarchived later.

#### Endpoint

`PUT /v1/messages/{message_id}/archived`

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
  "archived_at": "2025-01-01T00:04:00Z",
  "channel_id": "123e4567-e89b-12d3-a456-426614174000",
  "clicked_at": null,
  "data": {
    "foo": "bar"
  },
  "engagement_statuses": [
    "seen",
    "archived"
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

