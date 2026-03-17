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

## Interface AssociateDescription2D<Desc>

- 
Type Parameters:`Desc` - Feature description type.

All Superinterfaces:
Associate

All Known Subinterfaces:
AssociateMaxDistance<D>

All Known Implementing Classes:
AssociateDescTo2D, AssociateMaxDistanceNaive, AssociateStereo2D, BaseAssociateLocation2DFilter, EnforceUniqueByScore.Describe2D

---

```
public interface AssociateDescription2D<Desc>
extends Associate
```

Associates features from two images together using both 2D location and descriptor information.  Each
 source feature is paired up with a single feature in the destination.  If a match is not found then it
 is added to the unassociated list.
Author:
  Peter Abeles

- 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`void`
`**setDestination**(FastQueue<Point2D_F64> location,
              FastQueue<Desc> descriptions)`
Provide the location and descriptions for destination features.

`void`
`**setSource**(FastQueue<Point2D_F64> location,
         FastQueue<Desc> descriptions)`
Provide the location and descriptions for source features.

    - 

### Methods inherited from interface boofcv.abst.feature.associate.Associate

`associate, getMatches, getScoreType, getUnassociatedDestination, getUnassociatedSource, setThreshold, uniqueDestination, uniqueSource`

- 

  - 

### Method Detail

    - 

#### setSource

```
void setSource(FastQueue<Point2D_F64> location,
             FastQueue<Desc> descriptions)
```

Provide the location and descriptions for source features.
Parameters:`location` - Feature locations.`descriptions` - Feature descriptions.

    - 

#### setDestination

```
void setDestination(FastQueue<Point2D_F64> location,
                  FastQueue<Desc> descriptions)
```

Provide the location and descriptions for destination features.
Parameters:`location` - Feature locations.`descriptions` - Feature descriptions.

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