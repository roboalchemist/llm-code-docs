# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/unscanned-artifact.md

# unscannedArtifact

Unscanned artifact information.

### Examples

```graphql
type UnscannedArtifact {
  id: String
  artifactId: String
  registryType: String
  registryName: String
  registryLink: String
  imageName: String
  imageTags: [String]
  imageCreationDate: String
  imageDigest: String
  reason: String
  error: String
  scanId: String
  cloudData: [CloudArtifactData]
}
```

### Fields

| Field                                                                                                                                       | Description                                 | Supported fields                                                                                                                                                                                                                                                                                                                  |
| ------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id `String`                                                                                                                                 | Unique identifier of the unscanned artifact |                                                                                                                                                                                                                                                                                                                                   |
| artifactId `String`                                                                                                                         | Unique identifier of the artifact           |                                                                                                                                                                                                                                                                                                                                   |
| registryType `String`                                                                                                                       | Type of the registry                        |                                                                                                                                                                                                                                                                                                                                   |
| registryName `String`                                                                                                                       | Name of the registry                        |                                                                                                                                                                                                                                                                                                                                   |
| registryLink `String`                                                                                                                       | Link to the registry                        |                                                                                                                                                                                                                                                                                                                                   |
| imageName `String`                                                                                                                          | Name of the image                           |                                                                                                                                                                                                                                                                                                                                   |
| imageTags `[String]`                                                                                                                        | Tags of the image                           |                                                                                                                                                                                                                                                                                                                                   |
| imageCreationDate `String`                                                                                                                  | Creation date of the image                  |                                                                                                                                                                                                                                                                                                                                   |
| imageDigest `String`                                                                                                                        | Digest of the image                         |                                                                                                                                                                                                                                                                                                                                   |
| reason `String`                                                                                                                             | Reason for the unscanned artifact           |                                                                                                                                                                                                                                                                                                                                   |
| error `String`                                                                                                                              | Error message for the unscanned artifact    |                                                                                                                                                                                                                                                                                                                                   |
| scanId `String`                                                                                                                             | Scan identifier                             |                                                                                                                                                                                                                                                                                                                                   |
| cloudData [`[CloudArtifactData]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/cloud-artifact-data) | Cloud data for the unscanned artifact       | <p>cloudIdentifier <code>String</code><br>link <code>String</code><br>lastExecutionTime <code>Float</code><br>lastModifiedTime <code>Float</code><br>account <code>String</code><br>zone <code>String</code><br>cluster <code>String</code><br>cloudDescription <a href="cloud-description"><code>CloudDescription</code></a></p> |

### References

#### Queries using this object

* [\<?> getUnscannedArtifact](https://docs.ox.security/api-documentation/api-reference/api--artifact/queries/get-unscanned-artifact)

#### Fields with this object

* [{} UnscannedArtifactsResponse.unscannedArtifacts](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/unscanned-artifacts-response)
