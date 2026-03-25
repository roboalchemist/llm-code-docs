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

boofcv.alg.feature.associate

## Class AssociateSurfBasic

- java.lang.Object

- 

  - boofcv.alg.feature.associate.AssociateSurfBasic

- 

---

```
public class AssociateSurfBasic
extends java.lang.Object
```

Basic algorithm for specializing association for SURF features.  Two list of features are
 created depending on the sign of the laplacian.  These lists are associated independently then
 combined.
Author:
  Peter Abeles

- 

  - 

### Nested Class Summary

Nested Classes 

Modifier and Type
Class and Description

`static class `
`**AssociateSurfBasic.Helper**` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AssociateSurfBasic**(AssociateDescription<TupleDesc_F64> assoc)` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`void`
`**associate**()`
Associates the features together.

`AssociateDescription<TupleDesc_F64>`
`**getAssoc**()` 

`FastQueue<AssociatedIndex>`
`**getMatches**()`
Returns a list of found matches.

`GrowQueue_I32`
`**getUnassociatedSrc**()` 

`void`
`**setDst**(FastQueue<SurfFeature> dst)` 

`void`
`**setSrc**(FastQueue<SurfFeature> src)` 

`void`
`**swapLists**()`
Swaps the source and dest feature list.

`int`
`**totalDestination**()` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AssociateSurfBasic

```
public AssociateSurfBasic(AssociateDescription<TupleDesc_F64> assoc)
```

  - 

### Method Detail

    - 

#### setSrc

```
public void setSrc(FastQueue<SurfFeature> src)
```

    - 

#### setDst

```
public void setDst(FastQueue<SurfFeature> dst)
```

    - 

#### swapLists

```
public void swapLists()
```

Swaps the source and dest feature list.  Useful when processing a sequence
 of images and don't want to resort everything.

    - 

#### associate

```
public void associate()
```

Associates the features together.

    - 

#### getMatches

```
public FastQueue<AssociatedIndex> getMatches()
```

Returns a list of found matches.

    - 

#### totalDestination

```
public int totalDestination()
```

    - 

#### getUnassociatedSrc

```
public GrowQueue_I32 getUnassociatedSrc()
```

    - 

#### getAssoc

```
public AssociateDescription<TupleDesc_F64> getAssoc()
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