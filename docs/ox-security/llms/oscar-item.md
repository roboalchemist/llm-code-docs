# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/oscar-item.md

# oscarItem

Information about an Oscar item related to an issue.

### Examples

```graphql
type OscarItem {
  name: String
  description: String
  url: String
  id: String
}
```

### Fields

| Field                | Description                         | Supported fields |
| -------------------- | ----------------------------------- | ---------------- |
| name `String`        | Name of the Oscar item              |                  |
| description `String` | Description of the Oscar item       |                  |
| url `String`         | URL link for the Oscar item         |                  |
| id `String`          | Unique identifier of the Oscar item |                  |

### References

#### Fields with this object

* [{} Issue.oscarData](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
