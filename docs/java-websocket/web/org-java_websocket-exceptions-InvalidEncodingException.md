Package org.java_websocket.exceptions

# Class InvalidEncodingException


java.lang.Object
java.lang.Throwable
java.lang.Exception
java.lang.RuntimeException
org.java_websocket.exceptions.InvalidEncodingException






All Implemented Interfaces:
`Serializable`


---

public class InvalidEncodingException
extends RuntimeException
The Character Encoding is not supported.

Since:
1.4.0
See Also:




- Serialized Form










- 


## Constructor Summary

Constructors

Constructor
Description
`InvalidEncodingException(UnsupportedEncodingException encodingException)`

constructor for InvalidEncodingException






- 


## Method Summary





Modifier and Type
Method
Description
`UnsupportedEncodingException`
`getEncodingException()`

Get the exception which includes more information on the unsupported encoding






### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`


### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### InvalidEncodingException

public InvalidEncodingException(UnsupportedEncodingException encodingException)
constructor for InvalidEncodingException

Parameters:
`encodingException` - the cause for this exception









- 


## Method Details




  - 


### getEncodingException

public UnsupportedEncodingException getEncodingException()
Get the exception which includes more information on the unsupported encoding

Returns:
an UnsupportedEncodingException