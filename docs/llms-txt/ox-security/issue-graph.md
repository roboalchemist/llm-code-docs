# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue-graph.md

# issueGraph

### Examples

```graphql
type IssueGraph {
  nodes: [Node!]!
  edges: [Edge!]!
}
```

### Fields

| Field                                                                                                      | Description                                                             | Supported fields                                                                                                                                                                        |
| ---------------------------------------------------------------------------------------------------------- | ----------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| nodes [`[Node!]!`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/node) | List of nodes representing various entities in the issue graph          | <p>id <code>Float!</code><br>type <a href="../enums/node-type"><code>NodeType!</code></a><br>metaData <code>JSON!</code></p>                                                            |
| edges [`[Edge!]!`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/edge) | List of edges representing connections between nodes in the issue graph | <p>id <code>Float!</code><br>type <a href="../enums/edge-type"><code>EdgeType!</code></a><br>metaData <code>JSON</code><br>target <code>Float!</code><br>source <code>Float!</code></p> |

### References

#### Queries using this object

* [\<?> getIssueGraph](https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-issue-graph)
* [\<?> getCBOMAssetGraph](https://docs.ox.security/api-documentation/api-reference/api--issue/queries/get-cbom-asset-graph)
