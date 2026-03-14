# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/issues-trend-data-filters-field-name.md

# issuesTrendDataFiltersFieldName

Field name for issues trend data filters.

### Examples

```graphql
enum IssuesTrendDataFiltersFieldName {
  criticality
  categories
  apps
  orgUnit
  tags
}
```

### Enum values

| Enum value  | Description                   |
| ----------- | ----------------------------- |
| criticality | Filter by severity levels     |
| categories  | Filter by categories          |
| apps        | Filter by application names   |
| orgUnit     | Filter by organizational unit |
| tags        | Filter by tag names           |

### References

#### Fields with this object

* [{} IssuesTrendDataConditionalFilters.fieldName](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-trend-data-conditional-filters)
