# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-unscanned-artifacts-input.md

# getUnscannedArtifactsInput

Input parameters for retrieving unscanned artifacts with filtering and pagination support.

### Examples

```graphql
input GetUnscannedArtifactsInput {
  limit: Int
  offset: Int
  sort: UnscannedArtifactSort
  dateRange: DateRange
  filters: UnscannedArtifactFilters
  owners: [String]
  search: String
  openItems: [FilterTypes]
  topFilters: [UnscannedArtifactTopFilters]
}
```

### Fields

| Field                                                                                                                                                           | Description                                                       | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                               |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| limit `Int`                                                                                                                                                     | Maximum number of unscanned artifacts to return (default: 100)    |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| offset `Int`                                                                                                                                                    | Number of unscanned artifacts to skip for pagination (default: 0) |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| sort [`UnscannedArtifactSort`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/unscanned-artifact-sort)                     | Sorting criteria for unscanned artifacts                          | <p>field <a href="../enums/unscanned-artifacts-sort-by-fields"><code>\[UnscannedArtifactsSortByFields]</code></a><br>order <a href="../../../api--audit/types/enums/direction"><code>\[Direction]</code></a></p>                                                                                                                                                                                                               |
| dateRange [`DateRange`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/date-range)                                      | Date range filter using epoch timestamps                          | <p>from <code>Float</code><br>to <code>Float</code></p>                                                                                                                                                                                                                                                                                                                                                                        |
| filters [`UnscannedArtifactFilters`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/unscanned-artifact-filters)            | Additional filters applied to unscanned artifacts                 | <p>reason <code>\[String]</code><br>registryType <code>\[String]</code><br>registryName <code>\[String]</code><br>imageName <code>\[String]</code><br>imageDigest <code>\[String]</code><br>imageTags <code>\[String]</code><br>cloudDeployments <code>\[String]</code><br>cluster <code>\[String]</code><br>namespace <code>\[String]</code><br>reachability <code>\[String]</code><br>imageSource <code>\[String]</code></p> |
| owners `[String]`                                                                                                                                               | List of artifact owners to filter by                              |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| search `String`                                                                                                                                                 | Search string to filter unscanned artifacts by name or metadata   |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| openItems [`[FilterTypes]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/filter-types)                                 | List of open item filter types to apply                           |                                                                                                                                                                                                                                                                                                                                                                                                                                |
| topFilters [`[UnscannedArtifactTopFilters]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/unscanned-artifact-top-filters) | List of predefined top-level filters to apply                     |                                                                                                                                                                                                                                                                                                                                                                                                                                |

### References

#### Queries using this object

* [\<?> getUnscannedArtifacts.getUnscannedArtifactsInput](https://docs.ox.security/api-documentation/api-reference/api--artifact/queries/get-unscanned-artifacts)
