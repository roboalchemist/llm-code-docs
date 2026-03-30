# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/artifact-item.md

# artifactItem

Represents an artifact associated with an application, including its type, hash, and location.

### Examples

```graphql
type ArtifactItem {
  type: String
  name: String
  hashType: String
  system: String
  subType: String
  hash: String
  size: String
  date: String
  location: [AppFlowItemLocation]
  linkName: String
  k8sType: String
  cluster: String
  region: String
}
```

### Fields

| Field                                                                                                                                              | Description                                                         | Supported fields                                                                                                           |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------- |
| type `String`                                                                                                                                      | Type of the artifact                                                |                                                                                                                            |
| name `String`                                                                                                                                      | Name of the artifact                                                |                                                                                                                            |
| hashType `String`                                                                                                                                  | Type of hash algorithm used, e.g., SHA-256, MD5, SHA-1              |                                                                                                                            |
| system `String`                                                                                                                                    | System associated with the artifact                                 |                                                                                                                            |
| subType `String`                                                                                                                                   | Subtype of the artifact, providing further categorization           |                                                                                                                            |
| hash `String`                                                                                                                                      | Hash value of the artifact                                          |                                                                                                                            |
| size `String`                                                                                                                                      | Size of the artifact in bytes                                       |                                                                                                                            |
| date `String`                                                                                                                                      | Timestamp indicating when the artifact was created or last modified |                                                                                                                            |
| location [`[AppFlowItemLocation]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-flow-item-location) | Location details of the application flow item                       | <p>runBy <code>String</code><br>foundBy <code>String</code><br>foundIn <code>String</code><br>link <code>String</code></p> |
| linkName `String`                                                                                                                                  | Name of the associated link                                         |                                                                                                                            |
| k8sType `String`                                                                                                                                   | Type of Kubernetes workload                                         |                                                                                                                            |
| cluster `String`                                                                                                                                   | Name of the Kubernetes cluster                                      |                                                                                                                            |
| region `String`                                                                                                                                    | Cloud or physical region where the resource is deployed             |                                                                                                                            |

### References

#### Fields with this object

* [{} ApplicationFlow.artifacts](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-flow)
