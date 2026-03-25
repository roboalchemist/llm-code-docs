# Interface BaseHibernateValidatorConfiguration<S extends BaseHibernateValidatorConfiguration<S>>

Type Parameters:
`S` - The actual type of the configuration.

All Superinterfaces:
`Configuration<S>`

All Known Subinterfaces:
`HibernateValidatorConfiguration, PredefinedScopeHibernateValidatorConfiguration`

---

public interface BaseHibernateValidatorConfiguration<S extends BaseHibernateValidatorConfiguration<S>>
extends Configuration<S>
Base interface for Hibernate Validator specific configurations.

Should not be used directly, prefer `HibernateValidatorConfiguration` or
`PredefinedScopeHibernateValidatorConfiguration`.

Author:
Emmanuel Bernard, Gunnar Morling, Kevin Pollet <[email protected]> (C) 2011 SERLI, Hardy Ferentschik, Chris Beckey <[email protected]>

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`ALLOW_MULTIPLE_CASCADED_VALIDATION_ON_RESULT`

Property corresponding to the `allowMultipleCascadedValidationOnReturnValues(boolean)` method.

`static final String`
`ALLOW_PARALLEL_METHODS_DEFINE_PARAMETER_CONSTRAINTS`

Property corresponding to the `allowParallelMethodsDefineParameterConstraints(boolean)` method.

`static final String`
`ALLOW_PARAMETER_CONSTRAINT_OVERRIDE`

Property corresponding to the `allowOverridingMethodAlterParameterConstraint(boolean)` method.

`static final String`
`CONSTRAINT_EXPRESSION_LANGUAGE_FEATURE_LEVEL`

Property for configuring the Expression Language feature level for constraints, allowing to define which
Expression Language features are available for message interpolation.

`static final String`
`CONSTRAINT_MAPPING_CONTRIBUTORS`

Property for configuring constraint mapping contributors, allowing to set up one or more constraint mappings for
the default validator factory.

`static final String`
`CUSTOM_VIOLATION_EXPRESSION_LANGUAGE_FEATURE_LEVEL`

Property for configuring the Expression Language feature level for custom violations, allowing to define which
Expression Language features are available for message interpolation.

`static final String`
`ENABLE_TRAVERSABLE_RESOLVER_RESULT_CACHE`

Property corresponding to the `enableTraversableResolverResultCache(boolean)`.

`static final String`
`FAIL_FAST`

Property corresponding to the `failFast(boolean)` method.

`static final String`
`FAIL_FAST_ON_PROPERTY_VIOLATION`

Property corresponding to the `failFastOnPropertyViolation(boolean)` method.

`static final String`
`GETTER_PROPERTY_SELECTION_STRATEGY_CLASSNAME`

Property for configuring the getter property selection strategy, allowing to set which rules will be applied
to determine if a method is a valid JavaBean getter.

`static final String`
`LOCALE_RESOLVER_CLASSNAME`

Property for configuring the locale resolver, allowing to select an implementation of `LocaleResolver`
which will be used for locale resolution when interpolating a message.

`static final String`
`PROPERTY_NODE_NAME_PROVIDER_CLASSNAME`

Property for configuring the property node name provider, allowing to select an implementation of `PropertyNodeNameProvider`
which will be used for property name resolution when creating a property path.

`static final String`
`SCRIPT_EVALUATOR_FACTORY_CLASSNAME`

Property for configuring the script evaluator factory, allowing to set up which factory will be used to create
`ScriptEvaluator`s for evaluation of script expressions in
`ScriptAssert` and `ParameterScriptAssert`
constraints.

`static final String`
`SHOW_VALIDATED_VALUE_IN_TRACE_LOGS`

Property for trace level logs to include values under validation when constraint checks are executed.

`static final String`
`TEMPORAL_VALIDATION_TOLERANCE`

Property for configuring temporal validation tolerance, allowing to set the acceptable margin of error when
comparing date/time in temporal constraints.

- 

## Method Summary

Modifier and Type
Method
Description
`<T, V extends T>
S`
`addConstraintValidatorInitializationSharedData(Class<T> dataClass,
 V constraintValidatorInitializationSharedData)`

Allows adding a shared data object which will be available during the constraint validators initialization to all constraints.

`S`
`addConstraintValidatorInitializationSharedData(Object constraintValidatorInitializationSharedService)`

