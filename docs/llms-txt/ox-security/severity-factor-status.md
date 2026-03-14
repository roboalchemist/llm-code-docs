# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/severity-factor-status.md

# severityFactorStatus

Status of severity factor changes.

### Examples

```graphql
enum SeverityFactorStatus {
  new
  increased
  decreased
  removed
}
```

### Enum values

| Enum value | Description                                 |
| ---------- | ------------------------------------------- |
| new        | A new severity factor has been identified   |
| increased  | The severity factor has increased in impact |
| decreased  | The severity factor has decreased in impact |
| removed    | The severity factor is no longer applicable |

### References

#### Fields with this object

* [{} SeverityFactorsDiff.status](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/severity-factors-diff)
