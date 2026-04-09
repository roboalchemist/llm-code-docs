Module org.easymock
Package org.easymock.internal

## Interface IProxyFactory

- 

All Known Implementing Classes:
`AndroidClassProxyFactory`, `ClassProxyFactory`, `JavaProxyFactory`

---

```
public interface IProxyFactory
```

Reponsible of creating proxies for objects. The implementation used for an object to proxy depends on its type but also
 on the JVM we are running.

Author:
OFFIS, Tammo Freese

- 

  - 

### Method Summary

All Methods Instance Methods Abstract Methods 

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

  - 

### Method Detail

    - 

#### createProxy

```
<T> T createProxy​(Class<T> toMock,
                  InvocationHandler handler,
                  Method[] mockedMethods,
                  ConstructorArgs constructorArgs)
```

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
InvocationHandler getInvocationHandler​(Object mock)
```

Returns the invocation handler for `mock`;

Parameters:
`mock` - a mock instance previously returned by `createProxy`.
Returns:
the handler handling method calls for the `mock`