Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class HandshakeException

java.lang.Object
java.lang.Throwable
java.lang.Exception
org.glassfish.tyrus.core.HandshakeException

All Implemented Interfaces:
`Serializable`

---

public class HandshakeException
extends Exception
`Exception`, which describes the error, occurred during the handshake phase.

Author:
Alexey Stashok, Pavel Bucek
See Also:

- Serialized Form

-

## Constructor Summary

Constructors

Constructor
Description
`HandshakeException(int httpStatusCode,
 String message)`

Constructor.

`HandshakeException(String message)`

Construct a HandshakeException.

-

## Method Summary

Modifier and Type
Method
Description
`int`
`getHttpStatusCode()`

Get the error code.

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

-

## Constructor Details

-

### HandshakeException

public HandshakeException(String message)
Construct a HandshakeException. HTTP status code will be set to `500`.

Parameters:
`message` - error description

-

### HandshakeException

public HandshakeException(int httpStatusCode,
 String message)
Constructor.

Parameters:
`httpStatusCode` - http status code to be set to response.
`message` - the detail message. The detail message is saved for later retrieval by the `Throwable.getMessage()` method.

-

## Method Details

-

### getHttpStatusCode

public int getHttpStatusCode()
Get the error code.

Returns:
the error code.
