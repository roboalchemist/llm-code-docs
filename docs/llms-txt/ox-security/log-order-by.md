# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/inputs/log-order-by.md

# logOrderBy

Specifies the sorting criteria for audit logs.

### Examples

```graphql
input LogOrderBy {
  field: String
  direction: Direction
}
```

### Fields

| Field                                                                                                              | Description          | Supported fields |
| ------------------------------------------------------------------------------------------------------------------ | -------------------- | ---------------- |
| field `String`                                                                                                     | The field to sort by |                  |
| direction [`Direction`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/direction) | The sort direction   |                  |

### References

#### Fields with this object

* [{} GetLogsInput.orderBy](https://docs.ox.security/api-documentation/api-reference/api--audit/types/inputs/get-logs-input)
