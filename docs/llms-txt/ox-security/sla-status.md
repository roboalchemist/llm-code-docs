# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/sla-status.md

# slaStatus

Defines the possible statuses for SLA (Service Level Agreement) compliance of an issue. Indicates the current state of an issue relative to its resolution deadline.

### Examples

```graphql
enum SlaStatus {
  Overdue
  Near
  Within
  Dismissed
  BeforeSlaStartDate
}
```

### Enum values

| Enum value         | Description                                         |
| ------------------ | --------------------------------------------------- |
| Overdue            | Issue has exceeded its SLA resolution deadline      |
| Near               | Issue is approaching its SLA resolution deadline    |
| Within             | Issue is within acceptable SLA resolution timeframe |
| Dismissed          | Issue has been dismissed from SLA tracking          |
| BeforeSlaStartDate | Issue is scheduled for future SLA tracking          |

### References

#### Fields with this object

* [{} SlaData.status](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sla-data)
