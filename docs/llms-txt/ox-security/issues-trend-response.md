# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issues-trend-response.md

# issuesTrendResponse

### Examples

```graphql
type IssuesTrendResponse {
  scanId: String
  scanDate: Float
  info: Int
  low: Int
  medium: Int
  high: Int
  critical: Int
  appox: Int
}
```

### Fields

| Field            | Description | Supported fields |
| ---------------- | ----------- | ---------------- |
| scanId `String`  |             |                  |
| scanDate `Float` |             |                  |
| info `Int`       |             |                  |
| low `Int`        |             |                  |
| medium `Int`     |             |                  |
| high `Int`       |             |                  |
| critical `Int`   |             |                  |
| appox `Int`      |             |                  |

### References

#### Queries using this object

* [\<?> getIssuesTrendData](https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-issues-trend-data)
