Package org.jbake.launcher

# Enum Class SystemExit

java.lang.Object
java.lang.Enum<SystemExit>
org.jbake.launcher.SystemExit

All Implemented Interfaces:
`Serializable`, `Comparable<SystemExit>`, `Constable`

---

public enum SystemExit
extends Enum<SystemExit>

- 

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`

- 

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`CONFIGURATION_ERROR`
 
`ERROR`
 
`INIT_ERROR`
 
`SERVER_ERROR`
 
`SUCCESS`
 

- 

## Method Summary

Modifier and Type
Method
Description
`int`
`getStatus()`
 
`static SystemExit`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static SystemExit[]`
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

### SUCCESS

public static final SystemExit SUCCESS

  - 

### ERROR

public static final SystemExit ERROR

  - 

### CONFIGURATION_ERROR

public static final SystemExit CONFIGURATION_ERROR

  - 

### INIT_ERROR

public static final SystemExit INIT_ERROR

  - 

### SERVER_ERROR

public static final SystemExit SERVER_ERROR

- 

## Method Details

  - 

### values

public static SystemExit[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared

  - 

### valueOf

public static SystemExit valueOf(String name)
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

  - 

### getStatus

public int getStatus()