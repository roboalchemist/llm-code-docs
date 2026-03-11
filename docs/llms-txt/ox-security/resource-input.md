# Source: https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/resource-input.md

# resourceInput

Specifies the configuration for a single resource.

### Examples

```graphql
input ResourceInput {
  id: String!
  name: String!
  isMonitored: Boolean!
  resourceType: ResourceType
  credentialsId: String
}
```

### Fields

| Field                                                                                                                             | Description                                                                                         | Supported fields |
| --------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------- | ---------------- |
| id `String!`                                                                                                                      | Unique identifier of the resource                                                                   |                  |
| name `String!`                                                                                                                    | Name of the resource                                                                                |                  |
| isMonitored `Boolean!`                                                                                                            | Determines if the resource is being monitored                                                       |                  |
| resourceType [`ResourceType`](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/enums/resource-type) | Defines the category or classification of the resource                                              |                  |
| credentialsId `String`                                                                                                            | Corresponding credentials ID. Only relevant when saving resources from several credentials together |                  |

### References

#### Fields with this object

* [{} MonitorConnectorResourceInput.resources](https://docs.ox.security/api-documentation/api-reference/api--connectors/types/inputs/monitor-connector-resource-input)
