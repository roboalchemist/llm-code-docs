# Source: https://docs.ox.security/api-documentation/api-reference/api--sbom/types/objects/sbom-vulnerable-libraries-response.md

# sbomVulnerableLibrariesResponse

Describes response with vulnerable libraries breakdown by severity.

### Examples

```graphql
type SbomVulnerableLibrariesResponse {
  data: [SbomVulnerableLibrariesResponseItem]!
}
```

### Fields

| Field                                                                                                                                                                     | Description                                            | Supported fields                                                                                       |
| ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------ | ------------------------------------------------------------------------------------------------------ |
| data [`[SbomVulnerableLibrariesResponseItem]!`](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/objects/sbom-vulnerable-libraries-response-item) | List of vulnerability counts grouped by severity level | <p>name <a href="../enums/severity-risk"><code>SeverityRisk!</code></a><br>count <code>Int!</code></p> |

### References

#### Queries using this object

* [\<?> getSbomVulnerableLibraries](https://docs.ox.security/api-documentation/api-reference/api--sbom/queries/get-sbom-vulnerable-libraries)
