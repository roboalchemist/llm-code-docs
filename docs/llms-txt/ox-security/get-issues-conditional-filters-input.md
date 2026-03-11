# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/get-issues-conditional-filters-input.md

# getIssuesConditionalFiltersInput

### Examples

```graphql
input GetIssuesConditionalFiltersInput {
  scanID: String
  limit: Int
  search: [AutoCompleteSearch]
  owners: [String]
  tagIds: [String]
  inventoryFilters: [InventoryTypes]
  dateRange: DateRange
  openItems: [FilterTypes]
  conditionalFilters: [ConditionalFilters]
  topLevelSearch: String
}
```

### Fields

| Field                                                                                                                                                   | Description                                                        | Supported fields                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scanID `String`                                                                                                                                         | Retrieve issues associated with a specific scan execution          |                                                                                                                                                                                                                                                                                                                         |
| limit `Int`                                                                                                                                             | Maximum number of filter options to return (default: 50, max: 100) |                                                                                                                                                                                                                                                                                                                         |
| search [`[AutoCompleteSearch]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/auto-complete-search)            | List of search filters for finding specific issues                 | <p>fieldName <code>String</code><br>value <code>\[String]</code></p>                                                                                                                                                                                                                                                    |
| owners `[String]`                                                                                                                                       | Filter issues by specific owner identifiers                        |                                                                                                                                                                                                                                                                                                                         |
| tagIds `[String]`                                                                                                                                       | Filter issues by tag identifiers for RBAC scoping                  |                                                                                                                                                                                                                                                                                                                         |
| inventoryFilters [`[InventoryTypes]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/inventory-types)                  | Filters for inventory queries targeting top issues                 |                                                                                                                                                                                                                                                                                                                         |
| dateRange [`DateRange`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/date-range)                              | Date range for filtering issues                                    | <p>from <code>Float</code><br>to <code>Float</code></p>                                                                                                                                                                                                                                                                 |
| openItems [`[FilterTypes]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/filter-types)                         | Filters specifying open items                                      |                                                                                                                                                                                                                                                                                                                         |
| conditionalFilters [`[ConditionalFilters]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/conditional-filters) | Complex conditional filters for advanced filtering                 | <p>condition <a href="../../../api--application/types/enums/condition-type"><code>ConditionType</code></a><br>fieldName <a href="../../../api--application/types/enums/filter-types"><code>FilterTypes</code></a><br>values <code>\[String]</code><br>greaterThan <code>Float</code><br>lessThan <code>Float</code></p> |
| topLevelSearch `String`                                                                                                                                 | Search string for top-level issue search                           |                                                                                                                                                                                                                                                                                                                         |

### References

#### Queries using this object

* [\<?> getIssuesConditionalFiltersLazy.getIssuesConditionalFiltersInput](https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-issues-conditional-filters-lazy)
