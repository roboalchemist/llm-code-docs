Module org.easymock
Package org.easymock.internal

## Class ClassMockingData

- java.lang.Object

- 

  - org.easymock.internal.ClassMockingData

- 

All Implemented Interfaces:
`Serializable`

---

```
public final class ClassMockingData
extends Object
implements Serializable
```

Class containing the data required for a class mock to work.

See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`ClassMockingData​(InvocationHandler handler,
                Method... mockedMethods)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`InvocationHandler`
`handler()`
 

`boolean`
`isMocked​(Method method)`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ClassMockingData

```
public ClassMockingData​(InvocationHandler handler,
                        Method... mockedMethods)
```

  - 

### Method Detail

    - 

#### isMocked

```
public boolean isMocked​(Method method)
```

    - 

#### handler

```
public InvocationHandler handler()
```