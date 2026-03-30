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

boofcv.testing

## Class BoofTesting

- java.lang.Object

- 

  - boofcv.testing.BoofTesting

- 

---

```
public class BoofTesting
extends java.lang.Object
```

Functions to aid in unit testing code for correctly handling sub-images
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BoofTesting**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`static void`
`**assertEquals**(double[] a,
            double[] b,
            double tol)` 

`static void`
`**assertEquals**(double[] a,
            float[] b,
            double tol)` 

`static void`
`**assertEquals**(double[] a,
            int[] b)` 

`static void`
`**assertEquals**(float[] a,
            float[] b,
            float tol)` 

`static void`
`**assertEquals**(ImageBase imgA,
            ImageBase imgB,
            double tol)` 

`static void`
`**assertEqualsBorder**(ImageSingleBand imgA,
                  ImageSingleBand imgB,
                  double tol,
                  int borderX,
                  int borderY)`
Checks to see if only the image borders are equal to each other within tolerance

`static void`
`**assertEqualsInner**(ImageBase imgA,
                 ImageBase imgB,
                 double tol,
                 int borderX,
                 int borderY,
                 boolean relative)` 

`static void`
`**assertEqualsRelative**(ImageBase imgA,
                    ImageBase imgB,
                    double tolFrac)` 

`static void`
`**callStaticMethod**(java.lang.Class<?> classType,
                java.lang.String name,
                java.lang.Object... inputs)`
Looks up the static method then passes in the specified inputs.

`static void`
`**checkBorderZero**(ImageSingleBand outputImage,
               int border)` 

`static void`
`**checkEquals**(java.awt.image.BufferedImage imgA,
           ImageBase imgB,
           double tol)` 

`static void`
`**checkEquals**(java.awt.image.BufferedImage imgA,
           ImageFloat32 imgB,
           float tol)`
Checks to see if the BufferedImage has the same intensity values as the ImageUInt8

`static void`
`**checkEquals**(java.awt.image.BufferedImage imgA,
           ImageInterleavedInt8 imgB)`
Checks to see if the BufferedImage has the same intensity values as the ImageUInt8

`static void`
`**checkEquals**(java.awt.image.BufferedImage imgA,
           ImageUInt8 imgB)`
Checks to see if the BufferedImage has the same intensity values as the ImageUInt8

`static void`
`**checkEquals**(java.awt.image.BufferedImage imgA,
           MultiSpectral imgB,
           float tol)` 

`static void`
`**checkImageDimensionValidation**(java.lang.Object testClass,
                             int numFunctions)`
Searches for functions that accept only images and makes sure they only accept
 images which have he same width and height.

`static void`
`**checkSubImage**(java.lang.Object testClass,
             java.lang.String function,
             boolean checkEquals,
             java.lang.Object... inputParam)`
Tests the specified function with the original image provided and with an equivalent
 sub-image.

`static <T> T`
`**convertGenericToSpecificType**(java.lang.Class<?> type)`
If an image is to be created then the generic type can't be used a specific one needs to be.

`static <T> T`
`**convertToGenericType**(java.lang.Class<?> type)` 

`static ImageTypeInfo`
`**convertToGenericType**(ImageTypeInfo<?> type)` 

`static <T extends ImageSingleBand> 
T`
`**createSubImageOf**(T input)`

 Returns an image which is a sub-image but contains the same values of the input image.

`static java.lang.reflect.Method`
`**findMethod**(java.lang.Class<?> type,
          java.lang.String name,
          java.lang.Class<?>... params)`
Searches for a function which is a perfect match.

`static int`
`**findMethodThenCall**(java.lang.Object owner,
                  java.lang.String ownerMethod,
                  java.lang.Class target,
                  java.lang.String targetMethod)`
Searches for all functions with the specified name in the target class.

`static void`
`**printDiff**(ImageSingleBand imgA,
         ImageSingleBand imgB)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BoofTesting

```
public BoofTesting()
```

  - 

### Method Detail

    - 

#### convertToGenericType

```
public static <T> T convertToGenericType(java.lang.Class<?> type)
```

    - 

#### convertToGenericType

```
public static ImageTypeInfo convertToGenericType(ImageTypeInfo<?> type)
```

    - 

#### convertGenericToSpecificType

```
public static <T> T convertGenericToSpecificType(java.lang.Class<?> type)
```

If an image is to be created then the generic type can't be used a specific one needs to be.  An arbitrary
 specific image type is returned here.

    - 

#### createSubImageOf

```
public static <T extends ImageSingleBand> T createSubImageOf(T input)
```

 Returns an image which is a sub-image but contains the same values of the input image.  Use for
 testing compliance with sub-images.  The subimage is created by creating a larger image,
 copying over the input image into the inner portion, then creating a subimage of the copied part.
 

    - 

#### checkImageDimensionValidation

```
public static void checkImageDimensionValidation(java.lang.Object testClass,
                                 int numFunctions)
```

Searches for functions that accept only images and makes sure they only accept
 images which have he same width and height.
Parameters:`testClass` - Instance of the class being tested

    - 

#### checkSubImage

```
public static void checkSubImage(java.lang.Object testClass,
                 java.lang.String function,
                 boolean checkEquals,
                 java.lang.Object... inputParam)
```

Tests the specified function with the original image provided and with an equivalent
 sub-image.  The two results are then compared. The function being tested must only
 have one input parameter of type `ImageUInt8`.
Parameters:`testClass` - Instance of the class that contains the function being tested.`function` - The name of the function being tested.`checkEquals` - Checks to see if the two images have been modified the same way on output`inputParam` - The original input parameters

    - 

#### findMethod

```
public static java.lang.reflect.Method findMethod(java.lang.Class<?> type,
                                  java.lang.String name,
                                  java.lang.Class<?>... params)
```

Searches for a function which is a perfect match.  if none it exists it checks
 to see if any matches that could accept an input of the specified type.  If there
 is only one such match that is returned.

    - 

#### callStaticMethod

```
public static void callStaticMethod(java.lang.Class<?> classType,
                    java.lang.String name,
                    java.lang.Object... inputs)
```

Looks up the static method then passes in the specified inputs.

    - 

#### findMethodThenCall

```
public static int findMethodThenCall(java.lang.Object owner,
                     java.lang.String ownerMethod,
                     java.lang.Class target,
                     java.lang.String targetMethod)
```

Searches for all functions with the specified name in the target class.  Once it finds
 that function it invokes the specified function in the owner class. That function must
 take in a Method as its one and only parameter.  The method will be one of the matching
 ones in the target class.
Parameters:`owner` - `ownerMethod` - `target` - `targetMethod` - 
Returns:The number of times 'targetMethod' was found and called.

    - 

#### assertEquals

```
public static void assertEquals(double[] a,
                double[] b,
                double tol)
```

    - 

#### assertEquals

```
public static void assertEquals(double[] a,
                float[] b,
                double tol)
```

    - 

#### assertEquals

```
public static void assertEquals(double[] a,
                int[] b)
```

    - 

#### assertEquals

```
public static void assertEquals(float[] a,
                float[] b,
                float tol)
```

    - 

#### assertEquals

```
public static void assertEquals(ImageBase imgA,
                ImageBase imgB,
                double tol)
```

    - 

#### assertEqualsInner

```
public static void assertEqualsInner(ImageBase imgA,
                     ImageBase imgB,
                     double tol,
                     int borderX,
                     int borderY,
                     boolean relative)
```

    - 

#### assertEqualsRelative

```
public static void assertEqualsRelative(ImageBase imgA,
                        ImageBase imgB,
                        double tolFrac)
```

    - 

#### assertEqualsBorder

```
public static void assertEqualsBorder(ImageSingleBand imgA,
                      ImageSingleBand imgB,
                      double tol,
                      int borderX,
                      int borderY)
```

Checks to see if only the image borders are equal to each other within tolerance

    - 

#### checkEquals

```
public static void checkEquals(java.awt.image.BufferedImage imgA,
               ImageBase imgB,
               double tol)
```

    - 

#### checkEquals

```
public static void checkEquals(java.awt.image.BufferedImage imgA,
               ImageUInt8 imgB)
```

Checks to see if the BufferedImage has the same intensity values as the ImageUInt8
Parameters:`imgA` - BufferedImage`imgB` - ImageUInt8

    - 

#### checkEquals

```
public static void checkEquals(java.awt.image.BufferedImage imgA,
               ImageFloat32 imgB,
               float tol)
```

Checks to see if the BufferedImage has the same intensity values as the ImageUInt8
Parameters:`imgA` - BufferedImage`imgB` - ImageUInt8

    - 

#### checkEquals

```
public static void checkEquals(java.awt.image.BufferedImage imgA,
               ImageInterleavedInt8 imgB)
```

Checks to see if the BufferedImage has the same intensity values as the ImageUInt8
Parameters:`imgA` - BufferedImage`imgB` - ImageUInt8

    - 

#### checkEquals

```
public static void checkEquals(java.awt.image.BufferedImage imgA,
               MultiSpectral imgB,
               float tol)
```

    - 

#### checkBorderZero

```
public static void checkBorderZero(ImageSingleBand outputImage,
                   int border)
```

    - 

#### printDiff

```
public static void printDiff(ImageSingleBand imgA,
             ImageSingleBand imgB)
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