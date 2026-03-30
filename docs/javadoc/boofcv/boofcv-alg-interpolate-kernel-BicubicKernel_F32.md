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

boofcv.alg.interpolate.kernel

## Class BicubicKernel_F32

- java.lang.Object

- 

  - boofcv.struct.convolve.KernelBase

  - 

    - boofcv.struct.convolve.Kernel1D

    - 

      - boofcv.struct.convolve.KernelContinuous1D_F32

      - 

        - boofcv.alg.interpolate.kernel.BicubicKernel_F32

- 

---

```
public class BicubicKernel_F32
extends KernelContinuous1D_F32
```

 A kernel can be used to approximate bicubic interpolation.  Full bicubic interpolation is much more expensive.
 The value of a=-0.5 is the best approximation.
 

 

 

 
  - R. Keys, (1981). "Cubic convolution interpolation for digital image processing".
 IEEE Transactions on Signal Processing, Acoustics, Speech, and Signal Processing 29: 1153 
 
  - http://en.wikipedia.org/wiki/Bicubic_interpolation for more information.  July 25, 2011
 

 
Author:
  Peter Abeles

- 

  - 

### Field Summary

    - 

### Fields inherited from class boofcv.struct.convolve.KernelBase

`width`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BicubicKernel_F32**(float a)`
Values of a =-0.5 and -0.75 are typical

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`float`
`**compute**(float x)`
Computes the value of the kernel at hte specified point.

`boolean`
`**isInteger**()` 

    - 

### Methods inherited from class boofcv.struct.convolve.Kernel1D

`getDimension`

    - 

### Methods inherited from class boofcv.struct.convolve.KernelBase

`getRadius, getWidth`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BicubicKernel_F32

```
public BicubicKernel_F32(float a)
```

Values of a =-0.5 and -0.75 are typical
Parameters:`a` - A parameter

  - 

### Method Detail

    - 

#### isInteger

```
public boolean isInteger()
```

**Specified by:**
`isInteger` in class `KernelBase`

    - 

#### compute

```
public float compute(float x)
```

**Description copied from class: `KernelContinuous1D_F32`**
Computes the value of the kernel at hte specified point.

**Specified by:**
`compute` in class `KernelContinuous1D_F32`
Parameters:`x` - Function's input.
Returns:Function's value at point 'x'

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