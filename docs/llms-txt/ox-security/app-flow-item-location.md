# Source: https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/app-flow-item-location.md

# appFlowItemLocation

Represents location information for various application flow items, including executor, source, and resource link.

### Examples

```graphql
type AppFlowItemLocation {
  runBy: String
  foundBy: String
  foundIn: String
  link: String
}
```

### Fields

| Field            | Description                                        | Supported fields |
| ---------------- | -------------------------------------------------- | ---------------- |
| runBy `String`   | Entity that executed or initiated the process      |                  |
| foundBy `String` | Source from which the item was found               |                  |
| foundIn `String` | Context or component where the item was identified |                  |
| link `String`    | Link to the relevant resource or location          |                  |

### References

#### Fields with this object

* [{} ArtifactItem.location](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/artifact-item)
* [{} CloudDeployment.location](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/cloud-deployment)
* [{} OrchestratorItem.location](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/orchestrator-item)
* [{} KubernetesItem.location](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/kubernetes-item)
* [{} RepositoryItem.location](https://docs.ox.security/api-documentation/api-reference/api--application/types/objects/repository-item)
