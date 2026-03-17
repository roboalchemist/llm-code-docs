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

## Interface BlurFilter<T extends ImageSingleBand>

- 

All Superinterfaces:
FilterImageInterface<T,T>

All Known Implementing Classes:
BlurStorageFilter, MedianImageFilter

---

```
public interface BlurFilter<T extends ImageSingleBand>
extends FilterImageInterface<T,T>
```

Interface for filters which blur the image.
Author:
  Peter Abeles

- 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`int`
`**getRadius**()`
Radius of the square region.

`void`
`**setRadius**(int radius)` 

    - 

### Methods inherited from interface boofcv.abst.filter.FilterImageInterface

`getHorizontalBorder, getInputType, getVerticalBorder, process`

- 

  - 

### Method Detail

    - 

#### getRadius

```
int getRadius()
```

Radius of the square region.  The width is defined as the radius*2 + 1.
Returns:Blur region's radius.

    - 

#### setRadius

```
void setRadius(int radius)
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