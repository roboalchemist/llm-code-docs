# Enum Class PropertyMapping.Skip

java.lang.Object
java.lang.Enum<PropertyMapping.Skip>
org.springframework.boot.test.context.PropertyMapping.Skip

All Implemented Interfaces:
`Serializable, Comparable<PropertyMapping.Skip>, Constable`

Enclosing class:
`PropertyMapping`

---

public static enum PropertyMapping.Skip
extends Enum<PropertyMapping.Skip>
Controls when mapping is skipped.

Since:
4.0.0

- 

## Nested Class Summary

### Nested classes/interfaces inherited from class Enum

`Enum.EnumDesc<E>`

- 

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`NO`

Don't skip mapping the property.

`ON_DEFAULT_VALUE`

Skip mapping the property when the default attribute value is specified.

`YES`

Skip mapping the property.

- 

## Method Summary

Modifier and Type
Method
Description
`static PropertyMapping.Skip`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static PropertyMapping.Skip[]`
`values()`

Returns an array containing the constants of this enum class, in
the order they are declared.

### Methods inherited from class Enum

`clone, compareTo, describeConstable, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`

### Methods inherited from class Object

`getClass, notify, notifyAll, wait, wait, wait`

- 

## Enum Constant Details

  - 

### YES

public static final PropertyMapping.Skip YES
Skip mapping the property.

  - 

### ON_DEFAULT_VALUE

public static final PropertyMapping.Skip ON_DEFAULT_VALUE
Skip mapping the property when the default attribute value is specified.

  - 

### NO

public static final PropertyMapping.Skip NO
Don't skip mapping the property.

- 

## Method Details

  - 

### values

public static PropertyMapping.Skip[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared

  - 

### valueOf

public static PropertyMapping.Skip valueOf(String name)
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