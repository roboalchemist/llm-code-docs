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

boofcv.alg.interpolate.impl

## Class BilinearRectangle_U8

- java.lang.Object

- 

  - boofcv.alg.interpolate.impl.BilinearRectangle_U8

- 

All Implemented Interfaces:
InterpolateRectangle<ImageUInt8>

---

```
public class BilinearRectangle_U8
extends java.lang.Object
implements InterpolateRectangle<ImageUInt8>
```

 Performs bilinear interpolation to extract values between pixels in an image.
 Image borders are detected and handled appropriately.
 

 

 NOTE: This code was automatically generated using `GenerateBilinearRectangle`.
 
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BilinearRectangle_U8**()` 

`**BilinearRectangle_U8**(ImageUInt8 image)` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`ImageUInt8`
`**getImage**()`
Returns the image which is being interpolated.

`void`
`**region**(float tl_x,
      float tl_y,
      ImageFloat32 output)`
Copies a grid from the source image starting at the specified coordinate
 into the destination image.

`void`
`**setImage**(ImageUInt8 image)`
Change the image that is being interpolated.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BilinearRectangle_U8

```
public BilinearRectangle_U8(ImageUInt8 image)
```

    - 

#### BilinearRectangle_U8

```
public BilinearRectangle_U8()
```

  - 

### Method Detail

    - 

#### setImage

```
public void setImage(ImageUInt8 image)
```

**Description copied from interface: `InterpolateRectangle`**
Change the image that is being interpolated.

**Specified by:**
`setImage` in interface `InterpolateRectangle<ImageUInt8>`
Parameters:`image` - An image.

    - 

#### getImage

```
public ImageUInt8 getImage()
```

**Description copied from interface: `InterpolateRectangle`**
Returns the image which is being interpolated.

**Specified by:**
`getImage` in interface `InterpolateRectangle<ImageUInt8>`
Returns:A reference to the image being interpolated.

    - 

#### region

```
public void region(float tl_x,
          float tl_y,
          ImageFloat32 output)
```

**Description copied from interface: `InterpolateRectangle`**
Copies a grid from the source image starting at the specified coordinate
 into the destination image.  The 'dest' image must be within the original image.

**Specified by:**
`region` in interface `InterpolateRectangle<ImageUInt8>`
Parameters:`tl_x` - upper left corner of the region in the image.`tl_y` - upper left corner of the region in the image.`output` - Where the interpolated region is to be copied into

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