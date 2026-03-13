# Package org.hibernate.validator.constraintvalidation

---

package org.hibernate.validator.constraintvalidation

Custom Hibernate Validator specific constraint validation extension classes.

This package is part of the public Hibernate Validator API.

- 

Related Packages

Package
Description
org.hibernate.validator

Bootstrap classes HibernateValidator and HibernateValidatorConfiguration which uniquely identify Hibernate Validator
and allow to configure it.

org.hibernate.validator.constraintvalidation.spi
 

- 

Interfaces

Class
Description
HibernateConstraintValidator<A extends Annotation, T>

Hibernate Validator specific extension to the `ConstraintValidator` contract.

HibernateConstraintValidatorContext

A custom `ConstraintValidatorContext` which allows to set additional message parameters for
interpolation.

HibernateConstraintValidatorInitializationContext

Provides contextual data and operations when initializing a constraint validator.

HibernateConstraintViolationBuilder
 
HibernateCrossParameterConstraintValidatorContext

A custom `ConstraintValidatorContext` which provides additional functionality for cross parameter validation contexts.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved