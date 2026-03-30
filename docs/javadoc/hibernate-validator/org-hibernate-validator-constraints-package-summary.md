# Package org.hibernate.validator.constraints

---

package org.hibernate.validator.constraints

Hibernate Validator specific constraints.

This package is part of the public Hibernate Validator API.

- 

Related Packages

Package
Description
org.hibernate.validator

Bootstrap classes HibernateValidator and HibernateValidatorConfiguration which uniquely identify Hibernate Validator
and allow to configure it.

org.hibernate.validator.constraints.br

Hibernate Validator Brazilian constraints.

org.hibernate.validator.constraints.kor

Hibernate Validator Korean constraints.

org.hibernate.validator.constraints.pl

Hibernate Validator Polish constraints.

org.hibernate.validator.constraints.ru

Hibernate Validator Russian constraints.

org.hibernate.validator.constraints.time

Hibernate Validator `Duration` constraints.

- 

Class
Description
BitcoinAddress

The string has to be a well-formed BTC (Bitcoin) Mainnet address.

BitcoinAddress.BitcoinAddressType
 
CodePointLength

Validate that the code point length of a character sequence is between min and max included.

CodePointLength.List

Defines several `@CodePointLength` annotations on the same element.

CodePointLength.NormalizationStrategy

Strategy for normalization.

CompositionType

The Enum `CompositionType` which is used as argument to the annotation `ConstraintComposition`.

ConstraintComposition

Boolean operator that is applied to all constraints of a composing constraint annotation.

CreditCardNumber

The annotated element has to represent a valid
credit card number.

CreditCardNumber.List

Defines several `@CreditCardNumber` annotations on the same element.

Currency

The `MonetaryAmount` has to be in the right `CurrencyUnit`.

Currency.List

Defines several `@Currency` annotations on the same element.

EAN

Checks that the annotated character sequence is a valid
EAN 13 number.

EAN.List

Defines several `@EAN` annotations on the same element.

EAN.Type
 
IpAddress

Checks that the annotated character sequence is a valid
IP address.

IpAddress.Type

Defines the IP address version.

ISBN

Checks that the annotated character sequence is a valid
ISBN.

ISBN.List

Defines several `@ISBN` annotations on the same element.

ISBN.Type

Defines the ISBN length.

Length

Validate that the string is between min and max included.

Length.List

Defines several `@Length` annotations on the same element.

LuhnCheck

Luhn algorithm check constraint.

LuhnCheck.List

Defines several `@LuhnCheck` annotations on the same element.

Mod10Check

@Modulo 10 check constraint.

Mod10Check.List

Defines several `@Mod10Check` annotations on the same element.

Mod11Check

Modulo 11 check constraint.

Mod11Check.List

Defines several `@Mod11Check` annotations on the same element.

Mod11Check.ProcessingDirection
 
Normalized

Validate that a character sequence is of normalization form.

Normalized.List

Defines several `@Normalized` annotations on the same element.

ParameterScriptAssert

A method-level constraint, that evaluates a script expression against the
annotated method or constructor.

ParameterScriptAssert.List

Defines several `ParameterScriptAssert` annotations on the same executable.

Range

The annotated element has to be in the appropriate range.

Range.List

Defines several `@Range` annotations on the same element.

ScriptAssert

A class-level constraint, that evaluates a script expression against the
annotated element.

ScriptAssert.List

Defines several `@ScriptAssert` annotations on the same element.

UniqueElements

Validates that every object in the provided `Collection` is unique, i.e. that we can't find 2 equal elements in
the collection.

UniqueElements.List

Defines several `@UniqueElements` annotations on the same element.

URL

Validates the annotated string is an URL.

URL.List

Defines several `@URL` annotations on the same element.

UUID

Checks that the annotated character sequence is a valid
UUID.

UUID.LetterCase

Required letter case for hex characters

UUID.List

Defines several `@UUID` annotations on the same element.

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved