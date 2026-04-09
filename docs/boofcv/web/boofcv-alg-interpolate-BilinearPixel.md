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

boofcv.alg.interpolate

## Class BilinearPixel<T extends ImageSingleBand>

- java.lang.Object

- 

  - boofcv.alg.interpolate.BilinearPixel<T>

- 

All Implemented Interfaces:
InterpolatePixel<T>

Direct Known Subclasses:
ImplBilinearPixel_F32, ImplBilinearPixel_S16, ImplBilinearPixel_S32, ImplBilinearPixel_U8

---

```
public abstract class BilinearPixel<T extends ImageSingleBand>
extends java.lang.Object
implements InterpolatePixel<T>
```

 Performs bilinear interpolation to extract values between pixels in an image.  When a boundary is encountered
 the number of pixels used to interpolate is automatically reduced.
 
Author:
  Peter Abeles

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`protected int`
`**height**` 

`protected T`
`**orig**` 

`protected int`
`**stride**` 

`protected int`
`**width**` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BilinearPixel**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`T`
`**getImage**()`
Returns the image which is being interpolated.

`int`
`**getUnsafeBorderX**()`
Border around the image that `InterpolatePixel.get_unsafe(float, float)` cannot be called.

`int`
`**getUnsafeBorderY**()`
Border around the image that `InterpolatePixel.get_unsafe(float, float)` cannot be called.

`boolean`
`**isInSafeBounds**(float x,
              float y)`
Is the requested pixel inside the image bounds in which get_unsafe() can be called without throwing
 an exception?

`void`
`**setImage**(T image)`
Change the image that is being interpolated.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

    - 

### Methods inherited from interface boofcv.alg.interpolate.InterpolatePixel

`get_unsafe, get`

- 

  - 

### Field Detail

    - 

#### orig

```
protected T extends ImageSingleBand orig
```

    - 

#### stride

```
protected int stride
```

    - 

#### width

```
protected int width
```

    - 

#### height

```
protected int height
```

  - 

### Constructor Detail

    - 

#### BilinearPixel

```
public BilinearPixel()
```

  - 

### Method Detail

    - 

#### setImage

```
public void setImage(T image)
```

**Description copied from interface: `InterpolatePixel`**
Change the image that is being interpolated.

**Specified by:**
`setImage` in interface `InterpolatePixel<T extends ImageSingleBand>`
Parameters:`image` - An image.

    - 

#### getImage

```
public T getImage()
```

**Description copied from interface: `InterpolatePixel`**
Returns the image which is being interpolated.

**Specified by:**
`getImage` in interface `InterpolatePixel<T extends ImageSingleBand>`
Returns:A reference to the image being interpolated.

    - 

#### isInSafeBounds

```
public boolean isInSafeBounds(float x,
                     float y)
```

**Description copied from interface: `InterpolatePixel`**
Is the requested pixel inside the image bounds in which get_unsafe() can be called without throwing
 an exception?

**Specified by:**
`isInSafeBounds` in interface `InterpolatePixel<T extends ImageSingleBand>`
Parameters:`x` - Point's x-coordinate.`y` - Point's y-coordinate.
Returns:true if get_unsafe() can be called.

    - 

#### getUnsafeBorderX

```
public int getUnsafeBorderX()
```

**Description copied from interface: `InterpolatePixel`**
Border around the image that `InterpolatePixel.get_unsafe(float, float)` cannot be called.

**Specified by:**
`getUnsafeBorderX` in interface `InterpolatePixel<T extends ImageSingleBand>`
Returns:Border size in pixels

    - 

#### getUnsafeBorderY

```
public int getUnsafeBorderY()
```

**Description copied from interface: `InterpolatePixel`**
Border around the image that `InterpolatePixel.get_unsafe(float, float)` cannot be called.

**Specified by:**
`getUnsafeBorderY` in interface `InterpolatePixel<T extends ImageSingleBand>`
Returns:Border size in pixels

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