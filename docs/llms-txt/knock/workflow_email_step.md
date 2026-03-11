# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_email_step.md

### WorkflowEmailStep

An email step within a workflow. Read more in the [docs](https://docs.knock.app/designing-workflows/channel-step).

#### Attributes

- **channel_group_key** (string) - The key of the channel group to which the channel step will be sending a notification. Either `channel_key` or `channel_group_key` must be provided, but not both.
- **channel_key** (string) - The key of a specific configured channel instance (e.g., 'knock-email', 'postmark', 'sendgrid-marketing') to send the notification through. Either `channel_key` or `channel_group_key` must be provided, but not both.
- **channel_overrides** (object) - A map of channel overrides for the channel step.
- **channel_type** (string) - The category of channel for this step. Always `email` for email steps. This identifies the type of notification (email, sms, push, etc.) while `channel_key` specifies which configured provider instance to use.
- **conditions** (object) - A set of conditions to be evaluated for this channel step.
- **description** (string) - An arbitrary string attached to a workflow step. Useful for adding notes about the workflow for internal purposes.
- **name** (string) - A name for the workflow step.
- **ref** (string) *required* - The reference key of the workflow step. Must be unique per workflow.
- **send_windows** (array) - A list of send window objects. Must include one send window object per day of the week.
- **template** (object) *required* - An email message template.
- **type** (string) *required* - The type of the workflow step.

#### Example

```json
{
  "channel_group_key": null,
  "channel_key": "postmark",
  "channel_overrides": null,
  "channel_type": "email",
  "conditions": null,
  "description": "This is a description of the channel step",
  "name": "Email channel step",
  "ref": "channel_step",
  "send_windows": null,
  "template": {
    "html_body": "<p>Hello, {{ recipient.name }}! Welcome to {{ vars.app_name }} <a href='{{ data.sign_in_url }}'>Get started here</a>.</p>",
    "settings": {
      "layout_key": "default"
    },
    "subject": "Welcome to {{ vars.app_name }}",
    "text_body": "Hello, {{ recipient.name }}! Welcome to {{ vars.app_name }} Get started here: {{ data.sign_in_url }}."
  },
  "type": "channel"
}
```

