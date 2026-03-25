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

## Class ArrayValue

- java.lang.Object

- 

  - graphql.language.AbstractNode<ArrayValue>

  - 

    - graphql.language.ArrayValue

- 

All Implemented Interfaces:
Node<ArrayValue>, Value<ArrayValue>, java.io.Serializable

---

```
@PublicApi
public class ArrayValue
extends AbstractNode<ArrayValue>
implements Value<ArrayValue>
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
`ArrayValue.Builder` 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`static java.lang.String`
`CHILD_VALUES` 

  - 

### Constructor Summary

Constructors 

Modifier
Constructor and Description

` `
`ArrayValue(java.util.List<Value> values)`
alternative to using a Builder for convenience

`protected `
`ArrayValue(java.util.List<Value> values,
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

`ArrayValue`
`deepCopy()` 

`java.util.List<Node>`
`getChildren()` 

`NodeChildrenContainer`
`getNamedChildren()`
Alternative to `Node.getChildren()` where the children are not all in one list regardless of type
 but grouped by name/type of the child.

`java.util.List<Value>`
`getValues()` 

`boolean`
`isEqualTo(Node o)`
Compares just the content and not the children.

`static ArrayValue.Builder`
`newArrayValue()` 

`java.lang.String`
`toString()` 

`ArrayValue`
`transform(java.util.function.Consumer<ArrayValue.Builder> builderConsumer)` 

`ArrayValue`
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

### Field Detail

    - 

#### CHILD_VALUES

```
public static final java.lang.String CHILD_VALUES
```

See Also:
Constant Field Values

  - 

### Constructor Detail

    - 

#### ArrayValue

```
protected ArrayValue(java.util.List<Value> values,
                     SourceLocation sourceLocation,
                     java.util.List<Comment> comments,
                     IgnoredChars ignoredChars,
                     java.util.Map<java.lang.String,java.lang.String> additionalData)
```

    - 

#### ArrayValue

```
public ArrayValue(java.util.List<Value> values)
```

alternative to using a Builder for convenience

Parameters:
`values` - of the array

  - 

### Method Detail

    - 

#### newArrayValue

```
public static ArrayValue.Builder newArrayValue()
```

    - 

#### getValues

```
public java.util.List<Value> getValues()
```

    - 

#### getChildren

```
public java.util.List<Node> getChildren()
```

Specified by:
`getChildren` in interface `Node<ArrayValue>`
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
`getNamedChildren` in interface `Node<ArrayValue>`
Returns:
a container of the child nodes

    - 

#### withNewChildren

```
public ArrayValue withNewChildren(NodeChildrenContainer newChildren)
```

Description copied from interface: `Node`
Replaces the specified children and returns a new Node.

Specified by:
`withNewChildren` in interface `Node<ArrayValue>`
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
`isEqualTo` in interface `Node<ArrayValue>`
Parameters:
`o` - the other node to compare to
Returns:
isEqualTo

    - 

#### toString

```
public java.lang.String toString()
```

Overrides:
`toString` in class `java.lang.Object`

    - 

#### deepCopy

```
public ArrayValue deepCopy()
```

Specified by:
`deepCopy` in interface `Node<ArrayValue>`
Returns:
a deep copy of this node

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
`accept` in interface `Node<ArrayValue>`
Parameters:
`context` - TraverserContext bound to this Node object
`visitor` - Visitor instance that performs actual processing on the Nodes(s)
Returns:
Result of Visitor's operation.
 Note! Visitor's operation might return special results to control traversal process.

    - 

#### transform

```
public ArrayValue transform(java.util.function.Consumer<ArrayValue.Builder> builderConsumer)
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