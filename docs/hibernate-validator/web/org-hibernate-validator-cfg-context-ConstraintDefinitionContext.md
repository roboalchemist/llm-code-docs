# Interface ConstraintDefinitionContext<A extends Annotation>

Type Parameters:
`A` - The annotation type represented by this context.

All Superinterfaces:
`ConstraintDefinitionTarget, ConstraintMappingTarget, TypeTarget`

---

public interface ConstraintDefinitionContext<A extends Annotation>
extends ConstraintMappingTarget
Constraint mapping creational context representing a constraint (i.e. annotation type). Allows to define which
validators should validate this constraint.

Author:
Yoann Rodiere

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Interface
Description
`static interface `
`ConstraintDefinitionContext.ConstraintValidatorDefinitionContext<A extends Annotation, T>`

Allows to specify a validation implementation for the given constraint and data type using a Lambda expression or
method reference.

`static interface `
`ConstraintDefinitionContext.ValidationCallable<T>`

Callable implementing a validation routine.

- 

## Method Summary

Modifier and Type
Method
Description
`ConstraintDefinitionContext<A>`
`includeExistingValidators(boolean includeExistingValidators)`

Specifies whether validators already mapped to this constraint (i.e. defined in the annotation declaration
through `Constraint.validatedBy()` or the validation engine defaults) should
be included or not.

`ConstraintDefinitionContext<A>`
`validatedBy(Class<? extends ConstraintValidator<A,?>> validator)`

Adds a new validator to validate this constraint.

`<T> ConstraintDefinitionContext.ConstraintValidatorDefinitionContext<A,T>`
`validateType(Class<T> type)`

Allows to configure a validation implementation using a Lambda expression or method reference.

### Methods inherited from interface ConstraintDefinitionTarget

`constraintDefinition`

### Methods inherited from interface TypeTarget

`type`

- 

## Method Details

  - 

### includeExistingValidators

ConstraintDefinitionContext<A> includeExistingValidators(boolean includeExistingValidators)
Specifies whether validators already mapped to this constraint (i.e. defined in the annotation declaration
through `Constraint.validatedBy()` or the validation engine defaults) should
be included or not.

Parameters:
`includeExistingValidators` - Whether or not to use already-mapped validators when validating this constraint.
Returns:
This context for method chaining.

  - 

### validatedBy

ConstraintDefinitionContext<A> validatedBy(Class<? extends ConstraintValidator<A,?>> validator)
Adds a new validator to validate this constraint.

Parameters:
`validator` - The validator to add.
Returns:
This context for method chaining.

  - 

### validateType

@Incubating
<T>
ConstraintDefinitionContext.ConstraintValidatorDefinitionContext<A,T> validateType(Class<T> type)
Allows to configure a validation implementation using a Lambda expression or method reference. Useful for simple
validations without the need for accessing constraint properties or customization of error messages etc.

Parameters:
`type` - The type of the value to validate
Returns:
This context for method chaining

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved