# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-sort.md

# issuesSort

### Examples

```graphql
input IssuesSort {
  fields: [IssueSortByFields]
  order: [Direction]
}
```

### Fields

| Field                                                                                                                                | Description                                                                | Supported fields |
| ------------------------------------------------------------------------------------------------------------------------------------ | -------------------------------------------------------------------------- | ---------------- |
| fields [`[IssueSortByFields]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/issue-sort-by-fields) | List of fields to sort issues by. Defaults to sorting by Severity          |                  |
| order [`[Direction]`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/direction)                     | Sort order for each field in the fields list. Defaults to descending order |                  |

### References

#### Fields with this object

* [{} IssuesInput.sort](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-input)
