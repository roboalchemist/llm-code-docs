# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/duration-trend-res.md

# durationTrendRes

Trend data showing pipeline execution duration statistics over time.

### Examples

```graphql
type DurationTrendRes {
  jobTriggeredAt: String
  avg: Int
  min: Int
  max: Int
}
```

### Fields

| Field                   | Description                                    | Supported fields |
| ----------------------- | ---------------------------------------------- | ---------------- |
| jobTriggeredAt `String` | Timestamp when the pipeline job was triggered  |                  |
| avg `Int`               | Average pipeline execution duration in seconds |                  |
| min `Int`               | Minimum pipeline execution duration in seconds |                  |
| max `Int`               | Maximum pipeline execution duration in seconds |                  |

### References

#### Queries using this object

* [\<?> getDurationTrend](https://docs.ox.security/api-documentation/api-reference/api--pipeline/queries/get-duration-trend)
