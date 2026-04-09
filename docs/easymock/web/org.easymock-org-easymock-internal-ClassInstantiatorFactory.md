Module org.easymock
Package org.easymock.internal

## Class ClassInstantiatorFactory

- java.lang.Object

- 

  - org.easymock.internal.ClassInstantiatorFactory

- 

---

```
public final class ClassInstantiatorFactory
extends Object
```

Factory returning a `IClassInstantiator`for the current JVM

Author:
Henri Tremblay

- 

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method
Description

`static IClassInstantiator`
`getInstantiator()`

Returns a class instantiator suitable for the current JVM

`static String`
`getJVM()`

Returns the current JVM as specified in the System properties

`static String`
`getJVMSpecificationVersion()`

Returns the current JVM specification version (1.5, 1.4, 1.3)

`static boolean`
`is1_3Specifications()`
 

`static void`
`setDefaultInstantiator()`

Set back the default instantiator

`static void`
`setInstantiator​(IClassInstantiator i)`

Allow to override the default instantiator.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Method Detail

    - 

#### getJVM

```
public static String getJVM()
```

Returns the current JVM as specified in the System properties

Returns:
current JVM

    - 

#### getJVMSpecificationVersion

```
public static String getJVMSpecificationVersion()
```

Returns the current JVM specification version (1.5, 1.4, 1.3)

Returns:
current JVM specification version

    - 

#### is1_3Specifications

```
public static boolean is1_3Specifications()
```

    - 

#### getInstantiator

```
public static IClassInstantiator getInstantiator()
```

Returns a class instantiator suitable for the current JVM

Returns:
a class instantiator usable on the current JVM

    - 

#### setInstantiator

```
public static void setInstantiator​(IClassInstantiator i)
```

Allow to override the default instantiator. Useful when the default one
 isn't able to create mocks in a given environment.

Parameters:
`i` - New instantiator

    - 

#### setDefaultInstantiator

```
public static void setDefaultInstantiator()
```

Set back the default instantiator