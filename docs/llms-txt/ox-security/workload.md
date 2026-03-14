# Source: https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/workload.md

# workload

Defines Kubernetes workload information.

### Examples

```graphql
type Workload {
  type: String
  namespace: String
  name: String
  cluster: String
  region: String
  isExposed: String
  consoleLink: String
  exposurePath: [ExposurePathItem]
}
```

### Fields

| Field                                                                                                                                              | Description                                                  | Supported fields                                                                          |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------------------------------------- |
| type `String`                                                                                                                                      | Type of Kubernetes workload (Deployment, Pod, Service, etc.) |                                                                                           |
| namespace `String`                                                                                                                                 | Kubernetes namespace                                         |                                                                                           |
| name `String`                                                                                                                                      | Name of the workload                                         |                                                                                           |
| cluster `String`                                                                                                                                   | Kubernetes cluster name                                      |                                                                                           |
| region `String`                                                                                                                                    | Cloud region where the cluster is located                    |                                                                                           |
| isExposed `String`                                                                                                                                 | Whether the workload is exposed to external traffic          |                                                                                           |
| consoleLink `String`                                                                                                                               | URL link to view the workload in the cloud console           |                                                                                           |
| exposurePath [`[ExposurePathItem]`](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/exposure-path-item) | Path showing how the workload is exposed                     | <p>type <code>String</code><br>name <code>String</code><br>cbomId <code>String</code></p> |

### References

#### Fields with this object

* [{} CloudItem.workloads](https://docs.ox.security/api-documentation/api-reference/api--cloud-security/types/objects/cloud-item)
