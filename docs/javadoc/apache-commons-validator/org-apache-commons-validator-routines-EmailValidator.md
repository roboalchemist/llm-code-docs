Package org.apache.commons.validator.routines

# Class EmailValidator

java.lang.Object
org.apache.commons.validator.routines.EmailValidator

All Implemented Interfaces:
`Serializable`

---

public class EmailValidator
extends Object
implements Serializable

Perform email validations.
 

 Based on a script by Sandeep V. Tamhankar
 https://javascript.internet.com
 
 

 This implementation is not guaranteed to catch all possible errors in an email address.
 .

Since:
1.4
See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`EmailValidator(boolean allowLocal)`

Protected constructor for subclasses to use.

`protected `
`EmailValidator(boolean allowLocal,
 boolean allowTld)`

Protected constructor for subclasses to use.

` `
`EmailValidator(boolean allowLocal,
 boolean allowTld,
 DomainValidator domainValidator)`

constructor for creating instances with the specified domainValidator

- 

## Method Summary

Modifier and Type
Method
Description
`static EmailValidator`
`getInstance()`

Returns the Singleton instance of this validator.

`static EmailValidator`
`getInstance(boolean allowLocal)`

Returns the Singleton instance of this validator,
  with local validation as required.

`static EmailValidator`
`getInstance(boolean allowLocal,
 boolean allowTld)`

Returns the Singleton instance of this validator, with local validation as required.

`boolean`
`isValid(String email)`

Checks if a field has a valid e-mail address.

`protected boolean`
`isValidDomain(String domain)`

Returns true if the domain component of an email address is valid.

`protected boolean`
`isValidUser(String user)`

Returns true if the user component of an email address is valid.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### EmailValidator

protected EmailValidator(boolean allowLocal)
Protected constructor for subclasses to use.

Parameters:
`allowLocal` - Should local addresses be considered valid?

  - 

### EmailValidator

protected EmailValidator(boolean allowLocal,
 boolean allowTld)
Protected constructor for subclasses to use.

Parameters:
`allowLocal` - Should local addresses be considered valid?
`allowTld` - Should TLDs be allowed?

  - 

### EmailValidator

public EmailValidator(boolean allowLocal,
 boolean allowTld,
 DomainValidator domainValidator)
constructor for creating instances with the specified domainValidator

Parameters:
`allowLocal` - Should local addresses be considered valid?
`allowTld` - Should TLDs be allowed?
`domainValidator` - allow override of the DomainValidator.
 The instance must have the same allowLocal setting.
Since:
1.7

- 

## Method Details

  - 

### getInstance

public static EmailValidator getInstance()
Returns the Singleton instance of this validator.

Returns:
singleton instance of this validator.

  - 

### getInstance

public static EmailValidator getInstance(boolean allowLocal)
Returns the Singleton instance of this validator,
  with local validation as required.

Parameters:
`allowLocal` - Should local addresses be considered valid?
Returns:
singleton instance of this validator

  - 

### getInstance

public static EmailValidator getInstance(boolean allowLocal,
 boolean allowTld)
Returns the Singleton instance of this validator, with local validation as required.

Parameters:
`allowLocal` - Should local addresses be considered valid?
`allowTld` - Should TLDs be allowed?
Returns:
singleton instance of this validator

  - 

### isValid

public boolean isValid(String email)

Checks if a field has a valid e-mail address.

Parameters:
`email` - The value validation is being performed on.  A `null`
              value is considered invalid.
Returns:
true if the email address is valid.

  - 

### isValidDomain

protected boolean isValidDomain(String domain)
Returns true if the domain component of an email address is valid.

Parameters:
`domain` - being validated, may be in IDN format
Returns:
true if the email address's domain is valid.

  - 

### isValidUser

protected boolean isValidUser(String user)
Returns true if the user component of an email address is valid.

Parameters:
`user` - being validated
Returns:
true if the username is valid.