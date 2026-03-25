# Package org.hibernate.validator.messageinterpolation

---

package org.hibernate.validator.messageinterpolation

Implementations of the MessageInterpolator interface in particular ResourceBundleMessageInterpolator which can be
used by custom implementations of the interface for delegation.

This package is part of the public Hibernate Validator API.

- 

Related Packages

Package
Description
org.hibernate.validator

Bootstrap classes HibernateValidator and HibernateValidatorConfiguration which uniquely identify Hibernate Validator
and allow to configure it.

- 

Class
Description
AbstractMessageInterpolator

Resource bundle backed message interpolator.

ExpressionLanguageFeatureLevel

Indicates the level of features enabled for the Expression Language engine.

HibernateMessageInterpolatorContext

Extension to `MessageInterpolator.Context` which provides functionality
specific to Hibernate Validator.

ParameterMessageInterpolator

Resource bundle message interpolator, it does not support EL expression
and does support parameter value expression

ResourceBundleMessageInterpolator

Resource bundle backed message interpolator.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved