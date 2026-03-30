# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-application.md

# artifactApplication

Application context description for an artifact.

### Examples

```graphql
type ArtifactApplication {
  appName: String
  appType: String
  appId: String
  businessPriority: Float
}
```

### Fields

| Field                    | Description                                                          | Supported fields |
| ------------------------ | -------------------------------------------------------------------- | ---------------- |
| appName `String`         | Name of the application                                              |                  |
| appType `String`         | Type of the application                                              |                  |
| appId `String`           | Unique identifier of the application                                 |                  |
| businessPriority `Float` | Business priority value indicating the importance of the application |                  |

### References

#### Fields with this object

* [{} ArtifactInfo.appDescription](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-info)
