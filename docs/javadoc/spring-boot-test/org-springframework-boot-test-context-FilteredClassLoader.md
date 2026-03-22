# Class FilteredClassLoader

java.lang.Object
java.lang.ClassLoader
java.security.SecureClassLoader
java.net.URLClassLoader
org.springframework.boot.test.context.FilteredClassLoader

All Implemented Interfaces:
`Closeable, AutoCloseable, org.springframework.core.SmartClassLoader`

---

public class FilteredClassLoader
extends URLClassLoader
implements org.springframework.core.SmartClassLoader
Test `URLClassLoader` that can filter the classes and resources it can load.

Since:
2.0.0

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class `
`FilteredClassLoader.ClassFilter`

Filter to restrict the classes that can be loaded.

`static final class `
`FilteredClassLoader.ClassPathResourceFilter`

Filter to restrict the resources that can be loaded.

`static final class `
`FilteredClassLoader.PackageFilter`

Filter to restrict the packages that can be loaded.

- 

## Constructor Summary

Constructors

Constructor
Description
`FilteredClassLoader(Class<?>... hiddenClasses)`

Create a `FilteredClassLoader` that hides the given classes.

`FilteredClassLoader(ClassLoader parent,
 Class<?>... hiddenClasses)`

Create a `FilteredClassLoader` with the given `parent` that hides the
given classes.

`FilteredClassLoader(String... hiddenPackages)`

Create a `FilteredClassLoader` that hides classes from the given packages.

`FilteredClassLoader(Predicate<String>... filters)`

Create a `FilteredClassLoader` that filters based on the given predicate.

`FilteredClassLoader(org.springframework.core.io.ClassPathResource... hiddenResources)`

Create a `FilteredClassLoader` that hides resources from the given
`classpath resources`.

- 

## Method Summary

Modifier and Type
Method
Description
`@Nullable URL`
`getResource(String name)`
 
`@Nullable InputStream`
`getResourceAsStream(String name)`
 
`Enumeration<URL>`
`getResources(String name)`
 
`protected Class<?>`
`loadClass(String name,
 boolean resolve)`
 
`Class<?>`
`publicDefineClass(String name,
 byte[] b,
 @Nullable ProtectionDomain protectionDomain)`
 

### Methods inherited from class URLClassLoader

`addURL, close, definePackage, findClass, findResource, findResources, getPermissions, getURLs, newInstance, newInstance`

### Methods inherited from class SecureClassLoader

`defineClass, defineClass`

### Methods inherited from class ClassLoader

`clearAssertionStatus, defineClass, defineClass, defineClass, defineClass, definePackage, findClass, findLibrary, findLoadedClass, findResource, findSystemClass, getClassLoadingLock, getDefinedPackage, getDefinedPackages, getName, getPackage, getPackages, getParent, getPlatformClassLoader, getSystemClassLoader, getSystemResource, getSystemResourceAsStream, getSystemResources, getUnnamedModule, isRegisteredAsParallelCapable, loadClass, registerAsParallelCapable, resolveClass, resources, setClassAssertionStatus, setDefaultAssertionStatus, setPackageAssertionStatus, setSigners`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface org.springframework.core.SmartClassLoader

`getOriginalClassLoader, isClassReloadable`

- 

## Constructor Details

  - 

### FilteredClassLoader

public FilteredClassLoader(Class<?>... hiddenClasses)
Create a `FilteredClassLoader` that hides the given classes.

Parameters:
`hiddenClasses` - the classes to hide

  - 

### FilteredClassLoader

public FilteredClassLoader(ClassLoader parent,
 Class<?>... hiddenClasses)
Create a `FilteredClassLoader` with the given `parent` that hides the
given classes.

Parameters:
`parent` - the parent class loader
`hiddenClasses` - the classes to hide

  - 

### FilteredClassLoader

public FilteredClassLoader(String... hiddenPackages)
Create a `FilteredClassLoader` that hides classes from the given packages.

Parameters:
`hiddenPackages` - the packages to hide

  - 

### FilteredClassLoader

public FilteredClassLoader(org.springframework.core.io.ClassPathResource... hiddenResources)
Create a `FilteredClassLoader` that hides resources from the given
`classpath resources`.

Parameters:
`hiddenResources` - the resources to hide
Since:
2.1.0

  - 

### FilteredClassLoader

@SafeVarargs
public FilteredClassLoader(Predicate<String>... filters)
Create a `FilteredClassLoader` that filters based on the given predicate.

Parameters:
`filters` - a set of filters to determine when a class name or resource should
be hidden. A `result` of `true` indicates a
filtered class or resource. The input of the predicate can either be the binary
name of a class or a resource name.

- 

## Method Details

  - 

### loadClass

protected Class<?> loadClass(String name,
 boolean resolve)
                      throws ClassNotFoundException

Overrides:
`loadClass` in class `ClassLoader`
Throws:
`ClassNotFoundException`

  - 

### getResource

public @Nullable URL getResource(String name)

Overrides:
`getResource` in class `ClassLoader`

  - 

### getResources

public Enumeration<URL> getResources(String name)
                              throws IOException

Overrides:
`getResources` in class `ClassLoader`
Throws:
`IOException`

  - 

### getResourceAsStream

public @Nullable InputStream getResourceAsStream(String name)

Overrides:
`getResourceAsStream` in class `URLClassLoader`

  - 

### publicDefineClass

public Class<?> publicDefineClass(String name,
 byte[] b,
 @Nullable ProtectionDomain protectionDomain)

Specified by:
`publicDefineClass` in interface `org.springframework.core.SmartClassLoader`