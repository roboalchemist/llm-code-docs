# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-lazy-response.md

# filterLazyResponse

Response for lazy-loaded filter data with pagination.

### Examples

```graphql
type FilterLazyResponse {
  total: Int
  totalFiltered: Int
  filters: [FilterLazy]
}
```

### Fields

| Field                                                                                                                         | Description                                  | Supported fields                                                                                                                       |
| ----------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- |
| total `Int`                                                                                                                   | Total number of items available              |                                                                                                                                        |
| totalFiltered `Int`                                                                                                           | Total number of items after applying filters |                                                                                                                                        |
| filters [`[FilterLazy]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/filter-lazy) | List of filter categories with their items   | <p>type <a href="../enums/filter-types"><code>FilterTypes</code></a><br>items <a href="filter-info"><code>\[FilterInfo]</code></a></p> |

### References

#### Queries using this object

* [\<?> getApplicationsConditionalFilters](https://docs.ox.security/api-documentation/api-reference/api--application/queries/get-applications-conditional-filters)
* [\<?> getIssuesConditionalFiltersLazy](https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-issues-conditional-filters-lazy)
* [\<?> getApiSecurityFiltersLazy](https://docs.ox.security/api-documentation/api-reference/api--api-security/queries/get-api-security-filters-lazy)
