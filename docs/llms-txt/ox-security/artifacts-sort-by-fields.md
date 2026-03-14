# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/artifacts-sort-by-fields.md

# artifactsSortByFields

Fields available for sorting artifacts in result sets.

### Examples

```graphql
enum ArtifactsSortByFields {
  AppName
  ArtifactType
  ArtifactName
  Version
  BusinessPriority
  Created
  CreatedBy
  Code
  CICDType
  RegistryType
}
```

### Enum values

| Enum value       | Description                  |
| ---------------- | ---------------------------- |
| AppName          | Sort by application name     |
| ArtifactType     | Sort by artifact type        |
| ArtifactName     | Sort by artifact name        |
| Version          | Sort by version number       |
| BusinessPriority | Sort by business priority    |
| Created          | Sort by creation date        |
| CreatedBy        | Sort by creator              |
| Code             | Sort by code characteristics |
| CICDType         | Sort by CI/CD type           |
| RegistryType     | Sort by registry type        |

### References

#### Fields with this object

* [{} ArtifactsSort.field](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/artifacts-sort)
