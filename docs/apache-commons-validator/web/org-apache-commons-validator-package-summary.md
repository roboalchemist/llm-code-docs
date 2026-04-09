# Package org.apache.commons.validator

---

package org.apache.commons.validator

The Validator package provides validation for JavaBeans based on an xml file.

 
 
 [Dependencies]
 [Introduction]
 [Overview]
 [Resources]
 [Usage Example]
 
 
 
## Introduction

 

A common issue when receiving data either electronically or from
 user input is verifying the integrity of the data.  This work is
 repetitive and becomes even more complicated when different sets
 of validation rules need to be applied to the same set of data based
 on locale for example.  Error messages may also vary by locale.
 This package attempts to address some of these issues and
 speed development and maintenance of validation rules.
 
 

In order to use the Validator, the following basic steps are required:
 

 
- Create a new instance of the
 `org.apache.commons.validator.Validator` class. Currently,
 Validator instances may be safely reused if the current ValidatorResources
 are the same, as long as
 you have completed any previous validation, and you do not try to utilize
 a particular Validator instance from more than one thread at a time.
 
- Add any resources
 needed to perform the validations.  Such as the JavaBean to validate.
 
- Call the validate method on `org.apache.commons.validator.Validator`.
 

 
 
## Overview

 

 The Commons Validator is a basic validation framework that
 lets you define validation rules for a JavaBean in an xml file.
 Validators, the validation definition, can also be defined in
 the xml file.  An example of a validator would be defining
 what method and class will be called to perform the validation
 for a required field.  Validation rules can be grouped together
 based on locale and a JavaBean/Form that the rules are associated
 with.  The framework has basic support for user-defined constants
 which can be used in some field attributes.
 
 

 Validation rules can be defined in an xml file which keeps
 them abstracted from JavaBean you are validating.  The
 property reference to a field supports nested properties
 using the Apache Commons BeanUtils
 (https://commons.apache.org/beanutils/) package.
 Error messages and the arguments for error messages can be
 associated with a field's validation.
 
 
 
## Resources

 

 After a Validator instance is created, instances of
 classes can be added to it to be passed into
 validation methods by calling the setParameter()
 method.  Below is a list of reserved parameters (class names).
 
 
 Reserved Parameters
 
 Class Name
 Validator Constant
 Description
 
 
 java.lang.Object
 Validator.BEAN_PARAM
 JavaBean that is being validated
 
 
 java.util.Locale
 Validator.LOCALE_PARAM
 
 Locale to use when retrieving a FormSet.
 The default locale will be used if one
 isn't specified.
 
 
 
 org.apache.commons.validator.ValidatorAction
 Validator.VALIDATOR_ACTION_PARAM
 
 This is automatically added to a Validator's
 resources as a validation is being processed.
 If this class name is used when defining
 a method signature for a pluggable validator,
 the current ValidatorAction will be passed into
 the validation method.
 
 
 
 org.apache.commons.validator.Field
 Validator.FIELD_PARAM
 
 This is automatically added to a Validator's
 resources as a validation is being processed.
 If this class name is used when defining
 a method signature for a pluggable validator,
 the current Field will be passed into
 the validation method.
 
 
 
 
 
## Usage Example

 

 This is a basic example setting up a required validator for
 a name bean.  This example is a working unit test (reference
 `org.apache.commons.validator.RequiredNameTest` and
 validator-name-required.xml located under validator/src/test).
 
 

 Create an xml file with your validator and validation rules.
 Setup your required validator in your xml file.

 

 XML Example

 Validator Example

 Pluggable Validator Example
 
 
 
## XML Example

 

 Definition of a 'required' pluggable validator.

 

```

 <form-validation>
 <global>
 <validator name="required"
 classname="org.apache.commons.validator.TestValidator"
 method="validateRequired"
 methodParams="java.lang.Object, org.apache.commons.validator.Field"/>
 </global>
 <formset>
 </formset>
 </form-validation>
 
```

 

 Add validation rules to require a first name and a last name.

 

```

 <form-validation>
 <global>
 <validator name="required"
 classname="org.apache.commons.validator.TestValidator"
 method="validateRequired"
 methodParams="java.lang.Object, org.apache.commons.validator.Field"/>
 </global>
 **
 <formset>
 <form    name="nameForm">
 <field property="firstName" depends="required">
 <arg0 key="nameForm.firstname.displayname"/>
 </field>
 <field property="lastName" depends="required">
 <arg0 key="nameForm.lastname.displayname"/>
 </field>
 </form>
 </formset>
 **
 </form-validation>
 
```

 
 
## Validator Example

 

 Excerpts from org.apache.commons.validator.RequiredNameTest
 
 

```

 InputStream in = this.getClass().getResourceAsStream("validator-name-required.xml");
 // Create an instance of ValidatorResources to initialize from an xml file.
 ValidatorResources resources = new ValidatorResources(in);
 // Create bean to run test on.
 Name name = new Name();
 // Construct validator based on the loaded resources and the form key
 Validator validator = new Validator(resources, "nameForm");
 // add the name bean to the validator as a resource
 // for the validations to be performed on.
 validator.setParameter(Validator.BEAN_PARAM, name);
 // Get results of the validation.
 Map results;
 // throws ValidatorException (catch clause not shown here)
 results = validator.validate();
 if (results.get("firstName") == null) {
 // no error
 } else {
 // number of errors for first name
 int errors = ((Integer) results.get("firstName")).intValue();
 }
 
```

 
 
## Pluggable Validator Example

 

 Validation method defined in the 'required' pluggable validator
 (excerpt from org.apache.commons.validator.TestValidator).
 
 

```

 public static boolean validateRequired(Object bean, Field field) {
 String value = ValidatorUtil.getValueAsString(bean, field.getProperty());
 return GenericValidator.isBlankOrNull(value);
 }
 
```

- 

Related Packages

Package
Description
org.apache.commons.validator.routines

This package contains *independent* validation routines.

org.apache.commons.validator.util

This package contains utility classes used by Commons Validator.

- 

Class
Description
Arg

 A default argument or an argument for a
 specific validator definition (ex: required)
 can be stored to pass into a message as parameters.

CreditCardValidator
Deprecated.
Use the new CreditCardValidator in the routines package.

CreditCardValidator.CreditCardType

CreditCardType implementations define how validation is performed
 for one type/brand of credit card.

DateValidator
Deprecated.
Use the new DateValidator, CalendarValidator or TimeValidator in the
 routines package.

EmailValidator
Deprecated.
Use the new EmailValidator in the routines package.

Field

This contains the list of pluggable validators to run on a field and any
 message information and variables to perform the validations and generate
 error messages.

Form

 This contains a set of validation rules for a form/JavaBean.

FormSet

Holds a set of `Form`s stored associated with a `Locale`
 based on the country, language, and variant specified.

FormSetFactory

Factory class used by Digester to create FormSet's.

GenericTypeValidator

This class contains basic methods for performing validations that return the
 correctly typed class based on the validation performed.

GenericValidator

This class contains basic methods for performing validations.

ISBNValidator
Deprecated.
Use the new ISBNValidator in the routines package

Msg

An alternative message can be associated with a `Field`
 and a pluggable validator instead of using the default message
 stored in the `ValidatorAction` (aka pluggable validator).

UrlValidator
Deprecated.
Use the new UrlValidator in the routines package.

Validator

Validations are processed by the validate method.

ValidatorAction

Contains the information to dynamically create and run a validation method.

ValidatorException

The base exception for the Validator Framework.

ValidatorResources

 General purpose class for storing `FormSet` objects based
 on their associated `Locale`.

ValidatorResult

This contains the results of a set of validation rules processed
 on a JavaBean.

ValidatorResult.ResultStatus

Contains the status of the validation.

ValidatorResults

This contains the results of a set of validation rules processed
 on a JavaBean.

Var

A variable that can be associated with a `Field` for
 passing in information to a pluggable validator.