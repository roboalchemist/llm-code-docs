# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/get-pipeline-workflow-applications-response.md

# getPipelineWorkflowApplicationsResponse

Response containing pipeline workflows with matching application counts.

### Examples

```graphql
type GetPipelineWorkflowApplicationsResponse {
  workflows: [PipelineWorkflowApplication!]
}
```

### Fields

| Field                                                                                                                                                                   | Description                            | Supported fields                                                                                                                                                          |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| workflows [`[PipelineWorkflowApplication!]`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/pipeline-workflow-application) | List of pipeline workflow applications | <p>isDefault <code>Boolean!</code><br>workflowName <code>String!</code><br>workflowId <code>String!</code><br>count <code>Int</code><br>enabled <code>Boolean!</code></p> |

### References

#### Queries using this object

* [\<?> getPipelineWorkflowApplications](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/queries/get-pipeline-workflow-applications)
