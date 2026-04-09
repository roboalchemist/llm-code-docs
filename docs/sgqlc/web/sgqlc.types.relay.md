# sgqlc.types.relay module

## GraphQL Types for Relay [https://facebook.github.io/relay/]

Exposes `Node` and `Connection`, matching Global Object
Identification [https://facebook.github.io/relay/graphql/objectidentification.htm]
and Cursor Connections [https://facebook.github.io/relay/graphql/connections.htm], which
are widely used.

### Examples

```
>>> from sgqlc.types import Type, Field, list_of
>>> class NodeBasedInterface(Node):
...     a_int = int
...
>>> NodeBasedInterface # or repr()
interface NodeBasedInterface implements Node {
  id: ID!
  aInt: Int
}
>>> class NodeBasedType(Type, Node):
...     a_int = int
...
>>> NodeBasedType # or repr()
type NodeBasedType implements Node {
  id: ID!
  aInt: Int
}

```