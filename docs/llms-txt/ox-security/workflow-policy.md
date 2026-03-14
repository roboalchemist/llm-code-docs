# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/workflow-policy.md

# workflowPolicy

### Examples

```graphql
type WorkflowPolicy {
  id: String!
  isValid: Boolean
  createdAt: Float!
  createdBy: String
  enabled: Boolean
  updatedAt: Float!
  updatedBy: String
  name: String!
  description: String
  actions: [Action!]!
  triggers: [Trigger!]!
  runs: Int
  lastRunTime: Float
  workflowType: WorkflowType!
  isDefault: Boolean!
  monitorAllNewlyCreatedRepositories: Float
  wfPipelineSettings: WfPipelineSettings
}
```

### Fields

| Field                                                                                                                                                       | Description                                                                                  | Supported fields                                                                                                      |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------- |
| id `String!`                                                                                                                                                | ID of the policy workflow                                                                    |                                                                                                                       |
| isValid `Boolean`                                                                                                                                           | defines if workflow is valid or not                                                          |                                                                                                                       |
| createdAt `Float!`                                                                                                                                          | Time the workflow was created                                                                |                                                                                                                       |
| createdBy `String`                                                                                                                                          | Workflow creator                                                                             |                                                                                                                       |
| enabled `Boolean`                                                                                                                                           | Enabled for evaluation                                                                       |                                                                                                                       |
| updatedAt `Float!`                                                                                                                                          | Time the workflow was updated                                                                |                                                                                                                       |
| updatedBy `String`                                                                                                                                          | Workflow last updated by                                                                     |                                                                                                                       |
| name `String!`                                                                                                                                              | Name of the workflow                                                                         |                                                                                                                       |
| description `String`                                                                                                                                        | Description of the workflow                                                                  |                                                                                                                       |
| actions [`[Action!]!`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/action)                                  |                                                                                              | <p>name <code>String</code><br>type <code>String</code></p>                                                           |
| triggers [`[Trigger!]!`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/trigger)                               |                                                                                              | <p>name <code>String</code><br>category <code>String</code></p>                                                       |
| runs `Int`                                                                                                                                                  | numbers of runs this workflow had                                                            |                                                                                                                       |
| lastRunTime `Float`                                                                                                                                         | last time this workflow had run                                                              |                                                                                                                       |
| workflowType [`WorkflowType!`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/enums/workflow-type)                     | type of the workflow (Regular scan / Pipeline scan)                                          |                                                                                                                       |
| isDefault `Boolean!`                                                                                                                                        | If the workflow is a default one                                                             |                                                                                                                       |
| monitorAllNewlyCreatedRepositories `Float`                                                                                                                  | If this workflow should trigger for all newly created repos starting from the time it is set |                                                                                                                       |
| wfPipelineSettings [`WfPipelineSettings`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/wf-pipeline-settings) | settings for pipeline                                                                        | apps [`[WfApp!]`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/wf-app) |

### References

#### Mutations using this object

* [<\~> updateWorkflow](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/mutations/update-workflow)
