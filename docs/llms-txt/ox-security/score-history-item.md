# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/score-history-item.md

# scoreHistoryItem

Historical data point tracking an application's security risk score over time.

### Examples

```graphql
type ScoreHistoryItem {
  appId: String
  appName: String
  score: Float
  date: Float
  new: Boolean
  updated: Boolean
  scanId: String
}
```

### Fields

| Field             | Description                                | Supported fields |
| ----------------- | ------------------------------------------ | ---------------- |
| appId `String`    | Application identifier                     |                  |
| appName `String`  | Application name                           |                  |
| score `Float`     | Security risk score at this point in time  |                  |
| date `Float`      | Timestamp when this score was recorded     |                  |
| new `Boolean`     | Indicates if this is a new score entry     |                  |
| updated `Boolean` | Indicates if this score was updated        |                  |
| scanId `String`   | Scan identifier associated with this score |                  |

### References

#### Fields with this object

* [{} Application.scoreHistory](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)
