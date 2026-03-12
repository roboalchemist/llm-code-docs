Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class OsgiRegistry

java.lang.Object
org.glassfish.tyrus.core.OsgiRegistry

All Implemented Interfaces:
`EventListener`, `org.osgi.framework.BundleListener`, `org.osgi.framework.SynchronousBundleListener`

---

public final class OsgiRegistry
extends Object
implements org.osgi.framework.SynchronousBundleListener
Taken from Jersey 2. Utility class to deal with OSGi runtime specific behavior.
 This is mainly to handle META-INF/services lookup
 and generic/application class lookup issue in OSGi.

 When OSGi runtime is detected by the `ServiceFinder` class,
 an instance of OsgiRegistry is created and associated with given
 OSGi BundleContext. META-INF/services entries are then being accessed
 via the OSGi Bundle API as direct ClassLoader#getResource() method invocation
 does not work in this case within OSGi.

Author:
Jakub Podlesak

-

## Method Summary

Modifier and Type
Method
Description
`void`
`bundleChanged(org.osgi.framework.BundleEvent event)`

`Class<?>`
`classForNameWithException(String className)`

Get the Class from the class name.

`static OsgiRegistry`
`getInstance()`

Returns an `OsgiRegistry` instance.

`Enumeration<URL>`
`getPackageResources(String packagePath,
 ClassLoader classLoader)`

`ResourceBundle`
`getResourceBundle(String bundleName)`

Tries to load resource bundle via OSGi means.

`void`
`hookUp()`

Will hook up this instance with the OSGi runtime.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Method Details

-

### getInstance

public static OsgiRegistry getInstance()
Returns an `OsgiRegistry` instance. Call this method only if sure that the application is running in OSGi
 environment, otherwise a call to this method can lead to an `ClassNotFoundException`.

Returns:
an `OsgiRegistry` instance.

-

### bundleChanged

public void bundleChanged(org.osgi.framework.BundleEvent event)

Specified by:
`bundleChanged` in interface `org.osgi.framework.BundleListener`

-

### getPackageResources

public Enumeration<URL> getPackageResources(String packagePath,
 ClassLoader classLoader)

-

### classForNameWithException

public Class<?> classForNameWithException(String className)
                                   throws ClassNotFoundException
Get the Class from the class name.

 The context class loader will be utilized if accessible and non-null.
 Otherwise the defining class loader of this class will
 be utilized.

Parameters:
`className` - the class name.
Returns:
the Class, otherwise null if the class cannot be found.
Throws:
`ClassNotFoundException` - if the class cannot be found.

-

### getResourceBundle

public ResourceBundle getResourceBundle(String bundleName)
Tries to load resource bundle via OSGi means. No caching involved here,
 as localization properties are being cached in Localizer class already.

Parameters:
`bundleName` - name of the resource bundle to load
Returns:
resource bundle instance if found, null otherwise

-

### hookUp

public void hookUp()
Will hook up this instance with the OSGi runtime.
 This is to actually update SPI provider lookup and class loading mechanisms in Jersey
 to utilize OSGi features.
