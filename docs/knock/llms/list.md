# Source: https://docs.knock.app/mapi-reference/members/list.md

# Source: https://docs.knock.app/mapi-reference/branches/list.md

# Source: https://docs.knock.app/mapi-reference/variables/list.md

# Source: https://docs.knock.app/mapi-reference/translations/list.md

# Source: https://docs.knock.app/mapi-reference/commits/list.md

# Source: https://docs.knock.app/mapi-reference/message_types/list.md

# Source: https://docs.knock.app/mapi-reference/guides/list.md

# Source: https://docs.knock.app/mapi-reference/partials/list.md

# Source: https://docs.knock.app/mapi-reference/email_layouts/list.md

# Source: https://docs.knock.app/mapi-reference/broadcasts/list.md

# Source: https://docs.knock.app/mapi-reference/workflows/list.md

# Source: https://docs.knock.app/mapi-reference/channel_groups/list.md

# Source: https://docs.knock.app/mapi-reference/channels/list.md

# Source: https://docs.knock.app/mapi-reference/environments/list.md

# Source: https://docs.knock.app/cli/message-type/list.md

# Source: https://docs.knock.app/cli/guide/list.md

# Source: https://docs.knock.app/cli/commit/list.md

# Source: https://docs.knock.app/cli/partial/list.md

# Source: https://docs.knock.app/cli/translation/list.md

# Source: https://docs.knock.app/cli/email-layout/list.md

# Source: https://docs.knock.app/cli/workflow/list.md

# Source: https://docs.knock.app/cli/branch/list.md

# Source: https://docs.knock.app/cli/channel/list.md

# Source: https://docs.knock.app/cli/environment/list.md

# Source: https://docs.knock.app/api-reference/schedules/list.md

# Source: https://docs.knock.app/api-reference/tenants/list.md

# Source: https://docs.knock.app/api-reference/objects/list.md

# Source: https://docs.knock.app/api-reference/users/list.md

# Source: https://docs.knock.app/api-reference/messages/list.md

### List messages

Returns a paginated list of messages for the current environment.

#### Endpoint

`GET /v1/messages`

**Rate limit tier:** 4

#### Query parameters

- **after** (string) - The cursor to fetch entries after.
- **before** (string) - The cursor to fetch entries before.
- **page_size** (integer) - The number of items per page (defaults to 50).
- **tenant** (string) - Limits the results to items with the corresponding tenant.
- **channel_id** (string) - Limits the results to items with the corresponding channel ID.
- **status[]** (array) - Limits the results to messages with the given delivery status.
- **engagement_status[]** (array) - Limits the results to messages with the given engagement status.
- **message_ids[]** (array) - Limits the results to only the message IDs given (max 50). Note: when using this option, the results will be subject to any other filters applied to the query.
- **workflow_categories[]** (array) - Limits the results to messages related to any of the provided categories.
- **source** (string) - Limits the results to messages triggered by the given workflow key.
- **workflow_run_id** (string) - Limits the results to messages associated with the top-level workflow run ID returned by the workflow trigger request.
- **workflow_recipient_run_id** (string) - Limits the results to messages for a specific recipient's workflow run.
- **trigger_data** (string) - Limits the results to only messages that were generated with the given data. See [trigger data filtering](/api-reference/overview/trigger-data-filtering) for more information.
- **inserted_at.gt** (string) - Limits the results to items inserted after the given date.
- **inserted_at.gte** (string) - Limits the results to items inserted after or on the given date.
- **inserted_at.lt** (string) - Limits the results to items inserted before the given date.
- **inserted_at.lte** (string) - Limits the results to items inserted before or on the given date.

#### Responses

##### 200

OK

###### Example

```json
{
  "items": [
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
  ],
  "page_info": {
    "__typename": "PageInfo",
    "after": null,
    "before": null,
    "page_size": 25
  }
}
```

