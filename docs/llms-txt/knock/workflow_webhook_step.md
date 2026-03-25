# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_webhook_step.md

### WorkflowWebhookStep

A webhook step within a workflow to send an HTTP request to a generic channel. Read more in the [docs](https://docs.knock.app/designing-workflows/channel-step).

#### Attributes

- **channel_group_key** (string) - The key of the channel group to which the channel step will be sending a notification. Either `channel_key` or `channel_group_key` must be provided, but not both.
- **channel_key** (string) - The key of a specific configured channel instance (e.g., 'knock-email', 'postmark', 'sendgrid-marketing') to send the notification through. Either `channel_key` or `channel_group_key` must be provided, but not both.
- **channel_type** (string) - The type of the channel step. Always `http` for webhook steps.
- **conditions** (object) - A set of conditions to be evaluated for this channel step.
- **description** (string) - An arbitrary string attached to a workflow step. Useful for adding notes about the workflow for internal purposes.
- **name** (string) - A name for the workflow step.
- **ref** (string) *required* - The reference key of the workflow step. Must be unique per workflow.
- **send_windows** (array) - A list of send window objects. Must include one send window object per day of the week.
- **template** (object) *required* - A webhook template. By default, a webhook step will use the request settings you configured in your webhook channel. You can override this as you see fit on a per-step basis.
- **type** (string) *required* - The type of the workflow step.

#### Example

```json
{
  "channel_group_key": null,
  "channel_key": "pagerduty",
  "channel_type": "http",
  "conditions": null,
  "description": "This is a description of the channel step",
  "name": "Webhook channel step",
  "ref": "channel_step",
  "send_windows": null,
  "template": {
    "body": null,
    "headers": [
      {
        "key": "X-API-Key",
        "value": "1234567890"
      }
    ],
    "method": "get",
    "query_params": [
      {
        "key": "key",
        "value": "value"
      }
    ],
    "url": "https://example.com"
  },
  "type": "channel"
}
```

