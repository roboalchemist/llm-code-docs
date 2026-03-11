# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/dependency-edge.md

# dependencyEdge

Represents a dependency edge from one node to another.

### Examples

```graphql
type DependencyEdge {
  v: String
  w: String
}
```

### Fields

| Field      | Description                     | Supported fields |
| ---------- | ------------------------------- | ---------------- |
| v `String` | ID of the parent/dependent node |                  |
| w `String` | ID of the child/dependency node |                  |

### References

#### Fields with this object

* [{} SbomDependencyGraphResponse.edges](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-dependency-graph-response)
* [{} SbomDependencyGraphResponse.allEdges](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/sbom-dependency-graph-response)
* [{} Issue.dependencyGraphEdges](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue)
