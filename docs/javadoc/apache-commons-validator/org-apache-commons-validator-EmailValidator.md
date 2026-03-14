Package org.apache.commons.validator

# Class EmailValidator

java.lang.Object
org.apache.commons.validator.EmailValidator

---

@Deprecated
public class EmailValidator
extends Object
Deprecated.
Use the new EmailValidator in the routines package. This class
 will be removed in a future release.

Perform email validations.
 

 This class is a Singleton; you can retrieve the instance via the getInstance() method.
 
 

 Based on a script by Sandeep V. Tamhankar
 https://javascript.internet.com
 
 

 This implementation is not guaranteed to catch all possible errors in an email address.
 For example, an address like [email protected] will pass validator, even though there
 is no TLD "somedog"
 .

Since:
1.1

- 

## Constructor Summary

Constructors

Modifier
Constructor
Description
`protected `
`EmailValidator()`

Deprecated.
Protected constructor for subclasses to use.

- 

## Method Summary

Modifier and Type
Method
Description
`static EmailValidator`
`getInstance()`

Deprecated.
Returns the Singleton instance of this validator.

`boolean`
`isValid(String email)`

Deprecated.
Checks if a field has a valid e-mail address.

`protected boolean`
`isValidDomain(String domain)`

Deprecated.
Returns true if the domain component of an email address is valid.

`protected boolean`
`isValidIpAddress(String ipAddress)`

Deprecated.
Validates an IP address.

`protected boolean`
`isValidSymbolicDomain(String domain)`

Deprecated.
Validates a symbolic domain name.

`protected boolean`
`isValidUser(String user)`

Deprecated.
Returns true if the user component of an email address is valid.

`protected String`
`stripComments(String emailStr)`

Deprecated.
Recursively remove comments, and replace with a single space.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### EmailValidator

protected EmailValidator()
Deprecated.
Protected constructor for subclasses to use.

- 

## Method Details

  - 

### getInstance

public static EmailValidator getInstance()
Deprecated.
Returns the Singleton instance of this validator.

Returns:
singleton instance of this validator.

  - 

### isValid

public boolean isValid(String email)
Deprecated.

Checks if a field has a valid e-mail address.

Parameters:
`email` - The value validation is being performed on.  A `null`
 value is considered invalid.
Returns:
true if the email address is valid.

  - 

### isValidDomain

protected boolean isValidDomain(String domain)
Deprecated.
Returns true if the domain component of an email address is valid.

Parameters:
`domain` - being validated.
Returns:
true if the email address's domain is valid.

  - 

### isValidIpAddress

protected boolean isValidIpAddress(String ipAddress)
Deprecated.
Validates an IP address. Returns true if valid.

Parameters:
`ipAddress` - IP address
Returns:
true if the ip address is valid.

  - 

### isValidSymbolicDomain

protected boolean isValidSymbolicDomain(String domain)
Deprecated.
Validates a symbolic domain name.  Returns true if it's valid.

Parameters:
`domain` - symbolic domain name
Returns:
true if the symbolic domain name is valid.

  - 

### isValidUser

protected boolean isValidUser(String user)
Deprecated.
Returns true if the user component of an email address is valid.

Parameters:
`user` - being validated
Returns:
true if the username is valid.

  - 

### stripComments

protected String stripComments(String emailStr)
Deprecated.
Recursively remove comments, and replace with a single space. The simpler regexps in the Email Addressing FAQ are imperfect - they will miss escaped
 chars in atoms, for example. Derived From Mail::RFC822::Address

Parameters:
`emailStr` - The email address
Returns:
address with comments removed.