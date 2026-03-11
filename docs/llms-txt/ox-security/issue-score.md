# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue-score.md

# issueScore

Represents a score assigned to an issue, along with optional comments.

### Examples

```graphql
type IssueScore {
  value: Float
  comments: String
}
```

### Fields

| Field             | Description                            | Supported fields |
| ----------------- | -------------------------------------- | ---------------- |
| value `Float`     | Numerical value of the score           |                  |
| comments `String` | Comments or notes related to the score |                  |

### References

#### Fields with this object

* [{} Issue.score](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
