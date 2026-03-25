Package org.java_websocket.enums

# Enum Class ReadyState


java.lang.Object
java.lang.Enum<ReadyState>
org.java_websocket.enums.ReadyState




All Implemented Interfaces:
`Serializable`, `Comparable<ReadyState>`, `Constable`


---

public enum ReadyState
extends Enum<ReadyState>
Enum which represents the state a websocket may be in






- 


## Nested Class Summary



## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`




- 


## Enum Constant Summary

Enum Constants

Enum Constant
Description
`CLOSED`
 
`CLOSING`
 
`NOT_YET_CONNECTED`
 
`OPEN`
 





- 


## Method Summary





Modifier and Type
Method
Description
`static ReadyState`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static ReadyState[]`
`values()`

Returns an array containing the constants of this enum class, in
the order they are declared.






### Methods inherited from class java.lang.Enum

`clone, compareTo, describeConstable, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`


### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`










- 


## Enum Constant Details




  - 


### NOT_YET_CONNECTED

public static final ReadyState NOT_YET_CONNECTED



  - 


### OPEN

public static final ReadyState OPEN



  - 


### CLOSING

public static final ReadyState CLOSING



  - 


### CLOSED

public static final ReadyState CLOSED








- 


## Method Details




  - 


### values

public static ReadyState[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared




  - 


### valueOf

public static ReadyState valueOf(String name)
Returns the enum constant of this class with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this class.  (Extraneous whitespace characters are 
not permitted.)

Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`IllegalArgumentException` - if this enum class has no constant with the specified name
`NullPointerException` - if the argument is null