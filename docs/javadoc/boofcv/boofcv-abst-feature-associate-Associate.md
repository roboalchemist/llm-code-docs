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

## Interface Associate

- 

All Known Subinterfaces:
AssociateDescription<Desc>, AssociateDescription2D<Desc>, AssociateMaxDistance<D>

All Known Implementing Classes:
AssociateDescTo2D, AssociateMaxDistanceNaive, AssociateNearestNeighbor, AssociateStereo2D, BaseAssociateLocation2DFilter, EnforceUniqueByScore, EnforceUniqueByScore.Describe, EnforceUniqueByScore.Describe2D, WrapAssociateGreedy, WrapAssociateSurfBasic

---

```
public interface Associate
```

 Common interface for associating features between two images.  Found associations are returned in a list of
 `AssociatedIndex` which specifies the index and score of the matching pair.  Implementing classes can
 optionally ensure that a unique pairing is found from source to destination and/or the reverse.  See
 functions `uniqueSource()` and `uniqueDestination()`.  Indexes refer to the index in the input
 list for source and destination lists.  Inputs are not specified in this interface but are specified in a child
 interface.
 

 

 DESIGN NOTES:

 **Indexes** of matching features are used instead of the descriptions because descriptions are often separated
 from another more complex data structure and the index can be easily matched to that data.

 **Unassociated feature** lists can be easily computed using the returned set of associations.  This functionality
 is provided since in some cases it can be computed at virtually no cost during association.

 
Author:
  Peter Abeles

- 

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
`**setThreshold**(double score)`
Associations are only considered if their score is less than the specified threshold.

`boolean`
`**uniqueDestination**()`
If at most one match is returned for each destination feature.

`boolean`
`**uniqueSource**()`
If at most one match is returned for each source feature.

- 

  - 

### Method Detail

    - 

#### associate

```
void associate()
```

Finds the best match for each item in the source list with an item in the destination list.

    - 

#### getMatches

```
FastQueue<AssociatedIndex> getMatches()
```

List of associated features.  Indexes refer to the index inside the input lists.
Returns:List of associated features.

    - 

#### getUnassociatedSource

```
GrowQueue_I32 getUnassociatedSource()
```

Indexes of features in the source set which are not associated.

 WARNING: In some implementations the unassociated list is recomputed each time this function is invoked.  In
 other implementations it was found virtually for free while the matches are found.
Returns:List of unassociated source features by index.

    - 

#### getUnassociatedDestination

```
GrowQueue_I32 getUnassociatedDestination()
```

Indexes of features in the destination set which are not associated.

 WARNING: In some implementations the unassociated list is recomputed each time this function is invoked.  In
 other implementations it was found virtually for free while the matches are found.
Returns:List of unassociated destination features by index.

    - 

#### setThreshold

```
void setThreshold(double score)
```

Associations are only considered if their score is less than the specified threshold.  To remove
 any threshold test set this value to Double.MAX_VALUE
Parameters:`score` - The threshold.

    - 

#### getScoreType

```
MatchScoreType getScoreType()
```

Specifies the type of score which is returned.
Returns:Type of association score.

    - 

#### uniqueSource

```
boolean uniqueSource()
```

If at most one match is returned for each source feature.
Returns:true for unique source association

    - 

#### uniqueDestination

```
boolean uniqueDestination()
```

If at most one match is returned for each destination feature.
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