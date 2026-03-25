# Source: https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/inputs/get-saas-bom-items-input.md

# getSaasBomItemsInput

Input parameters for retrieving and filtering SaaS BOM items.

### Examples

```graphql
input GetSaasBomItemsInput {
  scanId: String
  offset: Int
  limit: Int
  owners: [String]
  tagIds: [String]
  filters: SaasBomFilters
  filterSearch: [AutoCompleteSearch]
  openItems: [FilterTypes]
  orderBy: SaasBomOrderBy
  search: String
}
```

### Fields

| Field                                                                                                                                              | Description                                    | Supported fields                                                                                                                                                                      |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| scanId `String`                                                                                                                                    | ID of the specific scan to retrieve items from |                                                                                                                                                                                       |
| offset `Int`                                                                                                                                       | Number of items to skip for pagination         |                                                                                                                                                                                       |
| limit `Int`                                                                                                                                        | Maximum number of items to return              |                                                                                                                                                                                       |
| owners `[String]`                                                                                                                                  | Filter by application owners                   |                                                                                                                                                                                       |
| tagIds `[String]`                                                                                                                                  | Filter by tag identifiers                      |                                                                                                                                                                                       |
| filters [`SaasBomFilters`](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/inputs/saas-bom-filters)                  | Complex filters for detailed item filtering    | <p>apps <code>\[String]</code><br>categories <code>\[String]</code><br>name <code>\[String]</code><br>reachability <code>\[String]</code><br>detectionType <code>\[String]</code></p> |
| filterSearch [`[AutoCompleteSearch]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/inputs/auto-complete-search) | Autocomplete search criteria                   | <p>fieldName <code>String</code><br>value <code>\[String]</code></p>                                                                                                                  |
| openItems [`[FilterTypes]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/enums/filter-types)                    | Filter by open item types                      |                                                                                                                                                                                       |
| orderBy [`SaasBomOrderBy`](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/inputs/saas-bom-order-by)                 | Sorting criteria for the results               | <p>field <code>String</code><br>direction <a href="../../../api--audit/types/enums/direction"><code>Direction</code></a></p>                                                          |
| search `String`                                                                                                                                    | Text search query to filter items              |                                                                                                                                                                                       |

### References

#### Queries using this object

* [\<?> getSaasBomItems.getSaasBomItemsInput](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/queries/get-saas-bom-items)
