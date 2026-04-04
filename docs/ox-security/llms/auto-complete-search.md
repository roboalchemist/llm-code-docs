# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/auto-complete-search.md

# autoCompleteSearch

Input structure for performing autocomplete searches based on specific fields and values.

### Examples

```graphql
input AutoCompleteSearch {
  fieldName: String
  value: [String]
}
```

### Fields

| Field              | Description                                               | Supported fields |
| ------------------ | --------------------------------------------------------- | ---------------- |
| fieldName `String` | The name of the field to search within                    |                  |
| value `[String]`   | A list of values to search for within the specified field |                  |

### References

#### Fields with this object

* [{} GetApplicationsInput.filterSearch](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/get-applications-input)
* [{} IssuesInput.search](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-input)
* [{} GetIssuesConditionalFiltersInput.search](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/get-issues-conditional-filters-input)
* [{} GetApplicationsSbom.sbomSearch](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/get-applications-sbom)
* [{} ResolvedIssuesInput.search](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/resolved-issues-input)
* [{} ResolvedIssuesV2Input.search](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/resolved-issues-v2input)
* [{} DisappearedIssuesInput.search](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/disappeared-issues-input)
* [{} CICDIssuesInput.search](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issues-input)
* [{} GetApiSecurityInput.filterSearch](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/inputs/get-api-security-input)
* [{} GetSaasBomItemsInput.filterSearch](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/inputs/get-saas-bom-items-input)
* [{} CloudItemsInput.filterSearch](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/inputs/cloud-items-input)
