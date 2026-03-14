# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/exclusion-scope.md

# exclusionScope

Scope of application for an exclusion.

### Examples

```graphql
enum ExclusionScope {
  issue
  aggItem
  scaVulnerabilities
  application
  allApplications
  global
  cveAndLibrary
}
```

### Enum values

| Enum value         | Description                           |
| ------------------ | ------------------------------------- |
| issue              | Applies to specific issues            |
| aggItem            | Applies to aggregated items           |
| scaVulnerabilities |                                       |
| application        | Applies to specific applications      |
| allApplications    | Applies to all applications           |
| global             | Applies globally across all resources |
| cveAndLibrary      |                                       |

### References

#### Fields with this object

* [{} Exclusion.exclusionScope](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/exclusion)
