# Source: https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/app-info.md

# appInfo

Represents basic application information associated with cloud resources.

### Examples

```graphql
type AppInfo {
  id: String
  name: String
  type: String
}
```

### Fields

| Field         | Description            | Supported fields |
| ------------- | ---------------------- | ---------------- |
| id `String`   | Application identifier |                  |
| name `String` | Application name       |                  |
| type `String` | Application type       |                  |

### References

#### Fields with this object

* [{} CloudItem.applications](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item)