Allows adding a shared data object which will be available during the constraint validators initialization to all constraints.

`S`
`addMapping(ConstraintMapping mapping)`

Adds the specified `ConstraintMapping` instance to the configuration.

`S`
`allowMultipleCascadedValidationOnReturnValues(boolean allow)`

Define whether more than one constraint on a return value may be marked for cascading validation are allowed.

`S`
`allowOverridingMethodAlterParameterConstraint(boolean allow)`

Define whether overriding methods that override constraints should throw a `ConstraintDefinitionException`.

`S`
`allowParallelMethodsDefineParameterConstraints(boolean allow)`

Define whether parallel methods that define constraints should throw a `ConstraintDefinitionException`.

`S`
`beanMetaDataClassNormalizer(BeanMetaDataClassNormalizer beanMetaDataClassNormalizer)`
 
`S`
`constraintExpressionLanguageFeatureLevel(ExpressionLanguageFeatureLevel expressionLanguageFeatureLevel)`

Allows setting the Expression Language feature level for message interpolation of constraint messages.

`S`
`constraintValidatorPayload(Object constraintValidatorPayload)`

Allows to set a payload which will be passed to the constraint validators.

`ConstraintMapping`
`createConstraintMapping()`

Creates a new constraint mapping which can be used to programmatically configure the constraints for given types.

`S`
`customViolationExpressionLanguageFeatureLevel(ExpressionLanguageFeatureLevel expressionLanguageFeatureLevel)`

Allows setting the Expression Language feature level for message interpolation of custom violation messages.

`S`
`defaultLocale(Locale defaultLocale)`

Allows setting the default locale used to interpolate the constraint violation messages.

`S`
`enableTraversableResolverResultCache(boolean enabled)`

Define whether the per validation call caching of `TraversableResolver` results is enabled.

`S`
`externalClassLoader(ClassLoader externalClassLoader)`

Sets the class loader to be used for loading user-provided resources:

XML descriptors (`META-INF/validation.xml` as well as XML constraint mappings)
classes specified by name in XML descriptors (e.g. custom message interpolators etc.)
the `ValidationMessages` resource bundle

If no class loader is given, these resources will be obtained through the thread context class loader and as a
last fallback through Hibernate Validator's own class loader.

`S`
`failFast(boolean failFast)`

En- or disables the fail fast mode.

`S`
`failFastOnPropertyViolation(boolean failFastOnPropertyViolation)`

En- or disables the skipping of class level constraints based on validation of property level ones.

`ResourceBundleLocator`
`getDefaultResourceBundleLocator()`

Returns the `ResourceBundleLocator` used by the
`default message
interpolator` to load user-provided resource bundles.

`Set<ValueExtractor<?>>`
`getDefaultValueExtractors()`

Returns the default `ValueExtractor` implementations as per the
specification.

`S`
`getterPropertySelectionStrategy(GetterPropertySelectionStrategy getterPropertySelectionStrategy)`

Allows to set a getter property selection strategy defining the rules determining if a method is a getter
or not.

`S`
`localeResolver(LocaleResolver localeResolver)`

Allows setting a locale resolver, defining how the locale will be resolved when interpolating the message of a constraint violation.

`default S`
`locales(Locale... locales)`

Allows setting the list of the locales supported by this ValidatorFactory.

`S`
`locales(Set<Locale> locales)`

Allows setting the list of the locales supported by this ValidatorFactory.

`S`
`processedBeansTrackingVoter(ProcessedBeansTrackingVoter processedBeanTrackingVoter)`

Allows providing a custom bean tracking voter that helps to identify whether
the processed beans have to be tracked when cascaded into.

`S`
`propertyNodeNameProvider(PropertyNodeNameProvider propertyNodeNameProvider)`

Allows to set a property node name provider, defining how the name of a property node will be resolved
when constructing a property path as the one returned by `ConstraintViolation.getPropertyPath()`.

`S`
`scriptEvaluatorFactory(ScriptEvaluatorFactory scriptEvaluatorFactory)`

Allows to specify a custom `ScriptEvaluatorFactory` responsible for creating `ScriptEvaluator`s
used to evaluate script expressions for `ScriptAssert` and `ParameterScriptAssert` constraints.

`S`
`showValidatedValuesInTraceLogs(boolean enabled)`

