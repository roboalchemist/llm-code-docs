# Enum Class SpringBootTest.WebEnvironment

java.lang.Object
java.lang.Enum<SpringBootTest.WebEnvironment>
org.springframework.boot.test.context.SpringBootTest.WebEnvironment

All Implemented Interfaces:
`Serializable, Comparable<SpringBootTest.WebEnvironment>, Constable`

Enclosing class:
`SpringBootTest`

---

public static enum SpringBootTest.WebEnvironment
extends Enum<SpringBootTest.WebEnvironment>
An enumeration web environment modes.

Since:
1.4.0

- 

## Nested Class Summary

### Nested classes/interfaces inherited from class Enum

`Enum.EnumDesc<E>`

- 

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`DEFINED_PORT`

Creates a web application context (reactive or servlet based) without defining
any `server.port=0` `Environment` property.

`MOCK`

Creates a `WebApplicationContext` with a mock servlet environment if
servlet APIs are on the classpath, a `ReactiveWebApplicationContext` if
Spring WebFlux is on the classpath or a regular `ApplicationContext`
otherwise.

`NONE`

Creates an `ApplicationContext` and sets
`SpringApplication.setWebApplicationType(WebApplicationType)` to
`WebApplicationType.NONE`.

`RANDOM_PORT`

Creates a web application context (reactive or servlet based) and sets a
`server.port=0` `Environment` property (which usually triggers
listening on a random port).

- 

## Method Summary

Modifier and Type
Method
Description
`boolean`
`isEmbedded()`

Return if the environment uses an embedded web server.

`static SpringBootTest.WebEnvironment`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static SpringBootTest.WebEnvironment[]`
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

### MOCK

public static final SpringBootTest.WebEnvironment MOCK
Creates a `WebApplicationContext` with a mock servlet environment if
servlet APIs are on the classpath, a `ReactiveWebApplicationContext` if
Spring WebFlux is on the classpath or a regular `ApplicationContext`
otherwise.

  - 

### RANDOM_PORT

public static final SpringBootTest.WebEnvironment RANDOM_PORT
Creates a web application context (reactive or servlet based) and sets a
`server.port=0` `Environment` property (which usually triggers
listening on a random port). Requires a dependency on
`spring-boot-web-server`. Often used in conjunction with a
`@LocalServerPort` injected field on the test.

  - 

### DEFINED_PORT

public static final SpringBootTest.WebEnvironment DEFINED_PORT
Creates a web application context (reactive or servlet based) without defining
any `server.port=0` `Environment` property. Requires a dependency
on `spring-boot-web-server`.

  - 

### NONE

public static final SpringBootTest.WebEnvironment NONE
Creates an `ApplicationContext` and sets
`SpringApplication.setWebApplicationType(WebApplicationType)` to
`WebApplicationType.NONE`.

- 

## Method Details

  - 

### values

public static SpringBootTest.WebEnvironment[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared

  - 

### valueOf

public static SpringBootTest.WebEnvironment valueOf(String name)
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

### isEmbedded

public boolean isEmbedded()
Return if the environment uses an embedded web server.

Returns:
if an embedded web server is used