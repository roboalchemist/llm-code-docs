# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_delay_step.md

### WorkflowDelayStep

A delay function step. Read more in the [docs](https://docs.knock.app/designing-workflows/delay-function).

#### Attributes

- **conditions** (object) - A set of conditions to be evaluated for this delay step.
- **description** (string) - An arbitrary string attached to a workflow step. Useful for adding notes about the workflow for internal purposes.
- **name** (string) - A name for the workflow step.
- **ref** (string) *required* - The reference key of the workflow step. Must be unique per workflow.
- **settings** (object) *required* - The settings for the delay step. Both fields can be set to compute a delay where `delay_for` is an offset from the `delay_until_field_path`.
- **type** (string) *required* - The type of the workflow step.

#### Example

```json
{
  "conditions": {},
  "description": "Delay for 10 seconds",
  "name": "Delay",
  "ref": "delay_step",
  "settings": {
    "delay_for": {
      "unit": "seconds",
      "value": 10
    }
  },
  "type": "delay"
}
```

