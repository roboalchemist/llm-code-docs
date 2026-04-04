# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/unscanned-artifact-filters.md

# unscannedArtifactFilters

Input parameters for filtering unscanned artifacts.

### Examples

```graphql
input UnscannedArtifactFilters {
  reason: [String]
  registryType: [String]
  registryName: [String]
  imageName: [String]
  imageDigest: [String]
  imageTags: [String]
  cloudDeployments: [String]
  cluster: [String]
  namespace: [String]
  reachability: [String]
  imageSource: [String]
}
```

### Fields

| Field                       | Description                                 | Supported fields |
| --------------------------- | ------------------------------------------- | ---------------- |
| reason `[String]`           | Filter by reason for the unscanned artifact |                  |
| registryType `[String]`     | Filter by type of registry                  |                  |
| registryName `[String]`     | Filter by name of the registry              |                  |
| imageName `[String]`        | Filter by name of the image                 |                  |
| imageDigest `[String]`      | Filter by digest of the image               |                  |
| imageTags `[String]`        | Filter by tags of the image                 |                  |
| cloudDeployments `[String]` |                                             |                  |
| cluster `[String]`          | Filter by cluster name                      |                  |
| namespace `[String]`        | Filter by namespace                         |                  |
| reachability `[String]`     | Filter by reachability status               |                  |
| imageSource `[String]`      | Filter by source of the image               |                  |

### References

#### Fields with this object

* [{} GetUnscannedArtifactsInput.filters](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-unscanned-artifacts-input)
