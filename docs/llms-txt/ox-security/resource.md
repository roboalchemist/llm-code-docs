# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/resource.md

# resource

Detailed information about a resource that can be monitored.

### Examples

```graphql
type Resource {
  id: String
  name: String
  resourceOrgName: String
  isMonitored: Boolean
  resourceType: ResourceType
  children: [Resource]
  iconName: ResourceIcon
  settingsAvailable: Boolean
  credentialsId: String
}
```

### Fields

| Field                                                                                                                             | Description                                                                                         | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                          |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| id `String`                                                                                                                       | Unique identifier of the resource                                                                   |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| name `String`                                                                                                                     | Display name of the resource                                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| resourceOrgName `String`                                                                                                          | Organization name where the resource belongs                                                        |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| isMonitored `Boolean`                                                                                                             | Indicates if this resource is currently being monitored                                             |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| resourceType [`ResourceType`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/enums/resource-type) | Classification of the resource (node, edge)                                                         |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| children [`[Resource]`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/resource)          | Nested resources associated with this resource                                                      | <p>id <code>String</code><br>name <code>String</code><br>resourceOrgName <code>String</code><br>isMonitored <code>Boolean</code><br>resourceType <a href="../enums/resource-type"><code>ResourceType</code></a><br>children <a href="resource"><code>\[Resource]</code></a><br>iconName <a href="../enums/resource-icon"><code>ResourceIcon</code></a><br>settingsAvailable <code>Boolean</code><br>credentialsId <code>String</code></p> |
| iconName [`ResourceIcon`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/enums/resource-icon)     | Icon identifier for visual representation                                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| settingsAvailable `Boolean`                                                                                                       | Indicates if resource-specific settings can be configured                                           |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| credentialsId `String`                                                                                                            | Corresponding credentials ID. Only relevant when saving resources from several credentials together |                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### References

#### Fields with this object

* [{} ConnectorResourceResponse.resources](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector-resource-response)
* [{} Resource.children](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/resource)
