# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/cicd-fields.md

# cicdFields

Fields related to CI/CD metadata for an issue.

### Examples

```graphql
type CICDFields {
  issueStatus: CICDIssueStatus
  sourceBranch: String
  targetBranch: String
  isBlocking: Boolean
  jobId: String
  jobTriggeredAt: String
  jobTriggeredAtDate: Float
  jobTriggeredBy: String
  jobTriggeredReason: String
  jobUrl: String
  pullRequestId: String
  pullRequestUrl: String
  enforcement: String
  excludedByAlert: Boolean
  cicdEventType: String
  workflows: [OxWorkflow]
}
```

### Fields

| Field                                                                                                                              | Description                                                              | Supported fields                                          |
| ---------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------ | --------------------------------------------------------- |
| issueStatus [`CICDIssueStatus`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/cicd-issue-status) | Status of the issue in the CI/CD context                                 |                                                           |
| sourceBranch `String`                                                                                                              | Name of the source branch related to the issue                           |                                                           |
| targetBranch `String`                                                                                                              | Name of the target branch for the issue or PR                            |                                                           |
| ~~isBlocking `Boolean`~~ ⚠️                                                                                                        | **Deprecated**: use 'enforcement'                                        |                                                           |
| jobId `String`                                                                                                                     | ID of the CI/CD job related to the issue                                 |                                                           |
| jobTriggeredAt `String`                                                                                                            | Timestamp string when the job was triggered                              |                                                           |
| jobTriggeredAtDate `Float`                                                                                                         | Timestamp as float when the job was triggered                            |                                                           |
| jobTriggeredBy `String`                                                                                                            | User or system that triggered the CI/CD job                              |                                                           |
| jobTriggeredReason `String`                                                                                                        | Reason or context for triggering the job                                 |                                                           |
| jobUrl `String`                                                                                                                    | URL to the CI/CD job                                                     |                                                           |
| pullRequestId `String`                                                                                                             | ID of the related pull request                                           |                                                           |
| pullRequestUrl `String`                                                                                                            | URL link to the related pull request                                     |                                                           |
| enforcement `String`                                                                                                               | Enforcement level or status within the CI/CD pipeline                    |                                                           |
| excludedByAlert `Boolean`                                                                                                          | Indicates if the issue was excluded by an alert within the CI/CD context |                                                           |
| cicdEventType `String`                                                                                                             | Type of CI/CD event that triggered this issue or job                     |                                                           |
| workflows [`[OxWorkflow]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/ox-workflow)          | Workflows associated with the CI/CD issue                                | <p>id <code>String</code><br>name <code>String</code></p> |

### References

#### Fields with this object

* [{} Issue.cicdFields](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
