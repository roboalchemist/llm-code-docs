Package org.java_websocket.exceptions

# Class IncompleteHandshakeException


java.lang.Object
java.lang.Throwable
java.lang.Exception
java.lang.RuntimeException
org.java_websocket.exceptions.IncompleteHandshakeException






All Implemented Interfaces:
`Serializable`


---

public class IncompleteHandshakeException
extends RuntimeException
exception which indicates that a incomplete handshake was received

See Also:




- Serialized Form










- 


## Constructor Summary

Constructors

Constructor
Description
`IncompleteHandshakeException()`

constructor for a IncompleteHandshakeException

`IncompleteHandshakeException(int preferredSize)`

constructor for a IncompleteHandshakeException






- 


## Method Summary





Modifier and Type
Method
Description
`int`
`getPreferredSize()`

Getter preferredSize






### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`


### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### IncompleteHandshakeException

public IncompleteHandshakeException(int preferredSize)
constructor for a IncompleteHandshakeException
 



Parameters:
`preferredSize` - the preferred size




  - 


### IncompleteHandshakeException

public IncompleteHandshakeException()
constructor for a IncompleteHandshakeException
 


 preferredSize will be 0








- 


## Method Details




  - 


### getPreferredSize

public int getPreferredSize()
Getter preferredSize

Returns:
the preferredSize