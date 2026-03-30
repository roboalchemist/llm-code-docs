# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-dependency-graph-response.md

# sbomDependencyGraphResponse

Represents response for dependency graph information.

### Examples

```graphql
type SbomDependencyGraphResponse {
  nodes: [DependencyNode]
  allNodes: [DependencyNode]
  edges: [DependencyEdge]
  allEdges: [DependencyEdge]
}
```

### Fields

| Field                                                                                                                            | Description                                                    | Supported fields                                                                                                                                        |
| -------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------- |
| nodes [`[DependencyNode]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/dependency-node)    | Nodes in the current dependency graph                          | <p>id <code>String</code><br>name <code>String</code><br>width <code>String</code><br>height <code>String</code><br>vulnerable <code>Boolean</code></p> |
| allNodes [`[DependencyNode]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/dependency-node) | All nodes including transitive dependencies                    | <p>id <code>String</code><br>name <code>String</code><br>width <code>String</code><br>height <code>String</code><br>vulnerable <code>Boolean</code></p> |
| edges [`[DependencyEdge]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/dependency-edge)    | Edges in the current dependency graph (parent-child relations) | <p>v <code>String</code><br>w <code>String</code></p>                                                                                                   |
| allEdges [`[DependencyEdge]`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/dependency-edge) | All edges including transitive dependencies                    | <p>v <code>String</code><br>w <code>String</code></p>                                                                                                   |

### References

#### Fields with this object

* [{} SbomLib.dependencyGraph](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-lib)
* [{} Issue.dependencyGraph](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
