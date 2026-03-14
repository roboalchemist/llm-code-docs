# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-package.md

# artifactPackage

Information about a package included in an artifact.

### Examples

```graphql
type ArtifactPackage {
  appId: String
  appName: String
  repoName: String
  link: String
  type: String
}
```

### Fields

| Field             | Description                                  | Supported fields |
| ----------------- | -------------------------------------------- | ---------------- |
| appId `String`    | Application ID associated with the package   |                  |
| appName `String`  | Application name associated with the package |                  |
| repoName `String` | Repository name where the package is stored  |                  |
| link `String`     | Link to the package or repository            |                  |
| type `String`     | Type of the package                          |                  |

### References

#### Fields with this object

* [{} ArtifactInfo.packages](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-info)
