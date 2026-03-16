# Enum Class SpringBootTest.UseMainMethod

java.lang.Object
java.lang.Enum<SpringBootTest.UseMainMethod>
org.springframework.boot.test.context.SpringBootTest.UseMainMethod

All Implemented Interfaces:
`Serializable, Comparable<SpringBootTest.UseMainMethod>, Constable`

Enclosing class:
`SpringBootTest`

---

public static enum SpringBootTest.UseMainMethod
extends Enum<SpringBootTest.UseMainMethod>
Enumeration of how the main method of the
`@SpringBootConfiguration`-annotated class is used
when creating and running the `SpringApplication` under test.

Since:
3.0.0

- 

## Nested Class Summary

### Nested classes/interfaces inherited from class Enum

`Enum.EnumDesc<E>`

- 

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`ALWAYS`

Always use the `main` method.

`NEVER`

Never use the `main` method, creating a test-specific
`SpringApplication` instead.

`WHEN_AVAILABLE`

Use the `main` method when it is available.

- 

## Method Summary

Modifier and Type
Method
Description
`static SpringBootTest.UseMainMethod`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static SpringBootTest.UseMainMethod[]`
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

### ALWAYS

public static final SpringBootTest.UseMainMethod ALWAYS
Always use the `main` method. A failure will occur if there is no
`@SpringBootConfiguration`-annotated class or
that class does not have a main method.

  - 

### NEVER

public static final SpringBootTest.UseMainMethod NEVER
Never use the `main` method, creating a test-specific
`SpringApplication` instead.

  - 

### WHEN_AVAILABLE

public static final SpringBootTest.UseMainMethod WHEN_AVAILABLE
Use the `main` method when it is available. If there is no
`@SpringBootConfiguration`-annotated class or
that class does not have a main method, a test-specific
`SpringApplication` will be used.

- 

## Method Details

  - 

### values

public static SpringBootTest.UseMainMethod[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared

  - 

### valueOf

public static SpringBootTest.UseMainMethod valueOf(String name)
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