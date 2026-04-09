Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class DefaultComponentProvider

java.lang.Object
org.glassfish.tyrus.core.ComponentProvider
org.glassfish.tyrus.core.DefaultComponentProvider

---

public class DefaultComponentProvider
extends ComponentProvider
Provides instances using reflection.

Author:
Stepan Kopriva

-

## Constructor Summary

Constructors

Constructor
Description
`DefaultComponentProvider()`

-

## Method Summary

Modifier and Type
Method
Description
`<T> Object`
`create(Class<T> toLoad)`

Create new instance.

`boolean`
`destroy(Object o)`

Destroys the given managed instance.

`Method`
`getInvocableMethod(Method method)`

Get the method which should be invoked instead provided one.

`boolean`
`isApplicable(Class<?> c)`

Checks whether this component provider is able to provide an instance of given `Class`.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### DefaultComponentProvider

public DefaultComponentProvider()

-

## Method Details

-

### isApplicable

public boolean isApplicable(Class<?> c)
Description copied from class: `ComponentProvider`
Checks whether this component provider is able to provide an instance of given `Class`.

Specified by:
`isApplicable` in class `ComponentProvider`
Parameters:
`c` - `Class` to be checked.
Returns:
`true` iff this `ComponentProvider` is able to create an instance of the given `Class`.

-

### create

public <T> Object create(Class<T> toLoad)
Description copied from class: `ComponentProvider`
Create new instance.

Specified by:
`create` in class `ComponentProvider`
Type Parameters:
`T` - type of the created object.
Parameters:
`toLoad` - `Class` to be created.
Returns:
instance, iff found, `null` otherwise.

-

### destroy

public boolean destroy(Object o)
Description copied from class: `ComponentProvider`
Destroys the given managed instance.

Specified by:
`destroy` in class `ComponentProvider`
Parameters:
`o` - instance to be destroyed.
Returns:
`true` iff the instance was coupled to this `ComponentProvider`, false otherwise.

-

### getInvocableMethod

public Method getInvocableMethod(Method method)
Description copied from class: `ComponentProvider`
Get the method which should be invoked instead provided one.

 Useful mainly for EJB container support, where methods from endpoint class cannot be invoked directly - Tyrus
 needs
 to use method declared on remote interface.

 Default implementation returns method provided as parameter.

Overrides:
`getInvocableMethod` in class `ComponentProvider`
Parameters:
`method` - method from endpoint class.
Returns:
method which should be invoked.
