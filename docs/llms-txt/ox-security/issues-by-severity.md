# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issues-by-severity.md

# issuesBySeverity

Security issues breakdown by severity levels.

### Examples

```graphql
type IssuesBySeverity {
  appox: Int
  critical: Int
  high: Int
  medium: Int
  low: Int
  info: Int
}
```

### Fields

| Field          | Description                                     | Supported fields |
| -------------- | ----------------------------------------------- | ---------------- |
| appox `Int`    | Count of issues with Appoxalypse severity level |                  |
| critical `Int` | Count of critical severity issues               |                  |
| high `Int`     | Count of high severity issues                   |                  |
| medium `Int`   | Count of medium severity issues                 |                  |
| low `Int`      | Count of low severity issues                    |                  |
| info `Int`     | Count of informational severity issues          |                  |

### References

#### Fields with this object

* [{} SbomLib.vulnerabilityCounts](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-lib)
* [{} PipelineSummary.issues](https://docs.ox.security/api-documentation/api-reference/api--pipeline/types/objects/pipeline-summary)
