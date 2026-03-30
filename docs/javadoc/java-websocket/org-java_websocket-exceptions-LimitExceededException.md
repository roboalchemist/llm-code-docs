Package org.java_websocket.exceptions

# Class LimitExceededException


java.lang.Object
java.lang.Throwable
java.lang.Exception
org.java_websocket.exceptions.InvalidDataException
org.java_websocket.exceptions.LimitExceededException






All Implemented Interfaces:
`Serializable`


---

public class LimitExceededException
extends InvalidDataException
exception which indicates that the message limited was exceeded (CloseFrame.TOOBIG)

See Also:




- Serialized Form










- 


## Constructor Summary

Constructors

Constructor
Description
`LimitExceededException()`

constructor for a LimitExceededException

`LimitExceededException(int limit)`

constructor for a LimitExceededException

`LimitExceededException(String s)`

constructor for a LimitExceededException

`LimitExceededException(String s,
 int limit)`

constructor for a LimitExceededException






- 


## Method Summary





Modifier and Type
Method
Description
`int`
`getLimit()`

Get the limit which was hit so this exception was caused






### Methods inherited from class org.java_websocket.exceptions.InvalidDataException

`getCloseCode`


### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`


### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### LimitExceededException

public LimitExceededException()
constructor for a LimitExceededException
 


 calling LimitExceededException with closecode TOOBIG



  - 


### LimitExceededException

public LimitExceededException(int limit)
constructor for a LimitExceededException
 


 calling InvalidDataException with closecode TOOBIG

Parameters:
`limit` - the allowed size which was not enough




  - 


### LimitExceededException

public LimitExceededException(String s,
 int limit)
constructor for a LimitExceededException
 


 calling InvalidDataException with closecode TOOBIG

Parameters:
`s` - the detail message.
`limit` - the allowed size which was not enough




  - 


### LimitExceededException

public LimitExceededException(String s)
constructor for a LimitExceededException
 


 calling InvalidDataException with closecode TOOBIG

Parameters:
`s` - the detail message.









- 


## Method Details




  - 


### getLimit

public int getLimit()
Get the limit which was hit so this exception was caused

Returns:
the limit as int