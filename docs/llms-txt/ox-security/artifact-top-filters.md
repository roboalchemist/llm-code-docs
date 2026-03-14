# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/artifact-top-filters.md

# artifactTopFilters

Predefined filters for top-level artifact analysis.

### Examples

```graphql
enum ArtifactTopFilters {
  WithHighSeverityIssues
  LastVersion
  DeployedToCloud
}
```

### Enum values

| Enum value             | Description                                   |
| ---------------------- | --------------------------------------------- |
| WithHighSeverityIssues | Show artifacts with high severity issues      |
| LastVersion            | Show only the latest version of each artifact |
| DeployedToCloud        | Show artifacts deployed to cloud environments |

### References

#### Fields with this object

* [{} GetArtifactsInput.artifactTopFilters](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-artifacts-input)
* [{} ArtifactsTopFiltersResponse.name](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifacts-top-filters-response)
