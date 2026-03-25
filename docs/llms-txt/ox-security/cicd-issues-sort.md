# Source: https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issues-sort.md

# cicdIssuesSort

Specifies the sorting parameters for CI/CD issues.

### Examples

```graphql
input CICDIssuesSort {
  fields: [CICDIssueSortByFields]
  order: [Direction]
}
```

### Fields

| Field                                                                                                                                              | Description                                             | Supported fields |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------- | ---------------- |
| fields [`[CICDIssueSortByFields]`](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/enums/cicd-issue-sort-by-fields) | Specifies the fields to sort CI/CD issues by            |                  |
| order [`[Direction]`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/direction)                                   | Defines the sort direction for each field (ASC or DESC) |                  |

### References

#### Fields with this object

* [{} CICDIssuesInput.sort](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issues-input)
