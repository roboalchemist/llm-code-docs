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

boofcv.alg.filter.binary

## Class BinaryImageOps

- java.lang.Object

- 

  - boofcv.alg.filter.binary.BinaryImageOps

- 

---

```
public class BinaryImageOps
extends java.lang.Object
```

 Contains a standard set of operations performed on binary images. A pixel has a value of false if it is equal
 to zero or true equal to one.
 

 

 NOTE: If an element's value is not zero or one then each function's behavior is undefined.
 
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BinaryImageOps**()` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`static void`
`**clusterToBinary**(java.util.List<java.util.List<Point2D_I32>> clusters,
               ImageUInt8 binary)`
Sets each pixel in the list of clusters to one in the binary image.

`static java.util.List<Contour>`
`**contour**(ImageUInt8 input,
       int rule,
       ImageSInt32 output)`

 Given a binary image, connect together pixels to form blobs/clusters using the specified connectivity rule.

`static ImageUInt8`
`**dilate4**(ImageUInt8 input,
       ImageUInt8 output)`

 Dilates an image according to a 4-neighborhood.

`static ImageUInt8`
`**dilate8**(ImageUInt8 input,
       ImageUInt8 output)`

 Dilates an image according to a 8-neighborhood.

`static ImageUInt8`
`**edge4**(ImageUInt8 input,
     ImageUInt8 output)`

 Binary operation which is designed to remove all pixels but ones which are on the edge of an object.

`static ImageUInt8`
`**edge8**(ImageUInt8 input,
     ImageUInt8 output)`

 Binary operation which is designed to remove all pixels but ones which are on the edge of an object.

`static ImageUInt8`
`**erode4**(ImageUInt8 input,
      ImageUInt8 output)`

 Erodes an image according to a 4-neighborhood.

`static ImageUInt8`
`**erode8**(ImageUInt8 input,
      ImageUInt8 output)`

 Erodes an image according to a 8-neighborhood.

`static ImageUInt8`
`**labelToBinary**(ImageSInt32 labelImage,
             ImageUInt8 binaryImage)`
Converts a labeled image into a binary image by setting any non-zero value to one.

`static ImageUInt8`
`**labelToBinary**(ImageSInt32 labelImage,
             ImageUInt8 binaryImage,
             boolean[] selectedBlobs)`
Only converts the specified blobs over into the binary image

`static java.util.List<java.util.List<Point2D_I32>>`
`**labelToClusters**(ImageSInt32 labelImage,
               int numLabels,
               FastQueue<Point2D_I32> queue)`
Scans through the labeled image and adds the coordinate of each pixel that has been
 labeled to a list specific to its label.

`static ImageUInt8`
`**logicAnd**(ImageUInt8 inputA,
        ImageUInt8 inputB,
        ImageUInt8 output)`
For each pixel it applies the logical 'and' operator between two images.

`static ImageUInt8`
`**logicOr**(ImageUInt8 inputA,
       ImageUInt8 inputB,
       ImageUInt8 output)`
For each pixel it applies the logical 'or' operator between two images.

`static ImageUInt8`
`**logicXor**(ImageUInt8 inputA,
        ImageUInt8 inputB,
        ImageUInt8 output)`
For each pixel it applies the logical 'xor' operator between two images.

`static void`
`**relabel**(ImageSInt32 input,
       int[] labels)`
Used to change the labels in a labeled binary image.

`static ImageUInt8`
`**removePointNoise**(ImageUInt8 input,
                ImageUInt8 output)`
Binary operation which is designed to remove small bits of spurious noise.

`static int[]`
`**selectRandomColors**(int numBlobs,
                  java.util.Random rand)`
Several blob rending functions take in an array of colors so that the random blobs can be drawn
 with the same color each time.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BinaryImageOps

```
public BinaryImageOps()
```

  - 

### Method Detail

    - 

#### logicAnd

```
public static ImageUInt8 logicAnd(ImageUInt8 inputA,
                  ImageUInt8 inputB,
                  ImageUInt8 output)
```

For each pixel it applies the logical 'and' operator between two images.
Parameters:`inputA` - First input image. Not modified.`inputB` - Second input image. Not modified.`output` - Output image. Can be same as either input.  If null a new instance will be declared, Modified.
Returns:Output of logical operation.

    - 

#### logicOr

```
public static ImageUInt8 logicOr(ImageUInt8 inputA,
                 ImageUInt8 inputB,
                 ImageUInt8 output)
```

For each pixel it applies the logical 'or' operator between two images.
Parameters:`inputA` - First input image. Not modified.`inputB` - Second input image. Not modified.`output` - Output image. Can be same as either input.  If null a new instance will be declared, Modified.
Returns:Output of logical operation.

    - 

#### logicXor

```
public static ImageUInt8 logicXor(ImageUInt8 inputA,
                  ImageUInt8 inputB,
                  ImageUInt8 output)
```

For each pixel it applies the logical 'xor' operator between two images.
Parameters:`inputA` - First input image. Not modified.`inputB` - Second input image. Not modified.`output` - Output image. Can be same as either input.  If null a new instance will be declared, Modified.
Returns:Output of logical operation.

    - 

#### erode4

```
public static ImageUInt8 erode4(ImageUInt8 input,
                ImageUInt8 output)
```

 Erodes an image according to a 4-neighborhood.  Unless a pixel is connected to all its neighbors its value
 is set to zero.
 
Parameters:`input` - Input image. Not modified.`output` - If not null, the output image.  If null a new image is declared and returned.  Modified.
Returns:Output image.

    - 

#### dilate4

```
public static ImageUInt8 dilate4(ImageUInt8 input,
                 ImageUInt8 output)
