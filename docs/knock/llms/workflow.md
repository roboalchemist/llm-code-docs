# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow.md

### Workflow

A workflow object. Read more in the [docs](https://docs.knock.app/concepts/workflows).

#### Attributes

- **active** (boolean) *required* - Whether the workflow is [active](https://docs.knock.app/concepts/workflows#workflow-status) in the current environment. (read-only).
- **categories** (array) - A list of [categories](https://docs.knock.app/concepts/workflows#workflow-categories) that the workflow belongs to.
- **conditions** (object) - A conditions object that describes one or more conditions to be met for the workflow to be executed. (optional).
- **created_at** (string) *required* - The timestamp of when the workflow was created. (read-only).
- **deleted_at** (string) - The timestamp of when the workflow was deleted. (read-only).
- **description** (string) - An arbitrary string attached to a workflow object. Useful for adding notes about the workflow for internal purposes. Maximum of 280 characters allowed.
- **environment** (string) *required* - The slug of the environment in which the workflow exists. (read-only).
- **key** (string) *required* - The unique key string for the workflow object. Must be at minimum 3 characters and at maximum 255 characters in length. Must be in the format of ^[a-z0-9_-]+$.
- **name** (string) *required* - A name for the workflow. Must be at maximum 255 characters in length.
- **settings** (object) - A map of workflow settings.
- **sha** (string) *required* - The SHA hash of the workflow data. (read-only).
- **steps** (array) *required* - A list of workflow step objects in the workflow.
- **trigger_data_json_schema** (object) - A JSON schema for the expected structure of the workflow trigger's `data` payload (available in templates as `{{ data.field_name }}`). Used to validate trigger requests. Read more in the [docs](https://docs.knock.app/developer-tools/validating-trigger-data).
- **trigger_frequency** (string) - The frequency at which the workflow should be triggered. One of: `once_per_recipient`, `once_per_recipient_per_tenant`, `every_trigger`. Defaults to `every_trigger`. Read more in [docs](https://docs.knock.app/send-notifications/triggering-workflows/overview#controlling-workflow-trigger-frequency).
- **updated_at** (string) *required* - The timestamp of when the workflow was last updated. (read-only).
- **valid** (boolean) *required* - Whether the workflow and its steps are in a valid state. (read-only).

#### Example

```json
{
  "active": false,
  "categories": [
    "marketing",
    "black-friday"
  ],
  "conditions": {
    "all": [
      {
        "argument": "admin",
        "operator": "equal_to",
        "variable": "recipient.role"
      }
    ]
  },
  "created_at": "2022-12-16T19:07:50.027113Z",
  "description": "This is a dummy workflow for demo purposes.",
  "environment": "development",
  "key": "december-16-demo",
  "name": "december-16-demo",
  "settings": {
    "override_preferences": true
  },
  "sha": "f7e9d3b2a1c8e6m4k5j7h9g0i2l3n4p6q8r0t1u3v5w7x9y",
  "steps": [
    {
      "channel_key": "in-app-feed",
      "channel_type": "in_app_feed",
      "description": "Main in-app feed",
      "name": "In-app step",
      "ref": "in_app_feed_1",
      "template": {
        "action_url": "{{ data.onboarding_url }}",
        "markdown_body": "Hello **{{ recipient.name }}**. Click here to get started."
      },
      "type": "channel"
    },
    {
      "ref": "delay_1",
      "settings": {
        "delay_for": {
          "unit": "hours",
          "value": 1
        }
      },
      "type": "delay"
    },
    {
      "channel_key": "postmark",
      "channel_type": "email",
      "ref": "email_1",
      "template": {
        "html_body": "<p>Hello, {{ recipient.name }}! Welcome to {{ vars.app_name }} <a href='{{ data.onboarding_url }}'>Get started here</a>.</p>",
        "settings": {
          "layout_key": "default"
        },
        "subject": "Welcome to {{ vars.app_name }}!"
      },
      "type": "channel"
    }
  ],
  "trigger_data_json_schema": {
    "properties": {
      "onboarding_url": {
        "type": "string"
      }
    },
    "required": [
      "onboarding_url"
    ],
    "type": "object"
  },
  "trigger_frequency": "every_trigger",
  "updated_at": "2023-02-08T22:15:19.846681Z",
  "valid": true
}
```

