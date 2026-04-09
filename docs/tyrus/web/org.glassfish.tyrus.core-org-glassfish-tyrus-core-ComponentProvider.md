Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class ComponentProvider

java.lang.Object
org.glassfish.tyrus.core.ComponentProvider

Direct Known Subclasses:
`DefaultComponentProvider`

---

public abstract class ComponentProvider
extends Object
Provides an instance.

 Method `isApplicable(Class)` is called first to check whether the provider is able to provide the given
 `Class`.  Method `create(Class)` is called to get the instance.

Author:
Stepan Kopriva, Martin Matula, Pavel Bucek

-

## Constructor Summary

Constructors

Constructor
Description
`ComponentProvider()`

-

## Method Summary

Modifier and Type
Method
Description
`abstract <T> Object`
`create(Class<T> c)`

Create new instance.

`abstract boolean`
`destroy(Object o)`

Destroys the given managed instance.

`Method`
`getInvocableMethod(Method method)`

Get the method which should be invoked instead provided one.

`abstract boolean`
`isApplicable(Class<?> c)`

Checks whether this component provider is able to provide an instance of given `Class`.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### ComponentProvider

public ComponentProvider()

-

## Method Details

-

### isApplicable

public abstract boolean isApplicable(Class<?> c)
Checks whether this component provider is able to provide an instance of given `Class`.

Parameters:
`c` - `Class` to be checked.
Returns:
`true` iff this `ComponentProvider` is able to create an instance of the given `Class`.

-

### create

public abstract <T> Object create(Class<T> c)
Create new instance.

Type Parameters:
`T` - type of the created object.
Parameters:
`c` - `Class` to be created.
Returns:
instance, iff found, `null` otherwise.

-

### getInvocableMethod

public Method getInvocableMethod(Method method)
Get the method which should be invoked instead provided one.

 Useful mainly for EJB container support, where methods from endpoint class cannot be invoked directly - Tyrus
 needs
 to use method declared on remote interface.

 Default implementation returns method provided as parameter.

Parameters:
`method` - method from endpoint class.
Returns:
method which should be invoked.

-

### destroy

public abstract boolean destroy(Object o)
Destroys the given managed instance.

Parameters:
`o` - instance to be destroyed.
Returns:
`true` iff the instance was coupled to this `ComponentProvider`, false otherwise.
