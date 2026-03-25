# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/unscanned-artifacts-response.md

# unscannedArtifactsResponse

Response containing unscanned artifacts with filtering and pagination support.

### Examples

```graphql
type UnscannedArtifactsResponse {
  unscannedArtifacts: [UnscannedArtifact]
  offset: Int
  total: Int
  totalFilteredUnscannedArtifacts: Int
}
```

### Fields

| Field                                                                                                                                               | Description                              | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |
| --------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| unscannedArtifacts [`[UnscannedArtifact]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/unscanned-artifact) | Unscanned Artifacts                      | <p>id <code>String</code><br>artifactId <code>String</code><br>registryType <code>String</code><br>registryName <code>String</code><br>registryLink <code>String</code><br>imageName <code>String</code><br>imageTags <code>\[String]</code><br>imageCreationDate <code>String</code><br>imageDigest <code>String</code><br>reason <code>String</code><br>error <code>String</code><br>scanId <code>String</code><br>cloudData <a href="cloud-artifact-data"><code>\[CloudArtifactData]</code></a></p> |
| offset `Int`                                                                                                                                        | Offset Value for Virtualization          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| total `Int`                                                                                                                                         | Total Unscanned Artifacts Count          |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| totalFilteredUnscannedArtifacts `Int`                                                                                                               | Total Filtered Unscanned Artifacts Count |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |

### References

#### Queries using this object

* [\<?> getUnscannedArtifacts](https://docs.ox.security/api-documentation/api-reference/api--artifact/queries/get-unscanned-artifacts)
