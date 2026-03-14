# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/orchestrator-item.md

# orchestratorItem

Represents an orchestrator system involved in the application's flow, such as Kubernetes or Docker.

### Examples

```graphql
type OrchestratorItem {
  type: String
  name: String
  hashType: String
  system: String
  hash: String
  size: String
  date: String
  location: [AppFlowItemLocation]
}
```

### Fields

| Field                                                                                                                                              | Description                                                                  | Supported fields                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| type `String`                                                                                                                                      | Type of the orchestrator                                                     |                                                                                                                            |
| name `String`                                                                                                                                      | Name of the orchestrator item                                                |                                                                                                                            |
| hashType `String`                                                                                                                                  | Type of hash used for the orchestrator item                                  |                                                                                                                            |
| system `String`                                                                                                                                    | System associated with the orchestrator item                                 |                                                                                                                            |
| hash `String`                                                                                                                                      | Hash value of the orchestrator item                                          |                                                                                                                            |
| size `String`                                                                                                                                      | Size of the orchestrator item in bytes                                       |                                                                                                                            |
| date `String`                                                                                                                                      | Timestamp indicating when the orchestrator item was created or last modified |                                                                                                                            |
| location [`[AppFlowItemLocation]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-flow-item-location) | Locations where the orchestrator item is deployed or stored                  | <p>runBy <code>String</code><br>foundBy <code>String</code><br>foundIn <code>String</code><br>link <code>String</code></p> |

### References

#### Fields with this object

* [{} ApplicationFlow.orchestrators](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-flow)
