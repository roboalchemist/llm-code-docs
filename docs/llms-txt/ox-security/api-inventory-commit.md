# Source: https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-inventory-commit.md

# apiInventoryCommit

Git commit information associated with an API discovery.

### Examples

```graphql
type ApiInventoryCommit {
  commitInfo: ApiInventoryCommitInfo
  match: String
  snippet: String
  snippetLineNumber: Int
  startLineNumber: Int
  fileName: String
  link: String
}
```

### Fields

| Field                                                                                                                                                     | Description                                        | Supported fields                                                                                                                                                                                                                                                                   |
| --------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| commitInfo [`ApiInventoryCommitInfo`](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-inventory-commit-info) | Detailed information about the Git commit          | <p>authorName <code>String</code><br>authorEmail <code>String</code><br>committerName <code>String</code><br>committerEmail <code>String</code><br>commitId <code>String</code><br>message <code>String</code><br>authorDate <code>Date</code><br>commitDate <code>Date</code></p> |
| match `String`                                                                                                                                            | Text match found in the commit                     |                                                                                                                                                                                                                                                                                    |
| snippet `String`                                                                                                                                          | Code snippet from the commit showing the API usage |                                                                                                                                                                                                                                                                                    |
| snippetLineNumber `Int`                                                                                                                                   | Line number where the snippet appears              |                                                                                                                                                                                                                                                                                    |
| startLineNumber `Int`                                                                                                                                     | Starting line number of the relevant code section  |                                                                                                                                                                                                                                                                                    |
| fileName `String`                                                                                                                                         | Name of the file modified in this commit           |                                                                                                                                                                                                                                                                                    |
| link `String`                                                                                                                                             | URL link to view this commit                       |                                                                                                                                                                                                                                                                                    |

### References

#### Fields with this object

* [{} ApiSecurityItem.commits](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-security-item)
