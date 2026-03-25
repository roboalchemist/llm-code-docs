# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/artifact-filters.md

# artifactFilters

### Examples

```graphql
input ArtifactFilters {
  apps: [String]
  artifactType: [String]
  artifactName: [String]
  artifactFullName: [String]
  version: [String]
  sourceType: [String]
  sourceTools: [String]
  registryType: [String]
  registryName: [String]
  cloud: [String]
  cluster: [String]
  namespace: [String]
  cloudDeployments: [String]
  categories: [String]
  issueSeverities: [String]
  reachability: [String]
  artifactIntegrity: [String]
  artifactSha: [String]
  imageSource: [String]
}
```

### Fields

| Field                        | Description                                                  | Supported fields |
| ---------------------------- | ------------------------------------------------------------ | ---------------- |
| apps `[String]`              | Filter by one or more application IDs or names               |                  |
| artifactType `[String]`      | Filter by artifact types                                     |                  |
| artifactName `[String]`      | Filter by artifact names                                     |                  |
| artifactFullName `[String]`  | Filter by full artifact names including version or namespace |                  |
| version `[String]`           | Filter by artifact version strings                           |                  |
| sourceType `[String]`        | Filter by source types                                       |                  |
| sourceTools `[String]`       | Filter by source tools                                       |                  |
| registryType `[String]`      | Filter by types of artifact registries                       |                  |
| registryName `[String]`      | Filter by registry names                                     |                  |
| cloud `[String]`             | Filter by cloud provider or environment names                |                  |
| cluster `[String]`           | Filter by cluster names in cloud environments                |                  |
| namespace `[String]`         | Filter by namespace within a cluster or cloud environment    |                  |
| cloudDeployments `[String]`  | Filter by cloud deployment identifiers or names              |                  |
| categories `[String]`        | Filter by artifact categories or tags                        |                  |
| issueSeverities `[String]`   | Filter by issue severities related to the artifact           |                  |
| reachability `[String]`      | Filter by artifact reachability status                       |                  |
| artifactIntegrity `[String]` | Filter by artifact integrity status or checksums             |                  |
| artifactSha `[String]`       | Filter by SHA identifiers of the artifact                    |                  |
| imageSource `[String]`       |                                                              |                  |

### References

#### Fields with this object

* [{} GetArtifactsInput.filters](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-artifacts-input)
