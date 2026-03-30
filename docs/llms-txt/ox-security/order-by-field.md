# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/order-by-field.md

# orderByField

Available fields for sorting operations in queries.

### Examples

```graphql
enum OrderByField {
  BusinessPriority
  ScoreCreationTime
  AppName
  SecurityPosture
  CategoryViolations
  Severities
  OxInPipeline
  Developers
  LastCodeChange
  Reasons
  Info
  IrrelevantDate
}
```

### Enum values

| Enum value         | Description                             |
| ------------------ | --------------------------------------- |
| BusinessPriority   | Sort by business priority score         |
| ScoreCreationTime  | Sort by score creation timestamp        |
| AppName            | Sort alphabetically by application name |
| SecurityPosture    | Sort by security posture score          |
| CategoryViolations | Sort by number of category violations   |
| Severities         | Sort by severity levels                 |
| OxInPipeline       | Sort by Ox pipeline integration status  |
| Developers         | Sort by number of developers            |
| LastCodeChange     | Sort by last code change timestamp      |
| Reasons            | Sort by reason descriptions             |
| Info               | Sort by informational content           |
| IrrelevantDate     | Sort by irrelevant date                 |

### References

#### Fields with this object

* [{} OrderAppsBy.field](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/order-apps-by)
* [{} OrderBy.field](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/order-by)
