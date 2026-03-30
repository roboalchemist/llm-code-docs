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

boofcv.alg.feature.associate

## Class AssociateMaxDistanceNaive<D>

- java.lang.Object

- 

  - boofcv.alg.feature.associate.BaseAssociateLocation2DFilter<D>

  - 

    - boofcv.alg.feature.associate.AssociateMaxDistanceNaive<D>

- 

All Implemented Interfaces:
Associate, AssociateDescription2D<D>, AssociateMaxDistance<D>

---

```
public class AssociateMaxDistanceNaive<D>
extends BaseAssociateLocation2DFilter<D>
implements AssociateMaxDistance<D>
```

Two features are only considered for association if they are within the specified max distance
 of each other.  Every possible association is considered, but only features that are close to
 each other are scored.
Author:
  Peter Abeles

- 

  - 

### Field Summary

Fields 

Modifier and Type
Field and Description

`protected double`
`**maxDistanceNotSquared**` 

    - 

### Fields inherited from class boofcv.alg.feature.associate.BaseAssociateLocation2DFilter

`maxDistance, maxError`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AssociateMaxDistanceNaive**(ScoreAssociation<D> scoreAssociation,
                         boolean backwardsValidation,
                         double maxError)`
Specifies score mechanism

`**AssociateMaxDistanceNaive**(ScoreAssociation<D> scoreAssociation,
                         boolean backwardsValidation,
                         double maxError,
                         double maxDistance)` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`protected double`
`**computeDistanceToSource**(Point2D_F64 p)` 

`double`
`**getMaxDistance**()` 

`protected void`
`**setActiveSource**(Point2D_F64 p)` 

`void`
`**setMaxDistance**(double maxDistance)` 

    - 

### Methods inherited from class boofcv.alg.feature.associate.BaseAssociateLocation2DFilter

`associate, getMatches, getScoreType, getUnassociatedDestination, getUnassociatedSource, setDestination, setSource, setThreshold, uniqueDestination, uniqueSource`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

    - 

### Methods inherited from interface boofcv.abst.feature.associate.AssociateDescription2D

`setDestination, setSource`

    - 

### Methods inherited from interface boofcv.abst.feature.associate.Associate

`associate, getMatches, getScoreType, getUnassociatedDestination, getUnassociatedSource, setThreshold, uniqueDestination, uniqueSource`

- 

  - 

### Field Detail

    - 

#### maxDistanceNotSquared

```
protected double maxDistanceNotSquared
```

  - 

### Constructor Detail

    - 

#### AssociateMaxDistanceNaive

```
public AssociateMaxDistanceNaive(ScoreAssociation<D> scoreAssociation,
                         boolean backwardsValidation,
                         double maxError)
```

Specifies score mechanism
Parameters:`scoreAssociation` - How features are scored.

    - 

#### AssociateMaxDistanceNaive

```
public AssociateMaxDistanceNaive(ScoreAssociation<D> scoreAssociation,
                         boolean backwardsValidation,
                         double maxError,
                         double maxDistance)
```

  - 

### Method Detail

    - 

#### getMaxDistance

```
public double getMaxDistance()
```

**Specified by:**
`getMaxDistance` in interface `AssociateMaxDistance<D>`
**Overrides:**
`getMaxDistance` in class `BaseAssociateLocation2DFilter<D>`

    - 

#### setMaxDistance

```
public void setMaxDistance(double maxDistance)
```

**Specified by:**
`setMaxDistance` in interface `AssociateMaxDistance<D>`
**Overrides:**
`setMaxDistance` in class `BaseAssociateLocation2DFilter<D>`

    - 

#### setActiveSource

```
protected void setActiveSource(Point2D_F64 p)
```

**Specified by:**
`setActiveSource` in class `BaseAssociateLocation2DFilter<D>`

    - 

#### computeDistanceToSource

```
protected double computeDistanceToSource(Point2D_F64 p)
```

**Specified by:**
`computeDistanceToSource` in class `BaseAssociateLocation2DFilter<D>`

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