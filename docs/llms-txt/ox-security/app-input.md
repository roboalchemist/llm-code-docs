# Source: https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/inputs/app-input.md

# appInput

Application entry for pipeline workflow monitoring.

### Examples

```graphql
input AppInput {
  appId: String!
  appName: String!
  appType: String!
  selected: Boolean!
  disabled: Boolean!
}
```

### Fields

| Field               | Description                              | Supported fields |
| ------------------- | ---------------------------------------- | ---------------- |
| appId `String!`     | Unique identifier of the application     |                  |
| appName `String!`   | Display name of the application          |                  |
| appType `String!`   | Type of the application                  |                  |
| selected `Boolean!` | Indicates if the application is selected |                  |
| disabled `Boolean!` | Indicates if the application is disabled |                  |

### References

#### Fields with this object

* [{} PipelineSettingsInput.apps](https://docs.ox.security/api-documentation/api-reference/api--workflow-policy/types/inputs/pipeline-settings-input)
