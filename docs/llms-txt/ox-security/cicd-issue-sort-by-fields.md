# Source: https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/enums/cicd-issue-sort-by-fields.md

# cicdIssueSortByFields

Defines the available fields for sorting CI/CD pipeline issues in result sets.

### Examples

```graphql
enum CICDIssueSortByFields {
  IssueScore
  Category
  IssueName
  RepoName
  JobTriggeredAt
  IsBlocking
  Severity
  JobTriggeredBy
  Enforcement
  CicdIssueStatus
  JobId
  SourceBranch
  FalsePositiveComment
}
```

### Enum values

| Enum value           | Description                                                 |
| -------------------- | ----------------------------------------------------------- |
| IssueScore           | Sort by calculated issue score based on severity and impact |
| Category             | Sort by issue category or type                              |
| IssueName            | Sort by issue name or title                                 |
| RepoName             | Sort by repository name                                     |
| JobTriggeredAt       | Sort by when the job was triggered in the pipeline          |
| IsBlocking           | Sort by whether the issue is blocking the pipeline          |
| Severity             | Sort by issue severity level                                |
| JobTriggeredBy       | Sort by user or system that triggered the job               |
| Enforcement          | Sort by enforcement level in the pipeline                   |
| CicdIssueStatus      | Sort by issue status in the CI/CD context                   |
| JobId                | Sort by job identifier                                      |
| SourceBranch         | Sort by source branch name                                  |
| FalsePositiveComment | Sort by false positive comment                              |

### References

#### Fields with this object

* [{} CICDIssuesSort.fields](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issues-sort)
