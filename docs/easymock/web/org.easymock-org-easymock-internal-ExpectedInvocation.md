Module org.easymock
Package org.easymock.internal

## Class ExpectedInvocation

- java.lang.Object

- 

  - org.easymock.internal.ExpectedInvocation

- 

All Implemented Interfaces:
`Serializable`

---

```
public final class ExpectedInvocation
extends Object
implements Serializable
```

One expected invocation. It is composed of the method invoked and the matchers used to expect the arguments.

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

`ExpectedInvocation​(Invocation invocation,
                  List<IArgumentMatcher> matchers)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`boolean`
`equals​(Object o)`
 

`Method`
`getMethod()`
 

`int`
`hashCode()`
 

`boolean`
`matches​(Invocation actual)`

Tells if the actual invocation matches this expected invocation.

`String`
`toString()`
 

    - 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ExpectedInvocation

```
public ExpectedInvocation​(Invocation invocation,
                          List<IArgumentMatcher> matchers)
```

  - 

### Method Detail

    - 

#### equals

```
public boolean equals​(Object o)
```

Overrides:
`equals` in class `Object`

    - 

#### hashCode

```
public int hashCode()
```

Overrides:
`hashCode` in class `Object`

    - 

#### matches

```
public boolean matches​(Invocation actual)
```

Tells if the actual invocation matches this expected invocation. It needs to be on the same mock, method and
 have the same arguments.

Parameters:
`actual` - the actual invocation to match with the expected one
Returns:
the invocation to compare

    - 

#### toString

```
public String toString()
```

Overrides:
`toString` in class `Object`

    - 

#### getMethod

```
public Method getMethod()
```