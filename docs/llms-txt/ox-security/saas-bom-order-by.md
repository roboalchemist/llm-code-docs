# Source: https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/inputs/saas-bom-order-by.md

# saasBomOrderBy

Sorting configuration for SaaS BOM items.

### Examples

```graphql
input SaasBomOrderBy {
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

* [{} GetSaasBomItemsInput.orderBy](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/inputs/get-saas-bom-items-input)
