# Source: https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/objects/saas-bom-item.md

# saasBomItem

Represents a SaaS application entry in the Bill of Materials with its associated metadata and security information.

### Examples

```graphql
type SaasBomItem {
  id: String
  appId: String
  appName: String
  appType: String
  name: String
  link: String
  category: String
  createdAt: Date
  extraInfo: [ApplicationExtraInfo]
  issuesBySeverity: Severities
}
```

### Fields

| Field                                                                                                                                                | Description                                               | Supported fields                                                                                                                                                             |
| ---------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id `String`                                                                                                                                          | Unique identifier of the SaaS BOM item                    |                                                                                                                                                                              |
| appId `String`                                                                                                                                       | Unique identifier of the application                      |                                                                                                                                                                              |
| appName `String`                                                                                                                                     | Name of the application                                   |                                                                                                                                                                              |
| appType `String`                                                                                                                                     | Type/category of the application                          |                                                                                                                                                                              |
| name `String`                                                                                                                                        | Display name of the SaaS BOM item                         |                                                                                                                                                                              |
| link `String`                                                                                                                                        | URL or reference link to the application                  |                                                                                                                                                                              |
| category `String`                                                                                                                                    | Business category of the application                      |                                                                                                                                                                              |
| createdAt `Date`                                                                                                                                     | Timestamp when the item was created                       |                                                                                                                                                                              |
| extraInfo [`[ApplicationExtraInfo]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-extra-info) | Additional metadata and information about the application | <p>key <code>String</code><br>link <code>String</code><br>snippet <a href="../../../api--application/types/objects/extra-info-snippet"><code>ExtraInfoSnippet</code></a></p> |
| issuesBySeverity [`Severities`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/severities)                  | Security issues grouped by severity levels                | <p>info <code>Int</code><br>low <code>Int</code><br>medium <code>Int</code><br>high <code>Int</code><br>critical <code>Int</code><br>appox <code>Int</code></p>              |

### References

#### Fields with this object

* [{} SaasBomItemsResponse.saasBomItems](https://docs.ox.security/api-documentation/api-reference/api--saas-sbom/types/objects/saas-bom-items-response)
