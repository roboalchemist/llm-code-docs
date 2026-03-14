# Interface PredefinedScopeHibernateValidatorConfiguration

All Superinterfaces:
`BaseHibernateValidatorConfiguration<PredefinedScopeHibernateValidatorConfiguration>, Configuration<PredefinedScopeHibernateValidatorConfiguration>`

---

@Incubating
public interface PredefinedScopeHibernateValidatorConfiguration
extends BaseHibernateValidatorConfiguration<PredefinedScopeHibernateValidatorConfiguration>
Extension of `HibernateValidatorConfiguration` with additional methods dedicated to defining the predefined
scope of bean validation e.g. validated classes, constraint validators...

Since:
6.1
Author:
Guillaume Smet

- 

## Field Summary

### Fields inherited from interface BaseHibernateValidatorConfiguration

`ALLOW_MULTIPLE_CASCADED_VALIDATION_ON_RESULT, ALLOW_PARALLEL_METHODS_DEFINE_PARAMETER_CONSTRAINTS, ALLOW_PARAMETER_CONSTRAINT_OVERRIDE, CONSTRAINT_EXPRESSION_LANGUAGE_FEATURE_LEVEL, CONSTRAINT_MAPPING_CONTRIBUTORS, CUSTOM_VIOLATION_EXPRESSION_LANGUAGE_FEATURE_LEVEL, ENABLE_TRAVERSABLE_RESOLVER_RESULT_CACHE, FAIL_FAST, FAIL_FAST_ON_PROPERTY_VIOLATION, GETTER_PROPERTY_SELECTION_STRATEGY_CLASSNAME, LOCALE_RESOLVER_CLASSNAME, PROPERTY_NODE_NAME_PROVIDER_CLASSNAME, SCRIPT_EVALUATOR_FACTORY_CLASSNAME, SHOW_VALIDATED_VALUE_IN_TRACE_LOGS, TEMPORAL_VALIDATION_TOLERANCE`

- 

## Method Summary

Modifier and Type
Method
Description
`PredefinedScopeHibernateValidatorConfiguration`
`builtinConstraints(Set<String> constraints)`
 
`PredefinedScopeHibernateValidatorConfiguration`
`includeBeansAndConstraintsDefinedOnlyInXml(boolean include)`

Specify whether to append the `built-in constraints` and `beans to initialize`
with constraints and beans provided only through XML mapping.

`PredefinedScopeHibernateValidatorConfiguration`
`initializeBeanMetaData(Set<Class<?>> beanClassesToInitialize)`
 

### Methods inherited from interface BaseHibernateValidatorConfiguration

`addConstraintValidatorInitializationSharedData, addConstraintValidatorInitializationSharedData, addMapping, allowMultipleCascadedValidationOnReturnValues, allowOverridingMethodAlterParameterConstraint, allowParallelMethodsDefineParameterConstraints, beanMetaDataClassNormalizer, constraintExpressionLanguageFeatureLevel, constraintValidatorPayload, createConstraintMapping, customViolationExpressionLanguageFeatureLevel, defaultLocale, enableTraversableResolverResultCache, externalClassLoader, failFast, failFastOnPropertyViolation, getDefaultResourceBundleLocator, getDefaultValueExtractors, getterPropertySelectionStrategy, localeResolver, locales, locales, processedBeansTrackingVoter, propertyNodeNameProvider, scriptEvaluatorFactory, showValidatedValuesInTraceLogs, temporalValidationTolerance`

### Methods inherited from interface Configuration

`addMapping, addProperty, addValueExtractor, buildValidatorFactory, clockProvider, constraintValidatorFactory, getBootstrapConfiguration, getDefaultClockProvider, getDefaultConstraintValidatorFactory, getDefaultMessageInterpolator, getDefaultParameterNameProvider, getDefaultTraversableResolver, ignoreXmlConfiguration, messageInterpolator, parameterNameProvider, traversableResolver`

- 

## Method Details

  - 

### builtinConstraints

@Incubating
PredefinedScopeHibernateValidatorConfiguration builtinConstraints(Set<String> constraints)

  - 

### initializeBeanMetaData

@Incubating
PredefinedScopeHibernateValidatorConfiguration initializeBeanMetaData(Set<Class<?>> beanClassesToInitialize)

  - 

### includeBeansAndConstraintsDefinedOnlyInXml

@Incubating
PredefinedScopeHibernateValidatorConfiguration includeBeansAndConstraintsDefinedOnlyInXml(boolean include)
Specify whether to append the `built-in constraints` and `beans to initialize`
with constraints and beans provided only through XML mapping.

This option is enabled by default.

Parameters:
`include` - Whether to include the beans defined only in xml as part of the `set of beans to initialize`
and also add built-in constraints used only in xml definitions as part of the `set of built-in constraints`.
Returns:
`this` for chaining configuration method calls.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved