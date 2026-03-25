# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/triage.md

# triage

Triage information for the aggregation.

### Examples

```graphql
type Triage {
  triageStatus: String
  createdBy: String
  createdAt: Date
}
```

### Fields

| Field                 | Description                           | Supported fields |
| --------------------- | ------------------------------------- | ---------------- |
| triageStatus `String` | Triage status of the aggregation      |                  |
| createdBy `String`    | User who triaged the aggregation      |                  |
| createdAt `Date`      | Date when the aggregation was triaged |                  |

### References

#### Fields with this object

* [{} AggItem.triage](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/agg-item)
