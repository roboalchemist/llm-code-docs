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

## Class BooleanValue

- java.lang.Object

- 

  - graphql.language.AbstractNode<BooleanValue>

  - 

    - graphql.language.BooleanValue

- 

All Implemented Interfaces:
Node<BooleanValue>, ScalarValue<BooleanValue>, Value<BooleanValue>, java.io.Serializable

---

```
@PublicApi
public class BooleanValue
extends AbstractNode<BooleanValue>
implements ScalarValue<BooleanValue>
```

See Also:
Serialized Form

- 

  - 

### Nested Class Summary

Nested Classes 

Modifier and Type
Class and Description

`static class `
`BooleanValue.Builder` 

  - 

### Constructor Summary

Constructors 

Modifier
Constructor and Description

` `
`BooleanValue(boolean value)`
alternative to using a Builder for convenience

`protected `
`BooleanValue(boolean value,
            SourceLocation sourceLocation,
            java.util.List<Comment> comments,
            IgnoredChars ignoredChars,
            java.util.Map<java.lang.String,java.lang.String> additionalData)` 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`TraversalControl`
`accept(TraverserContext<Node> context,
      NodeVisitor visitor)`
Double-dispatch entry point.

`BooleanValue`
`deepCopy()` 

`java.util.List<Node>`
`getChildren()` 

`NodeChildrenContainer`
`getNamedChildren()`
Alternative to `Node.getChildren()` where the children are not all in one list regardless of type
 but grouped by name/type of the child.

`boolean`
`isEqualTo(Node o)`
Compares just the content and not the children.

`boolean`
`isValue()` 

`static BooleanValue.Builder`
`newBooleanValue()` 

`static BooleanValue.Builder`
`newBooleanValue(boolean value)` 

`java.lang.String`
`toString()` 

`BooleanValue`
`transform(java.util.function.Consumer<BooleanValue.Builder> builderConsumer)` 

`BooleanValue`
`withNewChildren(NodeChildrenContainer newChildren)`
Replaces the specified children and returns a new Node.

    - 

### Methods inherited from class graphql.language.AbstractNode

`deepCopy, deepCopy, getAdditionalData, getComments, getIgnoredChars, getSourceLocation`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

    - 

### Methods inherited from interface graphql.language.Node

`getAdditionalData, getComments, getIgnoredChars, getSourceLocation`

- 

  - 

### Constructor Detail

    - 

#### BooleanValue

```
protected BooleanValue(boolean value,
                       SourceLocation sourceLocation,
                       java.util.List<Comment> comments,
                       IgnoredChars ignoredChars,
                       java.util.Map<java.lang.String,java.lang.String> additionalData)
```

    - 

#### BooleanValue

```
public BooleanValue(boolean value)
```

alternative to using a Builder for convenience

Parameters:
`value` - of the Boolean

  - 

### Method Detail

    - 

#### isValue

```
public boolean isValue()
```

    - 

#### getChildren

```
public java.util.List<Node> getChildren()
```

Specified by:
`getChildren` in interface `Node<BooleanValue>`
Returns:
a list of the children of this node

    - 

#### getNamedChildren

```
public NodeChildrenContainer getNamedChildren()
```

Description copied from interface: `Node`
Alternative to `Node.getChildren()` where the children are not all in one list regardless of type
 but grouped by name/type of the child.

Specified by:
`getNamedChildren` in interface `Node<BooleanValue>`
Returns:
a container of the child nodes

    - 

#### withNewChildren

```
public BooleanValue withNewChildren(NodeChildrenContainer newChildren)
```

Description copied from interface: `Node`
Replaces the specified children and returns a new Node.

Specified by:
`withNewChildren` in interface `Node<BooleanValue>`
Parameters:
`newChildren` - must be empty for Nodes without children
Returns:
a new node

    - 

#### isEqualTo

```
public boolean isEqualTo(Node o)
```

Description copied from interface: `Node`
Compares just the content and not the children.

Specified by:
`isEqualTo` in interface `Node<BooleanValue>`
Parameters:
`o` - the other node to compare to
Returns:
isEqualTo

    - 

#### deepCopy

```
public BooleanValue deepCopy()
```

Specified by:
`deepCopy` in interface `Node<BooleanValue>`
Returns:
a deep copy of this node

    - 

#### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`

    - 

#### accept

```
public TraversalControl accept(TraverserContext<Node> context,
                               NodeVisitor visitor)
```

Description copied from interface: `Node`
Double-dispatch entry point.
 A node receives a Visitor instance and then calls a method on a Visitor
 that corresponds to a actual type of this Node. This binding however happens
 at the compile time and therefore it allows to save on rather expensive
 reflection based `instanceOf` check when decision based on the actual
 type of Node is needed, which happens redundantly during traversing AST.

 Additional advantage of this pattern is to decouple tree traversal mechanism
 from the code that needs to be executed when traversal "visits" a particular Node
 in the tree. This leads to a better code re-usability and maintainability.

Specified by:
`accept` in interface `Node<BooleanValue>`
Parameters:
`context` - TraverserContext bound to this Node object
`visitor` - Visitor instance that performs actual processing on the Nodes(s)
Returns:
Result of Visitor's operation.
 Note! Visitor's operation might return special results to control traversal process.

    - 

#### newBooleanValue

```
public static BooleanValue.Builder newBooleanValue()
```

    - 

#### newBooleanValue

```
public static BooleanValue.Builder newBooleanValue(boolean value)
```

    - 

#### transform

```
public BooleanValue transform(java.util.function.Consumer<BooleanValue.Builder> builderConsumer)
```

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