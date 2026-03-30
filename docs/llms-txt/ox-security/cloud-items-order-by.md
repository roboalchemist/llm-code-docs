# Source: https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/inputs/cloud-items-order-by.md

# cloudItemsOrderBy

Defines sorting configuration for cloud security items.

### Examples

```graphql
input CloudItemsOrderBy {
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

* [{} CloudItemsInput.orderBy](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/inputs/cloud-items-input)
