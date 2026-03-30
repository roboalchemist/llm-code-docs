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

## Class AbstractNode<T extends Node>

- java.lang.Object

- 

  - graphql.language.AbstractNode<T>

- 

All Implemented Interfaces:
Node<T>, java.io.Serializable

Direct Known Subclasses:
AbstractDescribedNode, Argument, ArrayValue, BooleanValue, Directive, DirectiveLocation, Document, EnumValue, Field, FloatValue, FragmentDefinition, FragmentSpread, InlineFragment, IntValue, ListType, NonNullType, NullValue, ObjectField, ObjectValue, OperationDefinition, OperationTypeDefinition, SelectionSet, StringValue, TypeName, VariableDefinition, VariableReference

---

```
@PublicApi
public abstract class AbstractNode<T extends Node>
extends java.lang.Object
implements Node<T>
```

See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AbstractNode(SourceLocation sourceLocation,
            java.util.List<Comment> comments,
            IgnoredChars ignoredChars)` 

`AbstractNode(SourceLocation sourceLocation,
            java.util.List<Comment> comments,
            IgnoredChars ignoredChars,
            java.util.Map<java.lang.String,java.lang.String> additionalData)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`protected <V extends Node>
java.util.List<V>`
`deepCopy(java.util.List<? extends Node> list)` 

`protected <V extends Node>
V`
`deepCopy(V nullableObj)` 

`java.util.Map<java.lang.String,java.lang.String>`
`getAdditionalData()`
A node can have a map of additional data associated with it.

`java.util.List<Comment>`
`getComments()`
Nodes can have comments made on them, the following is one comment per line before a node.

`IgnoredChars`
`getIgnoredChars()`
The chars which are ignored by the parser.

`SourceLocation`
`getSourceLocation()` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

    - 

### Methods inherited from interface graphql.language.Node

`accept, deepCopy, getChildren, getNamedChildren, isEqualTo, withNewChildren`

- 

  - 

### Constructor Detail

    - 

#### AbstractNode

```
public AbstractNode(SourceLocation sourceLocation,
                    java.util.List<Comment> comments,
                    IgnoredChars ignoredChars)
```

    - 

#### AbstractNode

```
public AbstractNode(SourceLocation sourceLocation,
                    java.util.List<Comment> comments,
                    IgnoredChars ignoredChars,
                    java.util.Map<java.lang.String,java.lang.String> additionalData)
```

  - 

### Method Detail

    - 

#### getSourceLocation

```
public SourceLocation getSourceLocation()
```

Specified by:
`getSourceLocation` in interface `Node<T extends Node>`
Returns:
the source location where this node occurs

    - 

#### getComments

```
public java.util.List<Comment> getComments()
```

Description copied from interface: `Node`
Nodes can have comments made on them, the following is one comment per line before a node.

Specified by:
`getComments` in interface `Node<T extends Node>`
Returns:
the list of comments or an empty list of there are none

    - 

#### getIgnoredChars

```
public IgnoredChars getIgnoredChars()
```

Description copied from interface: `Node`
The chars which are ignored by the parser. (Before and after the current node)

Specified by:
`getIgnoredChars` in interface `Node<T extends Node>`
Returns:
the ignored chars

    - 

#### getAdditionalData

```
public java.util.Map<java.lang.String,java.lang.String> getAdditionalData()
```

Description copied from interface: `Node`
A node can have a map of additional data associated with it.

 

 NOTE: The reason this is a map of strings is so the Node
 can stay an immutable object, which Map<String,Object> would not allow
 say.

Specified by:
`getAdditionalData` in interface `Node<T extends Node>`
Returns:
the map of additional data about this node

    - 

#### deepCopy

```
protected <V extends Node> V deepCopy(V nullableObj)
```

    - 

#### deepCopy

```
protected <V extends Node> java.util.List<V> deepCopy(java.util.List<? extends Node> list)
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