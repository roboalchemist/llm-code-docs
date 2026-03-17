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

boofcv.misc

## Class BoofMiscOps

- java.lang.Object

- 

  - boofcv.misc.BoofMiscOps

- 

---

```
public class BoofMiscOps
extends java.lang.Object
```

Miscellaneous functions which have no better place to go.
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BoofMiscOps**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`static void`
`**boundRectangleInside**(ImageBase b,
                    ImageRectangle r)`
Bounds the provided rectangle to be inside the image.

`static boolean`
`**checkInside**(ImageBase b,
           double x,
           double y,
           double radius)`
Returns true if the point is contained inside the image and 'radius' away from the image border.

`static boolean`
`**checkInside**(ImageBase b,
           float x,
           float y,
           float radius)`
Returns true if the point is contained inside the image and 'radius' away from the image border.

`static boolean`
`**checkInside**(ImageBase b,
           ImageRectangle r)` 

`static boolean`
`**checkInside**(ImageBase b,
           int x,
           int y,
           int radius)`
Returns true if the point is contained inside the image and 'radius' away from the image border.

`static boolean`
`**checkInside**(ImageBase b,
           int c_x,
           int c_y,
           int radius,
           double theta)` 

`static boolean`
`**checkInside**(ImageBase b,
           int x,
           int y,
           int radiusWidth,
           int radiusHeight)` 

`static float[]`
`**convertTo_F32**(double[] a,
             float[] ret)` 

`static double[]`
`**convertTo_F64**(int[] a)` 

`static int[]`
`**convertTo_I32**(double[] a,
             int[] ret)` 

`static int`
`**countNotZero**(int[] a,
            int size)` 

`static java.util.List<java.lang.String>`
`**directoryList**(java.lang.String directory,
             java.lang.String prefix)`
Loads a list of files with the specified prefix.

`static <T> T`
`**loadXML**(java.io.Reader r)` 

`static <T> T`
`**loadXML**(java.lang.String fileName)` 

`static void`
`**pause**(long milli)`
Invokes wait until the elapsed time has passed.

`static void`
`**print**(ImageFloat32 a)` 

`static void`
`**print**(ImageFloat64 a)` 

`static void`
`**print**(ImageInteger a)` 

`static void`
`**print**(ImageSingleBand a)` 

`static void`
`**saveXML**(java.lang.Object o,
       java.lang.String fileName)` 

`static java.lang.String`
`**toString**(java.io.Reader r)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BoofMiscOps

```
public BoofMiscOps()
```

  - 

### Method Detail

    - 

#### saveXML

```
public static void saveXML(java.lang.Object o,
           java.lang.String fileName)
```

    - 

#### loadXML

```
public static <T> T loadXML(java.lang.String fileName)
```

    - 

#### loadXML

```
public static <T> T loadXML(java.io.Reader r)
```

    - 

#### toString

```
public static java.lang.String toString(java.io.Reader r)
```

    - 

#### countNotZero

```
public static int countNotZero(int[] a,
               int size)
```

    - 

#### convertTo_F64

```
public static double[] convertTo_F64(int[] a)
```

    - 

#### convertTo_F32

```
public static float[] convertTo_F32(double[] a,
                    float[] ret)
```

    - 

#### convertTo_I32

```
public static int[] convertTo_I32(double[] a,
                  int[] ret)
```

    - 

#### boundRectangleInside

```
public static void boundRectangleInside(ImageBase b,
                        ImageRectangle r)
```

Bounds the provided rectangle to be inside the image.
Parameters:`b` - An image.`r` - Rectangle

    - 

#### checkInside

```
public static boolean checkInside(ImageBase b,
                  ImageRectangle r)
```

    - 

#### checkInside

```
public static boolean checkInside(ImageBase b,
                  int x,
                  int y,
                  int radius)
```

Returns true if the point is contained inside the image and 'radius' away from the image border.
Parameters:`b` - Image`x` - x-coordinate of point`y` - y-coordinate of point`radius` - How many pixels away from the border it needs to be to be considered inside
Returns:true if the point is inside and false if it is outside

    - 

#### checkInside

```
public static boolean checkInside(ImageBase b,
                  float x,
                  float y,
                  float radius)
```

Returns true if the point is contained inside the image and 'radius' away from the image border.
Parameters:`b` - Image`x` - x-coordinate of point`y` - y-coordinate of point`radius` - How many pixels away from the border it needs to be to be considered inside
Returns:true if the point is inside and false if it is outside

    - 

#### checkInside

```
public static boolean checkInside(ImageBase b,
                  double x,
                  double y,
                  double radius)
```

Returns true if the point is contained inside the image and 'radius' away from the image border.
Parameters:`b` - Image`x` - x-coordinate of point`y` - y-coordinate of point`radius` - How many pixels away from the border it needs to be to be considered inside
Returns:true if the point is inside and false if it is outside

    - 

#### checkInside

```
public static boolean checkInside(ImageBase b,
                  int x,
                  int y,
                  int radiusWidth,
                  int radiusHeight)
```

    - 

#### checkInside

```
public static boolean checkInside(ImageBase b,
                  int c_x,
                  int c_y,
                  int radius,
                  double theta)
```

    - 

#### pause

```
public static void pause(long milli)
```

Invokes wait until the elapsed time has passed.  In the thread is interrupted, the interrupt is ignored.
Parameters:`milli` - Length of desired pause in milliseconds.

    - 

#### print

```
public static void print(ImageSingleBand a)
```

    - 

#### print

```
public static void print(ImageFloat64 a)
```

    - 

#### print

```
public static void print(ImageFloat32 a)
```

    - 

#### print

```
public static void print(ImageInteger a)
```

    - 

#### directoryList

```
public static java.util.List<java.lang.String> directoryList(java.lang.String directory,
                                             java.lang.String prefix)
```

Loads a list of files with the specified prefix.
Parameters:`directory` - Directory it looks inside of`prefix` - Prefix that the file must have
Returns:List of files that are in the directory and match the prefix.

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