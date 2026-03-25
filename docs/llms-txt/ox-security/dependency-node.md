# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/dependency-node.md

# dependencyNode

Represents a node in a dependency graph.

### Examples

```graphql
type DependencyNode {
  id: String
  name: String
  width: String
  height: String
  vulnerable: Boolean
}
```

### Fields

| Field                | Description                                      | Supported fields |
| -------------------- | ------------------------------------------------ | ---------------- |
| id `String`          | Unique identifier of the node                    |                  |
| name `String`        | Name of the dependency or component              |                  |
| width `String`       | Width for UI display                             |                  |
| height `String`      | Height for UI display                            |                  |
| vulnerable `Boolean` | Indicates if this node has known vulnerabilities |                  |

### References

#### Fields with this object

* [{} SbomDependencyGraphResponse.nodes](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-dependency-graph-response)
* [{} SbomDependencyGraphResponse.allNodes](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-dependency-graph-response)
* [{} Issue.dependencyGraphNodes](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
