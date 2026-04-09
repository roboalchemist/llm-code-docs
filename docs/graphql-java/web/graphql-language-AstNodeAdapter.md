JavaScript is disabled on your browser.

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

graphql.language

## Class AstNodeAdapter

- java.lang.Object

- 

  - graphql.language.AstNodeAdapter

- 

All Implemented Interfaces:
NodeAdapter<Node>

---

```
@PublicApi
public class AstNodeAdapter
extends java.lang.Object
implements NodeAdapter<Node>
```

Adapts an Ast node to the general node from the util package

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`static AstNodeAdapter`
`AST_NODE_ADAPTER` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`java.util.Map<java.lang.String,java.util.List<Node>>`
`getNamedChildren(Node node)` 

`Node`
`removeChild(Node node,
           NodeLocation location)` 

`Node`
`withNewChildren(Node node,
               java.util.Map<java.lang.String,java.util.List<Node>> newChildren)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### AST_NODE_ADAPTER

```
public static final AstNodeAdapter AST_NODE_ADAPTER
```

  - 

### Method Detail

    - 

#### getNamedChildren

```
public java.util.Map<java.lang.String,java.util.List<Node>> getNamedChildren(Node node)
```

Specified by:
`getNamedChildren` in interface `NodeAdapter<Node>`

    - 

#### withNewChildren

```
public Node withNewChildren(Node node,
                            java.util.Map<java.lang.String,java.util.List<Node>> newChildren)
```

Specified by:
`withNewChildren` in interface `NodeAdapter<Node>`

    - 

#### removeChild

```
public Node removeChild(Node node,
                        NodeLocation location)
```

Specified by:
`removeChild` in interface `NodeAdapter<Node>`

Skip navigation links

- Overview

- Package

- Class

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method