# Enum Class ApplicationContextAssert.Scope

java.lang.Object
java.lang.Enum<ApplicationContextAssert.Scope>
org.springframework.boot.test.context.assertj.ApplicationContextAssert.Scope

All Implemented Interfaces:
`Serializable, Comparable<ApplicationContextAssert.Scope>, Constable`

Enclosing class:
`ApplicationContextAssert<C extends org.springframework.context.ApplicationContext>`

---

public static enum ApplicationContextAssert.Scope
extends Enum<ApplicationContextAssert.Scope>
The scope of an assertion.

Since:
2.0.0

- 

## Nested Class Summary

### Nested classes/interfaces inherited from class Enum

`Enum.EnumDesc<E>`

- 

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`INCLUDE_ANCESTORS`

Consider the ancestor contexts as well as the current context.

`NO_ANCESTORS`

Limited to the current context.

- 

## Method Summary

Modifier and Type
Method
Description
`static ApplicationContextAssert.Scope`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static ApplicationContextAssert.Scope[]`
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

### NO_ANCESTORS

public static final ApplicationContextAssert.Scope NO_ANCESTORS
Limited to the current context.

  - 

### INCLUDE_ANCESTORS

public static final ApplicationContextAssert.Scope INCLUDE_ANCESTORS
Consider the ancestor contexts as well as the current context.

- 

## Method Details

  - 

### values

public static ApplicationContextAssert.Scope[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared

  - 

### valueOf

public static ApplicationContextAssert.Scope valueOf(String name)
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