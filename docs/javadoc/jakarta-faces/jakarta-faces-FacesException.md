Package jakarta.faces

# Class FacesException

java.lang.Object
java.lang.Throwable
java.lang.Exception
java.lang.RuntimeException
jakarta.faces.FacesException

All Implemented Interfaces:
`Serializable`

Direct Known Subclasses:
`AbortProcessingException`, `ComponentNotFoundException`, `ConverterException`, `FaceletException`, `ProtectedViewException`, `UpdateModelException`, `ValidatorException`, `ViewExpiredException`

---

public class FacesException
extends RuntimeException

 This class encapsulates general Jakarta Faces exceptions.

See Also:

- Serialized Form

-

## Constructor Summary

Constructors

Constructor
Description
`FacesException()`

 Construct a new exception with no detail message or root cause.

`FacesException(String message)`

 Construct a new exception with the specified detail message and no root cause.

`FacesException(String message,
 Throwable cause)`

 Construct a new exception with the specified detail message and root cause.

`FacesException(Throwable cause)`

 Construct a new exception with the specified root cause.

-

## Method Summary

Modifier and Type
Method
Description
`Throwable`
`getCause()`

 Return the cause of this exception, or `null` if the cause is nonexistent or unknown.

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

-

## Constructor Details

-

### FacesException

public FacesException()

 Construct a new exception with no detail message or root cause.

-

### FacesException

public FacesException(String message)

 Construct a new exception with the specified detail message and no root cause.

Parameters:
`message` - The detail message for this exception

-

### FacesException

public FacesException(Throwable cause)

 Construct a new exception with the specified root cause. The detail message will be set to
 `(cause == null ? null :
 cause.toString()`

Parameters:
`cause` - The root cause for this exception

-

### FacesException

public FacesException(String message,
 Throwable cause)

 Construct a new exception with the specified detail message and root cause.

Parameters:
`message` - The detail message for this exception
`cause` - The root cause for this exception

-

## Method Details

-

### getCause

public Throwable getCause()

 Return the cause of this exception, or `null` if the cause is nonexistent or unknown.

Overrides:
`getCause` in class `Throwable`
