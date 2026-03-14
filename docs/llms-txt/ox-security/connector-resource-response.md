# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/connector-resource-response.md

# connectorResourceResponse

Response containing information about connector resources and monitoring status.

### Examples

```graphql
type ConnectorResourceResponse {
  resources: [Resource]
  monitorAllNewlyCreatedResources: Boolean
  total: Int
  selected: Int
}
```

### Fields

| Field                                                                                                                     | Description                                                            | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                          |
| ------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| resources [`[Resource]`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/objects/resource) | List of resources that are available and their monitoring status       | <p>id <code>String</code><br>name <code>String</code><br>resourceOrgName <code>String</code><br>isMonitored <code>Boolean</code><br>resourceType <a href="../enums/resource-type"><code>ResourceType</code></a><br>children <a href="resource"><code>\[Resource]</code></a><br>iconName <a href="../enums/resource-icon"><code>ResourceIcon</code></a><br>settingsAvailable <code>Boolean</code><br>credentialsId <code>String</code></p> |
| monitorAllNewlyCreatedResources `Boolean`                                                                                 | Indicates if newly created resources should be automatically monitored |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| total `Int`                                                                                                               | Total number of available resources                                    |                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| selected `Int`                                                                                                            | Number of selected (monitored) resources                               |                                                                                                                                                                                                                                                                                                                                                                                                                                           |

### References

#### Queries using this object

* [\<?> getConnectorResources](https://docs.ox.security/api-documentation/api-reference/api--connectors/queries/get-connector-resources)
