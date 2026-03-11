# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issues-breakdown.md

# issuesBreakdown

Describes breakdown of security issues by severity level.

### Examples

```graphql
type IssuesBreakdown {
  severity: String
  count: Int
}
```

### Fields

| Field             | Description                             | Supported fields |
| ----------------- | --------------------------------------- | ---------------- |
| severity `String` | Severity level of the issues            |                  |
| count `Int`       | Number of issues at this severity level |                  |

### References

#### Queries using this object

* [\<?> getSbomIssuesBreakdown](https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-sbom-issues-breakdown)
