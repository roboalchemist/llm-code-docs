Module org.easymock
Package org.easymock.internal

## Class ClassProxyFactory.MockMethodInterceptor

- java.lang.Object

- 

  - org.easymock.internal.ClassProxyFactory.MockMethodInterceptor

- 

All Implemented Interfaces:
`Serializable`

Enclosing class:
ClassProxyFactory

---

```
public static class ClassProxyFactory.MockMethodInterceptor
extends Object
implements Serializable
```

See Also:
Serialized Form

- 

  - 

### Constructor Summary

Constructors 

Constructor
Description

`MockMethodInterceptor()`
 

  - 

### Method Summary

All Methods Static Methods Concrete Methods 

Modifier and Type
Method
Description

`static Object`
`interceptAbstract​(Object obj,
                 ClassMockingData mockingData,
                 Object stubValue,
                 Method method,
                 Object[] args)`
 

`static Object`
`interceptSuperCallable​(Object obj,
                      ClassMockingData mockingData,
                      Method method,
                      Object[] args,
                      Callable<?> superCall)`
 

    - 

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

  - 

### Constructor Detail

    - 

#### MockMethodInterceptor

```
public MockMethodInterceptor()
```

  - 

### Method Detail

    - 

#### interceptSuperCallable

```
@RuntimeType
@BindingPriority(2)
public static Object interceptSuperCallable​(@This
                                            Object obj,
                                            @FieldValue("$callback")
                                            ClassMockingData mockingData,
                                            @Origin
                                            Method method,
                                            @AllArguments
                                            Object[] args,
                                            @SuperCall(serializableProxy=true)
                                            Callable<?> superCall)
                                     throws Throwable
```

Throws:
`Throwable`

    - 

#### interceptAbstract

```
@RuntimeType
public static Object interceptAbstract​(@This
                                       Object obj,
                                       @FieldValue("$callback")
                                       ClassMockingData mockingData,
                                       @StubValue
                                       Object stubValue,
                                       @Origin
                                       Method method,
                                       @AllArguments
                                       Object[] args)
                                throws Throwable
```

Throws:
`Throwable`