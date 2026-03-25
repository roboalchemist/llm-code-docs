Package org.jbake.app

# Class JBakeException

java.lang.Object
java.lang.Throwable
java.lang.Exception
java.lang.RuntimeException
org.jbake.app.JBakeException

All Implemented Interfaces:
`Serializable`

---

public class JBakeException
extends RuntimeException
This runtime exception is thrown by JBake API to indicate an processing
 error.
 

 It always contains an error message and if available the cause.

See Also:

- Serialized Form

- 

## Constructor Summary

Constructors

Constructor
Description
`JBakeException(SystemExit exit,
 String message)`
 
`JBakeException(SystemExit exit,
 String message,
 Throwable cause)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`int`
`getExit()`
 

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### JBakeException

public JBakeException(SystemExit exit,
 String message,
 Throwable cause)

Parameters:
`message` - The error message.
`cause` - The causing exception or `null` if no cause
            available.

  - 

### JBakeException

public JBakeException(SystemExit exit,
 String message)

- 

## Method Details

  - 

### getExit

public int getExit()