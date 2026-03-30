# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/single-app.md

# singleApp

Basic application information associated with pipeline executions.

### Examples

```graphql
type SingleApp {
  appId: String
  appName: String
  appType: String
}
```

### Fields

| Field            | Description                               | Supported fields |
| ---------------- | ----------------------------------------- | ---------------- |
| appId `String`   | Application identifier                    |                  |
| appName `String` | Application name                          |                  |
| appType `String` | Application type (web, mobile, API, etc.) |                  |

### References

#### Fields with this object

* [{} PipelineSummary.apps](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/pipeline-summary)
