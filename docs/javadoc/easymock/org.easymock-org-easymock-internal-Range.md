Module org.easymock
Package org.easymock.internal

## Class Range

- java.lang.Object

- 

  - org.easymock.internal.Range

- 

All Implemented Interfaces:
`Serializable`

---

```
public final class Range
extends Object
implements Serializable
```

The range of a number of invocations. It knows the expected minimum and maximum number of invocations.

Author:
OFFIS, Tammo Freese
See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`Range​(int count)`
 

`Range​(int minimum,
     int maximum)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`boolean`
`contains​(int count)`
 

`String`
`expectedCount()`
 

`int`
`getMaximum()`
 

`int`
`getMinimum()`
 

`boolean`
`hasFixedCount()`
 

`boolean`
`hasOpenCount()`
 

`String`
`toString()`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Range

```
public Range​(int count)
```

    - 

#### Range

```
public Range​(int minimum,
             int maximum)
```

  - 

### Method Detail

    - 

#### hasFixedCount

```
public boolean hasFixedCount()
```

    - 

#### getMaximum

```
public int getMaximum()
```

    - 

#### getMinimum

```
public int getMinimum()
```

    - 

#### toString

```
public String toString()
```

Overrides:
`toString` in class `Object`

    - 

#### expectedCount

```
public String expectedCount()
```

    - 

#### contains

```
public boolean contains​(int count)
```

    - 

#### hasOpenCount

```
public boolean hasOpenCount()
```