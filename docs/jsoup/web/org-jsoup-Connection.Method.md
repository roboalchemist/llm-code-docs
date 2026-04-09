Package org.jsoup

# Enum Connection.Method

java.lang.Object
java.lang.Enum<Connection.Method>
org.jsoup.Connection.Method

All Implemented Interfaces:
`Serializable`, `Comparable<Connection.Method>`, `java.lang.constant.Constable`

Enclosing interface:
Connection

---

public static enum Connection.Method
extends Enum<Connection.Method>
GET and POST http methods.

- 

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`

- 

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`DELETE`
 
`GET`
 
`HEAD`
 
`OPTIONS`
 
`PATCH`

Note that unfortunately, PATCH is not supported in many JDKs.

`POST`
 
`PUT`
 
`TRACE`
 

- 

## Method Summary

Modifier and Type
Method
Description
`final boolean`
`hasBody()`

Check if this HTTP method has/needs a request body

`static Connection.Method`
`valueOf(String name)`

Returns the enum constant of this type with the specified name.

`static Connection.Method[]`
`values()`

Returns an array containing the constants of this enum type, in
the order they are declared.

### Methods inherited from class java.lang.Enum

`clone, compareTo, describeConstable, equals, finalize, getDeclaringClass, hashCode, name, ordinal, toString, valueOf`

### Methods inherited from class java.lang.Object

`getClass, notify, notifyAll, wait, wait, wait`

- 

## Enum Constant Details

  - 

### GET

public static final Connection.Method GET

  - 

### POST

public static final Connection.Method POST

  - 

### PUT

public static final Connection.Method PUT

  - 

### DELETE

public static final Connection.Method DELETE

  - 

### PATCH

public static final Connection.Method PATCH
Note that unfortunately, PATCH is not supported in many JDKs.

  - 

### HEAD

public static final Connection.Method HEAD

  - 

### OPTIONS

public static final Connection.Method OPTIONS

  - 

### TRACE

public static final Connection.Method TRACE

- 

## Method Details

  - 

### values

public static Connection.Method[] values()
Returns an array containing the constants of this enum type, in
the order they are declared.

Returns:
an array containing the constants of this enum type, in the order they are declared

  - 

### valueOf

public static Connection.Method valueOf(String name)
Returns the enum constant of this type with the specified name.
The string must match *exactly* an identifier used to declare an
enum constant in this type.  (Extraneous whitespace characters are 
not permitted.)

Parameters:
`name` - the name of the enum constant to be returned.
Returns:
the enum constant with the specified name
Throws:
`IllegalArgumentException` - if this enum type has no constant with the specified name
`NullPointerException` - if the argument is null

  - 

### hasBody

public final boolean hasBody()
Check if this HTTP method has/needs a request body

Returns:
if body needed