Allows setting the logging configuration that would include validated values in trace level logs.

`S`
`temporalValidationTolerance(Duration temporalValidationTolerance)`

Allows to set the acceptable margin of error when comparing date/time in temporal constraints such as
`Past`/`PastOrPresent` and `Future`/`FutureOrPresent`.

### Methods inherited from interface Configuration

`addMapping, addProperty, addValueExtractor, buildValidatorFactory, clockProvider, constraintValidatorFactory, getBootstrapConfiguration, getDefaultClockProvider, getDefaultConstraintValidatorFactory, getDefaultMessageInterpolator, getDefaultParameterNameProvider, getDefaultTraversableResolver, ignoreXmlConfiguration, messageInterpolator, parameterNameProvider, traversableResolver`

- 

## Field Details

  - 

### FAIL_FAST

static final String FAIL_FAST
Property corresponding to the `failFast(boolean)` method.
Accepts `true` or `false`. Defaults to `false`.

See Also:

    - Constant Field Values

  - 

### ALLOW_PARAMETER_CONSTRAINT_OVERRIDE

static final String ALLOW_PARAMETER_CONSTRAINT_OVERRIDE
Property corresponding to the `allowOverridingMethodAlterParameterConstraint(boolean)` method.
Accepts `true` or `false`.
Defaults to `false`.

See Also:

    - Constant Field Values

  - 

### ALLOW_MULTIPLE_CASCADED_VALIDATION_ON_RESULT

static final String ALLOW_MULTIPLE_CASCADED_VALIDATION_ON_RESULT
Property corresponding to the `allowMultipleCascadedValidationOnReturnValues(boolean)` method.
Accepts `true` or `false`.
Defaults to `false`.

See Also:

    - Constant Field Values

  - 

### ALLOW_PARALLEL_METHODS_DEFINE_PARAMETER_CONSTRAINTS

static final String ALLOW_PARALLEL_METHODS_DEFINE_PARAMETER_CONSTRAINTS
Property corresponding to the `allowParallelMethodsDefineParameterConstraints(boolean)` method.
Accepts `true` or `false`.
Defaults to `false`.

See Also:

    - Constant Field Values

  - 

### CONSTRAINT_MAPPING_CONTRIBUTORS

static final String CONSTRAINT_MAPPING_CONTRIBUTORS
Property for configuring constraint mapping contributors, allowing to set up one or more constraint mappings for
the default validator factory. Accepts a String with the comma separated fully-qualified class names of one or more
`ConstraintMappingContributor` implementations.

Since:
5.3
See Also:

    - Constant Field Values

  - 

### ENABLE_TRAVERSABLE_RESOLVER_RESULT_CACHE

static final String ENABLE_TRAVERSABLE_RESOLVER_RESULT_CACHE
Property corresponding to the `enableTraversableResolverResultCache(boolean)`.
Accepts `true` or `false`.
Defaults to `true`.

Since:
6.0.3
See Also:

    - Constant Field Values

  - 

### SCRIPT_EVALUATOR_FACTORY_CLASSNAME

@Incubating
static final String SCRIPT_EVALUATOR_FACTORY_CLASSNAME
Property for configuring the script evaluator factory, allowing to set up which factory will be used to create
`ScriptEvaluator`s for evaluation of script expressions in
`ScriptAssert` and `ParameterScriptAssert`
constraints. A fully qualified name of a class implementing `ScriptEvaluatorFactory` is expected as a value.

Since:
6.0.3
See Also:

    - Constant Field Values

  - 

### TEMPORAL_VALIDATION_TOLERANCE

@Incubating
static final String TEMPORAL_VALIDATION_TOLERANCE
Property for configuring temporal validation tolerance, allowing to set the acceptable margin of error when
comparing date/time in temporal constraints. In milliseconds.

Since:
6.0.5
See Also:

    - Constant Field Values

  - 

### GETTER_PROPERTY_SELECTION_STRATEGY_CLASSNAME

@Incubating
static final String GETTER_PROPERTY_SELECTION_STRATEGY_CLASSNAME
Property for configuring the getter property selection strategy, allowing to set which rules will be applied
to determine if a method is a valid JavaBean getter.

Since:
6.1.0
See Also:

    - Constant Field Values

  - 

