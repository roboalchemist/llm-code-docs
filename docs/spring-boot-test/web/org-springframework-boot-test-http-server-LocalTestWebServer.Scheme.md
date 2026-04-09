# Enum Class LocalTestWebServer.Scheme

java.lang.Object
java.lang.Enum<LocalTestWebServer.Scheme>
org.springframework.boot.test.http.server.LocalTestWebServer.Scheme

All Implemented Interfaces:
`Serializable, Comparable<LocalTestWebServer.Scheme>, Constable`

Enclosing class:
`LocalTestWebServer`

---

public static enum LocalTestWebServer.Scheme
extends Enum<LocalTestWebServer.Scheme>
Supported HTTP schemes.

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
`HTTP`

HTTP scheme.

`HTTPS`

HTTPS scheme.

- 

## Method Summary

Modifier and Type
Method
Description
`static LocalTestWebServer.Scheme`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static LocalTestWebServer.Scheme[]`
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

### HTTP

public static final LocalTestWebServer.Scheme HTTP
HTTP scheme.

  - 

### HTTPS

public static final LocalTestWebServer.Scheme HTTPS
HTTPS scheme.

- 

## Method Details

  - 

### values

public static LocalTestWebServer.Scheme[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared

  - 

### valueOf

public static LocalTestWebServer.Scheme valueOf(String name)
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