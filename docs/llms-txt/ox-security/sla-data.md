# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sla-data.md

# slaData

Data object representing SLA information, including status, days past the SLA, and any custom SLA settings.

### Examples

```graphql
type SlaData {
  daysPastSLA: Float
  status: SlaStatus
}
```

### Fields

| Field                                                                                                            | Description                          | Supported fields |
| ---------------------------------------------------------------------------------------------------------------- | ------------------------------------ | ---------------- |
| daysPastSLA `Float`                                                                                              | Number of days past the SLA due date |                  |
| status [`SlaStatus`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/sla-status) | Current SLA status                   |                  |

### References

#### Fields with this object

* [{} Issue.sla](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
