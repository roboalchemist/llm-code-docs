Package org.jbake.app.configuration

# Enum Class Property.Group

java.lang.Object
java.lang.Enum<Property.Group>
org.jbake.app.configuration.Property.Group

All Implemented Interfaces:
`Serializable`, `Comparable<Property.Group>`, `Constable`

Enclosing class:
Property

---

public static enum Property.Group
extends Enum<Property.Group>

- 

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`

- 

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`CUSTOM`
 
`DEFAULT`
 

- 

## Method Summary

Modifier and Type
Method
Description
`static Property.Group`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static Property.Group[]`
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

### DEFAULT

public static final Property.Group DEFAULT

  - 

### CUSTOM

public static final Property.Group CUSTOM

- 

## Method Details

  - 

### values

public static Property.Group[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared

  - 

### valueOf

public static Property.Group valueOf(String name)
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