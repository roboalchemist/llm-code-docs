Package org.java_websocket.enums

# Enum Class Opcode


java.lang.Object
java.lang.Enum<Opcode>
org.java_websocket.enums.Opcode




All Implemented Interfaces:
`Serializable`, `Comparable<Opcode>`, `Constable`


---

public enum Opcode
extends Enum<Opcode>
Enum which contains the different valid opcodes






- 


## Nested Class Summary



## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`




- 


## Enum Constant Summary

Enum Constants

Enum Constant
Description
`BINARY`
 
`CLOSING`
 
`CONTINUOUS`
 
`PING`
 
`PONG`
 
`TEXT`
 





- 


## Method Summary





Modifier and Type
Method
Description
`static Opcode`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static Opcode[]`
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


### CONTINUOUS

public static final Opcode CONTINUOUS



  - 


### TEXT

public static final Opcode TEXT



  - 


### BINARY

public static final Opcode BINARY



  - 


### PING

public static final Opcode PING



  - 


### PONG

public static final Opcode PONG



  - 


### CLOSING

public static final Opcode CLOSING








- 


## Method Details




  - 


### values

public static Opcode[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared




  - 


### valueOf

public static Opcode valueOf(String name)
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