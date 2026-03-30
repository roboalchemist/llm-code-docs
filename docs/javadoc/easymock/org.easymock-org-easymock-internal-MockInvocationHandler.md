Module org.easymock
Package org.easymock.internal

## Class MockInvocationHandler

- java.lang.Object

- 

  - org.easymock.internal.MockInvocationHandler

- 

All Implemented Interfaces:
`Serializable`, `InvocationHandler`

---

```
public final class MockInvocationHandler
extends Object
implements InvocationHandler, Serializable
```

The handler of all invocations on a mock interface.

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

`MockInvocationHandler​(MocksControl control)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`MocksControl`
`getControl()`
 

`Object`
`invoke​(Object proxy,
      Method method,
      Object[] args)`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### MockInvocationHandler

```
public MockInvocationHandler​(MocksControl control)
```

  - 

### Method Detail

    - 

#### invoke

```
public Object invoke​(Object proxy,
                     Method method,
                     Object[] args)
              throws Throwable
```

Specified by:
`invoke` in interface `InvocationHandler`
Throws:
`Throwable`

    - 

#### getControl

```
public MocksControl getControl()
```