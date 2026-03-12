Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class ProtocolException

java.lang.Object
java.lang.Throwable
java.lang.Exception
java.lang.RuntimeException
org.glassfish.tyrus.core.WebSocketException
org.glassfish.tyrus.core.ProtocolException

All Implemented Interfaces:
`Serializable`

---

public class ProtocolException
extends WebSocketException
Represents issue with parsing or producing websocket frame.

Author:
Pavel Bucek
See Also:

- Serialized Form

-

## Constructor Summary

Constructors

Constructor
Description
`ProtocolException(String reasonPhrase)`

-

## Method Summary

Modifier and Type
Method
Description
`jakarta.websocket.CloseReason`
`getCloseReason()`

Get close reason.

### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

-

## Constructor Details

-

### ProtocolException

public ProtocolException(String reasonPhrase)

-

## Method Details

-

### getCloseReason

public jakarta.websocket.CloseReason getCloseReason()
Description copied from class: `WebSocketException`
Get close reason.

Specified by:
`getCloseReason` in class `WebSocketException`
Returns:
close reason used when processing this exception.
