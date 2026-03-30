# Source: https://docs.ox.security/api-documentation/api-reference/api--issue/types/enums/edge-type.md

# edgeType

Types of connections between nodes in the issue graph.

### Examples

```graphql
enum EdgeType {
  Default
  Arrow
  Step
}
```

### Enum values

| Enum value | Description                                             |
| ---------- | ------------------------------------------------------- |
| Default    | Standard connection between nodes                       |
| Arrow      | Directional connection indicating flow or dependency    |
| Step       | Sequential connection representing steps or progression |

### References

#### Fields with this object

* [{} Edge.type](https://docs.ox.security/api-documentation/api-reference/api--issue/types/objects/edge)
