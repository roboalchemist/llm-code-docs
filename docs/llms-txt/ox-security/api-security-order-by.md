# Source: https://docs.ox.security/api-documentation/api-reference/api--api-security/types/inputs/api-security-order-by.md

# apiSecurityOrderBy

Sorting configuration for API security items.

### Examples

```graphql
input ApiSecurityOrderBy {
  field: String
  direction: Direction
}
```

### Fields

| Field                                                                                                              | Description                              | Supported fields |
| ------------------------------------------------------------------------------------------------------------------ | ---------------------------------------- | ---------------- |
| field `String`                                                                                                     | Field name to sort by                    |                  |
| direction [`Direction`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/direction) | Sort direction (ascending or descending) |                  |

### References

#### Fields with this object

* [{} GetApiSecurityInput.orderBy](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/inputs/get-api-security-input)
