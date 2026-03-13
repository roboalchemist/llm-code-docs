# Class HibernateValidator

java.lang.Object
org.hibernate.validator.HibernateValidator

All Implemented Interfaces:
`ValidationProvider<HibernateValidatorConfiguration>`

---

public class HibernateValidator
extends Object
implements ValidationProvider<HibernateValidatorConfiguration>
Default implementation of `ValidationProvider` within Hibernate Validator.

Author:
Emmanuel Bernard, Hardy Ferentschik

- 

## Constructor Summary

Constructors

Constructor
Description
`HibernateValidator()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`ValidatorFactory`
`buildValidatorFactory(ConfigurationState configurationState)`
 
`Configuration<?>`
`createGenericConfiguration(BootstrapState state)`
 
`HibernateValidatorConfiguration`
`createSpecializedConfiguration(BootstrapState state)`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### HibernateValidator

public HibernateValidator()

- 

## Method Details

  - 

### createSpecializedConfiguration

public HibernateValidatorConfiguration createSpecializedConfiguration(BootstrapState state)

Specified by:
`createSpecializedConfiguration` in interface `ValidationProvider<HibernateValidatorConfiguration>`

  - 

### createGenericConfiguration

public Configuration<?> createGenericConfiguration(BootstrapState state)

Specified by:
`createGenericConfiguration` in interface `ValidationProvider<HibernateValidatorConfiguration>`

  - 

### buildValidatorFactory

public ValidatorFactory buildValidatorFactory(ConfigurationState configurationState)

Specified by:
`buildValidatorFactory` in interface `ValidationProvider<HibernateValidatorConfiguration>`

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved