# Interface HibernateValidatorFactory

All Superinterfaces:
`AutoCloseable, ValidatorFactory`

All Known Subinterfaces:
`PredefinedScopeHibernateValidatorFactory`

---

public interface HibernateValidatorFactory
extends ValidatorFactory
Provides Hibernate Validator extensions to `ValidatorFactory`.

Author:
Emmanuel Bernard, Kevin Pollet <[email protected]> (C) 2011 SERLI

- 

## Method Summary

Modifier and Type
Method
Description
`GetterPropertySelectionStrategy`
`getGetterPropertySelectionStrategy()`

Returns the getter property selection strategy defining the rules determining if a method is a getter or not.

`PropertyNodeNameProvider`
`getPropertyNodeNameProvider()`

Returns the property node name provider used to resolve the name of a property node when creating the property path.

`ScriptEvaluatorFactory`
`getScriptEvaluatorFactory()`

Returns the factory responsible for creating `ScriptEvaluator`s used to
evaluate script expressions of `ScriptAssert` and `ParameterScriptAssert`
constraints.

`Duration`
`getTemporalValidationTolerance()`

Returns the temporal validation tolerance i.e. the acceptable margin of error when comparing date/time in
temporal constraints.

`HibernateValidatorContext`
`usingContext()`

Returns a context for validator configuration via options from the
Bean Validation API as well as specific ones from Hibernate Validator.

### Methods inherited from interface ValidatorFactory

`close, getClockProvider, getConstraintValidatorFactory, getMessageInterpolator, getParameterNameProvider, getTraversableResolver, getValidator, unwrap`

- 

## Method Details

  - 

### getScriptEvaluatorFactory

@Incubating
ScriptEvaluatorFactory getScriptEvaluatorFactory()
Returns the factory responsible for creating `ScriptEvaluator`s used to
evaluate script expressions of `ScriptAssert` and `ParameterScriptAssert`
constraints.

Returns:
a `ScriptEvaluatorFactory` instance
Since:
6.0.3

  - 

### getTemporalValidationTolerance

@Incubating
Duration getTemporalValidationTolerance()
Returns the temporal validation tolerance i.e. the acceptable margin of error when comparing date/time in
temporal constraints.

Returns:
the tolerance
Since:
6.0.5

  - 

### getGetterPropertySelectionStrategy

@Incubating
GetterPropertySelectionStrategy getGetterPropertySelectionStrategy()
Returns the getter property selection strategy defining the rules determining if a method is a getter or not.

Returns:
the getter property selection strategy of the current `ValidatorFactory`
Since:
6.1.0

  - 

### getPropertyNodeNameProvider

@Incubating
PropertyNodeNameProvider getPropertyNodeNameProvider()
Returns the property node name provider used to resolve the name of a property node when creating the property path.

Returns:
the property node name provider of the current `ValidatorFactory`
Since:
6.2.1

  - 

### usingContext

HibernateValidatorContext usingContext()
Returns a context for validator configuration via options from the
Bean Validation API as well as specific ones from Hibernate Validator.

Specified by:
`usingContext` in interface `ValidatorFactory`
Returns:
A context for validator configuration.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved