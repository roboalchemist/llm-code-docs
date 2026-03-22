Package org.jsoup

# Class SerializationException

java.lang.Object
java.lang.Throwable
java.lang.Exception
java.lang.RuntimeException
org.jsoup.SerializationException

All Implemented Interfaces:
`Serializable`

---

public final class SerializationException
extends RuntimeException
A SerializationException is raised whenever serialization of a DOM element fails. This exception usually wraps an
 `IOException` that may be thrown due to an inaccessible output stream.

See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`SerializationException()`

Creates and initializes a new serialization exception with no error message and cause.

`SerializationException(String message)`

Creates and initializes a new serialization exception with the given error message and no cause.

`SerializationException(String message,
 Throwable cause)`

Creates and initializes a new serialization exception with the given error message and cause.

`SerializationException(Throwable cause)`

Creates and initializes a new serialization exception with the specified cause and an error message of
 `(cause==null ?`

- 

## Method Summary

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### SerializationException

public SerializationException()
Creates and initializes a new serialization exception with no error message and cause.

  - 

### SerializationException

public SerializationException(String message)
Creates and initializes a new serialization exception with the given error message and no cause.

Parameters:
`message` - the error message of the new serialization exception (may be `null`).

  - 

### SerializationException

public SerializationException(Throwable cause)
Creates and initializes a new serialization exception with the specified cause and an error message of
 `(cause==null ? null : cause.toString())` (which typically contains the class and error message of
 `cause`).

Parameters:
`cause` - the cause of the new serialization exception (may be `null`).

  - 

### SerializationException

public SerializationException(String message,
 Throwable cause)
Creates and initializes a new serialization exception with the given error message and cause.

Parameters:
`message` - the error message of the new serialization exception.
`cause` - the cause of the new serialization exception.