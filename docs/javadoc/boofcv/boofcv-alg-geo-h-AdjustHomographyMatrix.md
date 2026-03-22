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

boofcv.alg.geo.h

## Class AdjustHomographyMatrix

- java.lang.Object

- 

  - boofcv.alg.geo.h.AdjustHomographyMatrix

- 

---

```
public class AdjustHomographyMatrix
extends java.lang.Object
```

The scale and sign of a homography matrix is ambiguous.  This contains functions which pick a reasonable scale
 and the correct sign.  The second smallest singular value is set to one and the sign is chosen such that
 the basic properties work.
Author:
  Peter Abeles

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`protected `
`**svd**` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AdjustHomographyMatrix**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`boolean`
`**adjust**(DenseMatrix64F H,
      AssociatedPair p)` 

`boolean`
`**adjust**(DenseMatrix64F H,
      PairLineNorm p)` 

`protected void`
`**adjustHomographSign**(AssociatedPair p,
                   DenseMatrix64F H)`
Since the sign of the homography is ambiguous a point is required to make sure the correct
 one was selected.

`protected void`
`**adjustHomographSign**(PairLineNorm p,
                   DenseMatrix64F H)`
Since the sign of the homography is ambiguous a point is required to make sure the correct
 one was selected.

`protected boolean`
`**findScaleH**(DenseMatrix64F H)`
The scale of H is found by computing the second smallest singular value.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### svd

```
protected  svd
```

  - 

### Constructor Detail

    - 

#### AdjustHomographyMatrix

```
public AdjustHomographyMatrix()
```

  - 

### Method Detail

    - 

#### adjust

```
public boolean adjust(DenseMatrix64F H,
             AssociatedPair p)
```

    - 

#### adjust

```
public boolean adjust(DenseMatrix64F H,
             PairLineNorm p)
```

    - 

#### findScaleH

```
protected boolean findScaleH(DenseMatrix64F H)
```

The scale of H is found by computing the second smallest singular value.

    - 

#### adjustHomographSign

```
protected void adjustHomographSign(AssociatedPair p,
                       DenseMatrix64F H)
```

Since the sign of the homography is ambiguous a point is required to make sure the correct
 one was selected.
Parameters:`p` - test point, used to determine the sign of the matrix.

    - 

#### adjustHomographSign

```
protected void adjustHomographSign(PairLineNorm p,
                       DenseMatrix64F H)
```

Since the sign of the homography is ambiguous a point is required to make sure the correct
 one was selected.
Parameters:`p` - test point, used to determine the sign of the matrix.

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