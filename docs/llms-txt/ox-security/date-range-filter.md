# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/date-range-filter.md

# dateRangeFilter

Date range filter for time-based queries.

### Examples

```graphql
input DateRangeFilter {
  from: Float
  to: Float
}
```

### Fields

| Field        | Description                 | Supported fields |
| ------------ | --------------------------- | ---------------- |
| from `Float` | Start timestamp (UTC epoch) |                  |
| to `Float`   | End timestamp (UTC epoch)   |                  |

### References

#### Fields with this object

* [{} FetchDashboardInput.dateRange](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/fetch-dashboard-input)
