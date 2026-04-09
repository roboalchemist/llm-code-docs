Package org.java_websocket.exceptions

# Class IncompleteException


java.lang.Object
java.lang.Throwable
java.lang.Exception
org.java_websocket.exceptions.IncompleteException





All Implemented Interfaces:
`Serializable`


---

public class IncompleteException
extends Exception
Exception which indicates that the frame is not yet complete

See Also:




- Serialized Form










- 


## Constructor Summary

Constructors

Constructor
Description
`IncompleteException(int preferredSize)`

Constructor for the preferred size of a frame






- 


## Method Summary





Modifier and Type
Method
Description
`int`
`getPreferredSize()`

Getter for the preferredSize






### Methods inherited from class java.lang.Throwable

`addSuppressed, fillInStackTrace, getCause, getLocalizedMessage, getMessage, getStackTrace, getSuppressed, initCause, printStackTrace, printStackTrace, printStackTrace, setStackTrace, toString`


### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`










- 


## Constructor Details




  - 


### IncompleteException

public IncompleteException(int preferredSize)
Constructor for the preferred size of a frame

Parameters:
`preferredSize` - the preferred size of a frame









- 


## Method Details




  - 


### getPreferredSize

public int getPreferredSize()
Getter for the preferredSize

Returns:
the value of the preferred size