### PROPERTY_NODE_NAME_PROVIDER_CLASSNAME

@Incubating
static final String PROPERTY_NODE_NAME_PROVIDER_CLASSNAME
Property for configuring the property node name provider, allowing to select an implementation of `PropertyNodeNameProvider`
which will be used for property name resolution when creating a property path.

Since:
6.1.0
See Also:

    - Constant Field Values

  - 

### LOCALE_RESOLVER_CLASSNAME

@Incubating
static final String LOCALE_RESOLVER_CLASSNAME
Property for configuring the locale resolver, allowing to select an implementation of `LocaleResolver`
which will be used for locale resolution when interpolating a message.

Since:
6.1.1
See Also:

    - Constant Field Values

  - 

### CONSTRAINT_EXPRESSION_LANGUAGE_FEATURE_LEVEL

@Incubating
static final String CONSTRAINT_EXPRESSION_LANGUAGE_FEATURE_LEVEL
Property for configuring the Expression Language feature level for constraints, allowing to define which
Expression Language features are available for message interpolation.

This property only affects the EL feature level of "static" constraint violation messages. In particular, it
doesn't affect the default EL feature level for custom violations. Refer to
`CUSTOM_VIOLATION_EXPRESSION_LANGUAGE_FEATURE_LEVEL` to configure that.

Since:
6.2
See Also:

    - Constant Field Values

  - 

### CUSTOM_VIOLATION_EXPRESSION_LANGUAGE_FEATURE_LEVEL

@Incubating
static final String CUSTOM_VIOLATION_EXPRESSION_LANGUAGE_FEATURE_LEVEL
Property for configuring the Expression Language feature level for custom violations, allowing to define which
Expression Language features are available for message interpolation.

Since:
6.2
See Also:

    - Constant Field Values

  - 

### SHOW_VALIDATED_VALUE_IN_TRACE_LOGS

@Incubating
static final String SHOW_VALIDATED_VALUE_IN_TRACE_LOGS
Property for trace level logs to include values under validation when constraint checks are executed.

Since:
8.0
See Also:

    - Constant Field Values

  - 

### FAIL_FAST_ON_PROPERTY_VIOLATION

@Incubating
static final String FAIL_FAST_ON_PROPERTY_VIOLATION
Property corresponding to the `failFastOnPropertyViolation(boolean)` method.
Accepts `true` or `false`. Defaults to `false`.

Since:
9.0
See Also:

    - Constant Field Values

- 

## Method Details

  - 

### getDefaultResourceBundleLocator

ResourceBundleLocator getDefaultResourceBundleLocator()

Returns the `ResourceBundleLocator` used by the
`default message
interpolator` to load user-provided resource bundles. In conformance with
the specification this default locator retrieves the bundle
"ValidationMessages".

This locator can be used as delegate for custom locators when setting a
customized `ResourceBundleMessageInterpolator`:

```

	HibernateValidatorConfiguration configure =
   Validation.byProvider(HibernateValidator.class).configure();

 ResourceBundleLocator defaultResourceBundleLocator =
   configure.getDefaultBundleLocator();
 ResourceBundleLocator myResourceBundleLocator =
   new MyResourceBundleLocator(defaultResourceBundleLocator);

 configure.messageInterpolator(
   new ResourceBundleMessageInterpolator(myResourceBundleLocator));

```

Returns:
The default `ResourceBundleLocator`. Never null.

  - 

### createConstraintMapping

ConstraintMapping createConstraintMapping()
Creates a new constraint mapping which can be used to programmatically configure the constraints for given types. After
the mapping has been set up, it must be added to this configuration via `addMapping(ConstraintMapping)`.

Returns:
A new constraint mapping.

  - 

### getDefaultValueExtractors

@Incubating
Set<ValueExtractor<?>> getDefaultValueExtractors()
Returns the default `ValueExtractor` implementations as per the
specification.

Returns:
the default `ValueExtractor` implementations compliant
with the specification
Since:
6.0

  - 

### addMapping

S addMapping(ConstraintMapping mapping)
Adds the specified `ConstraintMapping` instance to the configuration. Constraints configured in `mapping`
will be added to the constraints configured via annotations and/or xml.

Parameters:
`mapping` - `ConstraintMapping` instance containing programmatic configured constraints
Returns:
`this` following the chaining method pattern
Throws:
`IllegalArgumentException` - if `mapping` is `null`

  - 

