# Class FilteredClassLoader.PackageFilter

java.lang.Object
org.springframework.boot.test.context.FilteredClassLoader.PackageFilter

All Implemented Interfaces:
`Predicate<String>`

Enclosing class:
`FilteredClassLoader`

---

public static final class FilteredClassLoader.PackageFilter
extends Object
implements Predicate<String>
Filter to restrict the packages that can be loaded.

Since:
2.0.0

- 

## Method Summary

Modifier and Type
Method
Description
`static FilteredClassLoader.PackageFilter`
`of(String... hiddenPackages)`
 
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

public static FilteredClassLoader.PackageFilter of(String... hiddenPackages)