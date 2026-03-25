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

## Interface AssociateMaxDistance<D>

- 

All Superinterfaces:
Associate, AssociateDescription2D<D>

All Known Implementing Classes:
AssociateMaxDistanceNaive

---

```
public interface AssociateMaxDistance<D>
extends AssociateDescription2D<D>
```

Two features can only be associated if their distance in image space is less than the specified number.
Author:
  Peter Abeles

- 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`double`
`**getMaxDistance**()` 

`void`
`**setMaxDistance**(double maxDistance)` 

    - 

### Methods inherited from interface boofcv.abst.feature.associate.AssociateDescription2D

`setDestination, setSource`

    - 

### Methods inherited from interface boofcv.abst.feature.associate.Associate

`associate, getMatches, getScoreType, getUnassociatedDestination, getUnassociatedSource, setThreshold, uniqueDestination, uniqueSource`

- 

  - 

### Method Detail

    - 

#### getMaxDistance

```
double getMaxDistance()
```

    - 

#### setMaxDistance

```
void setMaxDistance(double maxDistance)
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