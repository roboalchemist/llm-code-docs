# Source: https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/cloud-artifact-data.md

# cloudArtifactData

Cloud-related data for an artifact.

### Examples

```graphql
type CloudArtifactData {
  cloudIdentifier: String
  link: String
  lastExecutionTime: Float
  lastModifiedTime: Float
  account: String
  zone: String
  cluster: String
  cloudDescription: CloudDescription
}
```

### Fields

| Field                                                                                                                                         | Description                                                      | Supported fields                                                                                                                                                                                                                                                           |
| --------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| cloudIdentifier `String`                                                                                                                      | Unique identifier for the cloud resource or artifact             |                                                                                                                                                                                                                                                                            |
| link `String`                                                                                                                                 | URL or link to access the cloud resource or artifact             |                                                                                                                                                                                                                                                                            |
| lastExecutionTime `Float`                                                                                                                     | Timestamp (epoch) of the last execution related to this artifact |                                                                                                                                                                                                                                                                            |
| lastModifiedTime `Float`                                                                                                                      | Timestamp (epoch) of the last modification time of the artifact  |                                                                                                                                                                                                                                                                            |
| account `String`                                                                                                                              | Cloud account associated with the artifact                       |                                                                                                                                                                                                                                                                            |
| zone `String`                                                                                                                                 | Cloud availability zone or region                                |                                                                                                                                                                                                                                                                            |
| cluster `String`                                                                                                                              | Cluster name where the artifact is deployed or used              |                                                                                                                                                                                                                                                                            |
| cloudDescription [`CloudDescription`](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/cloud-description) | Additional descriptive details about the cloud resource          | <p>type <a href="../enums/cloud-types"><code>CloudTypes</code></a><br>subType <a href="../enums/cloud-sub-types"><code>CloudSubTypes</code></a><br>cloudEntityAttributes <a href="../unions/common-cloud-attributes-union"><code>CommonCloudAttributesUnion</code></a></p> |

### References

#### Fields with this object

* [{} ArtifactInfo.cloudData](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-info)
* [{} UnscannedArtifact.cloudData](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/unscanned-artifact)
