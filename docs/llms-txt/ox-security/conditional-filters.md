# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/conditional-filters.md

# conditionalFilters

### Examples

```graphql
input ConditionalFilters {
  condition: ConditionType
  fieldName: FilterTypes
  values: [String]
  greaterThan: Float
  lessThan: Float
}
```

### Fields

| Field                                                                                                                             | Description                                                                              | Supported fields |
| --------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------- | ---------------- |
| condition [`ConditionType`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/condition-type) | NOT condition type can be used to exclude filter values                                  |                  |
| fieldName [`FilterTypes`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/filter-types)     | The field to apply the filter on                                                         |                  |
| values `[String]`                                                                                                                 | List of string values to filter by, depending on the condition                           |                  |
| greaterThan `Float`                                                                                                               | Lower bound value for BETWEEN condition (exclusive or inclusive based on implementation) |                  |
| lessThan `Float`                                                                                                                  | Upper bound value for BETWEEN condition (exclusive or inclusive based on implementation) |                  |

### References

#### Fields with this object

* [{} GetApplicationsInput.conditionalFilters](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/get-applications-input)
* [{} IssuesInput.conditionalFilters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-input)
* [{} GetIssuesConditionalFiltersInput.conditionalFilters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/get-issues-conditional-filters-input)
* [{} GetSbomInput.conditionalFilters](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/get-sbom-input)
* [{} ResolvedIssuesInput.conditionalFilters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/resolved-issues-input)
* [{} ResolvedIssuesV2Input.conditionalFilters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/resolved-issues-v2input)
* [{} DisappearedIssuesInput.conditionalFilters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/disappeared-issues-input)
* [{} CICDIssuesInput.conditionalFilters](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issues-input)
* [{} GetArtifactsV2Input.conditionalFilters](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-artifacts-v2input)
