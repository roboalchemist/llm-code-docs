# Interface HibernateValidatorContext

All Superinterfaces:
`ValidatorContext`

---

public interface HibernateValidatorContext
extends ValidatorContext
Represents a Hibernate Validator specific context that is used to create
`Validator` instances. Adds additional configuration options to those
provided by `ValidatorContext`.

Author:
Emmanuel Bernard, Kevin Pollet <[email protected]> (C) 2011 SERLI, Gunnar Morling, Chris Beckey <[email protected]>

- 

## Method Summary

Modifier and Type
Method
Description
`HibernateValidatorContext`
`addValueExtractor(ValueExtractor<?> extractor)`
 
`HibernateValidatorContext`
`allowMultipleCascadedValidationOnReturnValues(boolean allow)`

Define whether more than one constraint on a return value may be marked for cascading validation are allowed.

`HibernateValidatorContext`
`allowOverridingMethodAlterParameterConstraint(boolean allow)`

Define whether overriding methods that override constraints should throw a `ConstraintDefinitionException`.

`HibernateValidatorContext`
`allowParallelMethodsDefineParameterConstraints(boolean allow)`

Define whether parallel methods that define constraints should throw a `ConstraintDefinitionException`.

`HibernateValidatorContext`
`clockProvider(ClockProvider clockProvider)`
 
`HibernateValidatorContext`
`constraintValidatorFactory(ConstraintValidatorFactory factory)`
 
`HibernateValidatorContext`
`constraintValidatorPayload(Object constraintValidatorPayload)`

Define a payload passed to the constraint validators.

`HibernateValidatorContext`
`enableTraversableResolverResultCache(boolean enabled)`

Define whether the per validation call caching of `TraversableResolver` results is enabled.

`HibernateValidatorContext`
`failFast(boolean failFast)`

En- or disables the fail fast mode.

`HibernateValidatorContext`
`failFastOnPropertyViolation(boolean failFastOnPropertyViolation)`

En- or disables the skipping of class level constraints based on validation of property level ones.

`HibernateValidatorContext`
`messageInterpolator(MessageInterpolator messageInterpolator)`
 
`HibernateValidatorContext`
`parameterNameProvider(ParameterNameProvider parameterNameProvider)`
 
`HibernateValidatorContext`
`showValidatedValuesInTraceLogs(boolean enabled)`

Define whether values that are currently being validated should be part of the logging at trace level, or not.

`HibernateValidatorContext`
`temporalValidationTolerance(Duration temporalValidationTolerance)`

Define the temporal validation tolerance i.e. the acceptable margin of error
when comparing date/time in temporal constraints.

`HibernateValidatorContext`
`traversableResolver(TraversableResolver traversableResolver)`
 

### Methods inherited from interface ValidatorContext

`getValidator`

- 

## Method Details

  - 

### messageInterpolator

HibernateValidatorContext messageInterpolator(MessageInterpolator messageInterpolator)

Specified by:
`messageInterpolator` in interface `ValidatorContext`

  - 

### traversableResolver

HibernateValidatorContext traversableResolver(TraversableResolver traversableResolver)

Specified by:
`traversableResolver` in interface `ValidatorContext`

  - 

### constraintValidatorFactory

HibernateValidatorContext constraintValidatorFactory(ConstraintValidatorFactory factory)

Specified by:
`constraintValidatorFactory` in interface `ValidatorContext`

  - 

### parameterNameProvider

HibernateValidatorContext parameterNameProvider(ParameterNameProvider parameterNameProvider)

Specified by:
`parameterNameProvider` in interface `ValidatorContext`
Since:
5.2

  - 

### clockProvider

HibernateValidatorContext clockProvider(ClockProvider clockProvider)

Specified by:
`clockProvider` in interface `ValidatorContext`
Since:
6.0

  - 

### addValueExtractor

HibernateValidatorContext addValueExtractor(ValueExtractor<?> extractor)

Specified by:
`addValueExtractor` in interface `ValidatorContext`
Since:
6.0

  - 

### failFast

HibernateValidatorContext failFast(boolean failFast)
En- or disables the fail fast mode. When fail fast is enabled the validation
will stop on the first constraint violation detected.

Parameters:
`failFast` - `true` to enable fail fast, `false` otherwise.
Returns:
`this` following the chaining method pattern

  - 

### allowOverridingMethodAlterParameterConstraint

HibernateValidatorContext allowOverridingMethodAlterParameterConstraint(boolean allow)
Define whether overriding methods that override constraints should throw a `ConstraintDefinitionException`.
The default value is `false`, i.e. do not allow.

See Section 4.5.5 of the JSR 380 specification, specifically

```

"In sub types (be it sub classes/interfaces or interface implementations), no parameter constraints may
be declared on overridden or implemented methods, nor may parameters be marked for cascaded validation.
This would pose a strengthening of preconditions to be fulfilled by the caller."

```

Parameters:
`allow` - flag determining whether validation will allow overriding to alter parameter constraints.
Returns:
`this` following the chaining method pattern
Since:
5.3

  - 

### allowMultipleCascadedValidationOnReturnValues

HibernateValidatorContext allowMultipleCascadedValidationOnReturnValues(boolean allow)
Define whether more than one constraint on a return value may be marked for cascading validation are allowed.
The default value is `false`, i.e. do not allow.

See Section 4.5.5 of the JSR 380 specification, specifically

```

"One must not mark a method return value for cascaded validation more than once in a line of a class hierarchy.
In other words, overriding methods on sub types (be it sub classes/interfaces or interface implementations)
cannot mark the return value for cascaded validation if the return value has already been marked on the
overridden method of the super type or interface."

```

Parameters:
`allow` - flag determining whether validation will allow multiple cascaded validation on return values.
Returns:
`this` following the chaining method pattern
Since:
5.3

  - 

### allowParallelMethodsDefineParameterConstraints

HibernateValidatorContext allowParallelMethodsDefineParameterConstraints(boolean allow)
Define whether parallel methods that define constraints should throw a `ConstraintDefinitionException`. The
default value is `false`, i.e. do not allow.

See Section 4.5.5 of the JSR 380 specification, specifically

```

"If a sub type overrides/implements a method originally defined in several parallel types of the hierarchy
(e.g. two interfaces not extending each other, or a class and an interface not implemented by said class),
no parameter constraints may be declared for that method at all nor parameters be marked for cascaded validation.
This again is to avoid an unexpected strengthening of preconditions to be fulfilled by the caller."

```

Parameters:
`allow` - flag determining whether validation will allow parameter constraints in parallel hierarchies
Returns:
`this` following the chaining method pattern
Since:
5.3

  - 

### enableTraversableResolverResultCache

HibernateValidatorContext enableTraversableResolverResultCache(boolean enabled)
Define whether the per validation call caching of `TraversableResolver` results is enabled. The default
value is `true`, i.e. the caching is enabled.

This behavior was initially introduced to cache the `JPATraversableResolver` results but the map lookups it
introduces can be counterproductive when the `TraversableResolver` calls are very fast.

Parameters:
`enabled` - flag determining whether per validation call caching is enabled for `TraversableResolver`
results.
Returns:
`this` following the chaining method pattern
Since:
6.0.3

  - 

### temporalValidationTolerance

@Incubating
HibernateValidatorContext temporalValidationTolerance(Duration temporalValidationTolerance)
Define the temporal validation tolerance i.e. the acceptable margin of error
when comparing date/time in temporal constraints.

Parameters:
`temporalValidationTolerance` - the tolerance
Returns:
`this` following the chaining method pattern
Since:
6.0.5

  - 

### constraintValidatorPayload

@Incubating
HibernateValidatorContext constraintValidatorPayload(Object constraintValidatorPayload)
Define a payload passed to the constraint validators. If the method is called multiple times, only the payload
passed last will be propagated.

Parameters:
`constraintValidatorPayload` - the payload passed to constraint validators
Returns:
`this` following the chaining method pattern
Since:
6.0.8

  - 

### showValidatedValuesInTraceLogs

@Incubating
HibernateValidatorContext showValidatedValuesInTraceLogs(boolean enabled)
Define whether values that are currently being validated should be part of the logging at trace level, or not.

Parameters:
`enabled` - `true` to show the values at trace level, `false` otherwise.
Returns:
`this` following the chaining method pattern
Since:
8.0

  - 

### failFastOnPropertyViolation

@Incubating
HibernateValidatorContext failFastOnPropertyViolation(boolean failFastOnPropertyViolation)
En- or disables the skipping of class level constraints based on validation of property level ones. When this
mode is enabled the validation of class level constraints will not be performed if any of the property level
constraints generated a violation.

Parameters:
`failFastOnPropertyViolation` - `true` to enable the skipping mode, `false` otherwise.
Returns:
`this` following the chaining method pattern
Since:
9.0

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved