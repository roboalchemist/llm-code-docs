# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/blocked-vs-monitor-trend-res.md

# blockedVsMonitorTrendRes

Trend data showing blocked vs monitor pipeline results over time.

### Examples

```graphql
type BlockedVsMonitorTrendRes {
  jobTriggeredAt: String
  passed: Int
  monitor: Int
  block: Int
  total: Int
}
```

### Fields

| Field                   | Description                                                         | Supported fields |
| ----------------------- | ------------------------------------------------------------------- | ---------------- |
| jobTriggeredAt `String` | Timestamp when the pipeline job was triggered                       |                  |
| passed `Int`            | Number of pipelines that passed security checks                     |                  |
| monitor `Int`           | Number of pipelines in monitor mode (issues found but not blocking) |                  |
| block `Int`             | Number of pipelines blocked due to security issues                  |                  |
| total `Int`             | Total number of pipeline executions                                 |                  |

### References

#### Queries using this object

* [\<?> getBlockedVsMonitorTrend](https://docs.ox.security/api-documentation/api-reference/api--pipeline/queries/get-blocked-vs-monitor-trend)
