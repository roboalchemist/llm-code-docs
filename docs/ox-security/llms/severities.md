# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/severities.md

# severities

Represents the count of issues categorized by severity levels within a specific context.

### Examples

```graphql
type Severities {
  info: Int
  low: Int
  medium: Int
  high: Int
  critical: Int
  appox: Int
}
```

### Fields

| Field          | Description                            | Supported fields |
| -------------- | -------------------------------------- | ---------------- |
| info `Int`     | Count of informational severity issues |                  |
| low `Int`      | Count of low severity issues           |                  |
| medium `Int`   | Count of medium severity issues        |                  |
| high `Int`     | Count of high severity issues          |                  |
| critical `Int` | Count of critical severity issues      |                  |
| appox `Int`    | Count of appoxalypse severity issues   |                  |

### References

#### Fields with this object

* [{} Application.issuesBySeverity](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)
* [{} ArtifactCategories.severities](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-categories)
* [{} ArtifactInfo.totalIssuesBySeverity](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-info)
* [{} IssueSeverityBreakdown.severities](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/issue-severity-breakdown)
* [{} ApiSecurityItem.issuesBySeverity](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/objects/api-security-item)
* [{} SaasBomItem.issuesBySeverity](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/objects/saas-bom-item)
* [{} CloudItem.relatedIssues](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item)
* [{} CloudIssueSeverityBreakdown.severities](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-issue-severity-breakdown)
