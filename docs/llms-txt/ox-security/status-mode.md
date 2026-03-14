# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/status-mode.md

# statusMode

Status modes for exclusions indicating their current state.

### Examples

```graphql
enum StatusMode {
  hasComment
  isExpired
  expiresOneWeek
}
```

### Enum values

| Enum value     | Description                           |
| -------------- | ------------------------------------- |
| hasComment     | Exclusion has an associated comment   |
| isExpired      | Exclusion has already expired         |
| expiresOneWeek | Exclusion will expire within one week |

### References

#### Fields with this object

* [{} Exclusion.status](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/exclusion)
