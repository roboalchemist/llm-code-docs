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

## Class BorderIndex1D

- java.lang.Object

- 

  - boofcv.core.image.border.BorderIndex1D

- 

Direct Known Subclasses:
BorderIndex1D_Exception, BorderIndex1D_Extend, BorderIndex1D_Reflect, BorderIndex1D_Wrap

---

```
public abstract class BorderIndex1D
extends java.lang.Object
```

Remaps references to elements outside of an array to elements inside of the array.
Author:
  Peter Abeles

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`protected int`
`**length**` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BorderIndex1D**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`abstract int`
`**getIndex**(int index)` 

`int`
`**getLength**()` 

`void`
`**setLength**(int length)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### length

```
protected int length
```

  - 

### Constructor Detail

    - 

#### BorderIndex1D

```
public BorderIndex1D()
```

  - 

### Method Detail

    - 

#### setLength

```
public void setLength(int length)
```

    - 

#### getLength

```
public int getLength()
```

    - 

#### getIndex

```
public abstract int getIndex(int index)
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