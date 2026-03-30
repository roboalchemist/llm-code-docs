Module org.easymock
Package org.easymock

## Class ConstructorArgs

- java.lang.Object

- 

  - org.easymock.ConstructorArgs

- 

---

```
public final class ConstructorArgs
extends Object
```

Class wrapping arguments to create a partial class mock that gets
 instantiated by calling one of its constructors.

Author:
Henri Tremblay

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`ConstructorArgs​(Constructor<?> constructor,
               Object... initArgs)`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`Constructor<?>`
`getConstructor()`
 

`Object[]`
`getInitArgs()`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ConstructorArgs

```
public ConstructorArgs​(Constructor<?> constructor,
                       Object... initArgs)
```

Parameters:
`constructor` - Constructor to be called when creating the mock
`initArgs` - Arguments passed to the constructor

  - 

### Method Detail

    - 

#### getInitArgs

```
public Object[] getInitArgs()
```

Returns:
arguments to be passed to the constructor

    - 

#### getConstructor

```
public Constructor<?> getConstructor()
```

Returns:
constructor to be called