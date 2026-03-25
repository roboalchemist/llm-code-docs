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

boofcv.struct.feature

## Class AssociatedIndex

- java.lang.Object

- 

  - boofcv.struct.feature.AssociatedIndex

- 

---

```
public class AssociatedIndex
extends java.lang.Object
```

Indexes of two associated features and the fit score..
Author:
  Peter Abeles

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`int`
`**dst**`
index of the feature in the destination image

`double`
`**fitScore**`
The association score.

`int`
`**src**`
index of the feature in the source image

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AssociatedIndex**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`void`
`**set**(AssociatedIndex a)` 

`void`
`**setAssociation**(int src,
              int dst,
              double fitScore)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### src

```
public int src
```

index of the feature in the source image

    - 

#### dst

```
public int dst
```

index of the feature in the destination image

    - 

#### fitScore

```
public double fitScore
```

The association score.  Meaning will very depending on implementation

  - 

### Constructor Detail

    - 

#### AssociatedIndex

```
public AssociatedIndex()
```

  - 

### Method Detail

    - 

#### setAssociation

```
public void setAssociation(int src,
                  int dst,
                  double fitScore)
```

    - 

#### set

```
public void set(AssociatedIndex a)
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