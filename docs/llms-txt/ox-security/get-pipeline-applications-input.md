# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/inputs/get-pipeline-applications-input.md

# getPipelineApplicationsInput

Input for querying pipeline applications with optional workflow selection state.

### Examples

```graphql
input GetPipelineApplicationsInput {
  isDefault: Boolean
  policyWorkflowId: String
  searchValue: String
  offset: Float
  limit: Float
}
```

### Fields

| Field                     | Description                                             | Supported fields |
| ------------------------- | ------------------------------------------------------- | ---------------- |
| isDefault `Boolean`       | Filter by default workflow status                       |                  |
| policyWorkflowId `String` | Workflow ID to retrieve application selection state for |                  |
| searchValue `String`      | Search filter for application names                     |                  |
| offset `Float`            | Pagination offset                                       |                  |
| limit `Float`             | Maximum number of applications to return                |                  |

### References

#### Queries using this object

* [\<?> getPipelineApplications.input](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/queries/get-pipeline-applications)
