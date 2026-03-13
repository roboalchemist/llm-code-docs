# Interface ConstraintDefinitionContext.ConstraintValidatorDefinitionContext<A extends Annotation, T>

Enclosing interface:
`ConstraintDefinitionContext<A extends Annotation>`

---

@Incubating
public static interface ConstraintDefinitionContext.ConstraintValidatorDefinitionContext<A extends Annotation, T>
Allows to specify a validation implementation for the given constraint and data type using a Lambda expression or
method reference.

Author:
Yoann Rodiere

- 

## Method Summary

Modifier and Type
Method
Description
`ConstraintDefinitionContext<A>`
`with(ConstraintDefinitionContext.ValidationCallable<T> vc)`

Applies the given Lambda expression or referenced method to values to be validated.

- 

## Method Details

  - 

### with

ConstraintDefinitionContext<A> with(ConstraintDefinitionContext.ValidationCallable<T> vc)
Applies the given Lambda expression or referenced method to values to be validated. It is guaranteed that
`null` is never passed to these expressions or methods.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved