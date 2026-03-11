# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_step.md

### WorkflowStep

A step within a workflow. Each workflow step, regardless of its type, share a common set of core attributes (`type`, `ref`, `name`, `description`, `conditions`).

#### Attributes

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

