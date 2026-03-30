# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_update_object_step.md

### WorkflowUpdateObjectStep

An update object step. Updates properties of a specific object referenced in the workflow.

#### Attributes

- **conditions** (object) - A conditions object that describes one or more conditions to be met in order for the step to be executed.
- **description** (string) - An arbitrary string attached to a workflow step. Useful for adding notes about the workflow for internal purposes.
- **name** (string) - A name for the workflow step.
- **ref** (string) *required* - The reference key of the workflow step. Must be unique per workflow.
- **settings** (object) *required* - The settings for the update object step.
- **type** (string) *required* - The type of the workflow step.

#### Example

```json
{
  "description": "Update object step description.",
  "name": "Update object",
  "ref": "update_object_1",
  "settings": {
    "recipient_gid": "gid://Object/projects/123",
    "update_properties": "{\"status\": \"active\"}"
  },
  "type": "update_object"
}
```

