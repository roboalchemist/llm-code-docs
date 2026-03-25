Module org.easymock
Package org.easymock.internal

## Class DefaultClassInstantiator

- java.lang.Object

- 

  - org.easymock.internal.DefaultClassInstantiator

- 

All Implemented Interfaces:
`IClassInstantiator`

---

```
public class DefaultClassInstantiator
extends Object
implements IClassInstantiator
```

Default class instantiator that is pretty limited. It just hope that the
 mocked class has a public empty constructor.

Author:
Henri Tremblay

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`DefaultClassInstantiator()`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`Object[]`
`getArgsForTypes​(Class<?>[] methodTypes)`

Get some default instances of provided classes

`Constructor<?>`
`getConstructorToUse​(Class<?> clazz)`

Return the constructor considered the best to use with this class.

`Object`
`newInstance​(Class<?> c)`

Try to instantiate a class without using a special constructor.

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### DefaultClassInstantiator

```
public DefaultClassInstantiator()
```

  - 

### Method Detail

    - 

#### newInstance

```
public Object newInstance​(Class<?> c)
                   throws InstantiationException
```

Try to instantiate a class without using a special constructor. See
 documentation for the algorithm.

Specified by:
`newInstance` in interface `IClassInstantiator`
Parameters:
`c` - Class to instantiate
Returns:
new instance of clazz
Throws:
`InstantiationException` - when an error occured during instantiation

    - 

#### getConstructorToUse

```
public Constructor<?> getConstructorToUse​(Class<?> clazz)
```

Return the constructor considered the best to use with this class.
 Algorithm is: No args constructor and then first constructor defined in
 the class

Parameters:
`clazz` - Class in which constructor is searched
Returns:
Constructor to use

    - 

#### getArgsForTypes

```
public Object[] getArgsForTypes​(Class<?>[] methodTypes)
                         throws InstantiationException
```

Get some default instances of provided classes

Parameters:
`methodTypes` - Classes to instantiate
Returns:
Instances of methodTypes in order
Throws:
`InstantiationException` - Thrown if the class instantiation fails