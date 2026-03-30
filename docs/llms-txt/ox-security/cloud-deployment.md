# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/cloud-deployment.md

# cloudDeployment

Represents a cloud deployment associated with an application, including type, subtype, hash, and location details.

### Examples

```graphql
type CloudDeployment {
  type: String
  subType: String
  name: String
  hash: String
  hashType: String
  link: String
  location: [AppFlowItemLocation]
  k8sType: String
  imageName: String
  date: String
  cluster: String
  region: String
}
```

### Fields

| Field                                                                                                                                              | Description                                                     | Supported fields                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| type `String`                                                                                                                                      | Type of cloud deployment                                        |                                                                                                                            |
| subType `String`                                                                                                                                   | Subtype of the deployment                                       |                                                                                                                            |
| name `String`                                                                                                                                      | Name of the deployment                                          |                                                                                                                            |
| hash `String`                                                                                                                                      | Hash value representing the deployment version or configuration |                                                                                                                            |
| hashType `String`                                                                                                                                  | Type of hash used                                               |                                                                                                                            |
| link `String`                                                                                                                                      | Link to the cloud deployment or resource                        |                                                                                                                            |
| location [`[AppFlowItemLocation]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-flow-item-location) | Locations associated with the cloud deployment                  | <p>runBy <code>String</code><br>foundBy <code>String</code><br>foundIn <code>String</code><br>link <code>String</code></p> |
| k8sType `String`                                                                                                                                   | Type of Kubernetes resource (if applicable)                     |                                                                                                                            |
| imageName `String`                                                                                                                                 | Name of the container image (if applicable)                     |                                                                                                                            |
| date `String`                                                                                                                                      | Timestamp of the deployment                                     |                                                                                                                            |
| cluster `String`                                                                                                                                   | Cluster where the deployment is located                         |                                                                                                                            |
| region `String`                                                                                                                                    | Region where the deployment is hosted                           |                                                                                                                            |

### References

#### Fields with this object

* [{} ApplicationFlow.cloudDeployments](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-flow)
