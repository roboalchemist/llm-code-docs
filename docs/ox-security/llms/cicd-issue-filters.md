# Source: https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issue-filters.md

# cicdIssueFilters

Specifies the filter criteria for CI/CD issues.

### Examples

```graphql
input CICDIssueFilters {
  apps: [String]
  criticality: [CriticalityFilter]
  policies: [String]
  issueOwners: [String]
  categories: [String]
  issueNames: [String]
  sourceTools: [String]
  businessPriority: Range
  issueImportance: Range
  appId: [String]
  cwe: [String]
  severityChange: [String]
  severityChangeReasons: [String]
  issueActions: [String]
  jobTriggeredBy: [String]
  cicdIssueStatus: [String]
  jobNumber: [String]
  enforcement: [String]
  pullRequests: [String]
  sourceBranch: [String]
  issueIds: [String]
}
```

### Fields

| Field                                                                                                                                   | Description                                          | Supported fields                                        |
| --------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------- |
| apps `[String]`                                                                                                                         | Filters issues by application names                  |                                                         |
| criticality [`[CriticalityFilter]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/criticality-filter) | Filters issues by their severity levels              |                                                         |
| policies `[String]`                                                                                                                     | Filters issues by policy names                       |                                                         |
| issueOwners `[String]`                                                                                                                  | Filters issues by their assigned owners              |                                                         |
| categories `[String]`                                                                                                                   | Filters issues by their categories                   |                                                         |
| issueNames `[String]`                                                                                                                   | Filters issues by their names or titles              |                                                         |
| sourceTools `[String]`                                                                                                                  | Filters issues by their source tools                 |                                                         |
| businessPriority [`Range`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/range)                | Filters issues by repository business priority range | <p>from <code>Float</code><br>to <code>Float</code></p> |
| issueImportance [`Range`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/range)                 | Filters issues by their importance score range       | <p>from <code>Float</code><br>to <code>Float</code></p> |
| appId `[String]`                                                                                                                        | Filters issues by application IDs                    |                                                         |
| cwe `[String]`                                                                                                                          | Filters issues by CWE identifiers                    |                                                         |
| severityChange `[String]`                                                                                                               | Filters issues by their severity change status       |                                                         |
| severityChangeReasons `[String]`                                                                                                        | Filters issues by their severity change reasons      |                                                         |
| issueActions `[String]`                                                                                                                 | Filters issues by their action status                |                                                         |
| jobTriggeredBy `[String]`                                                                                                               | Filters issues by the entity that triggered the job  |                                                         |
| cicdIssueStatus `[String]`                                                                                                              | Filters issues by their CI/CD pipeline status        |                                                         |
| jobNumber `[String]`                                                                                                                    | Filters issues by job identifiers                    |                                                         |
| enforcement `[String]`                                                                                                                  | Filters issues by their enforcement level            |                                                         |
| pullRequests `[String]`                                                                                                                 | Filters issues by associated pull request numbers    |                                                         |
| sourceBranch `[String]`                                                                                                                 | Filters issues by their source branch names          |                                                         |
| issueIds `[String]`                                                                                                                     | Filters issues by their unique identifiers           |                                                         |

### References

#### Fields with this object

* [{} CICDIssuesInput.filters](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issues-input)
