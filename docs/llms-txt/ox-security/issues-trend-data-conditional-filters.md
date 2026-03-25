# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-trend-data-conditional-filters.md

# issuesTrendDataConditionalFilters

Conditional filters for issues trend data.

### Examples

```graphql
input IssuesTrendDataConditionalFilters {
  condition: IssuesTrendDataFiltersCondition
  fieldName: IssuesTrendDataFiltersFieldName
  values: [String]
}
```

### Fields

| Field                                                                                                                                                               | Description                                   | Supported fields |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------- | ---------------- |
| condition [`IssuesTrendDataFiltersCondition`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/issues-trend-data-filters-condition)  | Condition type for issues trend data filters. |                  |
| fieldName [`IssuesTrendDataFiltersFieldName`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/issues-trend-data-filters-field-name) | Field name for issues trend data filters.     |                  |
| values `[String]`                                                                                                                                                   | Values for issues trend data filters.         |                  |

### References

#### Fields with this object

* [{} FetchDashboardInput.conditionalFilters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/fetch-dashboard-input)
