# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/inputs/get-pipeline-workflow-applications-input.md

# getPipelineWorkflowApplicationsInput

Input for checking which pipeline workflows contain the specified applications.

### Examples

```graphql
input getPipelineWorkflowApplicationsInput {
  appIds: [String!]
}
```

### Fields

| Field              | Description                                                 | Supported fields |
| ------------------ | ----------------------------------------------------------- | ---------------- |
| appIds `[String!]` | List of application IDs to check against pipeline workflows |                  |

### References

#### Queries using this object

* [\<?> getPipelineWorkflowApplications.input](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/queries/get-pipeline-workflow-applications)
