# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/unscanned-artifact-sort.md

# unscannedArtifactSort

Input parameters for sorting unscanned artifacts.

### Examples

```graphql
input UnscannedArtifactSort {
  field: [UnscannedArtifactsSortByFields]
  order: [Direction]
}
```

### Fields

| Field                                                                                                                                                             | Description                                                     | Supported fields |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | ---------------- |
| field [`[UnscannedArtifactsSortByFields]`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/enums/unscanned-artifacts-sort-by-fields) | Fields to sort unscanned artifacts by                           |                  |
| order [`[Direction]`](https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/direction)                                                  | Sort order for each field, ascending (ASC) or descending (DESC) |                  |

### References

#### Fields with this object

* [{} GetUnscannedArtifactsInput.sort](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/get-unscanned-artifacts-input)
