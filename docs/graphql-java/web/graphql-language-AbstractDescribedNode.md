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

## Class AbstractDescribedNode<T extends Node>

- java.lang.Object

- 

  - graphql.language.AbstractNode<T>

  - 

    - graphql.language.AbstractDescribedNode<T>

- 

All Implemented Interfaces:
DescribedNode<T>, Node<T>, java.io.Serializable

Direct Known Subclasses:
DirectiveDefinition, EnumTypeDefinition, EnumValueDefinition, FieldDefinition, InputObjectTypeDefinition, InputValueDefinition, InterfaceTypeDefinition, ObjectTypeDefinition, ScalarTypeDefinition, SchemaDefinition, UnionTypeDefinition

---

```
@PublicApi
public abstract class AbstractDescribedNode<T extends Node>
extends AbstractNode<T>
implements DescribedNode<T>
```

See Also:
Serialized Form

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`protected Description`
`description` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AbstractDescribedNode(SourceLocation sourceLocation,
                     java.util.List<Comment> comments,
                     IgnoredChars ignoredChars,
                     java.util.Map<java.lang.String,java.lang.String> additionalData,
                     Description description)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`Description`
`getDescription()` 

    - 

### Methods inherited from class graphql.language.AbstractNode

`deepCopy, deepCopy, getAdditionalData, getComments, getIgnoredChars, getSourceLocation`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

    - 

### Methods inherited from interface graphql.language.Node

`accept, deepCopy, getAdditionalData, getChildren, getComments, getIgnoredChars, getNamedChildren, getSourceLocation, isEqualTo, withNewChildren`

- 

  - 

### Field Detail

    - 

#### description

```
protected Description description
```

  - 

### Constructor Detail

    - 

#### AbstractDescribedNode

```
public AbstractDescribedNode(SourceLocation sourceLocation,
                             java.util.List<Comment> comments,
                             IgnoredChars ignoredChars,
                             java.util.Map<java.lang.String,java.lang.String> additionalData,
                             Description description)
```

  - 

### Method Detail

    - 

#### getDescription

```
public Description getDescription()
```

Specified by:
`getDescription` in interface `DescribedNode<T extends Node>`
Returns:
the description of this node

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