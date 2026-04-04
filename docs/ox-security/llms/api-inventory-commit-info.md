# Source: https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-inventory-commit-info.md

# apiInventoryCommitInfo

Detailed Git commit metadata.

### Examples

```graphql
type ApiInventoryCommitInfo {
  authorName: String
  authorEmail: String
  committerName: String
  committerEmail: String
  commitId: String
  message: String
  authorDate: Date
  commitDate: Date
}
```

### Fields

| Field                   | Description                                  | Supported fields |
| ----------------------- | -------------------------------------------- | ---------------- |
| authorName `String`     | Name of the commit author                    |                  |
| authorEmail `String`    | Email address of the commit author           |                  |
| committerName `String`  | Name of the person who committed the changes |                  |
| committerEmail `String` | Email address of the committer               |                  |
| commitId `String`       | Unique identifier of the commit              |                  |
| message `String`        | Commit message describing the changes        |                  |
| authorDate `Date`       | Date when the changes were authored          |                  |
| commitDate `Date`       | Date when the changes were committed         |                  |

### References

#### Fields with this object

* [{} ApiInventoryCommit.commitInfo](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-inventory-commit)
