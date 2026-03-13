# Class GenericConstraintDef<A extends Annotation>

java.lang.Object
org.hibernate.validator.cfg.AnnotationDef<GenericConstraintDef<A>, A>
org.hibernate.validator.cfg.ConstraintDef<GenericConstraintDef<A>, A>
org.hibernate.validator.cfg.GenericConstraintDef<A>

Type Parameters:
`A` - The constraint annotation type.

---

public class GenericConstraintDef<A extends Annotation>
extends ConstraintDef<GenericConstraintDef<A>, A>
A `ConstraintDef` class which can be used to configure any constraint
type. For this purpose the class defines a generic method
`param(String, Object)` which allows to add
arbitrary constraint parameters.

Author:
Hardy Ferentschik, Gunnar Morling

- 

## Constructor Summary

Constructors

Constructor
Description
`GenericConstraintDef(Class<A> constraintType)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`GenericConstraintDef<A>`
`param(String key,
 Object value)`
 

### Methods inherited from class ConstraintDef

`groups, message, payload`

### Methods inherited from class AnnotationDef

`addAnnotationAsParameter, addParameter, toString`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### GenericConstraintDef

public GenericConstraintDef(Class<A> constraintType)

- 

## Method Details

  - 

### param

public GenericConstraintDef<A> param(String key,
 Object value)

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved