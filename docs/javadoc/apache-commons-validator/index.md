# Apache Commons Validator 1.10.1 API

 
  
  
# 
    Introduction
  

  

Apache Commons Validator helps you with common issues when receiving data either electronically or from user input and verifying the integrity of that
    data. This work is repetitive and becomes even more complicated when different sets of validation rules need to be applied to the same set of data based on
    locale. Error messages may also vary by locale. This package addresses some of these issues to speed development and maintenance of validation rules.
  
# 
    Features
  

  

Commons Validator provides two distinct sets of functionality:
  

    
- A configurable (typically XML) validation engine
    
- Reusable "primitive" validation methods
  

  

Your validation methods are plugged into the engine and executed against your data. Often, these methods use resources specific to one application or
    framework so Commons Validator doesn't directly provide pluggable validator actions. However, it does have a set of common validation methods (email
    addresses, dates, URLs, etc.) that help in creating pluggable actions.
  
# 
    Using Commons Validator
  

  

In order to use the Validator, the following basic steps are required:
  

    
- Create a new instance of the `org.apache.commons.validator.Validator` class. Currently Validator instances may be safely reused if the
      current ValidatorResources are the same, as long as you have completed any previous validation, and you do not try to utilize a particular Validator
      instance from more than one thread at a time.
    
    
- Add any resources needed to perform the validations, such as the JavaBean to validate.
    
- Call the validate method on `org.apache.commons.validator.Validator`.
    
  

  
# 
    Requirements
  

  

    
- Java 8 or above.
    
- If using OSGi, R7 or above.
  

Packages

Package
Description
org.apache.commons.validator

The Validator package provides validation for JavaBeans based on an xml file.

org.apache.commons.validator.routines

This package contains *independent* validation routines.

org.apache.commons.validator.routines.checkdigit

This package contains *Check Digit* validation/calculation routines.

org.apache.commons.validator.util

This package contains utility classes used by Commons Validator.