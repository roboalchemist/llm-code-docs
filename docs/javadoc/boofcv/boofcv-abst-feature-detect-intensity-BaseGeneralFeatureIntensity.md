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

boofcv.abst.feature.detect.intensity

## Class BaseGeneralFeatureIntensity<I extends ImageSingleBand,D extends ImageSingleBand>

- java.lang.Object

- 

  - boofcv.abst.feature.detect.intensity.BaseGeneralFeatureIntensity<I,D>

- 

All Implemented Interfaces:
GeneralFeatureIntensity<I,D>

Direct Known Subclasses:
WrapperFastCornerIntensity, WrapperGradientCornerIntensity, WrapperHessianBlobIntensity, WrapperKitRosCornerIntensity, WrapperLaplacianBlobIntensity, WrapperMedianCornerIntensity

---

```
public abstract class BaseGeneralFeatureIntensity<I extends ImageSingleBand,D extends ImageSingleBand>
extends java.lang.Object
implements GeneralFeatureIntensity<I,D>
```

Provides some basic functionality for implementing `GeneralFeatureIntensity`.
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BaseGeneralFeatureIntensity**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`ImageFloat32`
`**getIntensity**()`
Returns an image containing an intensity mapping showing how corner like each pixel is.

`void`
`**init**(int width,
    int height)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

    - 

### Methods inherited from interface boofcv.abst.feature.detect.intensity.GeneralFeatureIntensity

`getCandidatesMax, getCandidatesMin, getIgnoreBorder, getRequiresGradient, getRequiresHessian, hasCandidates, localMaximums, localMinimums, process`

- 

  - 

### Constructor Detail

    - 

#### BaseGeneralFeatureIntensity

```
public BaseGeneralFeatureIntensity()
```

  - 

### Method Detail

    - 

#### init

```
public void init(int width,
        int height)
```

    - 

#### getIntensity

```
public ImageFloat32 getIntensity()
```

**Description copied from interface: `GeneralFeatureIntensity`**
Returns an image containing an intensity mapping showing how corner like each pixel is.
 Unprocessed image borders will have a value of zero.

**Specified by:**
`getIntensity` in interface `GeneralFeatureIntensity<I extends ImageSingleBand,D extends ImageSingleBand>`
Returns:Corner intensity image.

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