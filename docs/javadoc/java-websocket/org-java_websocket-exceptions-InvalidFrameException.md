Package org.java_websocket.exceptions

# Class InvalidFrameException


java.lang.Object
java.lang.Throwable
java.lang.Exception
org.java_websocket.exceptions.InvalidDataException
org.java_websocket.exceptions.InvalidFrameException






All Implemented Interfaces:
`Serializable`


---

public class InvalidFrameException
extends InvalidDataException
exception which indicates that a invalid frame was received (CloseFrame.PROTOCOL_ERROR)

See Also:




- Serialized Form










- 


## Constructor Summary

Constructors

Constructor
Description
`InvalidFrameException()`

constructor for a InvalidFrameException

`InvalidFrameException(String s)`

constructor for a InvalidFrameException

`InvalidFrameException(String s,
 Throwable t)`

constructor for a InvalidFrameException

`InvalidFrameException(Throwable t)`

constructor for a InvalidFrameException






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


### InvalidFrameException

public InvalidFrameException()
constructor for a InvalidFrameException
 


 calling InvalidDataException with closecode PROTOCOL_ERROR



  - 


### InvalidFrameException

public InvalidFrameException(String s)
constructor for a InvalidFrameException
 


 calling InvalidDataException with closecode PROTOCOL_ERROR

Parameters:
`s` - the detail message.




  - 


### InvalidFrameException

public InvalidFrameException(Throwable t)
constructor for a InvalidFrameException
 


 calling InvalidDataException with closecode PROTOCOL_ERROR

Parameters:
`t` - the throwable causing this exception.




  - 


### InvalidFrameException

public InvalidFrameException(String s,
 Throwable t)
constructor for a InvalidFrameException
 


 calling InvalidDataException with closecode PROTOCOL_ERROR

Parameters:
`s` - the detail message.
`t` - the throwable causing this exception.