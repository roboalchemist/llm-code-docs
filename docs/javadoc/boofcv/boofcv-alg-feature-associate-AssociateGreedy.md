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

## Class AssociateGreedy<D>

- java.lang.Object

- 

  - boofcv.alg.feature.associate.AssociateGreedy<D>

- 
Type Parameters:`D` - Feature description type.

---

```
public class AssociateGreedy<D>
extends java.lang.Object
```

 Brute force greedy association for objects described by a `TupleDesc_F64`.  An
 object is associated with whichever object has the best fit score and every possible combination
 is examined.  If there are a large number of features this can be quite slow.
 

 

 Optionally, backwards validation can be used to reduce the number of false associations.
 Backwards validation works by checking to see if two objects are mutually the best association
 for each other.  First an association is found from src to dst, then the best fit in dst is
 associated with feature in src.
 
Author:
  Peter Abeles

- 

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**AssociateGreedy**(ScoreAssociation<D> score,
               boolean backwardsValidation)`
Configure association

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`void`
`**associate**(FastQueue<D> src,
         FastQueue<D> dst)`
Associates the two sets objects against each other by minimizing fit score.

`double[]`
`**getFitQuality**()`
Quality of fit scores for each association.

`int[]`
`**getPairs**()`
Returns a list of association pairs.

`ScoreAssociation<D>`
`**getScore**()` 

`boolean`
`**isBackwardsValidation**()` 

`void`
`**setMaxFitError**(double maxFitError)` 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AssociateGreedy

```
public AssociateGreedy(ScoreAssociation<D> score,
               boolean backwardsValidation)
```

Configure association
Parameters:`score` - Computes the association score.`backwardsValidation` - If true then backwards validation is performed.

  - 

### Method Detail

    - 

#### associate

```
public void associate(FastQueue<D> src,
             FastQueue<D> dst)
```

Associates the two sets objects against each other by minimizing fit score.
Parameters:`src` - Source list.`dst` - Destination list.

    - 

#### getPairs

```
public int[] getPairs()
```

Returns a list of association pairs.  Each element in the returned list corresponds
 to an element in the src list.  The value contained in the index indicate which element
 in the dst list that object was associated with.  If a value of -1 is stored then
 no association was found.
Returns:Array containing associations by src index.

    - 

#### getFitQuality

```
public double[] getFitQuality()
```

Quality of fit scores for each association.  Lower fit scores are better.
Returns:Array of fit sources by src index.

    - 

#### setMaxFitError

```
public void setMaxFitError(double maxFitError)
```

    - 

#### getScore

```
public ScoreAssociation<D> getScore()
```

    - 

#### isBackwardsValidation

```
public boolean isBackwardsValidation()
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