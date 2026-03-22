Package org.jsoup.nodes

# Enum Entities.EscapeMode

java.lang.Object
java.lang.Enum<Entities.EscapeMode>
org.jsoup.nodes.Entities.EscapeMode

All Implemented Interfaces:
`Serializable`, `Comparable<Entities.EscapeMode>`, `java.lang.constant.Constable`

Enclosing class:
Entities

---

public static enum Entities.EscapeMode
extends Enum<Entities.EscapeMode>

- 

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`

- 

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`base`

Default HTML output entities.

`extended`

Complete HTML entities.

`xhtml`

Restricted entities suitable for XHTML output: lt, gt, amp, and quot only.

- 

## Method Summary

Modifier and Type
Method
Description
`static Entities.EscapeMode`
`valueOf(String name)`

Returns the enum constant of this type with the specified name.

`static Entities.EscapeMode[]`
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

### xhtml

public static final Entities.EscapeMode xhtml
Restricted entities suitable for XHTML output: lt, gt, amp, and quot only.

  - 

### base

public static final Entities.EscapeMode base
Default HTML output entities.

  - 

### extended

public static final Entities.EscapeMode extended
Complete HTML entities.

- 

## Method Details

  - 

### values

public static Entities.EscapeMode[] values()
Returns an array containing the constants of this enum type, in
the order they are declared.

Returns:
an array containing the constants of this enum type, in the order they are declared

  - 

### valueOf

public static Entities.EscapeMode valueOf(String name)
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