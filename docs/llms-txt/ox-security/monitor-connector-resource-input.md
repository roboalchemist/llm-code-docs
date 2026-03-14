# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/monitor-connector-resource-input.md

# monitorConnectorResourceInput

Configures monitoring settings for resources within a connector.

### Examples

```graphql
input MonitorConnectorResourceInput {
  connectorID: String!
  originalConnectorID: String
  credentialsId: String
  credentialsType: String
  resources: [ResourceInput]
  monitorAllResources: Boolean
  monitorAllNewlyCreatedResources: Float
  featureFlags: JSON
}
```

### Fields

| Field                                                                                                                               | Description                                                                                           | Supported fields                                                                                                                                                                                                     |
| ----------------------------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| connectorID `String!`                                                                                                               | Identifier of the connector to configure                                                              |                                                                                                                                                                                                                      |
| originalConnectorID `String`                                                                                                        | Identifier of the original (aliased) connector for which the update has been initiated                |                                                                                                                                                                                                                      |
| credentialsId `String`                                                                                                              | Authentication credentials identifier for accessing resources                                         |                                                                                                                                                                                                                      |
| credentialsType `String`                                                                                                            | Corresponding credentials type. Only relevant when saving resources from several credentials together |                                                                                                                                                                                                                      |
| resources [`[ResourceInput]`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/resource-input) | List of resources to configure monitoring for                                                         | <p>id <code>String!</code><br>name <code>String!</code><br>isMonitored <code>Boolean!</code><br>resourceType <a href="../enums/resource-type"><code>ResourceType</code></a><br>credentialsId <code>String</code></p> |
| monitorAllResources `Boolean`                                                                                                       | Enables monitoring for all resources, overrides the resources list if set to true                     |                                                                                                                                                                                                                      |
| monitorAllNewlyCreatedResources `Float`                                                                                             | Timestamp from which all new resources will be automatically monitored                                |                                                                                                                                                                                                                      |
| featureFlags `JSON`                                                                                                                 | Object with feature flags passed from FE                                                              |                                                                                                                                                                                                                      |

### References

#### Mutations using this object

* [<\~> monitorConnectorResources.monitorConnectorResourceInput](https://docs.ox.security/api-documentation/api-reference/api--connectors/mutations/monitor-connector-resources)
