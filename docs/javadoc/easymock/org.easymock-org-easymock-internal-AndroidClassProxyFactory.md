Module org.easymock
Package org.easymock.internal

## Class AndroidClassProxyFactory

- java.lang.Object

- 

  - org.easymock.internal.AndroidClassProxyFactory

- 

All Implemented Interfaces:
`IProxyFactory`

---

```
public final class AndroidClassProxyFactory
extends Object
implements IProxyFactory
```

Mocks concrete classes for Android's runtime by generating dex files.

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`AndroidClassProxyFactory()`
 

  - 

### Method Summary

All Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`<T> T`
`createProxy​(Class<T> toMock,
           InvocationHandler handler,
           Method[] mockedMethods,
           ConstructorArgs constructorArgs)`
 

`InvocationHandler`
`getInvocationHandler​(Object mock)`

Returns the invocation handler for `mock`;

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### AndroidClassProxyFactory

```
public AndroidClassProxyFactory()
```

  - 

### Method Detail

    - 

#### createProxy

```
public <T> T createProxy​(Class<T> toMock,
                         InvocationHandler handler,
                         Method[] mockedMethods,
                         ConstructorArgs constructorArgs)
```

Specified by:
`createProxy` in interface `IProxyFactory`
Type Parameters:
`T` - type of the class to mock
Parameters:
`toMock` - the class to mock by the factory
`handler` - the handler that will be linked to the created proxy
`mockedMethods` - the subset of `toMock`'s methods to mock, or
     null to mock all methods.
`constructorArgs` - the constructor arguments to use, or null to use
     heuristics to choose a constructor.
Returns:
the newly created proxy

    - 

#### getInvocationHandler

```
public InvocationHandler getInvocationHandler​(Object mock)
```

Description copied from interface: `IProxyFactory`
Returns the invocation handler for `mock`;

Specified by:
`getInvocationHandler` in interface `IProxyFactory`
Parameters:
`mock` - a mock instance previously returned by `createProxy`.
Returns:
the handler handling method calls for the `mock`