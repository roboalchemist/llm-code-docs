Package com.nimbusds.jose

# Class JOSEException

java.lang.Object
java.lang.Throwable
java.lang.Exception
com.nimbusds.jose.JOSEException

All Implemented Interfaces:
`Serializable`

Direct Known Subclasses:
`ActionRequiredForJWSCompletionException`, `IntegerOverflowException`, `KeyException`, `KeySourceException`

---

public class JOSEException
extends Exception
Javascript Object Signing and Encryption (JOSE) exception.

Version:
2023-01-05
Author:
Vladimir Dzhuvinov
See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`JOSEException()`

Creates a new JOSE exception with the specified cause.

`JOSEException(String message)`

Creates a new JOSE exception with the specified message.

`JOSEException(String message,
 Throwable cause)`

Creates a new JOSE exception with the specified message and cause.

`JOSEException(Throwable cause)`

Creates a new JOSE exception with the specified cause.

- 

## Method Summary

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### JOSEException

public JOSEException(String message)
Creates a new JOSE exception with the specified message.

Parameters:
`message` - The exception message.

  - 

### JOSEException

public JOSEException(String message,
 Throwable cause)
Creates a new JOSE exception with the specified message and cause.

Parameters:
`message` - The exception message.
`cause` - The exception cause.

  - 

### JOSEException

public JOSEException(Throwable cause)
Creates a new JOSE exception with the specified cause.

Parameters:
`cause` - The exception cause.

  - 

### JOSEException

public JOSEException()
Creates a new JOSE exception with the specified cause.