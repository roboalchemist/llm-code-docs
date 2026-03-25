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

## Class Argument

- java.lang.Object

- 

  - graphql.language.AbstractNode<Argument>

  - 

    - graphql.language.Argument

- 

All Implemented Interfaces:
NamedNode<Argument>, Node<Argument>, java.io.Serializable

---

```
@PublicApi
public class Argument
extends AbstractNode<Argument>
implements NamedNode<Argument>
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
`Argument.Builder` 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`static java.lang.String`
`CHILD_VALUE` 

  - 

### Constructor Summary

Constructors 

Modifier
Constructor and Description

` `
`Argument(java.lang.String name,
        Value value)`
alternative to using a Builder for convenience

`protected `
`Argument(java.lang.String name,
        Value value,
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

`Argument`
`deepCopy()` 

`java.util.List<Node>`
`getChildren()` 

`java.lang.String`
`getName()` 

`NodeChildrenContainer`
`getNamedChildren()`
Alternative to `Node.getChildren()` where the children are not all in one list regardless of type
 but grouped by name/type of the child.

`Value`
`getValue()` 

`boolean`
`isEqualTo(Node o)`
Compares just the content and not the children.

`static Argument.Builder`
`newArgument()` 

`static Argument.Builder`
`newArgument(java.lang.String name,
           Value value)` 

`java.lang.String`
`toString()` 

`Argument`
`transform(java.util.function.Consumer<Argument.Builder> builderConsumer)` 

`Argument`
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

#### CHILD_VALUE

```
public static final java.lang.String CHILD_VALUE
```

See Also:
Constant Field Values

  - 

### Constructor Detail

    - 

#### Argument

```
protected Argument(java.lang.String name,
                   Value value,
                   SourceLocation sourceLocation,
                   java.util.List<Comment> comments,
                   IgnoredChars ignoredChars,
                   java.util.Map<java.lang.String,java.lang.String> additionalData)
```

    - 

#### Argument

```
public Argument(java.lang.String name,
                Value value)
```

alternative to using a Builder for convenience

Parameters:
`name` - of the argument
`value` - of the argument

  - 

### Method Detail

    - 

#### newArgument

```
public static Argument.Builder newArgument()
```

    - 

#### newArgument

```
public static Argument.Builder newArgument(java.lang.String name,
                                           Value value)
```

    - 

#### getName

```
public java.lang.String getName()
```

Specified by:
`getName` in interface `NamedNode<Argument>`
Returns:
the name of this node

    - 

#### getValue

```
public Value getValue()
```

    - 

#### getChildren

```
public java.util.List<Node> getChildren()
```

Specified by:
`getChildren` in interface `Node<Argument>`
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
`getNamedChildren` in interface `Node<Argument>`
Returns:
a container of the child nodes

    - 

#### withNewChildren

```
public Argument withNewChildren(NodeChildrenContainer newChildren)
```

Description copied from interface: `Node`
Replaces the specified children and returns a new Node.

Specified by:
`withNewChildren` in interface `Node<Argument>`
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
`isEqualTo` in interface `Node<Argument>`
Parameters:
`o` - the other node to compare to
Returns:
isEqualTo

    - 

#### deepCopy

```
public Argument deepCopy()
```

Specified by:
`deepCopy` in interface `Node<Argument>`
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
`accept` in interface `Node<Argument>`
Parameters:
`context` - TraverserContext bound to this Node object
`visitor` - Visitor instance that performs actual processing on the Nodes(s)
Returns:
Result of Visitor's operation.
 Note! Visitor's operation might return special results to control traversal process.

    - 

#### transform

```
public Argument transform(java.util.function.Consumer<Argument.Builder> builderConsumer)
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