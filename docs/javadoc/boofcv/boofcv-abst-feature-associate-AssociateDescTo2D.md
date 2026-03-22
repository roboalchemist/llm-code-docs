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

boofcv.abst.feature.associate

## Class AssociateDescTo2D<D>

- java.lang.Object

- 

  - boofcv.abst.feature.associate.AssociateDescTo2D<D>

- 

All Implemented Interfaces:
Associate, AssociateDescription2D<D>

---

```
public class AssociateDescTo2D<D>
extends java.lang.Object
implements AssociateDescription2D<D>
```

Wrapper around `AssociateDescription` that allows it to be used inside of `AssociateDescription2D`
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AssociateDescTo2D**(AssociateDescription<D> alg)` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`void`
`**associate**()`
Finds the best match for each item in the source list with an item in the destination list.

`FastQueue<AssociatedIndex>`
`**getMatches**()`
List of associated features.

`MatchScoreType`
`**getScoreType**()`
Specifies the type of score which is returned.

`GrowQueue_I32`
`**getUnassociatedDestination**()`
Indexes of features in the destination set which are not associated.

`GrowQueue_I32`
`**getUnassociatedSource**()`
Indexes of features in the source set which are not associated.

`void`
`**setDestination**(FastQueue<Point2D_F64> location,
              FastQueue<D> descriptions)`
Provide the location and descriptions for destination features.

`void`
`**setSource**(FastQueue<Point2D_F64> location,
         FastQueue<D> descriptions)`
Provide the location and descriptions for source features.

`void`
`**setThreshold**(double score)`
Associations are only considered if their score is less than the specified threshold.

`boolean`
`**uniqueDestination**()`
If at most one match is returned for each destination feature.

`boolean`
`**uniqueSource**()`
If at most one match is returned for each source feature.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AssociateDescTo2D

```
public AssociateDescTo2D(AssociateDescription<D> alg)
```

  - 

### Method Detail

    - 

#### setSource

```
public void setSource(FastQueue<Point2D_F64> location,
             FastQueue<D> descriptions)
```

**Description copied from interface: `AssociateDescription2D`**
Provide the location and descriptions for source features.

**Specified by:**
`setSource` in interface `AssociateDescription2D<D>`
Parameters:`location` - Feature locations.`descriptions` - Feature descriptions.

    - 

#### setDestination

```
public void setDestination(FastQueue<Point2D_F64> location,
                  FastQueue<D> descriptions)
```

**Description copied from interface: `AssociateDescription2D`**
Provide the location and descriptions for destination features.

**Specified by:**
`setDestination` in interface `AssociateDescription2D<D>`
Parameters:`location` - Feature locations.`descriptions` - Feature descriptions.

    - 

#### associate

```
public void associate()
```

**Description copied from interface: `Associate`**
Finds the best match for each item in the source list with an item in the destination list.

**Specified by:**
`associate` in interface `Associate`

    - 

#### getMatches

```
public FastQueue<AssociatedIndex> getMatches()
```

**Description copied from interface: `Associate`**
List of associated features.  Indexes refer to the index inside the input lists.

**Specified by:**
`getMatches` in interface `Associate`
Returns:List of associated features.

    - 

#### getUnassociatedSource

```
public GrowQueue_I32 getUnassociatedSource()
```

**Description copied from interface: `Associate`**
Indexes of features in the source set which are not associated.

 WARNING: In some implementations the unassociated list is recomputed each time this function is invoked.  In
 other implementations it was found virtually for free while the matches are found.

**Specified by:**
`getUnassociatedSource` in interface `Associate`
Returns:List of unassociated source features by index.

    - 

#### getUnassociatedDestination

```
public GrowQueue_I32 getUnassociatedDestination()
```

**Description copied from interface: `Associate`**
Indexes of features in the destination set which are not associated.

 WARNING: In some implementations the unassociated list is recomputed each time this function is invoked.  In
 other implementations it was found virtually for free while the matches are found.

**Specified by:**
`getUnassociatedDestination` in interface `Associate`
Returns:List of unassociated destination features by index.

    - 

#### setThreshold

```
public void setThreshold(double score)
```

**Description copied from interface: `Associate`**
Associations are only considered if their score is less than the specified threshold.  To remove
 any threshold test set this value to Double.MAX_VALUE

**Specified by:**
`setThreshold` in interface `Associate`
Parameters:`score` - The threshold.

    - 

#### getScoreType

```
public MatchScoreType getScoreType()
```

**Description copied from interface: `Associate`**
Specifies the type of score which is returned.

**Specified by:**
`getScoreType` in interface `Associate`
Returns:Type of association score.

    - 

#### uniqueSource

```
public boolean uniqueSource()
```

**Description copied from interface: `Associate`**
If at most one match is returned for each source feature.

**Specified by:**
`uniqueSource` in interface `Associate`
Returns:true for unique source association

    - 

#### uniqueDestination

```
public boolean uniqueDestination()
```

**Description copied from interface: `Associate`**
If at most one match is returned for each destination feature.

**Specified by:**
`uniqueDestination` in interface `Associate`
Returns:true for unique destination association

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