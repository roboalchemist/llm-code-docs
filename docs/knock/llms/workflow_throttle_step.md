# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_throttle_step.md

### WorkflowThrottleStep

A throttle function step. Read more in the [docs](https://docs.knock.app/designing-workflows/throttle-function).

#### Attributes

- **conditions** (object) - A conditions object that describes one or more conditions to be met in order for the step to be executed.
- **description** (string) - An arbitrary string attached to a workflow step. Useful for adding notes about the workflow for internal purposes.
- **name** (string) - A name for the workflow step.
- **ref** (string) *required* - The reference key of the workflow step. Must be unique per workflow.
- **settings** (object) *required* - The settings for the throttle step.
- **type** (string) *required* - The type of the workflow step.

#### Example

```json
{
  "name": "Throttle step",
  "ref": "throttle_step",
  "settings": {
    "throttle_key": "data.project_id",
    "throttle_limit": 1,
    "throttle_window": {
      "unit": "minutes",
      "value": 10
    }
  },
  "type": "throttle"
}
```

