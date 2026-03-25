# Class AnnotatedClassFinder

java.lang.Object
org.springframework.boot.test.context.AnnotatedClassFinder

---

public final class AnnotatedClassFinder
extends Object
Utility class to find a class annotated with a particular annotation in a hierarchy.

Since:
2.1.0

- 

## Constructor Summary

Constructors

Constructor
Description
`AnnotatedClassFinder(Class<? extends Annotation> annotationType)`

Create a new instance with the `annotationType` to find.

- 

## Method Summary

Modifier and Type
Method
Description
`@Nullable Class<?>`
`findFromClass(Class<?> source)`

Find the first `Class` that is annotated with the target annotation, starting
from the package defined by the given `source` up to the root.

`@Nullable Class<?>`
`findFromPackage(String source)`

Find the first `Class` that is annotated with the target annotation, starting
from the package defined by the given `source` up to the root.

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### AnnotatedClassFinder

public AnnotatedClassFinder(Class<? extends Annotation> annotationType)
Create a new instance with the `annotationType` to find.

Parameters:
`annotationType` - the annotation to find

- 

## Method Details

  - 

### findFromClass

public @Nullable Class<?> findFromClass(Class<?> source)
Find the first `Class` that is annotated with the target annotation, starting
from the package defined by the given `source` up to the root.

Parameters:
`source` - the source class to use to initiate the search
Returns:
the first `Class` annotated with the target annotation within the
hierarchy defined by the given `source` or `null` if none is found.

  - 

### findFromPackage

public @Nullable Class<?> findFromPackage(String source)
Find the first `Class` that is annotated with the target annotation, starting
from the package defined by the given `source` up to the root.

Parameters:
`source` - the source package to use to initiate the search
Returns:
the first `Class` annotated with the target annotation within the
hierarchy defined by the given `source` or `null` if none is found.