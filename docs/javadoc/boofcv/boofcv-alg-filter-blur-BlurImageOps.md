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

boofcv.alg.filter.blur

## Class BlurImageOps

- java.lang.Object

- 

  - boofcv.alg.filter.blur.BlurImageOps

- 

---

```
public class BlurImageOps
extends java.lang.Object
```

Catch all class for function which "blur" an image, typically used to "reduce" the amount
 of noise in the image.
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BlurImageOps**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`static ImageFloat32`
`**gaussian**(ImageFloat32 input,
        ImageFloat32 output,
        double sigma,
        int radius,
        ImageFloat32 storage)`
Applies Gaussian blur.

`static ImageUInt8`
`**gaussian**(ImageUInt8 input,
        ImageUInt8 output,
        double sigma,
        int radius,
        ImageUInt8 storage)`
Applies Gaussian blur.

`static ImageFloat32`
`**mean**(ImageFloat32 input,
    ImageFloat32 output,
    int radius,
    ImageFloat32 storage)`
Applies a mean box filter.

`static ImageUInt8`
`**mean**(ImageUInt8 input,
    ImageUInt8 output,
    int radius,
    ImageUInt8 storage)`
Applies a mean box filter.

`static ImageFloat32`
`**median**(ImageFloat32 input,
      ImageFloat32 output,
      int radius)`
Applies a median filter.

`static ImageUInt8`
`**median**(ImageUInt8 input,
      ImageUInt8 output,
      int radius)`
Applies a median filter.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BlurImageOps

```
public BlurImageOps()
```

  - 

### Method Detail

    - 

#### mean

```
public static ImageUInt8 mean(ImageUInt8 input,
              ImageUInt8 output,
              int radius,
              ImageUInt8 storage)
```

Applies a mean box filter.
Parameters:`input` - Input image.  Not modified.`output` - (Optional) Storage for output image, Can be null.  Modified.`radius` - Radius of the box blur function.`storage` - (Optional) Storage for intermediate results.  Same size as input image.  Can be null.
Returns:Output blurred image.

    - 

#### median

```
public static ImageUInt8 median(ImageUInt8 input,
                ImageUInt8 output,
                int radius)
```

Applies a median filter.
Parameters:`input` - Input image.  Not modified.`output` - (Optional) Storage for output image, Can be null.  Modified.`radius` - Radius of the median blur function.
Returns:Output blurred image.

    - 

#### gaussian

```
public static ImageUInt8 gaussian(ImageUInt8 input,
                  ImageUInt8 output,
                  double sigma,
                  int radius,
                  ImageUInt8 storage)
```

Applies Gaussian blur.
Parameters:`input` - Input image.  Not modified.`output` - (Optional) Storage for output image, Can be null.  Modified.`sigma` - Gaussian distribution's sigma.  If <= 0 then will be selected based on radius.`radius` - Radius of the Gaussian blur function. If <= 0 then radius will be determined by sigma.`storage` - (Optional) Storage for intermediate results.  Same size as input image.  Can be null.
Returns:Output blurred image.

    - 

#### mean

```
public static ImageFloat32 mean(ImageFloat32 input,
                ImageFloat32 output,
                int radius,
                ImageFloat32 storage)
```

Applies a mean box filter.
Parameters:`input` - Input image.  Not modified.`output` - (Optional) Storage for output image, Can be null.  Modified.`radius` - Radius of the box blur function.`storage` - (Optional) Storage for intermediate results.  Same size as input image.  Can be null.
Returns:Output blurred image.

    - 

#### median

```
public static ImageFloat32 median(ImageFloat32 input,
                  ImageFloat32 output,
                  int radius)
```

Applies a median filter.
Parameters:`input` - Input image.  Not modified.`output` - (Optional) Storage for output image, Can be null.  Modified.`radius` - Radius of the median blur function.
Returns:Output blurred image.

    - 

#### gaussian

```
public static ImageFloat32 gaussian(ImageFloat32 input,
                    ImageFloat32 output,
                    double sigma,
                    int radius,
                    ImageFloat32 storage)
```

Applies Gaussian blur.
Parameters:`input` - Input image.  Not modified.`output` - (Optional) Storage for output image, Can be null.  Modified.`sigma` - Gaussian distribution's sigma.  If <= 0 then will be selected based on radius.`radius` - Radius of the Gaussian blur function. If <= 0 then radius will be determined by sigma.`storage` - (Optional) Storage for intermediate results.  Same size as input image.  Can be null.
Returns:Output blurred image.

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