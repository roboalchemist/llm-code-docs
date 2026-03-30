# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/expired-at-filter.md

# expiredAtFilter

Filter for exclusion expiry dates.

### Examples

```graphql
input ExpiredAtFilter {
  gte: DateTime
  lte: DateTime
}
```

### Fields

| Field          | Description                                     | Supported fields |
| -------------- | ----------------------------------------------- | ---------------- |
| gte `DateTime` | Filter for exclusions expiring after this date  |                  |
| lte `DateTime` | Filter for exclusions expiring before this date |                  |

### References

#### Fields with this object

* [{} ExclusionsFilters.expiredAt](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclusions-filters)
