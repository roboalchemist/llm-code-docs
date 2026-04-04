# Source: https://docs.ox.security/api-documentation/api-reference/api--audit/types/enums/direction.md

# direction

Sort direction for ordering results.

### Examples

```graphql
enum Direction {
  ASC
  DESC
}
```

### Enum values

| Enum value | Description                                         |
| ---------- | --------------------------------------------------- |
| ASC        | Sort in ascending order (A to Z, oldest to newest)  |
| DESC       | Sort in descending order (Z to A, newest to oldest) |

### References

#### Fields with this object

* [{} LogOrderBy.direction](https://docs.ox.security/api-documentation/api-reference/api--audit/types/inputs/log-order-by)
* [{} OrderAppsBy.direction](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/order-apps-by)
* [{} IssuesSort.order](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-sort)
* [{} OrderBy.direction](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/order-by)
* [{} SbomLibSortInput.order](https://docs.ox.security/api-documentation/api-reference/api--sbom/types/inputs/sbom-lib-sort-input)
* [{} RIssuesSort.order](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/r-issues-sort)
* [{} DIssuesSort.order](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/d-issues-sort)
* [{} CICDIssuesSort.order](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issues-sort)
* [{} ArtifactsSort.order](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/artifacts-sort)
* [{} UnscannedArtifactSort.order](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/inputs/unscanned-artifact-sort)
* [{} ApiSecurityOrderBy.direction](https://docs.ox.security/api-documentation/api-reference/api--api-security/types/inputs/api-security-order-by)
* [{} SaasBomOrderBy.direction](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/inputs/saas-bom-order-by)
* [{} CloudItemsOrderBy.direction](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/inputs/cloud-items-order-by)
