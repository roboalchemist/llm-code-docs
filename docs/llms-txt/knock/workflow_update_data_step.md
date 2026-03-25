# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_update_data_step.md

### WorkflowUpdateDataStep

An update data function step. Merges data into the workflow's `data` scope for use in subsequent steps.

#### Attributes

- **conditions** (object) - A conditions object that describes one or more conditions to be met in order for the step to be executed.
- **description** (string) - An arbitrary string attached to a workflow step. Useful for adding notes about the workflow for internal purposes.
- **name** (string) - A name for the workflow step.
- **ref** (string) *required* - The reference key of the workflow step. Must be unique per workflow.
- **settings** (object) *required* - The settings for the update data step.
- **type** (string) *required* - The type of the workflow step.

#### Example

```json
{
  "description": "Update data step description.",
  "name": "Update data",
  "ref": "update_data_1",
  "settings": {
    "data": "{\"key\": \"value\"}"
  },
  "type": "update_data"
}
```

