# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/artifacts-sort.md

# artifactsSort

### Examples

```graphql
input ArtifactsSort {
  field: [ArtifactsSortByFields]
  order: [Direction]
}
```

### Fields

| Field                                                                                                                                          | Description                                                                      | Supported fields |
| ---------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------- | ---------------- |
| field [`[ArtifactsSortByFields]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/artifacts-sort-by-fields) | Fields to sort artifacts by. Default is Created                                  |                  |
| order [`[Direction]`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/direction)                               | Sort order for each field, ascending (ASC) or descending (DESC). Default is DESC |                  |

### References

#### Fields with this object

* [{} GetArtifactsInput.sort](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-artifacts-input)
* [{} GetArtifactsV2Input.sort](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-artifacts-v2input)
