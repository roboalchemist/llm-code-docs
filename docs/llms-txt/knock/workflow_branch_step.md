# Source: https://docs.knock.app/mapi-reference/workflows/schemas/workflow_branch_step.md

### WorkflowBranchStep

A branch function step. Read more in the [docs](https://docs.knock.app/designing-workflows/branch-function).

#### Attributes

- **branches** (array) *required* - A list of workflow branches to be evaluated.
- **description** (string) - An arbitrary string attached to a workflow step. Useful for adding notes about the workflow for internal purposes.
- **name** (string) - A name for the workflow step.
- **ref** (string) *required* - The reference key of the workflow step. Must be unique per workflow.
- **type** (string) *required* - The type of step.

#### Example

```json
{
  "branches": [
    {
      "conditions": {
        "all": [
          {
            "argument": "pro",
            "operator": "equal_to",
            "variable": "recipient.plan_type"
          }
        ]
      },
      "name": "Pro plan",
      "steps": [],
      "terminates": false
    },
    {
      "conditions": null,
      "name": "Default",
      "steps": [],
      "terminates": false
    }
  ],
  "description": "Branch description",
  "name": "Branch 1",
  "ref": "branch_1",
  "type": "branch"
}
```

