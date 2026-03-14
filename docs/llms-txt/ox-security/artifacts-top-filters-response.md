# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifacts-top-filters-response.md

# artifactsTopFiltersResponse

Response containing top-level artifact filters and their metadata.

### Examples

```graphql
type ArtifactsTopFiltersResponse {
  name: ArtifactTopFilters
  label: String
  count: Int
  delta: Int
  trend: String
}
```

### Fields

| Field                                                                                                                                | Description | Supported fields |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------- | ---------------- |
| name [`ArtifactTopFilters`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/artifact-top-filters) |             |                  |
| label `String`                                                                                                                       |             |                  |
| count `Int`                                                                                                                          |             |                  |
| delta `Int`                                                                                                                          |             |                  |
| trend `String`                                                                                                                       |             |                  |

### References

#### Queries using this object

* [\<?> getArtifactsTopFilters](https://docs.ox.security/api-documentation/api-reference/api--artifact/queries/get-artifacts-top-filters)
