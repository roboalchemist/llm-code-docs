# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/i-artifact-info.md

# iArtifactInfo

Core metadata and information about an artifact.

### Examples

```graphql
type IArtifactInfo {
  type: ArtifactInfoTypes
  name: String
  version: String
  hash: String
  artifactIntegrity: String
  registry: String
  visibility: String
  firstSeenDate: Float
  runtime: Boolean
  cloudDeployed: Boolean
  biVisibility: String
  biName: String
  biVersion: String
  osName: String
  osVersion: String
}
```

### Fields

| Field                                                                                                                              | Description                                                | Supported fields |
| ---------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------- | ---------------- |
| type [`ArtifactInfoTypes`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/artifact-info-types) | Type of the artifact info (enum describing artifact types) |                  |
| name `String`                                                                                                                      | Name of the artifact                                       |                  |
| version `String`                                                                                                                   | Version of the artifact                                    |                  |
| hash `String`                                                                                                                      | Hash or checksum representing the artifact's contents      |                  |
| artifactIntegrity `String`                                                                                                         | Integrity status or checksum verification of the artifact  |                  |
| registry `String`                                                                                                                  | Registry where the artifact is stored                      |                  |
| visibility `String`                                                                                                                | Visibility of the artifact                                 |                  |
| firstSeenDate `Float`                                                                                                              | First seen date of the artifact                            |                  |
| runtime `Boolean`                                                                                                                  | Runtime of the artifact                                    |                  |
| cloudDeployed `Boolean`                                                                                                            | Cloud deployed of the artifact                             |                  |
| biVisibility `String`                                                                                                              | BI visibility of the artifact                              |                  |
| biName `String`                                                                                                                    | BI name of the artifact                                    |                  |
| biVersion `String`                                                                                                                 | BI version of the artifact                                 |                  |
| osName `String`                                                                                                                    | OS name of the artifact                                    |                  |
| osVersion `String`                                                                                                                 | OS version of the artifact                                 |                  |

### References

#### Fields with this object

* [{} ArtifactInfo.artifactInfo](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-info)
