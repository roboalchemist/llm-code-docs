# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_trigger_workflow_step.md

### WorkflowTriggerWorkflowStep

A workflow trigger function step. Read more in the [docs](https://docs.knock.app/designing-workflows/trigger-workflow-function).

#### Attributes

- **conditions** (object) - A set of conditions to be evaluated for this trigger workflow step.
- **description** (string) - A description for the workflow step.
- **name** (string) - A name for the workflow step.
- **ref** (string) *required* - The reference key of the workflow step. Must be unique per workflow.
- **settings** (object) *required* - The settings for the workflow trigger workflow step.
- **type** (string) *required* - The type of the workflow step.

#### Example

```json
{
  "name": "Trigger workflow step",
  "ref": "trigger_workflow_step",
  "settings": {
    "actor": "{{ actor.id }}",
    "cancellation_key": "{{ workflow.cancellation_key }}",
    "data": "{{ data | json }}",
    "recipients": "{{ recipient.id }}",
    "tenant": "{{ tenant.id }}",
    "workflow_key": "dinosaurs-loose"
  },
  "type": "trigger_workflow"
}
```

