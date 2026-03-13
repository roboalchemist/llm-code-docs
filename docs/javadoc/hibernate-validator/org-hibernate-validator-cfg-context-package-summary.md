# Package org.hibernate.validator.cfg.context

---

package org.hibernate.validator.cfg.context

Contains facet and creational context interfaces forming the API for programmatic constraint definition.

This package is part of the public Hibernate Validator API.

- 

Related Packages

Package
Description
org.hibernate.validator.cfg

Entry point for the programmatic constraint definition API.

org.hibernate.validator.cfg.defs

Constraint definition classes for programmatic constraint definition API.

- 

Interfaces

Class
Description
AnnotationIgnoreOptions<C extends AnnotationIgnoreOptions<C>>

Facet of a constraint mapping creational context which allows to configure how existing annotation should be treated.

Cascadable<C extends Cascadable<C>>

Facet of a constraint mapping creational context which allows to mark the underlying
element as to be validated in a cascaded way.

Constrainable<C extends Constrainable<C>>

Facet of a constraint mapping creational context which allows to place
constraints on the underlying element.

ConstraintDefinitionContext<A extends Annotation>

Constraint mapping creational context representing a constraint (i.e. annotation type).

ConstraintDefinitionContext.ConstraintValidatorDefinitionContext<A extends Annotation, T>

Allows to specify a validation implementation for the given constraint and data type using a Lambda expression or
method reference.

ConstraintDefinitionContext.ValidationCallable<T>

Callable implementing a validation routine.

ConstraintDefinitionTarget

Facet of a constraint definition creational context which allows to select the constraint (annotation type) to
which the next operations shall apply.

ConstraintMappingTarget

Facet of a constraint mapping creational context which allows to start a new constraint mapping or definition.

ConstructorConstraintMappingContext

Constraint mapping creational context representing a constructor.

ConstructorTarget

Facet of a constraint mapping creational context which allows to select the bean
constructor to which the next operations shall apply.

ContainerElementConstraintMappingContext

Constraint mapping creational context representing a type argument of a property, parameter or method return value
with a generic (return) type.

ContainerElementTarget

Facet of a constraint mapping creational context which allows to select a type argument or the component type of the
(return) type of the current property, parameter or method as target for the next operations.

CrossParameterConstraintMappingContext

Constraint mapping creational context allowing to add cross-parameter constraints to a method or constructor and to
navigate to other constraint targets.

CrossParameterTarget

Facet of a constraint mapping creational context which allows to select the cross-parameter element of a method
or constructor as target of the next operations.

GroupConversionTargetContext<C>

Creational context which allows to set the target group of a group conversion configured via
`Cascadable.convertGroup(Class)`.

MethodConstraintMappingContext

Constraint mapping creational context representing a method.

MethodTarget

Facet of a constraint mapping creational context which allows to select the bean
method to which the next operations shall apply.

ParameterConstraintMappingContext

Constraint mapping creational context representing a method parameter.

ParameterTarget

Facet of a constraint mapping creational context which allows to select a method or constructor parameter to
which the next operations shall apply.

PropertyConstraintMappingContext

Constraint mapping creational context representing a property of a bean.

PropertyTarget

Facet of a constraint mapping creational context which allows to select the bean
property to which the next operations shall apply.

ReturnValueConstraintMappingContext

Constraint mapping creational context representing a method return value.

ReturnValueTarget

Facet of a constraint mapping creational context which allows to select the current method's or constructor's
return value as target for the next operations.

TypeConstraintMappingContext<C>

Constraint mapping creational context representing a type.

TypeTarget

Facet of a constraint mapping creational context which allows to select the bean
type to which the next operations shall apply.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved