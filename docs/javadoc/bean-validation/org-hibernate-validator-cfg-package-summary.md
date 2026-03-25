# Package org.hibernate.validator.cfg

---

package org.hibernate.validator.cfg

Entry point for the programmatic constraint definition API.

This package is part of the public Hibernate Validator API.

- 

Related Packages

Package
Description
org.hibernate.validator

Bootstrap classes HibernateValidator and HibernateValidatorConfiguration which uniquely identify Hibernate Validator
and allow to configure it.

org.hibernate.validator.cfg.context

Contains facet and creational context interfaces forming the API for programmatic constraint definition.

org.hibernate.validator.cfg.defs

Constraint definition classes for programmatic constraint definition API.

- 

Class
Description
AnnotationDef<C extends AnnotationDef<C,A>, A extends Annotation>

Base class for all annotation definition types.

ConstraintDef<C extends ConstraintDef<C,A>, A extends Annotation>

Base class for all constraint definition types.

ConstraintMapping

Represents a constraint mapping configured via the programmatic API.

GenericConstraintDef<A extends Annotation>

A `ConstraintDef` class which can be used to configure any constraint
type.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved