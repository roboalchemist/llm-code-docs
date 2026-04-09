Package org.java_websocket.exceptions

# Class InvalidDataException


java.lang.Object
java.lang.Throwable
java.lang.Exception
org.java_websocket.exceptions.InvalidDataException





All Implemented Interfaces:
`Serializable`


Direct Known Subclasses:
`InvalidFrameException`, `InvalidHandshakeException`, `LimitExceededException`


---

public class InvalidDataException
extends Exception
exception which indicates that a invalid data was received

See Also:




- Serialized Form










- 


## Constructor Summary

Constructors

Constructor
Description
`InvalidDataException(int closecode)`

constructor for a InvalidDataException

`InvalidDataException(int closecode,
 String s)`

constructor for a InvalidDataException.

`InvalidDataException(int closecode,
 String s,
 Throwable t)`

constructor for a InvalidDataException.

`InvalidDataException(int closecode,
 Throwable t)`

constructor for a InvalidDataException.






- 


## Method Summary





Modifier and Type
Method
Description
`int`
`getCloseCode()`

Getter closecode






### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`


### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### InvalidDataException

public InvalidDataException(int closecode)
constructor for a InvalidDataException

Parameters:
`closecode` - the closecode which will be returned




  - 


### InvalidDataException

public InvalidDataException(int closecode,
 String s)
constructor for a InvalidDataException.

Parameters:
`closecode` - the closecode which will be returned.
`s` - the detail message.




  - 


### InvalidDataException

public InvalidDataException(int closecode,
 Throwable t)
constructor for a InvalidDataException.

Parameters:
`closecode` - the closecode which will be returned.
`t` - the throwable causing this exception.




  - 


### InvalidDataException

public InvalidDataException(int closecode,
 String s,
 Throwable t)
constructor for a InvalidDataException.

Parameters:
`closecode` - the closecode which will be returned.
`s` - the detail message.
`t` - the throwable causing this exception.









- 


## Method Details




  - 


### getCloseCode

public int getCloseCode()
Getter closecode

Returns:
the closecode