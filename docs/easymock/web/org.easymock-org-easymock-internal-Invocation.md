Module org.easymock
Package org.easymock.internal

## Class Invocation

- java.lang.Object

- 

  - org.easymock.internal.Invocation

- 

All Implemented Interfaces:
`Serializable`

---

```
public final class Invocation
extends Object
implements Serializable
```

Represents a method invocation on a mock object. It's used for record one or for actual calls.

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

`Invocation​(Object mock,
          Method method,
          Object[] args)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`void`
`addCapture​(Captures<Object> capture,
          Object value)`
 

`void`
`clearCaptures()`
 

`boolean`
`equals​(Object o)`
 

`Object[]`
`getArguments()`

Returns the arguments passed to the method invocation.

`Method`
`getMethod()`

Returns the method invoked on the mock object.

`Object`
`getMock()`

Returns the mock object on which the invocation was performed.

`String`
`getMockAndMethodName()`
 

`int`
`hashCode()`
 

`String`
`toString()`
 

`void`
`validateCaptures()`
 

    - 

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### Invocation

```
public Invocation​(Object mock,
                  Method method,
                  Object[] args)
```

  - 

### Method Detail

    - 

#### getMock

```
public Object getMock()
```

Returns the mock object on which the invocation was performed.

Returns:
the mock object on which the invocation was performed.

    - 

#### getMethod

```
public Method getMethod()
```

Returns the method invoked on the mock object.

Returns:
the method invoked on the mock object.

    - 

#### getArguments

```
public Object[] getArguments()
```

Returns the arguments passed to the method invocation.

Returns:
the arguments passed to the method invocation.

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

#### toString

```
public String toString()
```

Overrides:
`toString` in class `Object`

    - 

#### getMockAndMethodName

```
public String getMockAndMethodName()
```

    - 

#### addCapture

```
public void addCapture​(Captures<Object> capture,
                       Object value)
```

    - 

#### validateCaptures

```
public void validateCaptures()
```

    - 

#### clearCaptures

```
public void clearCaptures()
```