Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class ServiceFinder.DefaultServiceIteratorProvider

java.lang.Object
org.glassfish.tyrus.core.ServiceFinder.ServiceIteratorProvider
org.glassfish.tyrus.core.ServiceFinder.DefaultServiceIteratorProvider

Enclosing class:
`ServiceFinder<T>`

---

public static final class ServiceFinder.DefaultServiceIteratorProvider
extends ServiceFinder.ServiceIteratorProvider
The default service iterator provider that looks up provider classes in
 META-INF/services files.

 This class may utilized if a `ServiceFinder.ServiceIteratorProvider` needs to
 reuse the default implementation.

-

## Constructor Summary

Constructors

Constructor
Description
`DefaultServiceIteratorProvider()`

-

## Method Summary

Modifier and Type
Method
Description
`<T> Iterator<Class<T>>`
`createClassIterator(Class<T> service,
 String serviceName,
 ClassLoader loader,
 boolean ignoreOnClassNotFound)`

Iterate over provider classes of a service.

`<T> Iterator<T>`
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

### DefaultServiceIteratorProvider

public DefaultServiceIteratorProvider()

-

## Method Details

-

### createIterator

public <T> Iterator<T> createIterator(Class<T> service,
 String serviceName,
 ClassLoader loader,
 boolean ignoreOnClassNotFound)
Description copied from class: `ServiceFinder.ServiceIteratorProvider`
Iterate over provider instances of a service.

Specified by:
`createIterator` in class `ServiceFinder.ServiceIteratorProvider`
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

public <T> Iterator<Class<T>> createClassIterator(Class<T> service,
 String serviceName,
 ClassLoader loader,
 boolean ignoreOnClassNotFound)
Description copied from class: `ServiceFinder.ServiceIteratorProvider`
Iterate over provider classes of a service.

Specified by:
`createClassIterator` in class `ServiceFinder.ServiceIteratorProvider`
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
