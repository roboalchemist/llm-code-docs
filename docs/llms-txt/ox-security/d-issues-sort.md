# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/d-issues-sort.md

# dIssuesSort

Sorting configuration for disappeared issues.

### Examples

```graphql
input DIssuesSort {
  fields: [IssueSortByFields]
  order: [Direction]
}
```

### Fields

| Field                                                                                                                                | Description                                     | Supported fields |
| ------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------- | ---------------- |
| fields [`[IssueSortByFields]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/issue-sort-by-fields) | Fields to sort by (default: Severity)           |                  |
| order [`[Direction]`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/direction)                     | Sort order for each field (default: descending) |                  |

### References

#### Fields with this object

* [{} DisappearedIssuesInput.sort](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/disappeared-issues-input)
