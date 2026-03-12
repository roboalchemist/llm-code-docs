Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class ServiceFinder<T>

java.lang.Object
org.glassfish.tyrus.core.ServiceFinder<T>

Type Parameters:
`T` - the type of the service instance.

All Implemented Interfaces:
`Iterable<T>`

---

public final class ServiceFinder<T>
extends Object
implements Iterable<T>
A simple service-provider lookup mechanism.  A *service* is a
 well-known set of interfaces and (usually abstract) classes.  A *service
 provider* is a specific implementation of a service.  The classes in a
 provider typically implement the interfaces and subclass the classes defined
 in the service itself.  Service providers may be installed in an
 implementation of the Java platform in the form of extensions, that is, jar
 files placed into any of the usual extension directories.  Providers may
 also be made available by adding them to the applet or application class
 path or by some other platform-specific means.

 In this lookup mechanism a service is represented by an interface or an
 abstract class.  (A concrete class may be used, but this is not
 recommended.)  A provider of a given service contains one or more concrete
 classes that extend this *service class* with data and code specific to
 the provider.  This *provider class* will typically not be the entire
 provider itself but rather a proxy that contains enough information to
 decide whether the provider is able to satisfy a particular request together
 with code that can create the actual provider on demand.  The details of
 provider classes tend to be highly service-specific; no single class or
 interface could possibly unify them, so no such class has been defined.  The
 only requirement enforced here is that provider classes must have a
 zero-argument constructor so that they may be instantiated during lookup.

 The default service provider registration/lookup mechanism based
 on `META-INF/services` files is described below.
 For environments, where the basic mechanism is not suitable, clients
 can enforce a different approach by setting their custom `ServiceIteratorProvider`
 by calling `setIteratorProvider`. The call must be made prior to any lookup attempts.

 A service provider identifies itself by placing a provider-configuration
 file in the resource directory `META-INF/services`.  The file's name
 should consist of the fully-qualified name of the abstract service class.
 The file should contain a list of fully-qualified concrete provider-class
 names, one per line.  Space and tab characters surrounding each name, as
 well as blank lines, are ignored.  The comment character is `'#'`
 (`0x23`); on each line all characters following the first comment
 character are ignored.  The file must be encoded in UTF-8.

 If a particular concrete provider class is named in more than one
 configuration file, or is named in the same configuration file more than
 once, then the duplicates will be ignored.  The configuration file naming a
 particular provider need not be in the same jar file or other distribution
 unit as the provider itself.  The provider must be accessible from the same
 class loader that was initially queried to locate the configuration file;
 note that this is not necessarily the class loader that found the file.

 **Example:** Suppose we have a service class named
 `java.io.spi.CharCodec`.  It has two abstract methods:

```

   public abstract CharEncoder getEncoder(String encodingName);
   public abstract CharDecoder getDecoder(String encodingName);
 
```

 Each method returns an appropriate object or `null` if it cannot
 translate the given encoding.  Typical `CharCodec` providers will
 support more than one encoding.

 If `sun.io.StandardCodec` is a provider of the `CharCodec`
 service then its jar file would contain the file
 `META-INF/services/java.io.spi.CharCodec`.  This file would contain
 the single line:

```

   sun.io.StandardCodec    # Standard codecs for the platform
 
```

 To locate an codec for a given encoding name, the internal I/O code would
 do something like this:

```

   CharEncoder getEncoder(String encodingName) {
       for( CharCodec cc : ServiceFinder.find(CharCodec.class) ) {
           CharEncoder ce = cc.getEncoder(encodingName);
           if (ce != null)
               return ce;
       }
       return null;
   }
 
```

 The provider-lookup mechanism always executes in the security context of the
 caller.  Trusted system code should typically invoke the methods in this
 class from within a privileged security context.

