# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_update_user_step.md

### WorkflowUpdateUserStep

An update user step. Updates properties of a specific user referenced in the workflow.

#### Attributes

- **conditions** (object) - A conditions object that describes one or more conditions to be met in order for the step to be executed.
- **description** (string) - An arbitrary string attached to a workflow step. Useful for adding notes about the workflow for internal purposes.
- **name** (string) - A name for the workflow step.
- **ref** (string) *required* - The reference key of the workflow step. Must be unique per workflow.
- **settings** (object) *required* - The settings for the update user step.
- **type** (string) *required* - The type of the workflow step.

#### Example

```json
{
  "description": "Update user step description.",
  "name": "Update user",
  "ref": "update_user_1",
  "settings": {
    "recipient_gid": "gid://Object/$users/user-123",
    "recipient_mode": "reference",
    "update_properties": "{\"name\": \"Updated User\"}"
  },
  "type": "update_user"
}
```

