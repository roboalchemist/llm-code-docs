Module org.easymock
Package org.easymock.internal

## Class ClassProxyFactory

- java.lang.Object

- 

  - org.easymock.internal.ClassProxyFactory

- 

All Implemented Interfaces:
`IProxyFactory`

---

```
public class ClassProxyFactory
extends Object
implements IProxyFactory
```

Factory generating a mock for a class.

Author:
Henri Tremblay

- 

  - 

### Nested Class Summary

Nested Classes 

Modifier and Type
Class
Description

`static class `
`ClassProxyFactory.MockMethodInterceptor`
 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`ClassProxyFactory()`
 

  - 

### Method Summary

All Methods Static Methods Instance Methods Concrete Methods 

Modifier and Type
Method
Description

`<T> T`
`createProxy​(Class<T> toMock,
           InvocationHandler handler,
           Method[] mockedMethods,
           ConstructorArgs args)`
 

`InvocationHandler`
`getInvocationHandler​(Object mock)`

Returns the invocation handler for `mock`;

`static boolean`
`isCallerMockInvocationHandlerInvoke​(Throwable e)`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### ClassProxyFactory

```
public ClassProxyFactory()
```

  - 

### Method Detail

    - 

#### isCallerMockInvocationHandlerInvoke

```
public static boolean isCallerMockInvocationHandlerInvoke​(Throwable e)
```

    - 

#### createProxy

```
public <T> T createProxy​(Class<T> toMock,
                         InvocationHandler handler,
                         Method[] mockedMethods,
                         ConstructorArgs args)
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
`args` - the constructor arguments to use, or null to use
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