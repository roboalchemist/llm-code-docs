# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/kubernetes-item.md

# kubernetesItem

Represents a Kubernetes resource associated with the application, including its type, hash, and location.

### Examples

```graphql
type KubernetesItem {
  type: String
  name: String
  hashType: String
  system: String
  hash: String
  subType: String
  size: String
  date: String
  location: [AppFlowItemLocation]
}
```

### Fields

| Field                                                                                                                                              | Description                                                                    | Supported fields                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------- |
| type `String`                                                                                                                                      | Type of the Kubernetes resource                                                |                                                                                                                            |
| name `String`                                                                                                                                      | Name of the Kubernetes resource                                                |                                                                                                                            |
| hashType `String`                                                                                                                                  | Type of hash used for the Kubernetes resource                                  |                                                                                                                            |
| system `String`                                                                                                                                    | System associated with the Kubernetes resource                                 |                                                                                                                            |
| hash `String`                                                                                                                                      | Hash value of the Kubernetes resource                                          |                                                                                                                            |
| subType `String`                                                                                                                                   | Subtype of the Kubernetes resource                                             |                                                                                                                            |
| size `String`                                                                                                                                      | Size of the Kubernetes resource in bytes                                       |                                                                                                                            |
| date `String`                                                                                                                                      | Timestamp indicating when the Kubernetes resource was created or last modified |                                                                                                                            |
| location [`[AppFlowItemLocation]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-flow-item-location) | Locations where the Kubernetes resource is deployed or stored                  | <p>runBy <code>String</code><br>foundBy <code>String</code><br>foundIn <code>String</code><br>link <code>String</code></p> |

### References

#### Fields with this object

* [{} ApplicationFlow.kubernetes](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-flow)
