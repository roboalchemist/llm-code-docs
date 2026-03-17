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

boofcv.struct.geo

## Class AssociatedPair

- java.lang.Object

- 

  - boofcv.struct.geo.AssociatedPair

- 

Direct Known Subclasses:
AssociatedPairTrack

---

```
public class AssociatedPair
extends java.lang.Object
```

 Contains the location of a point feature in an image in the key frame and the current frame.
 Useful for applications where the motion or structure of a scene is computed between
 two images.
 
Author:
  Peter Abeles

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`Point2D_F64`
`**p1**`
Location of the feature in the first image

`Point2D_F64`
`**p2**`
Location of the feature in the second image.

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AssociatedPair**()` 

`**AssociatedPair**(boolean declare)`
Constructor which allows the points to not be declared.

`**AssociatedPair**(double x1,
              double y1,
              double x2,
              double y2)`
Creates a new associated point from the two provided points.

`**AssociatedPair**(Point2D_F64 p1,
              Point2D_F64 p2)`
Creates a new associated point from the two provided points.

`**AssociatedPair**(Point2D_F64 p1,
              Point2D_F64 p2,
              boolean newInstance)`
Creates a new associated point from the two provided points.

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`void`
`**assign**(Point2D_F64 p1,
      Point2D_F64 p2)`
Sets p1 and p2 to reference the passed in objects.

`Point2D_F64`
`**getP1**()` 

`Point2D_F64`
`**getP2**()` 

`void`
`**set**(Point2D_F64 p1,
   Point2D_F64 p2)`
Sets the value of p1 and p2 to be equal to the values of the passed in objects

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### p1

```
public Point2D_F64 p1
```

Location of the feature in the first image

    - 

#### p2

```
public Point2D_F64 p2
```

Location of the feature in the second image.

  - 

### Constructor Detail

    - 

#### AssociatedPair

```
public AssociatedPair()
```

    - 

#### AssociatedPair

```
public AssociatedPair(boolean declare)
```

Constructor which allows the points to not be declared.
Parameters:`declare` - If true then new points will be declared

    - 

#### AssociatedPair

```
public AssociatedPair(double x1,
              double y1,
              double x2,
              double y2)
```

Creates a new associated point from the two provided points.
Parameters:`x1` - image 1 location x-axis.`y1` - image 1 location y-axis.`x2` - image 2 location x-axis.`y2` - image 2 location y-axis.

    - 

#### AssociatedPair

```
public AssociatedPair(Point2D_F64 p1,
              Point2D_F64 p2)
```

Creates a new associated point from the two provided points.
Parameters:`p1` - image 1 location`p2` - image 2 location

    - 

#### AssociatedPair

```
public AssociatedPair(Point2D_F64 p1,
              Point2D_F64 p2,
              boolean newInstance)
```

Creates a new associated point from the two provided points.
Parameters:`p1` - image 1 location`p2` - image 2 location`newInstance` - Should it create new points or save a reference to these instances.

  - 

### Method Detail

    - 

#### set

```
public void set(Point2D_F64 p1,
       Point2D_F64 p2)
```

Sets the value of p1 and p2 to be equal to the values of the passed in objects

    - 

#### assign

```
public void assign(Point2D_F64 p1,
          Point2D_F64 p2)
```

Sets p1 and p2 to reference the passed in objects.

    - 

#### getP1

```
public Point2D_F64 getP1()
```

    - 

#### getP2

```
public Point2D_F64 getP2()
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