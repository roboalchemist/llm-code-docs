Package org.java_websocket.exceptions

# Class NotSendableException


java.lang.Object
java.lang.Throwable
java.lang.Exception
java.lang.RuntimeException
org.java_websocket.exceptions.NotSendableException






All Implemented Interfaces:
`Serializable`


---

public class NotSendableException
extends RuntimeException
exception which indicates the frame payload is not sendable

See Also:




- Serialized Form










- 


## Constructor Summary

Constructors

Constructor
Description
`NotSendableException(String s)`

constructor for a NotSendableException

`NotSendableException(String s,
 Throwable t)`

constructor for a NotSendableException

`NotSendableException(Throwable t)`

constructor for a NotSendableException






- 


## Method Summary



### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`


### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### NotSendableException

public NotSendableException(String s)
constructor for a NotSendableException

Parameters:
`s` - the detail message.




  - 


### NotSendableException

public NotSendableException(Throwable t)
constructor for a NotSendableException

Parameters:
`t` - the throwable causing this exception.




  - 


### NotSendableException

public NotSendableException(String s,
 Throwable t)
constructor for a NotSendableException

Parameters:
`s` - the detail message.
`t` - the throwable causing this exception.