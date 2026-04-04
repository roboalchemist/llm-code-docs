# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/order-by.md

# orderBy

Sorting configuration specifying field and direction.

### Examples

```graphql
input OrderBy {
  field: OrderByField
  direction: Direction
}
```

### Fields

| Field                                                                                                                        | Description                             | Supported fields |
| ---------------------------------------------------------------------------------------------------------------------------- | --------------------------------------- | ---------------- |
| field [`OrderByField`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/order-by-field) | Field to sort by                        |                  |
| direction [`Direction`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/direction)           | Sorting direction (default: descending) |                  |

### References

#### Fields with this object

* [{} FetchDashboardInput.orderBy](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/fetch-dashboard-input)
