Package org.jsoup.nodes

# Enum Document.QuirksMode

java.lang.Object
java.lang.Enum<Document.QuirksMode>
org.jsoup.nodes.Document.QuirksMode

All Implemented Interfaces:
`Serializable`, `Comparable<Document.QuirksMode>`, `java.lang.constant.Constable`

Enclosing class:
Document

---

public static enum Document.QuirksMode
extends Enum<Document.QuirksMode>

- 

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`

- 

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`limitedQuirks`
 
`noQuirks`
 
`quirks`
 

- 

## Method Summary

Modifier and Type
Method
Description
`static Document.QuirksMode`
`valueOf(String name)`

Returns the enum constant of this type with the specified name.

`static Document.QuirksMode[]`
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

### noQuirks

public static final Document.QuirksMode noQuirks

  - 

### quirks

public static final Document.QuirksMode quirks

  - 

### limitedQuirks

public static final Document.QuirksMode limitedQuirks

- 

## Method Details

  - 

### values

public static Document.QuirksMode[] values()
Returns an array containing the constants of this enum type, in
the order they are declared.

Returns:
an array containing the constants of this enum type, in the order they are declared

  - 

### valueOf

public static Document.QuirksMode valueOf(String name)
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