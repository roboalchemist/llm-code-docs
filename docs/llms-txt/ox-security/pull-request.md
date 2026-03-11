# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/pull-request.md

# pullRequest

Details about a Pull Request related to an issue.

### Examples

```graphql
type PullRequest {
  sourceControlType: String
  issueId: String
  appId: String
  repo: String
  prId: String
  prURL: String
  prBranchName: String
  commitMessage: String
  commiter: String
  comment: String
  date: Date
  prTitle: String
  prBody: String
  prStatus: String
  prApprover: String
  prReviewer: String
  prMergeTime: Date
}
```

### Fields

| Field                      | Description                                      | Supported fields |
| -------------------------- | ------------------------------------------------ | ---------------- |
| sourceControlType `String` | Type of source control system                    |                  |
| issueId `String`           | ID of the related issue                          |                  |
| appId `String`             | ID of the related application                    |                  |
| repo `String`              | Repository name                                  |                  |
| prId `String`              | Pull request unique identifier                   |                  |
| prURL `String`             | URL link to the pull request                     |                  |
| prBranchName `String`      | Name of the branch for the pull request          |                  |
| commitMessage `String`     | Commit message associated with the pull request  |                  |
| commiter `String`          | Name of the person who committed the changes     |                  |
| comment `String`           | Additional comment about the pull request        |                  |
| date `Date`                | Date when the pull request was created           |                  |
| prTitle `String`           | Title of the pull request                        |                  |
| prBody `String`            | Body/description of the pull request             |                  |
| prStatus `String`          | Current status of the pull request               |                  |
| prApprover `String`        | Name of the person who approved the pull request |                  |
| prReviewer `String`        | Name of the reviewer of the pull request         |                  |
| prMergeTime `Date`         | Date when the pull request was merged            |                  |

### References

#### Fields with this object

* [{} AggItem.prDeatils](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/agg-item)
* [{} Issue.prDeatils](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
