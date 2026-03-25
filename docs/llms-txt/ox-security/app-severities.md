# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-severities.md

# appSeverities

Represents severity counts for issues in an application.

### Examples

```graphql
type AppSeverities {
  info: Int
  low: Int
  medium: Int
  high: Int
  critical: Int
  appox: Int
}
```

### Fields

| Field          | Description                                 | Supported fields |
| -------------- | ------------------------------------------- | ---------------- |
| info `Int`     | The number of informational severity issues |                  |
| low `Int`      | The number of low severity issues           |                  |
| medium `Int`   | The number of medium severity issues        |                  |
| high `Int`     | The number of high severity issues          |                  |
| critical `Int` | The number of critical severity issues      |                  |
| appox `Int`    | The number of Appoxalypse severity issues   |                  |

### References

#### Fields with this object

* [{} AppCategories.severities](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-categories)
* [{} DependencyNode.issues](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/dependency-node)
