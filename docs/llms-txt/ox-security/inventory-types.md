# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/inventory-types.md

# inventoryTypes

Types of inventory items that can be analyzed in the system.

### Examples

```graphql
enum InventoryTypes {
  New
  InDevelopment
  DeployedProd
  ExternallyFacing
}
```

### Enum values

| Enum value       | Description                                       |
| ---------------- | ------------------------------------------------- |
| New              | Recently added items requiring initial assessment |
| InDevelopment    | Items currently in the development phase          |
| DeployedProd     | Items deployed to production environments         |
| ExternallyFacing | Items accessible from external networks           |

### References

#### Fields with this object

* [{} IssuesInput.inventoryFilters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/issues-input)
* [{} GetIssuesConditionalFiltersInput.inventoryFilters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/get-issues-conditional-filters-input)
* [{} FetchDashboardInput.filters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/fetch-dashboard-input)
* [{} ResolvedIssuesInput.inventoryFilters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/resolved-issues-input)
* [{} DisappearedIssuesInput.inventoryFilters](https://docs.ox.security/api-documentation/api-reference/api--issue/types/inputs/disappeared-issues-input)
* [{} CICDIssuesInput.inventoryFilters](https://docs.ox.security/api-documentation/api-reference/api--cicd-issue/types/inputs/cicd-issues-input)