### failFast

S failFast(boolean failFast)
En- or disables the fail fast mode. When fail fast is enabled the validation
will stop on the first constraint violation detected.

Parameters:
`failFast` - `true` to enable fail fast, `false` otherwise.
Returns:
`this` following the chaining method pattern

  - 

### externalClassLoader

S externalClassLoader(ClassLoader externalClassLoader)
Sets the class loader to be used for loading user-provided resources:

    - XML descriptors (`META-INF/validation.xml` as well as XML constraint mappings)

    - classes specified by name in XML descriptors (e.g. custom message interpolators etc.)

    - the `ValidationMessages` resource bundle

If no class loader is given, these resources will be obtained through the thread context class loader and as a
last fallback through Hibernate Validator's own class loader.

Parameters:
`externalClassLoader` - The class loader for loading user-provided resources.
Returns:
`this` following the chaining method pattern
Since:
5.2

  - 

### allowOverridingMethodAlterParameterConstraint

S allowOverridingMethodAlterParameterConstraint(boolean allow)
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

S allowMultipleCascadedValidationOnReturnValues(boolean allow)
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

S allowParallelMethodsDefineParameterConstraints(boolean allow)
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

S enableTraversableResolverResultCache(boolean enabled)
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

### scriptEvaluatorFactory

@Incubating
S scriptEvaluatorFactory(ScriptEvaluatorFactory scriptEvaluatorFactory)
Allows to specify a custom `ScriptEvaluatorFactory` responsible for creating `ScriptEvaluator`s
used to evaluate script expressions for `ScriptAssert` and `ParameterScriptAssert` constraints.

Parameters:
`scriptEvaluatorFactory` - the `ScriptEvaluatorFactory` to be used
Returns:
`this` following the chaining method pattern
Since:
6.0.3

  - 

### temporalValidationTolerance

@Incubating
S temporalValidationTolerance(Duration temporalValidationTolerance)
Allows to set the acceptable margin of error when comparing date/time in temporal constraints such as
`Past`/`PastOrPresent` and `Future`/`FutureOrPresent`.

Parameters:
`temporalValidationTolerance` - the acceptable tolerance
Returns:
`this` following the chaining method pattern
Since:
6.0.5

  - 

### constraintValidatorPayload

@Incubating
S constraintValidatorPayload(Object constraintValidatorPayload)
Allows to set a payload which will be passed to the constraint validators. If the method is called multiple
times, only the payload passed last will be propagated.

Parameters:
`constraintValidatorPayload` - the payload passed to constraint validators
Returns:
`this` following the chaining method pattern
Since:
6.0.8

  - 

### addConstraintValidatorInitializationSharedData

@Incubating
S addConstraintValidatorInitializationSharedData(Object constraintValidatorInitializationSharedService)
Allows adding a shared data object which will be available during the constraint validators initialization to all constraints.
If the method is called multiple times passing different instances of the same class,
only the instance passed last will be available for that type.

Parameters:
`constraintValidatorInitializationSharedService` - the data to retrieve from the constraint validator initializers
Returns:
`this` following the chaining method pattern
Since:
9.1.0

  - 

### addConstraintValidatorInitializationSharedData

@Incubating
<T, V extends T> S addConstraintValidatorInitializationSharedData(Class<T> dataClass,
 V constraintValidatorInitializationSharedData)
Allows adding a shared data object which will be available during the constraint validators initialization to all constraints.
If the method is called multiple times passing the same `dataClass`,
only the instance passed last will be available for that type.

Parameters:
`constraintValidatorInitializationSharedData` - the data to retrieve from the constraint validator initializers
Returns:
`this` following the chaining method pattern
Since:
9.1.0

  - 

### getterPropertySelectionStrategy

@Incubating
S getterPropertySelectionStrategy(GetterPropertySelectionStrategy getterPropertySelectionStrategy)
Allows to set a getter property selection strategy defining the rules determining if a method is a getter
or not.

Parameters:
`getterPropertySelectionStrategy` - the `GetterPropertySelectionStrategy` to be used
Returns:
`this` following the chaining method pattern
Since:
6.1.0

  - 

### propertyNodeNameProvider

