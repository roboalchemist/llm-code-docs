# Class AnnotationDef<C extends AnnotationDef<C,A>, A extends Annotation>

java.lang.Object
org.hibernate.validator.cfg.AnnotationDef<C,A>

Type Parameters:
`C` - The type of a concrete sub type. Following to the
"self referencing generic type" pattern each sub type has to be
parametrized with itself.
`A` - The constraint annotation type represented by a concrete sub type.

Direct Known Subclasses:
`ConstraintDef`

---

public abstract class AnnotationDef<C extends AnnotationDef<C,A>, A extends Annotation>
extends Object
Base class for all annotation definition types.

Note that any protected member in this type and its subtypes are not part of the public API and are only meant for internal use.

Author:
Hardy Ferentschik, Gunnar Morling, Marko Bekhta, Guillaume Smet

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`AnnotationDef(Class<A> annotationType)`
 
`protected `
`AnnotationDef(AnnotationDef<?,A> original)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`protected C`
`addAnnotationAsParameter(String key,
 AnnotationDef<?,?> value)`
 
`protected C`
`addParameter(String key,
 Object value)`
 
`String`
`toString()`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### AnnotationDef

protected AnnotationDef(Class<A> annotationType)

  - 

### AnnotationDef

protected AnnotationDef(AnnotationDef<?,A> original)

- 

## Method Details

  - 

### addParameter

protected C addParameter(String key,
 Object value)

  - 

### addAnnotationAsParameter

protected C addAnnotationAsParameter(String key,
 AnnotationDef<?,?> value)

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved