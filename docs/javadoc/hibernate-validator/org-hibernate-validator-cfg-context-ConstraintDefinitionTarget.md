# Interface ConstraintDefinitionTarget

All Known Subinterfaces:
`ConstraintDefinitionContext<A>, ConstraintMappingTarget, ContainerElementConstraintMappingContext, CrossParameterConstraintMappingContext, ParameterConstraintMappingContext, PropertyConstraintMappingContext, ReturnValueConstraintMappingContext, TypeConstraintMappingContext<C>`

---

public interface ConstraintDefinitionTarget
Facet of a constraint definition creational context which allows to select the constraint (annotation type) to
which the next operations shall apply.

Author:
Yoann Rodiere

- 

## Method Summary

Modifier and Type
Method
Description
`<A extends Annotation>
ConstraintDefinitionContext<A>`
`constraintDefinition(Class<A> annotationType)`

Selects the constraint (i.e. annotation type) to which the next operations shall apply.

- 

## Method Details

  - 

### constraintDefinition

<A extends Annotation>
ConstraintDefinitionContext<A> constraintDefinition(Class<A> annotationType)
Selects the constraint (i.e. annotation type) to which the next operations shall apply. A given constraint
may only be configured once.

Type Parameters:
`A` - The annotation type to select.
Parameters:
`annotationType` - The annotation type to select. This type must be an `@interface` annotated with
`jakarta.validation.Constraint`.
Returns:
A creational context representing the selected constraint.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved