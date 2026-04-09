Package org.apache.commons.validator

# Class ValidatorException

java.lang.Object
java.lang.Throwable
java.lang.Exception
org.apache.commons.validator.ValidatorException

All Implemented Interfaces:
`Serializable`

---

public class ValidatorException
extends Exception
The base exception for the Validator Framework.  All other
 `Exception`s thrown during calls to
 `Validator.validate()` are considered errors.

See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`ValidatorException()`

Constructs an Exception with no specified detail message.

`ValidatorException(String message)`

Constructs an Exception with the specified detail message.

- 

## Method Summary

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### ValidatorException

public ValidatorException()
Constructs an Exception with no specified detail message.

  - 

### ValidatorException

public ValidatorException(String message)
Constructs an Exception with the specified detail message.

Parameters:
`message` - The error message.