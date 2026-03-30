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

boofcv.abst.filter.blur

## Class BlurStorageFilter<T extends ImageSingleBand>

- java.lang.Object

- 

  - boofcv.abst.filter.blur.BlurStorageFilter<T>

- 

All Implemented Interfaces:
BlurFilter<T>, FilterImageInterface<T,T>

---

```
public class BlurStorageFilter<T extends ImageSingleBand>
extends java.lang.Object
implements BlurFilter<T>
```

Simplified interface for using a blur filter that requires storage.  Reflections are used to look up a function inside
 of `BlurImageOps` which is then invoked later on.
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BlurStorageFilter**(java.lang.String functionName,
                 java.lang.Class<T> inputType,
                 double sigma,
                 int radius)` 

`**BlurStorageFilter**(java.lang.String functionName,
                 java.lang.Class<T> inputType,
                 int radius)` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`int`
`**getHorizontalBorder**()`
How many pixels are not processed along the horizontal border.

`java.lang.Class<T>`
`**getInputType**()`
Specifies the type of image it takes as input.

`int`
`**getRadius**()`
Radius of the square region.

`int`
`**getVerticalBorder**()`
How many pixels are not processed along the vertical border.

`void`
`**process**(T input,
       T output)`
Processes the input image and writes the results to the output image.

`void`
`**setRadius**(int radius)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BlurStorageFilter

```
public BlurStorageFilter(java.lang.String functionName,
                 java.lang.Class<T> inputType,
                 int radius)
```

    - 

#### BlurStorageFilter

```
public BlurStorageFilter(java.lang.String functionName,
                 java.lang.Class<T> inputType,
                 double sigma,
                 int radius)
```

  - 

### Method Detail

    - 

#### getRadius

```
public int getRadius()
```

Radius of the square region.  The width is defined as the radius*2 + 1.

**Specified by:**
`getRadius` in interface `BlurFilter<T extends ImageSingleBand>`
Returns:Blur region's radius.

    - 

#### setRadius

```
public void setRadius(int radius)
```

**Specified by:**
`setRadius` in interface `BlurFilter<T extends ImageSingleBand>`

    - 

#### process

```
public void process(T input,
           T output)
```

**Description copied from interface: `FilterImageInterface`**
Processes the input image and writes the results to the output image.

**Specified by:**
`process` in interface `FilterImageInterface<T extends ImageSingleBand,T extends ImageSingleBand>`
Parameters:`input` - Input image.`output` - Output image.

    - 

#### getHorizontalBorder

```
public int getHorizontalBorder()
```

**Description copied from interface: `FilterImageInterface`**
How many pixels are not processed along the horizontal border.

**Specified by:**
`getHorizontalBorder` in interface `FilterImageInterface<T extends ImageSingleBand,T extends ImageSingleBand>`
Returns:Border size in pixels.

    - 

#### getVerticalBorder

```
public int getVerticalBorder()
```

**Description copied from interface: `FilterImageInterface`**
How many pixels are not processed along the vertical border.

**Specified by:**
`getVerticalBorder` in interface `FilterImageInterface<T extends ImageSingleBand,T extends ImageSingleBand>`
Returns:Border size in pixels.

    - 

#### getInputType

```
public java.lang.Class<T> getInputType()
```

**Description copied from interface: `FilterImageInterface`**
Specifies the type of image it takes as input.

**Specified by:**
`getInputType` in interface `FilterImageInterface<T extends ImageSingleBand,T extends ImageSingleBand>`
Returns:Input image type.

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