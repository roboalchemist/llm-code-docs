# Source: https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/inputs/saas-bom-filters.md

# saasBomFilters

Filtering options for SaaS BOM items based on various attributes.

### Examples

```graphql
input SaasBomFilters {
  apps: [String]
  categories: [String]
  name: [String]
  reachability: [String]
  detectionType: [String]
}
```

### Fields

| Field                    | Description                                | Supported fields |
| ------------------------ | ------------------------------------------ | ---------------- |
| apps `[String]`          | Filter by specific applications            |                  |
| categories `[String]`    | Filter by business categories              |                  |
| name `[String]`          | Filter by item names                       |                  |
| reachability `[String]`  | Filter by application reachability status  |                  |
| detectionType `[String]` | Filter by how the application was detected |                  |

### References

#### Fields with this object

* [{} GetSaasBomItemsInput.filters](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/inputs/get-saas-bom-items-input)