```

 Dilates an image according to a 4-neighborhood.  If a pixel is connected to any other pixel then its output
 value will be one.
 
Parameters:`input` - Input image. Not modified.`output` - If not null, the output image.  If null a new image is declared and returned.  Modified.
Returns:Output image.

    - 

#### edge4

```
public static ImageUInt8 edge4(ImageUInt8 input,
               ImageUInt8 output)
```

 Binary operation which is designed to remove all pixels but ones which are on the edge of an object.
 The edge is defined as lying on the object and not being surrounded by a pixel along a 4-neighborhood.
 
 

 

 NOTE: There are many ways to define an edge, this is just one of them.
 
Parameters:`input` - Input image. Not modified.`output` - If not null, the output image.  If null a new image is declared and returned.  Modified.
Returns:Output image.

    - 

#### erode8

```
public static ImageUInt8 erode8(ImageUInt8 input,
                ImageUInt8 output)
```

 Erodes an image according to a 8-neighborhood.  Unless a pixel is connected to all its neighbors its value
 is set to zero.
 
Parameters:`input` - Input image. Not modified.`output` - If not null, the output image.  If null a new image is declared and returned.  Modified.
Returns:Output image.

    - 

#### dilate8

```
public static ImageUInt8 dilate8(ImageUInt8 input,
                 ImageUInt8 output)
```

 Dilates an image according to a 8-neighborhood.  If a pixel is connected to any other pixel then its output
 value will be one.
 
Parameters:`input` - Input image. Not modified.`output` - If not null, the output image.  If null a new image is declared and returned.  Modified.
Returns:Output image.

    - 

#### edge8

```
public static ImageUInt8 edge8(ImageUInt8 input,
               ImageUInt8 output)
```

 Binary operation which is designed to remove all pixels but ones which are on the edge of an object.
 The edge is defined as lying on the object and not being surrounded by 8 pixels.
 
 

 

 NOTE: There are many ways to define an edge, this is just one of them.
 
Parameters:`input` - Input image. Not modified.`output` - If not null, the output image.  If null a new image is declared and returned.  Modified.
Returns:Output image.

    - 

#### removePointNoise

```
public static ImageUInt8 removePointNoise(ImageUInt8 input,
                          ImageUInt8 output)
```

Binary operation which is designed to remove small bits of spurious noise.  An 8-neighborhood is used.
 If a pixel is connected to less than 2 neighbors then its value zero.  If connected to more than 6 then
 its value is one.  Otherwise it retains its original value.
Parameters:`input` - Input image. Not modified.`output` - If not null, the output image.  If null a new image is declared and returned.  Modified.
Returns:Output image.

    - 

#### contour

```
public static java.util.List<Contour> contour(ImageUInt8 input,
                              int rule,
                              ImageSInt32 output)
```

 Given a binary image, connect together pixels to form blobs/clusters using the specified connectivity rule.
 The found blobs will be labeled in an output image and also described as a set of contours.  Pixels
 in the contours are consecutive order in a clockwise or counter-clockwise direction, depending on the
 implementation.
 

 

 The returned contours are traces of the object.  The trace of an object can be found by marking a point
 with a pen and then marking every point on the contour without removing the pen.  It is possible to have
 the same point multiple times in the contour.
 
Parameters:`input` - Input binary image.  Not modified.`output` - (Optional) Output labeled image. If null, an image will be declared internally.  Modified.
Returns:List of found contours for each blob.See Also:`LinearContourLabelChang2004`

    - 

#### relabel

```
public static void relabel(ImageSInt32 input,
           int[] labels)
```

Used to change the labels in a labeled binary image.
Parameters:`input` - Labeled binary image.`labels` - Look up table where the indexes are the current label and the value are its new value.

    - 

#### labelToBinary

```
public static ImageUInt8 labelToBinary(ImageSInt32 labelImage,
                       ImageUInt8 binaryImage)
```

Converts a labeled image into a binary image by setting any non-zero value to one.
Parameters:`labelImage` - Input image. Not modified.`binaryImage` - Output image. Modified.
Returns:The binary image.

    - 

#### labelToBinary

```
public static ImageUInt8 labelToBinary(ImageSInt32 labelImage,
                       ImageUInt8 binaryImage,
                       boolean[] selectedBlobs)
```

Only converts the specified blobs over into the binary image
Parameters:`labelImage` - Input image. Not modified.`binaryImage` - Output image. Modified.`selectedBlobs` - Each index corresponds to a blob and specifies if it is included or not.
Returns:The binary image.

    - 

#### labelToClusters

```
public static java.util.List<java.util.List<Point2D_I32>> labelToClusters(ImageSInt32 labelImage,
                                                          int numLabels,
                                                          FastQueue<Point2D_I32> queue)
```

Scans through the labeled image and adds the coordinate of each pixel that has been
 labeled to a list specific to its label.
Parameters:`labelImage` - The labeled image.`numLabels` - Number of labeled objects inside the image.`queue` - (Optional) Storage for pixel coordinates.  Improves runtime performance. Can be null.
Returns:List of pixels in each cluster.

    - 

#### clusterToBinary

```
public static void clusterToBinary(java.util.List<java.util.List<Point2D_I32>> clusters,
                   ImageUInt8 binary)
```

Sets each pixel in the list of clusters to one in the binary image.
Parameters:`clusters` - List of all the clusters.`binary` - Output

    - 

#### selectRandomColors

```
public static int[] selectRandomColors(int numBlobs,
                       java.util.Random rand)
```

Several blob rending functions take in an array of colors so that the random blobs can be drawn
 with the same color each time.  This function selects a random color for each blob and returns it
 in an array.
Parameters:`numBlobs` - Number of blobs found.`rand` - Random number generator
Returns:array of RGB colors for each blob + the background blob

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