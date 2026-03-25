# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/objects/audit-log-count.md

# auditLogCount

Count of audit log entries matching specified criteria.

### Examples

```graphql
type AuditLogCount {
  count: Float
}
```

### Fields

| Field         | Description                                | Supported fields |
| ------------- | ------------------------------------------ | ---------------- |
| count `Float` | Total number of matching audit log entries |                  |

### References

#### Queries using this object

* [\<?> getLogsCount](https://docs.ox.security/api-documentation/api-reference/api--audit/queries/get-logs-count)
