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

boofcv.alg.filter.misc

## Class AverageDownSampleOps

- java.lang.Object

- 

  - boofcv.alg.filter.misc.AverageDownSampleOps

- 

---

```
public class AverageDownSampleOps
extends java.lang.Object
```

 Operations related to down sampling image by computing the average within square regions. The first square region is
 from (0,0) to
 (w-1,w-1), inclusive.  Each square region after that is found by skipping over 'w' pixels in x and y directions.
 partial regions along the right and bottom borders are handled by computing the average with the rectangle defined
 by the intersection of the image and the square region.
 

 

 NOTE: Errors are reduced in integer images by rounding instead of standard integer division.
 
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AverageDownSampleOps**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`static void`
`**down**(ImageFloat32 input,
    int sampleWidth,
    ImageFloat32 output)`
Down samples the image.

`static void`
`**down**(ImageFloat64 input,
    int sampleWidth,
    ImageFloat64 output)`
Down samples the image.

`static void`
`**down**(ImageSingleBand input,
    int sampleWidth,
    ImageSingleBand output)`
Down samples image.

`static void`
`**down**(ImageSInt16 input,
    int sampleWidth,
    ImageInt16 output)`
Down samples the image.

`static void`
`**down**(ImageSInt32 input,
    int sampleWidth,
    ImageSInt32 output)`
Down samples the image.

`static void`
`**down**(ImageSInt8 input,
    int sampleWidth,
    ImageInt8 output)`
Down samples the image.

`static void`
`**down**(ImageUInt16 input,
    int sampleWidth,
    ImageInt16 output)`
Down samples the image.

`static void`
`**down**(ImageUInt8 input,
    int sampleWidth,
    ImageInt8 output)`
Down samples the image.

`static <T extends ImageSingleBand> 
void`
`**down**(MultiSpectral<T> input,
    int sampleWidth,
    MultiSpectral<T> output)`
Down samples a multi-spectral image.

`static int`
`**downSampleSize**(int length,
              int squareWidth)`
Computes the length of a down sampled image based on the original length and the square width

`static void`
`**reshapeDown**(ImageBase image,
           int inputWidth,
           int inputHeight,
           int squareWidth)`
Reshapes an image so that it is the correct size to store the down sampled image

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AverageDownSampleOps

```
public AverageDownSampleOps()
```

  - 

### Method Detail

    - 

#### downSampleSize

```
public static int downSampleSize(int length,
                 int squareWidth)
```

Computes the length of a down sampled image based on the original length and the square width
Parameters:`length` - Length of side in input image`squareWidth` - Width of region used to down sample images
Returns:Length of side in down sampled image

    - 

#### reshapeDown

```
public static void reshapeDown(ImageBase image,
               int inputWidth,
               int inputHeight,
               int squareWidth)
```

Reshapes an image so that it is the correct size to store the down sampled image

    - 

#### down

```
public static void down(ImageSingleBand input,
        int sampleWidth,
        ImageSingleBand output)
```

Down samples image.  Type checking is done at runtime.
Parameters:`input` - Input image. Not modified.`sampleWidth` - Width of square region.`output` - Output image. Modified.

    - 

#### down

```
public static <T extends ImageSingleBand> void down(MultiSpectral<T> input,
                                    int sampleWidth,
                                    MultiSpectral<T> output)
```

Down samples a multi-spectral image.  Type checking is done at runtime.
Parameters:`input` - Input image. Not modified.`sampleWidth` - Width of square region.`output` - Output image. Modified.

    - 

#### down

```
public static void down(ImageUInt8 input,
        int sampleWidth,
        ImageInt8 output)
```

Down samples the image.
Parameters:`input` - Input image. Not modified.`sampleWidth` - Width of square region.`output` - Output image. Modified.

    - 

#### down

```
public static void down(ImageSInt8 input,
        int sampleWidth,
        ImageInt8 output)
```

Down samples the image.
Parameters:`input` - Input image. Not modified.`sampleWidth` - Width of square region.`output` - Output image. Modified.

    - 

#### down

```
public static void down(ImageUInt16 input,
        int sampleWidth,
        ImageInt16 output)
```

Down samples the image.
Parameters:`input` - Input image. Not modified.`sampleWidth` - Width of square region.`output` - Output image. Modified.

    - 

#### down

```
public static void down(ImageSInt16 input,
        int sampleWidth,
        ImageInt16 output)
```

Down samples the image.
Parameters:`input` - Input image. Not modified.`sampleWidth` - Width of square region.`output` - Output image. Modified.

    - 

#### down

```
public static void down(ImageSInt32 input,
        int sampleWidth,
        ImageSInt32 output)
```

Down samples the image.
Parameters:`input` - Input image. Not modified.`sampleWidth` - Width of square region.`output` - Output image. Modified.

    - 

#### down

```
public static void down(ImageFloat32 input,
        int sampleWidth,
        ImageFloat32 output)
```

Down samples the image.
Parameters:`input` - Input image. Not modified.`sampleWidth` - Width of square region.`output` - Output image. Modified.

    - 

#### down

```
public static void down(ImageFloat64 input,
        int sampleWidth,
        ImageFloat64 output)
```

Down samples the image.
Parameters:`input` - Input image. Not modified.`sampleWidth` - Width of square region.`output` - Output image. Modified.

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