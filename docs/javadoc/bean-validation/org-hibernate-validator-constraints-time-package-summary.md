# Package org.hibernate.validator.constraints.time

---

package org.hibernate.validator.constraints.time

Hibernate Validator `Duration` constraints.

This package is part of the public Hibernate Validator API.

- 

Related Packages

Package
Description
org.hibernate.validator.constraints

Hibernate Validator specific constraints.

org.hibernate.validator.constraints.br

Hibernate Validator Brazilian constraints.

org.hibernate.validator.constraints.kor

Hibernate Validator Korean constraints.

org.hibernate.validator.constraints.pl

Hibernate Validator Polish constraints.

org.hibernate.validator.constraints.ru

Hibernate Validator Russian constraints.

- 

Annotation Interfaces

Class
Description
DurationMax

The annotated `Duration` element must be shorter than or equal to the one constructed as a sum of
`DurationMax.nanos()`, `DurationMax.millis()`, `DurationMax.seconds()`,
`DurationMax.minutes()`, `DurationMax.hours()`, `DurationMax.days()`.

DurationMax.List

Defines several `@DurationMax` annotations on the same element.

DurationMin

The annotated `Duration` element must be longer than or equal to the one constructed as a sum of
`DurationMin.nanos()`, `DurationMin.millis()`, `DurationMin.seconds()`,
`DurationMin.minutes()`, `DurationMin.hours()`, `DurationMin.days()`.

DurationMin.List

Defines several `@DurationMin` annotations on the same element.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved