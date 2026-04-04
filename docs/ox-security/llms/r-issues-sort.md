# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/r-issues-sort.md

# rIssuesSort

Sorting configuration for resolved issues.

### Examples

```graphql
input RIssuesSort {
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

* [{} ResolvedIssuesInput.sort](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/resolved-issues-input)
* [{} ResolvedIssuesV2Input.sort](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/resolved-issues-v2input)
