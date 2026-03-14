Package org.java_websocket.exceptions

# Class InvalidHandshakeException


java.lang.Object
java.lang.Throwable
java.lang.Exception
org.java_websocket.exceptions.InvalidDataException
org.java_websocket.exceptions.InvalidHandshakeException






All Implemented Interfaces:
`Serializable`


---

public class InvalidHandshakeException
extends InvalidDataException
exception which indicates that a invalid handshake was received (CloseFrame.PROTOCOL_ERROR)

See Also:




- Serialized Form










- 


## Constructor Summary

Constructors

Constructor
Description
`InvalidHandshakeException()`

constructor for a InvalidHandshakeException

`InvalidHandshakeException(String s)`

constructor for a InvalidHandshakeException

`InvalidHandshakeException(String s,
 Throwable t)`

constructor for a InvalidHandshakeException

`InvalidHandshakeException(Throwable t)`

constructor for a InvalidHandshakeException






- 


## Method Summary



### Methods inherited from class org.java_websocket.exceptions.InvalidDataException

`getCloseCode`


### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`


### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### InvalidHandshakeException

public InvalidHandshakeException()
constructor for a InvalidHandshakeException
 


 calling InvalidDataException with closecode PROTOCOL_ERROR



  - 


### InvalidHandshakeException

public InvalidHandshakeException(String s,
 Throwable t)
constructor for a InvalidHandshakeException
 


 calling InvalidDataException with closecode PROTOCOL_ERROR

Parameters:
`s` - the detail message.
`t` - the throwable causing this exception.




  - 


### InvalidHandshakeException

public InvalidHandshakeException(String s)
constructor for a InvalidHandshakeException
 


 calling InvalidDataException with closecode PROTOCOL_ERROR

Parameters:
`s` - the detail message.




  - 


### InvalidHandshakeException

public InvalidHandshakeException(Throwable t)
constructor for a InvalidHandshakeException
 


 calling InvalidDataException with closecode PROTOCOL_ERROR

Parameters:
`t` - the throwable causing this exception.