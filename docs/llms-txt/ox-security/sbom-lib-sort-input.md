# Source: https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/sbom-lib-sort-input.md

# sbomLibSortInput

Specifies sorting configuration for SBOM libraries.

### Examples

```graphql
input SbomLibSortInput {
  fields: [SbomLibSortFields]
  order: [Direction]
}
```

### Fields

| Field                                                                                                                               | Description                                         | Supported fields |
| ----------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------- | ---------------- |
| fields [`[SbomLibSortFields]`](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/enums/sbom-lib-sort-fields) | Fields to sort by                                   |                  |
| order [`[Direction]`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/direction)                    | Sort order for each field (ascending or descending) |                  |

### References

#### Fields with this object

* [{} GetApplicationsSbom.sort](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/get-applications-sbom)
* [{} GetSbomInput.sort](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/get-sbom-input)
