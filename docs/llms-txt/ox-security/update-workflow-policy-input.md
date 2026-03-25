# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/inputs/update-workflow-policy-input.md

# updateWorkflowPolicyInput

Input for updating an existing workflow.

### Examples

```graphql
input UpdateWorkflowPolicyInput {
  id: String!
  name: String
  description: String
  enabled: Boolean
  pipelineSettings: PipelineSettingsInput
  isDefault: Boolean
  monitorAllNewlyCreatedRepositories: Float
  monitorRepositories: MonitorRepositories
}
```

### Fields

| Field                                                                                                                                                          | Description                                                                                  | Supported fields                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| id `String!`                                                                                                                                                   | Id of the workflow to update                                                                 |                                                                                                                            |
| name `String`                                                                                                                                                  | Name of the workflow                                                                         |                                                                                                                            |
| description `String`                                                                                                                                           | Description of the workflow                                                                  |                                                                                                                            |
| enabled `Boolean`                                                                                                                                              | Enabled for evaluation                                                                       |                                                                                                                            |
| pipelineSettings [`PipelineSettingsInput`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/inputs/pipeline-settings-input) | settings for pipeline                                                                        | apps [`[AppInput!]`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/inputs/app-input) |
| isDefault `Boolean`                                                                                                                                            | If the workflow is a default workflow                                                        |                                                                                                                            |
| monitorAllNewlyCreatedRepositories `Float`                                                                                                                     | If this workflow should trigger for all newly created repos starting from the time it is set |                                                                                                                            |
| monitorRepositories [`MonitorRepositories`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/enums/monitor-repositories)    | If all repos are should be added or removed                                                  |                                                                                                                            |

### References

#### Mutations using this object

* [<\~> updateWorkflow.input](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/mutations/update-workflow)
