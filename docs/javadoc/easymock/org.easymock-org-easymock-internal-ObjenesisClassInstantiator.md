Module org.easymock
Package org.easymock.internal

## Class ObjenesisClassInstantiator

- java.lang.Object

- 

  - org.easymock.internal.ObjenesisClassInstantiator

- 

All Implemented Interfaces:
`IClassInstantiator`

---

```
public class ObjenesisClassInstantiator
extends Object
implements IClassInstantiator
```

Class instantiator using Objenesis to perform the instantiation without calling any constructor.

Author:
Henri Tremblay

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`ObjenesisClassInstantiator()`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`Object`
`newInstance​(Class<?> clazz)`

Return a new instance of the specified class.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ObjenesisClassInstantiator

```
public ObjenesisClassInstantiator()
```

  - 

### Method Detail

    - 

#### newInstance

```
public Object newInstance​(Class<?> clazz)
```

Description copied from interface: `IClassInstantiator`
Return a new instance of the specified class. The recommended way is
 without calling any constructor. This is usually done by doing like
 `ObjectInputStream.readObject()` which is JVM specific.

Specified by:
`newInstance` in interface `IClassInstantiator`
Parameters:
`clazz` - class to instantiate
Returns:
new instance of clazz