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

graphql.util

## Class Breadcrumb<T>

- java.lang.Object

- 

  - graphql.util.Breadcrumb<T>

- 

Type Parameters:
`T` - the generic type of object

---

```
@PublicApi
public class Breadcrumb<T>
extends java.lang.Object
```

A specific `NodeLocation` inside a node. This means  `getNode()` returns a Node which has a child
 at `getLocation()`
 

 A list of Breadcrumbs is used to identify the exact location of a specific node inside a tree.

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`Breadcrumb(T node,
          NodeLocation location)` 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method and Description

`boolean`
`equals(java.lang.Object o)` 

`NodeLocation`
`getLocation()` 

`T`
`getNode()` 

`int`
`hashCode()` 

    - 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Breadcrumb

```
public Breadcrumb(T node,
                  NodeLocation location)
```

  - 

### Method Detail

    - 

#### getNode

```
public T getNode()
```

    - 

#### getLocation

```
public NodeLocation getLocation()
```

    - 

#### equals

```
public boolean equals(java.lang.Object o)
```

Overrides:
`equals` in class `java.lang.Object`

    - 

#### hashCode

```
public int hashCode()
```

Overrides:
`hashCode` in class `java.lang.Object`

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