@Incubating
S propertyNodeNameProvider(PropertyNodeNameProvider propertyNodeNameProvider)
Allows to set a property node name provider, defining how the name of a property node will be resolved
when constructing a property path as the one returned by `ConstraintViolation.getPropertyPath()`.

Parameters:
`propertyNodeNameProvider` - the `PropertyNodeNameProvider` to be used
Returns:
`this` following the chaining method pattern
Since:
6.1.0

  - 

### locales

@Incubating
S locales(Set<Locale> locales)
Allows setting the list of the locales supported by this ValidatorFactory.

Can be used for advanced locale resolution and/or to force the initialization of the resource bundles at
bootstrap.

If not set, defaults to a singleton containing `Locale.getDefault()`.

Since:
6.1.1

  - 

### locales

@Incubating
default S locales(Locale... locales)
Allows setting the list of the locales supported by this ValidatorFactory.

Can be used for advanced locale resolution and/or to force the initialization of the resource bundles at
bootstrap.

If not set, defaults to a singleton containing `Locale.getDefault()`.

Since:
6.1.1

  - 

### defaultLocale

@Incubating
S defaultLocale(Locale defaultLocale)
Allows setting the default locale used to interpolate the constraint violation messages.

If not set, defaults to the system locale obtained via `Locale.getDefault()`.

Since:
6.1.1

  - 

### localeResolver

@Incubating
S localeResolver(LocaleResolver localeResolver)
Allows setting a locale resolver, defining how the locale will be resolved when interpolating the message of a constraint violation.

Parameters:
`localeResolver` - the `LocaleResolver` to be used
Returns:
`this` following the chaining method pattern
Since:
6.1.1

  - 

### beanMetaDataClassNormalizer

@Incubating
S beanMetaDataClassNormalizer(BeanMetaDataClassNormalizer beanMetaDataClassNormalizer)

  - 

### constraintExpressionLanguageFeatureLevel

@Incubating
S constraintExpressionLanguageFeatureLevel(ExpressionLanguageFeatureLevel expressionLanguageFeatureLevel)
Allows setting the Expression Language feature level for message interpolation of constraint messages.

This is the feature level used for messages hardcoded inside the constraint declaration.

If you are creating custom constraint violations, Expression Language support needs to be explicitly enabled and
use the safest feature level by default if enabled.

Parameters:
`expressionLanguageFeatureLevel` - the `ExpressionLanguageFeatureLevel` to be used
Returns:
`this` following the chaining method pattern
Since:
6.2

  - 

### customViolationExpressionLanguageFeatureLevel

@Incubating
S customViolationExpressionLanguageFeatureLevel(ExpressionLanguageFeatureLevel expressionLanguageFeatureLevel)
Allows setting the Expression Language feature level for message interpolation of custom violation messages.

This is the feature level used for messages of custom violations created by the `ConstraintValidatorContext`.

Parameters:
`expressionLanguageFeatureLevel` - the `ExpressionLanguageFeatureLevel` to be used
Returns:
`this` following the chaining method pattern
Since:
6.2

  - 

### showValidatedValuesInTraceLogs

@Incubating
S showValidatedValuesInTraceLogs(boolean enabled)
Allows setting the logging configuration that would include validated values in trace level logs.

By default, values will not be printed to the logs as they might contain sensitive data.

Parameters:
`enabled` - flag determining whether validated values will be printed out into trace level logs or not.
Returns:
`this` following the chaining method pattern
Since:
8.0

  - 

### failFastOnPropertyViolation

@Incubating
S failFastOnPropertyViolation(boolean failFastOnPropertyViolation)
En- or disables the skipping of class level constraints based on validation of property level ones. When this
mode is enabled the validation of class level constraints will not be performed if any of the property level
constraints generated a violation.

Parameters:
`failFastOnPropertyViolation` - `true` to enable the skipping mode, `false` otherwise.
Returns:
`this` following the chaining method pattern
Since:
9.0

  - 

### processedBeansTrackingVoter

@Incubating
S processedBeansTrackingVoter(ProcessedBeansTrackingVoter processedBeanTrackingVoter)
Allows providing a custom bean tracking voter that helps to identify whether
the processed beans have to be tracked when cascaded into.

Parameters:
`processedBeanTrackingVoter` - the `bean tracking voter` to apply.
Returns:
`this` following the chaining method pattern
Since:
9.1

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved