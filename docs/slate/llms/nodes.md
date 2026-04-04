# Source: https://docs.slatejs.org/api/nodes.md

# Node Types

The `Node` union type represents all of the different types of nodes that occur in a Slate document tree.

```typescript
type Node = Editor | Element | Text

type Descendant = Element | Text
type Ancestor = Editor | Element
```

* [Node](https://docs.slatejs.org/api/nodes/node)
* [NodeEntry](https://docs.slatejs.org/api/nodes/node-entry)
* [Editor](https://docs.slatejs.org/api/nodes/editor)
* [Element](https://docs.slatejs.org/api/nodes/element)
* [Text](https://docs.slatejs.org/api/nodes/text)
