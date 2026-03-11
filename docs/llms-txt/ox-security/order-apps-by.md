# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/order-apps-by.md

# orderAppsBy

Sorting configuration for applications, including field, direction, and optional category.

### Examples

```graphql
input OrderAppsBy {
  field: OrderByField
  direction: Direction
  category: String
}
```

### Fields

| Field                                                                                                                        | Description                                      | Supported fields |
| ---------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------ | ---------------- |
| field [`OrderByField`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/order-by-field) | Field to sort by. Default is BusinessPriority    |                  |
| direction [`Direction`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/direction)           | Sorting direction. Default is DESC               |                  |
| category `String`                                                                                                            | Optional category for additional sorting context |                  |

### References

#### Fields with this object

* [{} GetApplicationsInput.orderBy](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/get-applications-input)
