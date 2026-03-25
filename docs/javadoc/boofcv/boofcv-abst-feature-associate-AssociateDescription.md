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

## Interface AssociateDescription<Desc>

- 
Type Parameters:`Desc` - Feature description type.

All Superinterfaces:
Associate

All Known Implementing Classes:
AssociateNearestNeighbor, EnforceUniqueByScore.Describe, WrapAssociateGreedy, WrapAssociateSurfBasic

---

```
public interface AssociateDescription<Desc>
extends Associate
```

 Generalized interface for associating features.   Finds matches for each feature in the source
 list to one in the destination list.  There is only one match found for each member of source, but multiple
 matches can be found for destination.  If the best match has an error which is too high then a member of
 source might not be matched.
 

 

 DESIGN NOTE: `FastQueue` is used instead of `List` because in the association
 micro benchmark it produced results that were about 20% faster consistently.  Which is surprising since
 one would think descriptor comparisons would dominate.
 
Author:
  Peter Abeles

- 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`void`
`**setDestination**(FastQueue<Desc> listDst)`
Sets the list of destination features

 NOTE: A reference to the input list might be saved internally until the next call to this function.

`void`
`**setSource**(FastQueue<Desc> listSrc)`
Sets the list of source features.

    - 

### Methods inherited from interface boofcv.abst.feature.associate.Associate

`associate, getMatches, getScoreType, getUnassociatedDestination, getUnassociatedSource, setThreshold, uniqueDestination, uniqueSource`

- 

  - 

### Method Detail

    - 

#### setSource

```
void setSource(FastQueue<Desc> listSrc)
```

Sets the list of source features.

 NOTE: A reference to the input list might be saved internally until the next call to this function.
Parameters:`listSrc` - List of features

    - 

#### setDestination

```
void setDestination(FastQueue<Desc> listDst)
```

Sets the list of destination features

 NOTE: A reference to the input list might be saved internally until the next call to this function.
Parameters:`listDst` - List of features

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