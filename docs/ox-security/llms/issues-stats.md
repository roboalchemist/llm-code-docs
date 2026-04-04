# Source: https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/issues-stats.md

# issuesStats

Holds statistics about security issues found in cloud resources.

### Examples

```graphql
type IssuesStats {
  totalIssues: Int
  sourceTools: [IssueStat]
  categories: [IssueStat]
  severities: [IssueStat]
}
```

### Fields

| Field                                                                                                                              | Description                                  | Supported fields                                          |
| ---------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------- | --------------------------------------------------------- |
| totalIssues `Int`                                                                                                                  | Total number of security issues found        |                                                           |
| sourceTools [`[IssueStat]`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/issue-stat) | Breakdown of issues by source scanning tools | <p>name <code>String</code><br>total <code>Int</code></p> |
| categories [`[IssueStat]`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/issue-stat)  | Breakdown of issues by security categories   | <p>name <code>String</code><br>total <code>Int</code></p> |
| severities [`[IssueStat]`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/issue-stat)  | Breakdown of issues by severity levels       | <p>name <code>String</code><br>total <code>Int</code></p> |

### References

#### Fields with this object

* [{} CloudItem.issuesStats](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item)
