# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_batch_step.md

### WorkflowBatchStep

A batch function step. Read more in the [docs](https://docs.knock.app/designing-workflows/batch-function).

#### Attributes

- **description** (string) - An arbitrary string attached to a workflow step. Useful for adding notes about the workflow for internal purposes.
- **name** (string) - A name for the workflow step.
- **ref** (string) *required* - The reference key of the workflow step. Must be unique per workflow.
- **settings** (object) *required* - The settings for the batch step.
- **type** (string) *required* - The type of the workflow step.

#### Example

```json
{
  "description": "Batch step description",
  "name": "Batch step",
  "ref": "batch_step",
  "settings": {
    "batch_key": "data.project_id",
    "batch_window": {
      "unit": "minutes",
      "value": 10
    }
  },
  "type": "batch"
}
```

