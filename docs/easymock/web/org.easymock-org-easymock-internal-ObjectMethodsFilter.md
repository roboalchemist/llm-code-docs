Module org.easymock
Package org.easymock.internal

## Class ObjectMethodsFilter

- java.lang.Object

- 

  - org.easymock.internal.ObjectMethodsFilter

- 

All Implemented Interfaces:
`Serializable`, `InvocationHandler`

---

```
public final class ObjectMethodsFilter
extends Object
implements InvocationHandler, Serializable
```

The filter catching all calls to the mock. It handles `equals`, `hashCode`, `toString`,
 and `finalize` in a special way. Then, for other calls, it delegates to the mock handler.

Author:
OFFIS, Tammo Freese, Henri Tremblay
See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`ObjectMethodsFilter​(Class<?> toMock,
                   MockInvocationHandler delegate,
                   String name)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`MockInvocationHandler`
`getDelegate()`
 

`String`
`getName()`
 

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

#### ObjectMethodsFilter

```
public ObjectMethodsFilter​(Class<?> toMock,
                           MockInvocationHandler delegate,
                           String name)
```

  - 

### Method Detail

    - 

#### getName

```
public String getName()
```

    - 

#### invoke

```
public final Object invoke​(Object proxy,
                           Method method,
                           Object[] args)
                    throws Throwable
```

Specified by:
`invoke` in interface `InvocationHandler`
Throws:
`Throwable`

    - 

#### getDelegate

```
public MockInvocationHandler getDelegate()
```