# Class PredefinedScopeHibernateValidator

java.lang.Object
org.hibernate.validator.PredefinedScopeHibernateValidator

All Implemented Interfaces:
`ValidationProvider<PredefinedScopeHibernateValidatorConfiguration>`

---

@Incubating
public class PredefinedScopeHibernateValidator
extends Object
implements ValidationProvider<PredefinedScopeHibernateValidatorConfiguration>
Implementation of `ValidationProvider` limiting validation to a predefined scope.

It allows to collect all the necessary metadata at bootstrap.

Since:
6.1
Author:
Guillaume Smet

- 

## Constructor Summary

Constructors

Constructor
Description
`PredefinedScopeHibernateValidator()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`ValidatorFactory`
`buildValidatorFactory(ConfigurationState configurationState)`
 
`Configuration<?>`
`createGenericConfiguration(BootstrapState state)`
 
`PredefinedScopeHibernateValidatorConfiguration`
`createSpecializedConfiguration(BootstrapState state)`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### PredefinedScopeHibernateValidator

public PredefinedScopeHibernateValidator()

- 

## Method Details

  - 

### createSpecializedConfiguration

public PredefinedScopeHibernateValidatorConfiguration createSpecializedConfiguration(BootstrapState state)

Specified by:
`createSpecializedConfiguration` in interface `ValidationProvider<PredefinedScopeHibernateValidatorConfiguration>`

  - 

### createGenericConfiguration

public Configuration<?> createGenericConfiguration(BootstrapState state)

Specified by:
`createGenericConfiguration` in interface `ValidationProvider<PredefinedScopeHibernateValidatorConfiguration>`

  - 

### buildValidatorFactory

public ValidatorFactory buildValidatorFactory(ConfigurationState configurationState)

Specified by:
`buildValidatorFactory` in interface `ValidationProvider<PredefinedScopeHibernateValidatorConfiguration>`

---

Copyright © 2007-2025 Red Hat, Inc. All Rights Reserved