# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/get-pipeline-applications-response.md

# getPipelineApplicationsResponse

Response containing pipeline applications with selection state.

### Examples

```graphql
type GetPipelineApplicationsResponse {
  total: Int
  offset: Int
  totalFilteredApps: Int
  applications: [WfApp!]
}
```

### Fields

| Field                                                                                                                         | Description                           | Supported fields                                                                                                                                                 |
| ----------------------------------------------------------------------------------------------------------------------------- | ------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| total `Int`                                                                                                                   | Total number of applications          |                                                                                                                                                                  |
| offset `Int`                                                                                                                  | Pagination offset                     |                                                                                                                                                                  |
| totalFilteredApps `Int`                                                                                                       | Total number of filtered applications |                                                                                                                                                                  |
| applications [`[WfApp!]`](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/wf-app) | List of applications                  | <p>appName <code>String</code><br>appType <code>String</code><br>appId <code>String</code><br>selected <code>Boolean</code><br>disabled <code>Boolean</code></p> |

### References

#### Queries using this object

* [\<?> getPipelineApplications](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/queries/get-pipeline-applications)
