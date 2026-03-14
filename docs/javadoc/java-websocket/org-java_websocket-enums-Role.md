Package org.java_websocket.enums

# Enum Class Role


java.lang.Object
java.lang.Enum<Role>
org.java_websocket.enums.Role




All Implemented Interfaces:
`Serializable`, `Comparable<Role>`, `Constable`


---

public enum Role
extends Enum<Role>
Enum which represents the states a websocket may be in






- 


## Nested Class Summary



## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`




- 


## Enum Constant Summary

Enum Constants

Enum Constant
Description
`CLIENT`
 
`SERVER`
 





- 


## Method Summary





Modifier and Type
Method
Description
`static Role`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static Role[]`
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


### CLIENT

public static final Role CLIENT



  - 


### SERVER

public static final Role SERVER








- 


## Method Details




  - 


### values

public static Role[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared




  - 


### valueOf

public static Role valueOf(String name)
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