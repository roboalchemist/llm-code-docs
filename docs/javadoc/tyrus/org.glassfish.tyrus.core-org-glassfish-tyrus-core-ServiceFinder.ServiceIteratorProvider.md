Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class ServiceFinder.ServiceIteratorProvider

java.lang.Object
org.glassfish.tyrus.core.ServiceFinder.ServiceIteratorProvider

Direct Known Subclasses:
`ServiceFinder.DefaultServiceIteratorProvider`

Enclosing class:
`ServiceFinder<T>`

---

public abstract static class ServiceFinder.ServiceIteratorProvider
extends Object
Supports iteration of provider instances or classes.

 The default implementation looks up provider classes from META-INF/services
 files, see `ServiceFinder.DefaultServiceIteratorProvider`.
 This implementation may be overridden by invoking
 `ServiceFinder.setIteratorProvider(ServiceIteratorProvider)`

-

## Constructor Summary

Constructors

Constructor
Description
`ServiceIteratorProvider()`

-

## Method Summary

Modifier and Type
Method
Description
`abstract <T> Iterator<Class<T>>`
`createClassIterator(Class<T> service,
 String serviceName,
 ClassLoader loader,
 boolean ignoreOnClassNotFound)`

Iterate over provider classes of a service.

`abstract <T> Iterator<T>`
`createIterator(Class<T> service,
 String serviceName,
 ClassLoader loader,
 boolean ignoreOnClassNotFound)`

Iterate over provider instances of a service.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### ServiceIteratorProvider

public ServiceIteratorProvider()

-

## Method Details

-

### createIterator

public abstract <T> Iterator<T> createIterator(Class<T> service,
 String serviceName,
 ClassLoader loader,
 boolean ignoreOnClassNotFound)
Iterate over provider instances of a service.

Type Parameters:
`T` - the type of the service.
Parameters:
`service` - the service class.
`serviceName` - the service name.
`loader` - the class loader to utilize when loading provider
                              classes.
`ignoreOnClassNotFound` - if true ignore an instance if the
                              corresponding provider class if cannot be found,
                              otherwise throw a `ClassNotFoundException`.
Returns:
the provider instance iterator.

-

### createClassIterator

public abstract <T> Iterator<Class<T>> createClassIterator(Class<T> service,
 String serviceName,
 ClassLoader loader,
 boolean ignoreOnClassNotFound)
Iterate over provider classes of a service.

Type Parameters:
`T` - the type of the service.
Parameters:
`service` - the service class.
`serviceName` - the service name.
`loader` - the class loader to utilize when loading provider
                              classes.
`ignoreOnClassNotFound` - if true ignore the provider class if
                              cannot be found,
                              otherwise throw a `ClassNotFoundException`.
Returns:
the provider class iterator.
