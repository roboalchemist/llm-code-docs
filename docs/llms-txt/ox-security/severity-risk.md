# Source: https://docs.ox.security/api-documentation/api-reference/api--sbom/types/enums/severity-risk.md

# severityRisk

Defines risk severity levels for security findings.

### Examples

```graphql
enum SeverityRisk {
  info
  low
  medium
  high
  critical
  appox
}
```

### Enum values

| Enum value | Description                                              |
| ---------- | -------------------------------------------------------- |
| info       | Informational findings that don't pose immediate risk    |
| low        | Low severity findings with minimal security impact       |
| medium     | Medium severity findings requiring attention             |
| high       | High severity findings requiring prompt attention        |
| critical   | Critical severity findings requiring immediate attention |
| appox      | Highest severity findings with catastrophic impact       |

### References

#### Fields with this object

* [{} SbomVulnerableLibrariesResponseItem.name](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/objects/sbom-vulnerable-libraries-response-item)
