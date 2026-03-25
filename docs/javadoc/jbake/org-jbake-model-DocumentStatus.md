Package org.jbake.model

# Enum Class DocumentStatus

java.lang.Object
java.lang.Enum<DocumentStatus>
org.jbake.model.DocumentStatus

All Implemented Interfaces:
`Serializable`, `Comparable<DocumentStatus>`, `Constable`

---

public enum DocumentStatus
extends Enum<DocumentStatus>
Enumeration used to determine whether rendering of a document
 should be done.

- 

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`

- 

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`IDENTICAL`
 
`NEW`
 
`UPDATED`
 

- 

## Method Summary

Modifier and Type
Method
Description
`static DocumentStatus`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static DocumentStatus[]`
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

### NEW

public static final DocumentStatus NEW

  - 

### UPDATED

public static final DocumentStatus UPDATED

  - 

### IDENTICAL

public static final DocumentStatus IDENTICAL

- 

## Method Details

  - 

### values

public static DocumentStatus[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared

  - 

### valueOf

public static DocumentStatus valueOf(String name)
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