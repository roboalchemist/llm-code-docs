Package com.nimbusds.jose

# Enum JWSObjectJSON.State

java.lang.Object
java.lang.Enum<JWSObjectJSON.State>
com.nimbusds.jose.JWSObjectJSON.State

All Implemented Interfaces:
`Serializable`, `Comparable<JWSObjectJSON.State>`, `java.lang.constant.Constable`

Enclosing class:
JWSObjectJSON

---

public static enum JWSObjectJSON.State
extends Enum<JWSObjectJSON.State>
Enumeration of the states of a JSON Web Signature (JWS) secured
 object serialisable to JSON.

- 

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`

- 

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`SIGNED`

The object has one or more signatures; they are not (all)
 verified.

`UNSIGNED`

The object is not signed yet.

`VERIFIED`

All signatures are verified.

- 

## Method Summary

Modifier and Type
Method
Description
`static JWSObjectJSON.State`
`valueOf(String name)`

Returns the enum constant of this type with the specified name.

`static JWSObjectJSON.State[]`
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

### UNSIGNED

public static final JWSObjectJSON.State UNSIGNED
The object is not signed yet.

  - 

### SIGNED

public static final JWSObjectJSON.State SIGNED
The object has one or more signatures; they are not (all)
 verified.

  - 

### VERIFIED

public static final JWSObjectJSON.State VERIFIED
All signatures are verified.

- 

## Method Details

  - 

### values

public static JWSObjectJSON.State[] values()
Returns an array containing the constants of this enum type, in
the order they are declared.

Returns:
an array containing the constants of this enum type, in the order they are declared

  - 

### valueOf

public static JWSObjectJSON.State valueOf(String name)
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