Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class ReflectionHelper

java.lang.Object
org.glassfish.tyrus.core.ReflectionHelper

---

public class ReflectionHelper
extends Object
Utility methods for Java reflection.

Author:
[email protected]

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static class`
`ReflectionHelper.ClassTypePair`

A tuple consisting of a class and type of the class.

`static class`
`ReflectionHelper.DeclaringClassInterfacePair`

A tuple consisting of a concrete class, declaring class that declares a generic interface type.

`static final class`
`ReflectionHelper.TypeClassPair`

-

## Constructor Summary

Constructors

Constructor
Description
`ReflectionHelper()`

-

## Method Summary

Modifier and Type
Method
Description
`static Class`
`classForName(String name)`

Get the Class from the class name.

`static Class`
`classForName(String name,
 ClassLoader cl)`

Get the Class from the class name.

`static Class`
`classForNameWithException(String name)`

Get the Class from the class name.

`static Class`
`classForNameWithException(String name,
 ClassLoader cl)`

Get the Class from the class name.

`static <T> PrivilegedExceptionAction<Class<T>>`
`classForNameWithExceptionPEA(String name)`

Get privileged exception action to obtain Class from given class name.

`static <T> PrivilegedExceptionAction<Class<T>>`
`classForNameWithExceptionPEA(String name,
 ClassLoader cl)`

Get privileged exception action to obtain Class from given class name.

`static Method`
`findMethodOnClass(Class c,
 Method m)`

Find a method on a class given an existing method.

`static Class`
`getArrayClass(Class c)`

Get Array class of component class.

`static ReflectionHelper.DeclaringClassInterfacePair`
`getClass(Class concrete,
 Class iface)`

Find the declaring class that implements or extends an interface.

`static Class<?>`
`getClassType(Class<?> inspectedClass,
 Class<?> superClass)`

Find a type of the class given it's Superclass.

`static PrivilegedAction<ClassLoader>`
`getContextClassLoaderPA()`

Get privileged action to obtain context class loader.

`static Class`
`getDeclaringClass(AccessibleObject ao)`

Get declaring class of provided field, method or constructor.

`static Method`
`getFromStringStringMethod(Class c)`

Get the static fromString(String ) method.

`static Class`
`getGenericClass(Type parameterizedType)`

Get the class that is the type argument of a parameterized type.

`static <T> T`
`getInstance(Class<T> c)`

Creates an instance of `Class` c using `Class.newInstance()`.

`static <T> T`
`getInstance(Class<T> c,
 ErrorCollector collector)`

Creates an instance of `Class` c using `Class.newInstance()`.

`static OsgiRegistry`
`getOsgiRegistryInstance()`

Returns an `OsgiRegistry` instance.

`static Class[]`
`getParameterizedClassArguments(ReflectionHelper.DeclaringClassInterfacePair p)`

Get the parameterized class arguments for a declaring class that declares a generic interface type.

`static Type[]`
`getParameterizedTypeArguments(ReflectionHelper.DeclaringClassInterfacePair p)`

Get the parameterized type arguments for a declaring class that declares a generic interface type.

`static Constructor`
`getStringConstructor(Class c)`

Get the constructor that has a single parameter of String.

`static ReflectionHelper.TypeClassPair`
`getTypeArgumentAndClass(Type parameterizedType)`

`static Method`
`getValueOfStringMethod(Class c)`

Get the static valueOf(String ) method.

`static String`
`methodInstanceToString(Object o,
 Method m)`

Create a string representation of a method and an instance whose
 class implements the method.

`static String`
`objectToString(Object o)`

Create a string representation of an object.

`static ReflectionHelper.ClassTypePair`
`resolveTypeVariable(Class c,
 Class dc,
 TypeVariable tv)`

Given a type variable resolve the Java class of that variable.

`static void`
`setAccessibleMethod(Method m)`

Set a method to be accessible.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### ReflectionHelper

public ReflectionHelper()

-

## Method Details

-

### getDeclaringClass

public static Class getDeclaringClass(AccessibleObject ao)
Get declaring class of provided field, method or constructor.

Parameters:
`ao` - object for which the declared class will be returned.
Returns:
declaring class of provided object.

-

### objectToString

public static String objectToString(Object o)
Create a string representation of an object.

 Returns a string consisting of the name of the class of which the
 object is an instance, the at-sign character '`@`', and
 the unsigned hexadecimal representation of the hash code of the
 object. In other words, this method returns a string equal to the
 value of:

```

 o.getClass().getName() + '@' + Integer.toHexString(o.hashCode())
 
```

Parameters:
`o` - the object.
Returns:
the string representation of the object.

-

### methodInstanceToString

public static String methodInstanceToString(Object o,
 Method m)
Create a string representation of a method and an instance whose
 class implements the method.

 Returns a string consisting of the name of the class of which the object
 is an instance, the at-sign character '`@`',
 the unsigned hexadecimal representation of the hash code of the
 object, the character '`.`', the name of the method,
 the character '`(`', the list of method parameters, and
 the character '`)`'. In other words, thos method returns a
 string equal to the value of:

```

 o.getClass().getName() + '@' + Integer.toHexString(o.hashCode()) +
 '.' + m.getName() + '(' + <parameters> + ')'.
 
```

Parameters:
`o` - the object whose class implements `m`.
`m` - the method.
Returns:
the string representation of the method and instance.

-

### classForName

public static Class classForName(String name)
Get the Class from the class name.

 The context class loader will be utilized if accessible and non-null.
 Otherwise the defining class loader of this class will
 be utilized.

Parameters:
`name` - the class name.
Returns:
the Class, otherwise null if the class cannot be found.

-

### classForName

public static Class classForName(String name,
 ClassLoader cl)
Get the Class from the class name.

Parameters:
`name` - the class name.
`cl` - the class loader to use, if null then the defining class loader
             of this class will be utilized.
Returns:
the Class, otherwise null if the class cannot be found.

-

### classForNameWithException

public static Class classForNameWithException(String name)
                                       throws ClassNotFoundException
Get the Class from the class name.

 The context class loader will be utilized if accessible and non-null.
 Otherwise the defining class loader of this class will
 be utilized.

Parameters:
`name` - the class name.
Returns:
the Class, otherwise null if the class cannot be found.
Throws:
`ClassNotFoundException` - if the class cannot be found.

-

### classForNameWithException

public static Class classForNameWithException(String name,
 ClassLoader cl)
                                       throws ClassNotFoundException
Get the Class from the class name.

Parameters:
`name` - the class name.
`cl` - the class loader to use, if null then the defining class loader
             of this class will be utilized.
Returns:
the Class, otherwise null if the class cannot be found.
Throws:
`ClassNotFoundException` - if the class cannot be found.

-

### classForNameWithExceptionPEA

public static <T>
PrivilegedExceptionAction<Class<T>> classForNameWithExceptionPEA(String name)
                                                          throws ClassNotFoundException
Get privileged exception action to obtain Class from given class name.
 If run using security manager, the returned privileged exception action
 must be invoked within a doPrivileged block.

 The actual context class loader will be utilized if accessible and non-null.
 Otherwise the defining class loader of the calling class will be utilized.

Type Parameters:
`T` - class type.
Parameters:
`name` - class name.
Returns:
privileged exception action to obtain the Class.
 The action could throw `ClassNotFoundException` or return `null` if the class cannot be found.
Throws:
`ClassNotFoundException` - when provided string contains classname of unknown class.
See Also:

    - `AccessController.doPrivileged(java.security.PrivilegedExceptionAction)`

  -

### classForNameWithExceptionPEA

public static <T>
PrivilegedExceptionAction<Class<T>> classForNameWithExceptionPEA(String name,
 ClassLoader cl)
                                                          throws ClassNotFoundException
Get privileged exception action to obtain Class from given class name.
 If run using security manager, the returned privileged exception action
 must be invoked within a doPrivileged block.

Type Parameters:
`T` - class type.
Parameters:
`name` - class name.
`cl` - class loader to use, if `null` then the defining class loader
             of the calling class will be utilized.
Returns:
privileged exception action to obtain the Class.
 The action throws `ClassNotFoundException`
 or returns `null` if the class cannot be found.
Throws:
`ClassNotFoundException` - when provided string contains classname of unknown class.
See Also:

    - `AccessController.doPrivileged(java.security.PrivilegedExceptionAction)`

  -

### getContextClassLoaderPA

public static PrivilegedAction<ClassLoader> getContextClassLoaderPA()
Get privileged action to obtain context class loader.
 If run using security manager, the returned privileged action
 must be invoked within a doPrivileged block.

Returns:
privileged action to obtain the actual context class loader.
 The action could return `null` if context class loader has not been set.
See Also:

    - `AccessController.doPrivileged(java.security.PrivilegedAction)`

  -

### setAccessibleMethod

public static void setAccessibleMethod(Method m)
Set a method to be accessible.

Parameters:
`m` - the method to be set as accessible

-

### getGenericClass

public static Class getGenericClass(Type parameterizedType)
                             throws IllegalArgumentException
Get the class that is the type argument of a parameterized type.

Parameters:
`parameterizedType` - must be an instance of ParameterizedType
                          and have exactly one type argument.
Returns:
the class of the actual type argument. If the type argument
 is a class then the class is returned. If the type argument
 is a generic array type and the generic component type is a
 class then class of the array is returned. if the type argument
 is a parameterized type and it's raw type is a class then
 that class is returned.
 If the parameterizedType is not an instance of ParameterizedType
 or contains more than one type argument null is returned.
Throws:
`IllegalArgumentException` - if the single type argument is not of
                                  a class, or a generic array type, or the generic component type
                                  of the generic array type is not class, or not a parameterized
                                  type with a raw type that is not a class.

-

### getTypeArgumentAndClass

public static ReflectionHelper.TypeClassPair getTypeArgumentAndClass(Type parameterizedType)
                                                              throws IllegalArgumentException

Throws:
`IllegalArgumentException`

-

### getArrayClass

public static Class getArrayClass(Class c)
Get Array class of component class.

Parameters:
`c` - the component class of the array
Returns:
the array class.

-

### getValueOfStringMethod

public static Method getValueOfStringMethod(Class c)
Get the static valueOf(String ) method.

Parameters:
`c` - The class to obtain the method.
Returns:
the method, otherwise null if the method is not present.

-

### getFromStringStringMethod

public static Method getFromStringStringMethod(Class c)
Get the static fromString(String ) method.

Parameters:
`c` - The class to obtain the method.
Returns:
the method, otherwise null if the method is not present.

-

### getStringConstructor

public static Constructor getStringConstructor(Class c)
Get the constructor that has a single parameter of String.

Parameters:
`c` - The class to obtain the constructor.
Returns:
the constructor, otherwise null if the constructor is not present.

-

### getParameterizedClassArguments

public static Class[] getParameterizedClassArguments(ReflectionHelper.DeclaringClassInterfacePair p)
Get the parameterized class arguments for a declaring class that declares a generic interface type.

Parameters:
`p` - the declaring class
Returns:
the parameterized class arguments, or null if the generic interface type is not a parameterized type.

-

### getParameterizedTypeArguments

public static Type[] getParameterizedTypeArguments(ReflectionHelper.DeclaringClassInterfacePair p)
Get the parameterized type arguments for a declaring class that declares a generic interface type.

Parameters:
`p` - the declaring class
Returns:
the parameterized type arguments, or null if the generic interface type is not a parameterized type.

-

### getClass

public static ReflectionHelper.DeclaringClassInterfacePair getClass(Class concrete,
 Class iface)
Find the declaring class that implements or extends an interface.

Parameters:
`concrete` - the concrete class than directly or indirectly implements or extends an interface class.
`iface` - the interface class.
Returns:
the tuple of the declaring class and the generic interface type.

-

### resolveTypeVariable

public static ReflectionHelper.ClassTypePair resolveTypeVariable(Class c,
 Class dc,
 TypeVariable tv)
Given a type variable resolve the Java class of that variable.

Parameters:
`c` - the concrete class from which all type variables are resolved
`dc` - the declaring class where the type variable was defined
`tv` - the type variable
Returns:
the resolved Java class and type, otherwise null if the type variable could not be resolved

-

### findMethodOnClass

public static Method findMethodOnClass(Class c,
 Method m)
Find a method on a class given an existing method.

 If there exists a public method on the class that has the same name
 and parameters as the existing method then that public method is
 returned.

 Otherwise, if there exists a public method on the class that has
 the same name and the same number of parameters as the existing method,
 and each generic parameter type, in order, of the public method is equal
 to the generic parameter type, in the same order, of the existing method
 or is an instance of `TypeVariable` then that public method is
 returned.

Parameters:
`c` - the class to search for a public method
`m` - the method to find
Returns:
the found public method.

-

### getClassType

public static Class<?> getClassType(Class<?> inspectedClass,
 Class<?> superClass)
Find a type of the class given it's Superclass.

Parameters:
`inspectedClass` - Class whose type is searched for.
`superClass` - Class relatively to which the search is performed.
Returns:
type of the class.

-

### getOsgiRegistryInstance

public static OsgiRegistry getOsgiRegistryInstance()
Returns an `OsgiRegistry` instance.

Returns:
an `OsgiRegistry` instance or `null` if the class cannot be instantiated (not in OSGi
 environment).

-

### getInstance

public static <T> T getInstance(Class<T> c,
 ErrorCollector collector)
Creates an instance of `Class` c using `Class.newInstance()`. Exceptions are logged to `ErrorCollector`.

Type Parameters:
`T` - type.
Parameters:
`c` - `Class` whose instance is going to be created
`collector` - `ErrorCollector` which collects the `Exception`s.
Returns:
new instance of `Class`.

-

### getInstance

public static <T> T getInstance(Class<T> c)
                         throws IllegalAccessException,
InstantiationException
Creates an instance of `Class` c using `Class.newInstance()`.

Type Parameters:
`T` - type.
Parameters:
`c` - `Class` whose instance is going to be created
Returns:
new instance of `Class`.
Throws:
`IllegalAccessException` - if the class or its nullary
                                constructor is not accessible.
`InstantiationException` - if this `Class` represents an abstract class,
                                an interface, an array class, a primitive type, or void;
                                or if the class has no nullary constructor;
                                or if the instantiation fails for some other reason.