Author:
Mark Reinhold, Jakub Podlesak, Marek Potociar

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class`
`ServiceFinder.DefaultServiceIteratorProvider`

The default service iterator provider that looks up provider classes in
 META-INF/services files.

`static class`
`ServiceFinder.ServiceIteratorProvider`

Supports iteration of provider instances or classes.

-

## Method Summary

Modifier and Type
Method
Description
`static <T> ServiceFinder<T>`
`find(Class<T> service)`

Locates and incrementally instantiates the available providers of a
 given service using the context class loader.

`static <T> ServiceFinder<T>`
`find(Class<T> service,
 boolean ignoreOnClassNotFound)`

Locates and incrementally instantiates the available providers of a
 given service using the context class loader.

`static <T> ServiceFinder<T>`
`find(Class<T> service,
 ClassLoader loader)`

Locates and incrementally instantiates the available providers of a
 given service using the given class loader.

`static <T> ServiceFinder<T>`
`find(Class<T> service,
 ClassLoader loader,
 boolean ignoreOnClassNotFound)`

Locates and incrementally instantiates the available providers of a
 given service using the given class loader.

`static ServiceFinder<?>`
`find(String serviceName)`

Locates and incrementally instantiates the available classes of a given
 service file using the context class loader.

`Iterator<T>`
`iterator()`

Returns discovered objects incrementally.

`static void`
`setIteratorProvider(ServiceFinder.ServiceIteratorProvider sip)`

Register the service iterator provider to iterate on provider instances
 or classes.

`T[]`
`toArray()`

Returns discovered objects all at once.

`Class<T>[]`
`toClassArray()`

Returns discovered classes all at once.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface java.lang.Iterable

`forEach, spliterator`

-

## Method Details

-

### find

public static <T> ServiceFinder<T> find(Class<T> service,
 ClassLoader loader)
                                 throws ServiceConfigurationError
Locates and incrementally instantiates the available providers of a
 given service using the given class loader.

 This method transforms the name of the given service class into a
 provider-configuration filename as described above and then uses the
 `getResources` method of the given class loader to find all
 available files with that name.  These files are then read and parsed to
 produce a list of provider-class names.  The iterator that is returned
 uses the given class loader to lookup and then instantiate each element
 of the list.

 Because it is possible for extensions to be installed into a running
 Java virtual machine, this method may return different results each time
 it is invoked.

Type Parameters:
`T` - the type of the service instance.
Parameters:
`service` - The service's abstract service class
`loader` - The class loader to be used to load provider-configuration files
                and instantiate provider classes, or `null` if the system
                class loader (or, failing that the bootstrap class loader) is to
                be used
Returns:
the service finder
Throws:
`ServiceConfigurationError` - If a provider-configuration file violates the specified format
                                   or names a provider class that cannot be found and instantiated
See Also:

    - `find(Class)`

  -

### find

public static <T> ServiceFinder<T> find(Class<T> service,
 ClassLoader loader,
 boolean ignoreOnClassNotFound)
                                 throws ServiceConfigurationError
Locates and incrementally instantiates the available providers of a
 given service using the given class loader.

 This method transforms the name of the given service class into a
 provider-configuration filename as described above and then uses the
 `getResources` method of the given class loader to find all
 available files with that name.  These files are then read and parsed to
 produce a list of provider-class names.  The iterator that is returned
 uses the given class loader to lookup and then instantiate each element
 of the list.

 Because it is possible for extensions to be installed into a running
 Java virtual machine, this method may return different results each time
 it is invoked.

Type Parameters:
`T` - the type of the service instance.
Parameters:
`service` - The service's abstract service class
`loader` - The class loader to be used to load provider-configuration files
                              and instantiate provider classes, or `null` if the system
                              class loader (or, failing that the bootstrap class loader) is to
                              be used
`ignoreOnClassNotFound` - If a provider cannot be loaded by the class loader
                              then move on to the next available provider.
Returns:
the service finder
Throws:
`ServiceConfigurationError` - If a provider-configuration file violates the specified format
                                   or names a provider class that cannot be found and instantiated
See Also:

    - `find(Class)`

  -

### find

public static <T> ServiceFinder<T> find(Class<T> service)
                                 throws ServiceConfigurationError
Locates and incrementally instantiates the available providers of a
 given service using the context class loader.  This convenience method
 is equivalent to

```

   ClassLoader cl = Thread.currentThread().getContextClassLoader();
   return Service.providers(service, cl, false);
 
```

Type Parameters:
`T` - the type of the service instance.
Parameters:
`service` - The service's abstract service class
Returns:
the service finder
Throws:
`ServiceConfigurationError` - If a provider-configuration file violates the specified format
                                   or names a provider class that cannot be found and instantiated
See Also:

    - `find(Class, ClassLoader)`

  -

### find

public static <T> ServiceFinder<T> find(Class<T> service,
 boolean ignoreOnClassNotFound)
                                 throws ServiceConfigurationError
Locates and incrementally instantiates the available providers of a
 given service using the context class loader.  This convenience method
 is equivalent to

```

   ClassLoader cl = Thread.currentThread().getContextClassLoader();
   boolean ingore = ...
   return Service.providers(service, cl, ignore);
 
```

Type Parameters:
`T` - the type of the service instance.
Parameters:
`service` - The service's abstract service class
`ignoreOnClassNotFound` - If a provider cannot be loaded by the class loader
                              then move on to the next available provider.
Returns:
the service finder
Throws:
`ServiceConfigurationError` - If a provider-configuration file violates the specified format
                                   or names a provider class that cannot be found and instantiated
See Also:

    - `find(Class, ClassLoader)`

  -

### find

public static ServiceFinder<?> find(String serviceName)
                             throws ServiceConfigurationError
Locates and incrementally instantiates the available classes of a given
 service file using the context class loader.

Parameters:
`serviceName` - the service name correspond to a file in
                    META-INF/services that contains a list of fully qualified class
                    names
Returns:
the service finder
Throws:
`ServiceConfigurationError` - If a service file violates the specified format
                                   or names a provider class that cannot be found and instantiated

-

### setIteratorProvider

public static void setIteratorProvider(ServiceFinder.ServiceIteratorProvider sip)
                                throws SecurityException
Register the service iterator provider to iterate on provider instances
 or classes.

 The default implementation registered, `ServiceFinder.DefaultServiceIteratorProvider`,
 looks up provider classes in META-INF/service files.

 This method must be called prior to any attempts to obtain provider
 instances or classes.

Parameters:
`sip` - the service iterator provider.
Throws:
`SecurityException` - if the provider cannot be registered.

-

### iterator

public Iterator<T> iterator()
Returns discovered objects incrementally.

Specified by:
`iterator` in interface `Iterable<T>`
Returns:
An `Iterator` that yields provider objects for the given
 service, in some arbitrary order.  The iterator will throw a
 `ServiceConfigurationError` if a provider-configuration
 file violates the specified format or if a provider class cannot
 be found and instantiated.

-

### toArray

public T[] toArray()
            throws ServiceConfigurationError
Returns discovered objects all at once.

Returns:
can be empty but never null.
Throws:
`ServiceConfigurationError` - If a provider-configuration file violates the specified format
                                   or names a provider class that cannot be found and instantiated

-

### toClassArray

public Class<T>[] toClassArray()
                        throws ServiceConfigurationError
Returns discovered classes all at once.

Returns:
can be empty but never null.
Throws:
`ServiceConfigurationError` - If a provider-configuration file violates the specified format
                                   or names a provider class that cannot be found
