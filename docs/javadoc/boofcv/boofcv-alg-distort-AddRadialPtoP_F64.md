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

## Class AddRadialPtoP_F64

- java.lang.Object

- 

  - boofcv.alg.distort.AddRadialPtoP_F64

- 

All Implemented Interfaces:
PointTransform_F64

---

```
public class AddRadialPtoP_F64
extends java.lang.Object
implements PointTransform_F64
```

Given an undistorted pixel coordinate, compute the distorted coordinate.
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AddRadialPtoP_F64**()` 

`**AddRadialPtoP_F64**(double fx,
                 double fy,
                 double skew,
                 double cx,
                 double cy,
                 double... radial)` 

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
`**set**(double fx,
   double fy,
   double skew,
   double cx,
   double cy,
   double[] radial)`
Specify camera calibration parameters

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AddRadialPtoP_F64

```
public AddRadialPtoP_F64()
```

    - 

#### AddRadialPtoP_F64

```
public AddRadialPtoP_F64(double fx,
                 double fy,
                 double skew,
                 double cx,
                 double cy,
                 double... radial)
```

  - 

### Method Detail

    - 

#### set

```
public void set(double fx,
       double fy,
       double skew,
       double cx,
       double cy,
       double[] radial)
```

Specify camera calibration parameters
Parameters:`fx` - Focal length x-axis in pixels`fy` - Focal length y-axis in pixels`skew` - skew in pixels`cx` - camera center x-axis in pixels`cy` - center center y-axis in pixels`radial` - Radial distortion parameters

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
Parameters:`x` - Undistorted x-coordinate pixel`y` - Undistorted y-coordinate pixel`out` - Distorted pixel coordinate.

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