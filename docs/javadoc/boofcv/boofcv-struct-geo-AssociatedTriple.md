JavaScript is disabled on your browser.

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

boofcv.struct.geo

## Class AssociatedTriple

- java.lang.Object

- 

  - boofcv.struct.geo.AssociatedTriple

- 

---

```
public class AssociatedTriple
extends java.lang.Object
```

Contains a set of three observations of the same point feature in three different views.
Author:
  Peter Abeles

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`Point2D_F64`
`**p1**`
Observation in View 1

`Point2D_F64`
`**p2**`
Observation in View 2

`Point2D_F64`
`**p3**`
Observation in View 3

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AssociatedTriple**()` 

`**AssociatedTriple**(Point2D_F64 p1,
                Point2D_F64 p2,
                Point2D_F64 p3)` 

`**AssociatedTriple**(Point2D_F64 p1,
                Point2D_F64 p2,
                Point2D_F64 p3,
                boolean newInstance)` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`AssociatedTriple`
`**copy**()` 

`void`
`**print**()` 

`void`
`**set**(AssociatedTriple a)` 

`void`
`**set**(Point2D_F64 p1,
   Point2D_F64 p2,
   Point2D_F64 p3)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### p1

```
public Point2D_F64 p1
```

Observation in View 1

    - 

#### p2

```
public Point2D_F64 p2
```

Observation in View 2

    - 

#### p3

```
public Point2D_F64 p3
```

Observation in View 3

  - 

### Constructor Detail

    - 

#### AssociatedTriple

```
public AssociatedTriple(Point2D_F64 p1,
                Point2D_F64 p2,
                Point2D_F64 p3)
```

    - 

#### AssociatedTriple

```
public AssociatedTriple(Point2D_F64 p1,
                Point2D_F64 p2,
                Point2D_F64 p3,
                boolean newInstance)
```

    - 

#### AssociatedTriple

```
public AssociatedTriple()
```

  - 

### Method Detail

    - 

#### set

```
public void set(AssociatedTriple a)
```

    - 

#### set

```
public void set(Point2D_F64 p1,
       Point2D_F64 p2,
       Point2D_F64 p3)
```

    - 

#### copy

```
public AssociatedTriple copy()
```

    - 

#### print

```
public void print()
```

- Overview

- Package

- Class

- Use

- Tree

- Deprecated

- Index

- Help

- Prev Class

- Next Class

- Frames

- No Frames

- All Classes

- Summary: 

- Nested | 

- Field | 

- Constr | 

- Method

- Detail: 

- Field | 

- Constr | 

- Method

**Copyright © 2011-2012 Peter Abeles**