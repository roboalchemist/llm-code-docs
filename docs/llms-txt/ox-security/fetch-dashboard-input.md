# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/fetch-dashboard-input.md

# fetchDashboardInput

Input parameters for fetching dashboard data with filtering and pagination.

### Examples

```graphql
input FetchDashboardInput {
  scanId: String
  limit: Int
  orderBy: OrderBy
  dateRange: DateRangeFilter
  filters: [InventoryTypes]
  owners: [String]
  appIds: [String]
  tagIds: [String]
  isSingleRepoScan: Boolean
  apps: [String]
  orgUnits: [String]
  severities: [Int]
  categories: [Int]
  tags: [String]
  conditionalFilters: [IssuesTrendDataConditionalFilters]
}
```

### Fields

| Field                                                                                                                                                                              | Description                                                      | Supported fields                                                                                                                                                                                                                                                                |
| ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scanId `String`                                                                                                                                                                    | Specific scan identifier to retrieve data from                   |                                                                                                                                                                                                                                                                                 |
| limit `Int`                                                                                                                                                                        | Maximum number of results to return (default: 10)                |                                                                                                                                                                                                                                                                                 |
| orderBy [`OrderBy`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/order-by)                                                                     | Sorting configuration for the results                            | <p>field <a href="../../../api--application/types/enums/order-by-field"><code>OrderByField</code></a><br>direction <a href="../../../api--audit/types/enums/direction"><code>Direction</code></a></p>                                                                           |
| dateRange [`DateRangeFilter`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/date-range-filter)                                                  | Date range filter for organization scores (default: last 7 days) | <p>from <code>Float</code><br>to <code>Float</code></p>                                                                                                                                                                                                                         |
| filters [`[InventoryTypes]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/inventory-types)                                                      | Inventory type filters for dashboard data                        |                                                                                                                                                                                                                                                                                 |
| owners `[String]`                                                                                                                                                                  | Filter by application owners                                     |                                                                                                                                                                                                                                                                                 |
| appIds `[String]`                                                                                                                                                                  | Filter by specific application identifiers                       |                                                                                                                                                                                                                                                                                 |
| tagIds `[String]`                                                                                                                                                                  | Filter by tag identifiers for role-based access control          |                                                                                                                                                                                                                                                                                 |
| isSingleRepoScan `Boolean`                                                                                                                                                         | Whether this is a single repository scan                         |                                                                                                                                                                                                                                                                                 |
| apps `[String]`                                                                                                                                                                    | Filter by application identifiers                                |                                                                                                                                                                                                                                                                                 |
| orgUnits `[String]`                                                                                                                                                                | Filter by organizational unit identifiers                        |                                                                                                                                                                                                                                                                                 |
| severities `[Int]`                                                                                                                                                                 | Filter by severity levels                                        |                                                                                                                                                                                                                                                                                 |
| categories `[Int]`                                                                                                                                                                 | Filter by category levels                                        |                                                                                                                                                                                                                                                                                 |
| tags `[String]`                                                                                                                                                                    | Filter by tag identifiers                                        |                                                                                                                                                                                                                                                                                 |
| conditionalFilters [`[IssuesTrendDataConditionalFilters]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-trend-data-conditional-filters) | Filter by conditional filters                                    | <p>condition <a href="../enums/issues-trend-data-filters-condition"><code>IssuesTrendDataFiltersCondition</code></a><br>fieldName <a href="../enums/issues-trend-data-filters-field-name"><code>IssuesTrendDataFiltersFieldName</code></a><br>values <code>\[String]</code></p> |

### References

#### Queries using this object

* [\<?> getIssuesTrendData.getIssuesTrendInput](https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-issues-trend-data)
