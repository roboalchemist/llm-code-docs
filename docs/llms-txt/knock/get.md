# Source: https://docs.knock.app/cli/message-type/get.md

# Source: https://docs.knock.app/cli/guide/get.md

# Source: https://docs.knock.app/cli/commit/get.md

# Source: https://docs.knock.app/cli/partial/get.md

# Source: https://docs.knock.app/cli/translation/get.md

# Source: https://docs.knock.app/cli/email-layout/get.md

# Source: https://docs.knock.app/cli/workflow/get.md

# Source: https://docs.knock.app/api-reference/bulk_operations/get.md

# Source: https://docs.knock.app/api-reference/tenants/get.md

# Source: https://docs.knock.app/api-reference/objects/get.md

# Source: https://docs.knock.app/api-reference/users/get.md

# Source: https://docs.knock.app/api-reference/messages/get.md

### Get message

Retrieves a specific message by its ID.

#### Endpoint

`GET /v1/messages/{message_id}`

**Rate limit tier:** 4

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
    "mr_arnold",
    "mr_muldoon"
  ],
  "archived_at": null,
  "channel_id": "123e4567-e89b-12d3-a456-426614174000",
  "clicked_at": null,
  "data": {
    "affected_areas": [
      "visitor_center",
      "raptor_pen",
      "trex_paddock"
    ],
    "attraction_id": "paddock_rex_01",
    "evacuation_protocol": "active",
    "message": "Life finds a way",
    "severity": "critical",
    "system_status": "fences_failing"
  },
  "engagement_statuses": [
    "read",
    "seen"
  ],
  "id": "2w3YUpTTOxuDvZFji8OMsKrG176",
  "inserted_at": "1993-06-11T21:15:00Z",
  "interacted_at": null,
  "link_clicked_at": null,
  "metadata": {
    "external_id": "123e4567-e89b-12d3-a456-426614174000"
  },
  "read_at": "1993-06-11T21:30:00Z",
  "recipient": "dr_grant",
  "scheduled_at": null,
  "seen_at": "1993-06-11T21:29:45Z",
  "source": {
    "__typename": "NotificationSource",
    "categories": [
      "security",
      "emergency"
    ],
    "key": "security-breach-alert",
    "step_ref": "alert_step_1",
    "version_id": "123e4567-e89b-12d3-a456-426614174000",
    "workflow_recipient_run_id": "def01234-a56b-78c9-d012-345678901bcd",
    "workflow_run_id": "789e0123-f45a-67b8-c901-234567890abc"
  },
  "status": "sent",
  "tenant": "ingen_isla_nublar",
  "updated_at": "1993-06-11T21:30:05Z",
  "workflow": "security-breach-alert"
}
```

