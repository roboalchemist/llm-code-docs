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

## Class AstSorter

- java.lang.Object

- 

  - graphql.language.AstSorter

- 

---

```
@PublicApi
public class AstSorter
extends java.lang.Object
```

A class that helps you sort AST nodes

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`AstSorter()` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`<T extends Node>
T`
`sort(T nodeToBeSorted)`
This will sort nodes in specific orders and then alphabetically.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AstSorter

```
public AstSorter()
```

  - 

### Method Detail

    - 

#### sort

```
public <T extends Node> T sort(T nodeToBeSorted)
```

This will sort nodes in specific orders and then alphabetically.

 The order is :
 

 
      - Query operation definitions
 
      - Mutation operation definitions
 
      - Subscriptions operation definitions
 
      - Fragment definitions
 
      - Directive definitions
 
      - Schema definitions
 
      - Object Type definitions
 
      - Interface Type definitions
 
      - Union Type definitions
 
      - Enum Type definitions
 
      - Scalar Type definitions
 
      - Input Object Type definitions
 

 After those groupings they will be sorted alphabetic.  All arguments and directives on elements
 will be sorted alphabetically by name.

Type Parameters:
`T` - of type `Node`
Parameters:
`nodeToBeSorted` - the node to be sorted
Returns:
a new sorted node (because `Node`s are immutable)

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