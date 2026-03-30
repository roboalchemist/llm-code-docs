# Class FilteredClassLoader.ClassPathResourceFilter

java.lang.Object
org.springframework.boot.test.context.FilteredClassLoader.ClassPathResourceFilter

All Implemented Interfaces:
`Predicate<String>`

Enclosing class:
`FilteredClassLoader`

---

public static final class FilteredClassLoader.ClassPathResourceFilter
extends Object
implements Predicate<String>
Filter to restrict the resources that can be loaded.

Since:
2.1.0

- 

## Method Summary

Modifier and Type
Method
Description
`static FilteredClassLoader.ClassPathResourceFilter`
`of(org.springframework.core.io.ClassPathResource... hiddenResources)`
 
`boolean`
`test(String resourceName)`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface Predicate

`and, negate, or`

- 

## Method Details

  - 

### test

public boolean test(String resourceName)

Specified by:
`test` in interface `Predicate<String>`

  - 

### of

public static FilteredClassLoader.ClassPathResourceFilter of(org.springframework.core.io.ClassPathResource... hiddenResources)