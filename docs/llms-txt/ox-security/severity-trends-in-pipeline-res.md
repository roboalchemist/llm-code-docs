# Source: https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/severity-trends-in-pipeline-res.md

# severityTrendsInPipelineRes

Trend data showing severity distribution over time in pipelines.

### Examples

```graphql
type SeverityTrendsInPipelineRes {
  jobTriggeredAt: String
  info: Int
  low: Int
  medium: Int
  high: Int
  critical: Int
  appox: Int
}
```

### Fields

| Field                   | Description                                   | Supported fields |
| ----------------------- | --------------------------------------------- | ---------------- |
| jobTriggeredAt `String` | Timestamp when the pipeline job was triggered |                  |
| info `Int`              | Number of informational severity issues found |                  |
| low `Int`               | Number of low severity issues found           |                  |
| medium `Int`            | Number of medium severity issues found        |                  |
| high `Int`              | Number of high severity issues found          |                  |
| critical `Int`          | Number of critical severity issues found      |                  |
| appox `Int`             | Number of appoxalypse severity issues found   |                  |

### References

#### Queries using this object

* [\<?> getSeverityTrendsInPipeline](https://docs.ox.security/api-documentation/api-reference/api--pipeline/queries/get-severity-trends-in-pipeline)
