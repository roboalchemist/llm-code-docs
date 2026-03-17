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

boofcv.alg.feature.describe.brief

## Class BinaryCompareDefinition_I32

- java.lang.Object

- 

  - boofcv.alg.feature.describe.brief.BinaryCompareDefinition_I32

- 

---

```
public class BinaryCompareDefinition_I32
extends java.lang.Object
```

 Describes the layout of a BRIEF descriptor.  This descriptor is composed of a set of locations
 where image intensity is sampled and a list of which locations are compared against each other.
 

 

 NOTE: The data structure here is different than the one implied in the paper.  A single list of sample points
 is provided instead of two lists.  This way a single set of points can sample within the same set, reducing
 the number of samples taken.
 
Author:
  Peter Abeles

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`Point2D_I32[]`
`**compare**` 

`int`
`**radius**` 

`Point2D_I32[]`
`**samplePoints**` 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BinaryCompareDefinition_I32**(int radius,
                           int numSamples,
                           int numPairs)` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`int`
`**getLength**()`
Length of the descriptor (or number of bits required to encode it)

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Field Detail

    - 

#### radius

```
public int radius
```

    - 

#### samplePoints

```
public Point2D_I32[] samplePoints
```

    - 

#### compare

```
public Point2D_I32[] compare
```

  - 

### Constructor Detail

    - 

#### BinaryCompareDefinition_I32

```
public BinaryCompareDefinition_I32(int radius,
                           int numSamples,
                           int numPairs)
```

  - 

### Method Detail

    - 

#### getLength

```
public int getLength()
```

Length of the descriptor (or number of bits required to encode it)
Returns:Descriptor length.

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