# Interface ConstraintMapping

---

public interface ConstraintMapping
Represents a constraint mapping configured via the programmatic API.

Author:
Hardy Ferentschik, Gunnar Morling, Kevin Pollet <[email protected]> (C) 2011 SERLI, Yoann Rodiere

- 

## Method Summary

Modifier and Type
Method
Description
`<A extends Annotation>
ConstraintDefinitionContext<A>`
`constraintDefinition(Class<A> annotationClass)`

Starts defining `ConstraintValidator`s to be executed for the specified constraint (i.e. annotation class).

`<C> TypeConstraintMappingContext<C>`
`type(Class<C> beanClass)`

Starts defining constraints on the specified bean class.

- 

## Method Details

  - 

### type

<C> TypeConstraintMappingContext<C> type(Class<C> beanClass)
Starts defining constraints on the specified bean class. Each bean class may only be configured once within all
constraint mappings used for configuring one validator factory.

Type Parameters:
`C` - The type to be configured.
Parameters:
`beanClass` - The bean class on which to define constraints. All constraints defined after calling this method
are added to the bean of the type `beanClass` until the next call of `type` or `annotation`.
Returns:
Instance allowing for defining constraints on the specified class.

  - 

### constraintDefinition

<A extends Annotation>
ConstraintDefinitionContext<A> constraintDefinition(Class<A> annotationClass)
Starts defining `ConstraintValidator`s to be executed for the specified constraint (i.e. annotation class).
Each constraint may only be configured once within all constraint mappings used for configuring one validator
factory.

Type Parameters:
`A` - The annotation type to be configured.
Parameters:
`annotationClass` - The annotation class on which to define the validators. This type must be an
`@interface` annotated with `jakarta.validation.Constraint`. All validators defined after calling
this method are added to the annotation of the type `annotationClass` until the next call
of `type` or `annotation`.
Returns:
Instance allowing for defining validators to be executed for the specified constraint.
Since:
5.3

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved