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

boofcv.core.image.border

## Class BorderIndex1D_Reflect

- java.lang.Object

- 

  - boofcv.core.image.border.BorderIndex1D

  - 

    - boofcv.core.image.border.BorderIndex1D_Reflect

- 

---

```
public class BorderIndex1D_Reflect
extends BorderIndex1D
```

 Access to outside the array are reflected back into the array around the closest border.  This
 is an even symmetric function, e.g. f(-1) = f(1) = 1, f(-2) = f(2) = 2.
 
Author:
  Peter Abeles

- 

  - 

### Field Summary

    - 

### Fields inherited from class boofcv.core.image.border.BorderIndex1D

`length`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BorderIndex1D_Reflect**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`int`
`**getIndex**(int index)` 

    - 

### Methods inherited from class boofcv.core.image.border.BorderIndex1D

`getLength, setLength`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BorderIndex1D_Reflect

```
public BorderIndex1D_Reflect()
```

  - 

### Method Detail

    - 

#### getIndex

```
public int getIndex(int index)
```

**Specified by:**
`getIndex` in class `BorderIndex1D`

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