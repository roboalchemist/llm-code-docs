# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application-flow.md

# applicationFlow

Represents various components and systems associated with an application, including artifacts, cloud deployments, CICD information, orchestrators, and repositories.

### Examples

```graphql
type ApplicationFlow {
  artifacts: [ArtifactItem]
  cloudDeployments: [CloudDeployment]
  cicdInfo: [CicdInfo]
  orchestrators: [OrchestratorItem]
  kubernetes: [KubernetesItem]
  repository: [RepositoryItem]
}
```

### Fields

| Field                                                                                                                                            | Description                                                      | Supported fields                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| artifacts [`[ArtifactItem]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/artifact-item)              | List of artifacts associated with the application                | <p>type <code>String</code><br>name <code>String</code><br>hashType <code>String</code><br>system <code>String</code><br>subType <code>String</code><br>hash <code>String</code><br>size <code>String</code><br>date <code>String</code><br>location <a href="app-flow-item-location"><code>\[AppFlowItemLocation]</code></a><br>linkName <code>String</code><br>k8sType <code>String</code><br>cluster <code>String</code><br>region <code>String</code></p> |
| cloudDeployments [`[CloudDeployment]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/cloud-deployment) | List of cloud deployments associated with the application        | <p>type <code>String</code><br>subType <code>String</code><br>name <code>String</code><br>hash <code>String</code><br>hashType <code>String</code><br>link <code>String</code><br>location <a href="app-flow-item-location"><code>\[AppFlowItemLocation]</code></a><br>k8sType <code>String</code><br>imageName <code>String</code><br>date <code>String</code><br>cluster <code>String</code><br>region <code>String</code></p>                              |
| cicdInfo [`[CicdInfo]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/cicd-info)                       | List of CICD pipelines and related information                   | <p>type <code>String</code><br>system <code>String</code><br>latestDate <code>String</code><br>lastMonthJobCount <code>String</code><br>location <a href="cicd-info-location"><code>\[CicdInfoLocation]</code></a></p>                                                                                                                                                                                                                                        |
| orchestrators [`[OrchestratorItem]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/orchestrator-item)  | List of orchestrator systems involved in the application         | <p>type <code>String</code><br>name <code>String</code><br>hashType <code>String</code><br>system <code>String</code><br>hash <code>String</code><br>size <code>String</code><br>date <code>String</code><br>location <a href="app-flow-item-location"><code>\[AppFlowItemLocation]</code></a></p>                                                                                                                                                            |
| kubernetes [`[KubernetesItem]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/kubernetes-item)         | List of Kubernetes-related items associated with the application | <p>type <code>String</code><br>name <code>String</code><br>hashType <code>String</code><br>system <code>String</code><br>hash <code>String</code><br>subType <code>String</code><br>size <code>String</code><br>date <code>String</code><br>location <a href="app-flow-item-location"><code>\[AppFlowItemLocation]</code></a></p>                                                                                                                             |
| repository [`[RepositoryItem]`](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/repository-item)         | Repository-related information for the application               | <p>type <code>String</code><br>system <code>String</code><br>date <code>String</code><br>location <a href="app-flow-item-location"><code>\[AppFlowItemLocation]</code></a></p>                                                                                                                                                                                                                                                                                |

### References

#### Fields with this object

* [{} Application.applicationFlows](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/application)
* [{} IAppsInfo.applicationFlows](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/i-apps-info)
* [{} ArtifactApplication.appFlow](https://docs.ox.security/api-documentation/api-reference/api--artifact/types/objects/artifact-application)
