# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/system-filter.md

# systemFilter

System-level filter configuration for targeting specific system types and their configurations in application queries.

### Examples

```graphql
input SystemFilter {
  name: AppSystemsTypes
  type: String
}
```

### Fields

| Field                                                                                                                             | Description                                 | Supported fields |
| --------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ---------------- |
| name [`AppSystemsTypes`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/app-systems-types) | Type of system to filter by                 |                  |
| type `String`                                                                                                                     | Specific system implementation to filter by |                  |

### References

#### Fields with this object

* [{} GetApplicationsInput.systemFilter](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/get-applications-input)
