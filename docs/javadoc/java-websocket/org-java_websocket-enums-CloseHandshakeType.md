Package org.java_websocket.enums

# Enum Class CloseHandshakeType


java.lang.Object
java.lang.Enum<CloseHandshakeType>
org.java_websocket.enums.CloseHandshakeType




All Implemented Interfaces:
`Serializable`, `Comparable<CloseHandshakeType>`, `Constable`


---

public enum CloseHandshakeType
extends Enum<CloseHandshakeType>
Enum which represents type of handshake is required for a close






- 


## Nested Class Summary



## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`




- 


## Enum Constant Summary

Enum Constants

Enum Constant
Description
`NONE`
 
`ONEWAY`
 
`TWOWAY`
 





- 


## Method Summary





Modifier and Type
Method
Description
`static CloseHandshakeType`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static CloseHandshakeType[]`
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


### NONE

public static final CloseHandshakeType NONE



  - 


### ONEWAY

public static final CloseHandshakeType ONEWAY



  - 


### TWOWAY

public static final CloseHandshakeType TWOWAY








- 


## Method Details




  - 


### values

public static CloseHandshakeType[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared




  - 


### valueOf

public static CloseHandshakeType valueOf(String name)
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