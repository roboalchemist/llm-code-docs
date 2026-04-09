Module org.easymock
Package org.easymock.internal

## Class ExpectedInvocationAndResults

- java.lang.Object

- 

  - org.easymock.internal.ExpectedInvocationAndResults

- 

All Implemented Interfaces:
`Serializable`

---

```
public class ExpectedInvocationAndResults
extends Object
implements Serializable
```

The pair of an expected invocation and its results.

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

`ExpectedInvocationAndResults​(ExpectedInvocation expectedInvocation,
                            Results results)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`ExpectedInvocation`
`getExpectedInvocation()`
 

`Results`
`getResults()`
 

`String`
`toString()`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ExpectedInvocationAndResults

```
public ExpectedInvocationAndResults​(ExpectedInvocation expectedInvocation,
                                    Results results)
```

  - 

### Method Detail

    - 

#### getExpectedInvocation

```
public ExpectedInvocation getExpectedInvocation()
```

    - 

#### getResults

```
public Results getResults()
```

    - 

#### toString

```
public String toString()
```

Overrides:
`toString` in class `Object`