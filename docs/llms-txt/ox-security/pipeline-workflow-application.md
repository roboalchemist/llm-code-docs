# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/pipeline-workflow-application.md

# pipelineWorkflowApplication

Pipeline workflow with the count of matching applications.

### Examples

```graphql
type PipelineWorkflowApplication {
  isDefault: Boolean!
  workflowName: String!
  workflowId: String!
  count: Int
  enabled: Boolean!
}
```

### Fields

| Field                  | Description                                     | Supported fields |
| ---------------------- | ----------------------------------------------- | ---------------- |
| isDefault `Boolean!`   | Indicates if the workflow is a default workflow |                  |
| workflowName `String!` | Name of the workflow                            |                  |
| workflowId `String!`   | Unique identifier of the workflow               |                  |
| count `Int`            | Number of applications in the workflow          |                  |
| enabled `Boolean!`     | Indicates if the workflow is enabled            |                  |

### References

#### Fields with this object

* [{} GetPipelineWorkflowApplicationsResponse.workflows](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/get-pipeline-workflow-applications-response)
