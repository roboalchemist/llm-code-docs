Package org.java_websocket.exceptions

# Class WrappedIOException


java.lang.Object
java.lang.Throwable
java.lang.Exception
org.java_websocket.exceptions.WrappedIOException





All Implemented Interfaces:
`Serializable`


---

public class WrappedIOException
extends Exception
Exception to wrap an IOException and include information about the websocket which had the
 exception

Since:
1.4.1
See Also:




- Serialized Form










- 


## Constructor Summary

Constructors

Constructor
Description
`WrappedIOException(WebSocket connection,
 IOException ioException)`

Wrapp an IOException and include the websocket






- 


## Method Summary





Modifier and Type
Method
Description
`WebSocket`
`getConnection()`

The websocket where the IOException happened

`IOException`
`getIOException()`

The wrapped IOException






### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`


### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### WrappedIOException

public WrappedIOException(WebSocket connection,
 IOException ioException)
Wrapp an IOException and include the websocket

Parameters:
`connection` - the websocket where the IOException happened
`ioException` - the IOException









- 


## Method Details




  - 


### getConnection

public WebSocket getConnection()
The websocket where the IOException happened

Returns:
the websocket for the wrapped IOException




  - 


### getIOException

public IOException getIOException()
The wrapped IOException

Returns:
IOException which is wrapped