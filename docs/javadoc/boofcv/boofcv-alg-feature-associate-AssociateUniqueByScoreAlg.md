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

## Class AssociateUniqueByScoreAlg

- java.lang.Object

- 

  - boofcv.alg.feature.associate.AssociateUniqueByScoreAlg

- 

---

```
public class AssociateUniqueByScoreAlg
extends java.lang.Object
```

If multiple associations are found for a single source and/or destination feature then this ambiguity is
 removed by selecting the association with the best score.  If there are multiple best scores for a single
 feature index then there are no associations for that feature.
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AssociateUniqueByScoreAlg**(MatchScoreType type,
                         boolean checkSource,
                         boolean checkDestination)`
Configures algorithm.

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`boolean`
`**checkDestination**()` 

`boolean`
`**checkSource**()` 

`FastQueue<AssociatedIndex>`
`**getMatches**()` 

`void`
`**process**(FastQueue<AssociatedIndex> matches,
       int numSource,
       int numDestination)`
Given a set of matches, enforce the uniqueness rules it was configured to.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AssociateUniqueByScoreAlg

```
public AssociateUniqueByScoreAlg(MatchScoreType type,
                         boolean checkSource,
                         boolean checkDestination)
```

Configures algorithm.
Parameters:`type` - Used to determine which score is better`checkSource` - Should it check source features for uniqueness`checkDestination` - Should it check destination features for uniqueness

  - 

### Method Detail

    - 

#### process

```
public void process(FastQueue<AssociatedIndex> matches,
           int numSource,
           int numDestination)
```

Given a set of matches, enforce the uniqueness rules it was configured to.
Parameters:`matches` - Set of matching features`numSource` - Number of source features`numDestination` - Number of destination features

    - 

#### getMatches

```
public FastQueue<AssociatedIndex> getMatches()
```

    - 

#### checkSource

```
public boolean checkSource()
```

    - 

#### checkDestination

```
public boolean checkDestination()
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