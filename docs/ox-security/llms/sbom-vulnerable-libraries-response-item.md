# Source: https://docs.ox.security/api-documentation/api-reference/api--sbom/types/objects/sbom-vulnerable-libraries-response-item.md

# sbomVulnerableLibrariesResponseItem

Represents individual vulnerable library count by severity.

### Examples

```graphql
type SbomVulnerableLibrariesResponseItem {
  name: SeverityRisk!
  count: Int!
}
```

### Fields

| Field                                                                                                                | Description                                                     | Supported fields |
| -------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------- |
| name [`SeverityRisk!`](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/enums/severity-risk) | Severity level of the vulnerabilities                           |                  |
| count `Int!`                                                                                                         | Number of libraries with vulnerabilities at this severity level |                  |

### References

#### Fields with this object

* [{} SbomVulnerableLibrariesResponse.data](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/objects/sbom-vulnerable-libraries-response)
