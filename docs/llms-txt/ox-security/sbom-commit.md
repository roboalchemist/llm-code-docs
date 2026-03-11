# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-commit.md

# sbomCommit

Represents commit information associated with a dependency reference.

### Examples

```graphql
type SbomCommit {
  commitedAt: String
  committerName: String
  committerEmail: String
}
```

### Fields

| Field                   | Description                                              | Supported fields |
| ----------------------- | -------------------------------------------------------- | ---------------- |
| commitedAt `String`     | Date and time when the commit was made (ISO 8601 string) |                  |
| committerName `String`  | Name of the person who made the commit                   |                  |
| committerEmail `String` | Email of the committer                                   |                  |

### References

#### Fields with this object

* [{} SbomReference.commit](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-reference)
