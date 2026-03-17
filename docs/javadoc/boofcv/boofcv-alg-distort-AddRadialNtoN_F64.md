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

boofcv.alg.distort

## Class AddRadialNtoN_F64

- java.lang.Object

- 

  - boofcv.alg.distort.AddRadialNtoN_F64

- 

All Implemented Interfaces:
PointTransform_F64

---

```
public class AddRadialNtoN_F64
extends java.lang.Object
implements PointTransform_F64
```

Given an undistorted normalized pixel coordinate, compute the distorted normalized coordinate.
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AddRadialNtoN_F64**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`void`
`**compute**(double x,
       double y,
       Point2D_F64 out)`
Adds radial distortion

`void`
`**set**(double[] radial)`
Specify intrinsic camera parameters

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AddRadialNtoN_F64

```
public AddRadialNtoN_F64()
```

  - 

### Method Detail

    - 

#### set

```
public void set(double[] radial)
```

Specify intrinsic camera parameters
Parameters:`radial` - Radial distortion parameters

    - 

#### compute

```
public void compute(double x,
           double y,
           Point2D_F64 out)
```

Adds radial distortion

**Specified by:**
`compute` in interface `PointTransform_F64`
Parameters:`x` - Undistorted x-coordinate normalized image coordinates`y` - Undistorted y-coordinate normalized image coordinates`out` - Distorted normalized image coordinate.

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