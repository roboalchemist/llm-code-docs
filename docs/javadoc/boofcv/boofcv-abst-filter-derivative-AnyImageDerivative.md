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

boofcv.abst.filter.derivative

## Class AnyImageDerivative<I extends ImageSingleBand,D extends ImageSingleBand>

- java.lang.Object

- 

  - boofcv.abst.filter.derivative.AnyImageDerivative<I,D>

- 

---

```
public class AnyImageDerivative<I extends ImageSingleBand,D extends ImageSingleBand>
extends java.lang.Object
```

 A helpful class which allows a derivative of any order to be computed from an input image using a simple to use
 interface.  Higher order derivatives are computed from lower order derivatives.  Derivatives are computed
 using convolution kernels and thus might not be as efficient as when using functions from `FactoryDerivative`.
 
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AnyImageDerivative**(ConvolveInterface<I,D> derivX,
                  ConvolveInterface<I,D> derivY,
                  ConvolveInterface<D,D> derivXX,
                  ConvolveInterface<D,D> derivYY,
                  java.lang.Class<I> inputType,
                  ImageGenerator<D> derivGen)`
Constructor for when all derivative filters are specified

`**AnyImageDerivative**(Kernel1D deriv,
                  java.lang.Class<I> inputType,
                  ImageGenerator<D> derivGen)`
Constructor for 1D kernels.

`**AnyImageDerivative**(Kernel2D derivX,
                  java.lang.Class<I> inputType,
                  ImageGenerator<D> derivGen)`
Constructor for 2D kernels.

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`D`
`**getDerivative**(boolean... isX)`
Computes derivative images using previously computed lower level derivatives.

`void`
`**setInput**(I input)`
Sets the new input image from which the image derivatives are computed from.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AnyImageDerivative

```
public AnyImageDerivative(Kernel1D deriv,
                  java.lang.Class<I> inputType,
                  ImageGenerator<D> derivGen)
```

Constructor for 1D kernels.
Parameters:`deriv` - 1D convolution kernel for computing derivative along x and y axises.`inputType` - The type of input image.`derivGen` - Generator for derivative images.

    - 

#### AnyImageDerivative

```
public AnyImageDerivative(Kernel2D derivX,
                  java.lang.Class<I> inputType,
                  ImageGenerator<D> derivGen)
```

Constructor for 2D kernels.
Parameters:`derivX` - 2D convolution kernel for computing derivative along x axis`inputType` - The type of input image.`derivGen` - Generator for derivative images.

    - 

#### AnyImageDerivative

```
public AnyImageDerivative(ConvolveInterface<I,D> derivX,
                  ConvolveInterface<I,D> derivY,
                  ConvolveInterface<D,D> derivXX,
                  ConvolveInterface<D,D> derivYY,
                  java.lang.Class<I> inputType,
                  ImageGenerator<D> derivGen)
```

Constructor for when all derivative filters are specified
Parameters:`derivX` - Filter for computing derivative along x axis from input image.`derivY` - Filter for computing derivative along y axis from input image.`derivXX` - Filter for computing derivative along x axis from input image.`derivYY` - Filter for computing derivative along y axis from input image.`inputType` - The type of input image.`derivGen` - Generator for derivative images.

  - 

### Method Detail

    - 

#### setInput

```
public void setInput(I input)
```

Sets the new input image from which the image derivatives are computed from.
Parameters:`input` - Input image.

    - 

#### getDerivative

```
public D getDerivative(boolean... isX)
```

Computes derivative images using previously computed lower level derivatives.  Only
 computes/declares images as needed.

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