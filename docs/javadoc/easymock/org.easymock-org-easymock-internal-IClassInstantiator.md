Module org.easymock
Package org.easymock.internal

## Interface IClassInstantiator

- 

All Known Implementing Classes:
`DefaultClassInstantiator`, `ObjenesisClassInstantiator`

---

```
public interface IClassInstantiator
```

Used to instantiate a given class.

Author:
Henri Tremblay

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

Modifier and Type
Method
Description

`Object`
`newInstance​(Class<?> clazz)`

Return a new instance of the specified class.

- 

  - 

### Method Detail

    - 

#### newInstance

```
Object newInstance​(Class<?> clazz)
            throws InstantiationException
```

Return a new instance of the specified class. The recommended way is
 without calling any constructor. This is usually done by doing like
 `ObjectInputStream.readObject()` which is JVM specific.

Parameters:
`clazz` - class to instantiate
Returns:
new instance of clazz
Throws:
`InstantiationException` - when an error occured during instantiation