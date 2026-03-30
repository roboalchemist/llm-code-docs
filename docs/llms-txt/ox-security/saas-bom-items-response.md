# Source: https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/objects/saas-bom-items-response.md

# saasBomItemsResponse

Response type containing a list of SaaS BOM (Software Bill of Materials) items along with pagination information.

### Examples

```graphql
type SaasBomItemsResponse {
  saasBomItems: [SaasBomItem]
  total: Int
  totalFiltered: Int
}
```

### Fields

| Field                                                                                                                               | Description                                          | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ----------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| saasBomItems [`[SaasBomItem]`](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/objects/saas-bom-item) | List of SaaS BOM items matching the query criteria   | <p>id <code>String</code><br>appId <code>String</code><br>appName <code>String</code><br>appType <code>String</code><br>name <code>String</code><br>link <code>String</code><br>category <code>String</code><br>createdAt <code>Date</code><br>extraInfo <a href="../../../api--application/types/objects/application-extra-info"><code>\[ApplicationExtraInfo]</code></a><br>issuesBySeverity <a href="../../../api--application/types/objects/severities"><code>Severities</code></a></p> |
| total `Int`                                                                                                                         | Total number of items in the system                  |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| totalFiltered `Int`                                                                                                                 | Number of items matching the current filter criteria |                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |

### References

#### Queries using this object

* [\<?> getSaasBomItems](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/queries/get-saas-bom-items)
