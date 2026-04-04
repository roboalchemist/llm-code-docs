# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_random_cohort_step.md

### WorkflowRandomCohortStep

An experiment step. Deterministically assigns recipients to percentage-based cohorts for A/B testing and experimentation.

#### Attributes

- **cohort_branches** (array) *required* - A list of cohort branches. Must have between 2 and 10 branches, and percentages must sum to 100.
- **cohort_key** (string) - The key used to deterministically assign recipients to cohorts. Defaults to the recipient ID if not provided.
- **description** (string) - An arbitrary string attached to a workflow step. Useful for adding notes about the workflow for internal purposes.
- **name** (string) - A name for the workflow step.
- **ref** (string) *required* - The reference key of the workflow step. Must be unique per workflow.
- **type** (string) *required* - The type of step.

#### Example

```json
{
  "cohort_branches": [
    {
      "name": "Control",
      "percentage": "50",
      "steps": [],
      "terminates": false
    },
    {
      "name": "Variant",
      "percentage": "50",
      "steps": [],
      "terminates": false
    }
  ],
  "description": "Experiment step description.",
  "name": "Experiment",
  "ref": "experiment_1",
  "type": "random_cohort"
}
```

