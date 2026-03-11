# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue-resource.md

# issueResource

Represents a resource related to an issue.

### Examples

```graphql
type IssueResource {
  id: String
  type: String
}
```

### Fields

| Field         | Description                       | Supported fields |
| ------------- | --------------------------------- | ---------------- |
| id `String`   | Unique identifier of the resource |                  |
| type `String` | Type of the resource              |                  |

### References

#### Fields with this object

* [{} Issue.resource](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
