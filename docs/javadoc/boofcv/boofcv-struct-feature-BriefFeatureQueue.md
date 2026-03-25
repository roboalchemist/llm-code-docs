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

boofcv.struct.feature

## Class BriefFeatureQueue

- java.lang.Object

- 

  - boofcv.struct.FastQueue<TupleDesc_B>

  - 

    - boofcv.struct.feature.BriefFeatureQueue

- 

---

```
public class BriefFeatureQueue
extends FastQueue<TupleDesc_B>
```

`FastQueue` for `TupleDesc_B`.
Author:
  Peter Abeles

- 

  - 

### Field Summary

    - 

### Fields inherited from class boofcv.struct.FastQueue

`data, size, type`

  - 

### Constructor Summary

Constructors 

Constructor and Description

`**BriefFeatureQueue**(int numBits)` 

  - 

### Method Summary

Methods 

Modifier and Type
Method and Description

`protected TupleDesc_B`
`**createInstance**()` 

    - 

### Methods inherited from class boofcv.struct.FastQueue

`add, addAll, copyIntoList, get, getMaxSize, getTail, grow, growArray, init, removeTail, reset, size, toList`

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### BriefFeatureQueue

```
public BriefFeatureQueue(int numBits)
```

  - 

### Method Detail

    - 

#### createInstance

```
protected TupleDesc_B createInstance()
```

**Overrides:**
`createInstance` in class `FastQueue<TupleDesc_B>`

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