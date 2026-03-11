# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/range.md

# range

### Examples

```graphql
input Range {
  from: Float
  to: Float
}
```

### Fields

| Field        | Description                                 | Supported fields |
| ------------ | ------------------------------------------- | ---------------- |
| from `Float` | Start value of the range filter (inclusive) |                  |
| to `Float`   | End value of the range filter (inclusive)   |                  |

### References

#### Fields with this object

* [{} AppFilters.riskScore](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/app-filters)
* [{} AppFilters.businessPriority](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/app-filters)
* [{} IssueFilters.businessPriority](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issue-filters)
* [{} IssueFilters.epssScore](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issue-filters)
* [{} IssueFilters.epssPercentile](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issue-filters)
* [{} IssueFilters.issueImportance](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issue-filters)
* [{} CICDIssueFilters.businessPriority](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issue-filters)
* [{} CICDIssueFilters.issueImportance](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issue-filters)
