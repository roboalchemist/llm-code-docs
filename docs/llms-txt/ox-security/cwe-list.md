# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/cwe-list.md

# cweList

Basic information about a CWE (Common Weakness Enumeration) list entry.

### Examples

```graphql
type CweList {
  name: String
  description: String
  url: String
}
```

### Fields

| Field                | Description                                       | Supported fields |
| -------------------- | ------------------------------------------------- | ---------------- |
| name `String`        | Name of the CWE                                   |                  |
| description `String` | Description of the CWE                            |                  |
| url `String`         | URL linking to detailed information about the CWE |                  |

### References

#### Fields with this object

* [{} Issue.cweList](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
