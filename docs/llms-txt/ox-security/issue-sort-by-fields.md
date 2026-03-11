# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/issue-sort-by-fields.md

# issueSortByFields

Fields available for sorting security issues in result sets.

### Examples

```graphql
enum IssueSortByFields {
  Category
  IssueName
  RepoName
  Owner
  OpenDate
  Occurrences
  ResolvedDate
  ResolvedReason
  DisappearedDate
  DisappearedReason
  Severity
  BusinessPriority
  DaysPastSLA
  IssueScore
  FalsePositiveComment
}
```

### Enum values

| Enum value           | Description                               |
| -------------------- | ----------------------------------------- |
| Category             | Sort by issue category or classification  |
| IssueName            | Sort by issue name or title               |
| RepoName             | Sort by repository name                   |
| Owner                | Sort by assigned owner                    |
| OpenDate             | Sort by issue discovery date              |
| Occurrences          | Sort by frequency of issue occurrence     |
| ResolvedDate         | Sort by issue resolution date             |
| ResolvedReason       | Sort by resolution reason                 |
| DisappearedDate      | Sort by date when issue was last detected |
| DisappearedReason    | Sort by reason for issue disappearance    |
| Severity             | Sort by issue severity level              |
| BusinessPriority     | Sort by business impact priority          |
| DaysPastSLA          | Sort by SLA compliance status             |
| IssueScore           | Sort by calculated risk score             |
| FalsePositiveComment | Sort by false positive comment            |

### References

#### Fields with this object

* [{} IssuesSort.fields](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-sort)
* [{} RIssuesSort.fields](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/r-issues-sort)
* [{} DIssuesSort.fields](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/d-issues-sort)
