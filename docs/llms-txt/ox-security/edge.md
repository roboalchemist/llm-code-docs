# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/edge.md

# edge

### Examples

```graphql
type Edge {
  id: Float!
  type: EdgeType!
  metaData: JSON
  target: Float!
  source: Float!
}
```

### Fields

| Field                                                                                                         | Description                                 | Supported fields |
| ------------------------------------------------------------------------------------------------------------- | ------------------------------------------- | ---------------- |
| id `Float!`                                                                                                   | Unique identifier for the edge              |                  |
| type [`EdgeType!`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/edge-type) | Type of connection between nodes            |                  |
| metaData `JSON`                                                                                               | Optional metadata associated with the edge  |                  |
| target `Float!`                                                                                               | ID of the target node where the edge ends   |                  |
| source `Float!`                                                                                               | ID of the source node where the edge starts |                  |

### References

#### Fields with this object

* [{} IssueGraph.edges](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue-graph)
