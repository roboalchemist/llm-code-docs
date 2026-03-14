# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/inputs/log-date-range.md

# logDateRange

Specifies a time range for filtering audit logs.

### Examples

```graphql
input LogDateRange {
  from: DateTime
  to: DateTime
}
```

### Fields

| Field           | Description                         | Supported fields |
| --------------- | ----------------------------------- | ---------------- |
| from `DateTime` | Start date of the range (inclusive) |                  |
| to `DateTime`   | End date of the range (inclusive)   |                  |

### References

#### Fields with this object

* [{} GetLogsInput.dateRange](https://docs.ox.security/api-documentation/api-reference/api--audit/types/inputs/get-logs-input)
