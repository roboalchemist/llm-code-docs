# Source: https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/enums/exclusion-mode.md

# exclusionMode

Mode of operation for exclusions.

### Examples

```graphql
enum ExclusionMode {
  fullScan
  pipelineScan
}
```

### Enum values

| Enum value   | Description                                             |
| ------------ | ------------------------------------------------------- |
| fullScan     | Full scan mode - applies to complete scans              |
| pipelineScan | Pipeline scan mode - applies to CI/CD pipeline scanning |

### References

#### Fields with this object

* [{} ExclusionsFilters.exclusionMode](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclusions-filters)
* [{} Exclusion.exclusionMode](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/objects/exclusion)
* [{} ExcludeAlertInput.exclusionMode](https://docs.ox.security/api-documentation/api-reference/api--exclusions/types/inputs/exclude-alert-input)
