# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/wf-app.md

# wfApp

Application configured for pipeline workflow monitoring.

### Examples

```graphql
type WfApp {
  appName: String
  appType: String
  appId: String
  selected: Boolean
  disabled: Boolean
}
```

### Fields

| Field              | Description                              | Supported fields |
| ------------------ | ---------------------------------------- | ---------------- |
| appName `String`   | Display name of the application          |                  |
| appType `String`   | Type of the application                  |                  |
| appId `String`     | Unique identifier of the application     |                  |
| selected `Boolean` | Indicates if the application is selected |                  |
| disabled `Boolean` | Indicates if the application is disabled |                  |

### References

#### Fields with this object

* [{} GetPipelineApplicationsResponse.applications](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/get-pipeline-applications-response)
* [{} WfPipelineSettings.apps](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/objects/wf-pipeline-settings)
