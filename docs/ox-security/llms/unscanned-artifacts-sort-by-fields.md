# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/unscanned-artifacts-sort-by-fields.md

# unscannedArtifactsSortByFields

Fields available for sorting unscanned artifacts.

### Examples

```graphql
enum UnscannedArtifactsSortByFields {
  createdAt
  RegistryType
  ImageName
  ImageDigest
  Reason
  ImageTags
}
```

### Enum values

| Enum value   | Description |
| ------------ | ----------- |
| createdAt    |             |
| RegistryType |             |
| ImageName    |             |
| ImageDigest  |             |
| Reason       |             |
| ImageTags    |             |

### References

#### Fields with this object

* [{} UnscannedArtifactSort.field](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/unscanned-artifact-sort)
