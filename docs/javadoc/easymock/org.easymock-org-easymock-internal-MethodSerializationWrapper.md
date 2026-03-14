Module org.easymock
Package org.easymock.internal

## Class MethodSerializationWrapper

- java.lang.Object

- 

  - org.easymock.internal.MethodSerializationWrapper

- 

All Implemented Interfaces:
`Serializable`

---

```
public class MethodSerializationWrapper
extends Object
implements Serializable
```

Wrapper used to serialize a `java.lang.reflect.Method` object when a mock is serialized.

Author:
Henri Tremblay
See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`MethodSerializationWrapper​(Method m)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`Method`
`getMethod()`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### MethodSerializationWrapper

```
public MethodSerializationWrapper​(Method m)
```

  - 

### Method Detail

    - 

#### getMethod

```
public Method getMethod()
                 throws ClassNotFoundException,
                        NoSuchMethodException
```

Throws:
`ClassNotFoundException`
`NoSuchMethodException`