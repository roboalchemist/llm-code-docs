# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-artifacts-v2input.md

# getArtifactsV2input

Defines input parameters for retrieving artifacts with enhanced filtering and pagination support.

### Examples

```graphql
input GetArtifactsV2Input {
  scanId: String
  conditionalFilters: [ConditionalFilters]
  search: String
  limit: Int
  offset: Int
  sort: ArtifactsSort
  owners: [String]
  tagIds: [String]
}
```

### Fields

| Field                                                                                                                                                   | Description                                         | Supported fields                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scanId `String`                                                                                                                                         | Specific scan identifier to retrieve artifacts from |                                                                                                                                                                                                                                                                                                                         |
| conditionalFilters [`[ConditionalFilters]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/conditional-filters) | Conditional filters to apply for advanced querying  | <p>condition <a href="../../../api--application/types/enums/condition-type"><code>ConditionType</code></a><br>fieldName <a href="../../../api--application/types/enums/filter-types"><code>FilterTypes</code></a><br>values <code>\[String]</code><br>greaterThan <code>Float</code><br>lessThan <code>Float</code></p> |
| search `String`                                                                                                                                         | Text search query to find specific artifacts        |                                                                                                                                                                                                                                                                                                                         |
| limit `Int`                                                                                                                                             | Maximum number of artifacts to return               |                                                                                                                                                                                                                                                                                                                         |
| offset `Int`                                                                                                                                            | Number of artifacts to skip for pagination          |                                                                                                                                                                                                                                                                                                                         |
| sort [`ArtifactsSort`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/artifacts-sort)                              | Sorting configuration for the results               | <p>field <a href="../enums/artifacts-sort-by-fields"><code>\[ArtifactsSortByFields]</code></a><br>order <a href="../../../api--audit/types/enums/direction"><code>\[Direction]</code></a></p>                                                                                                                           |
| owners `[String]`                                                                                                                                       | List of artifact owners to filter by                |                                                                                                                                                                                                                                                                                                                         |
| tagIds `[String]`                                                                                                                                       | List of tag IDs to filter artifacts by              |                                                                                                                                                                                                                                                                                                                         |

### References

#### Queries using this object

* [\<?> getArtifactsV2.input](https://docs.ox.security/api-documentation/api-reference/api--artifact/queries/get-artifacts-v2)
