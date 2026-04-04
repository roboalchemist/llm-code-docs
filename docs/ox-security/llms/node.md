# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/node.md

# node

### Examples

```graphql
type Node {
  id: Float!
  type: NodeType!
  metaData: JSON!
}
```

### Fields

| Field                                                                                                         | Description                                           | Supported fields |
| ------------------------------------------------------------------------------------------------------------- | ----------------------------------------------------- | ---------------- |
| id `Float!`                                                                                                   | Unique identifier for the node                        |                  |
| type [`NodeType!`](https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/node-type) | Type of the node indicating what entity it represents |                  |
| metaData `JSON!`                                                                                              | Additional metadata associated with the node          |                  |

### References

#### Fields with this object

* [{} IssueGraph.nodes](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/issue-graph)
