# Class FilteredClassLoader.ClassFilter

java.lang.Object
org.springframework.boot.test.context.FilteredClassLoader.ClassFilter

All Implemented Interfaces:
`Predicate<String>`

Enclosing class:
`FilteredClassLoader`

---

public static final class FilteredClassLoader.ClassFilter
extends Object
implements Predicate<String>
Filter to restrict the classes that can be loaded.

Since:
2.0.0

- 

## Method Summary

Modifier and Type
Method
Description
`static FilteredClassLoader.ClassFilter`
`of(Class<?>... hiddenClasses)`
 
`boolean`
`test(String className)`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface Predicate

`and, negate, or`

- 

## Method Details

  - 

### test

public boolean test(String className)

Specified by:
`test` in interface `Predicate<String>`

  - 

### of

public static FilteredClassLoader.ClassFilter of(Class<?>... hiddenClasses)