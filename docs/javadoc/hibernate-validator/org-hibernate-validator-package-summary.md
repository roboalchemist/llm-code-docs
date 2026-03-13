# Package org.hibernate.validator

---

package org.hibernate.validator

Bootstrap classes HibernateValidator and HibernateValidatorConfiguration which uniquely identify Hibernate Validator
and allow to configure it.

This package is part of the public Hibernate Validator API.

- 

Related Packages

Package
Description
org.hibernate.validator.cfg

Entry point for the programmatic constraint definition API.

org.hibernate.validator.constraints

Hibernate Validator specific constraints.

org.hibernate.validator.constraintvalidation

Custom Hibernate Validator specific constraint validation extension classes.

org.hibernate.validator.constraintvalidators
 
org.hibernate.validator.engine
 
org.hibernate.validator.group

This package provides support for dynamic default group sequence definition.

org.hibernate.validator.messageinterpolation

Implementations of the MessageInterpolator interface in particular ResourceBundleMessageInterpolator which can be
used by custom implementations of the interface for delegation.

org.hibernate.validator.metadata
 
org.hibernate.validator.parameternameprovider

Custom Hibernate Validator `jakarta.validation.ParameterNameProvider` implementations.

org.hibernate.validator.path

Hibernate Validator extensions around `jakarta.validation.Path`.

org.hibernate.validator.resourceloading

ResourceBundleLocator interface and its various implementations.

- 

Class
Description
BaseHibernateValidatorConfiguration<S extends BaseHibernateValidatorConfiguration<S>>

Base interface for Hibernate Validator specific configurations.

HibernateValidator

Default implementation of `ValidationProvider` within Hibernate Validator.

HibernateValidatorConfiguration

Uniquely identifies Hibernate Validator in the Bean Validation bootstrap
strategy.

HibernateValidatorContext

Represents a Hibernate Validator specific context that is used to create
`Validator` instances.

HibernateValidatorFactory

Provides Hibernate Validator extensions to `ValidatorFactory`.

HibernateValidatorPermission
Deprecated, for removal: This API element is subject to removal in a future version.
This permission will be removed in the future versions of Hibernate Validator as it does not rely on the `SecurityManager` anymore.

Incubating

Marks the annotated element as incubating.

PredefinedScopeHibernateValidator

Implementation of `ValidationProvider` limiting validation to a predefined scope.

PredefinedScopeHibernateValidatorConfiguration

Extension of `HibernateValidatorConfiguration` with additional methods dedicated to defining the predefined
scope of bean validation e.g. validated classes, constraint validators...

PredefinedScopeHibernateValidatorFactory

Provides Hibernate Validator extensions to `ValidatorFactory` in the context of a predefined scope.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved