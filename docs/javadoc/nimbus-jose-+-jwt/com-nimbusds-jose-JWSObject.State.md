Package com.nimbusds.jose

# Enum JWSObject.State

java.lang.Object
java.lang.Enum<JWSObject.State>
com.nimbusds.jose.JWSObject.State

All Implemented Interfaces:
`Serializable`, `Comparable<JWSObject.State>`, `java.lang.constant.Constable`

Enclosing class:
JWSObject

---

public static enum JWSObject.State
extends Enum<JWSObject.State>
Enumeration of the states of a JSON Web Signature (JWS) secured
 object.

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

The JWS secured object is signed but its signature is not
 verified.

`UNSIGNED`

The object is not signed yet.

`VERIFIED`

The JWS secured object is signed and its signature was
 successfully verified.

- 

## Method Summary

Modifier and Type
Method
Description
`static JWSObject.State`
`valueOf(String name)`

Returns the enum constant of this type with the specified name.

`static JWSObject.State[]`
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

public static final JWSObject.State UNSIGNED
The object is not signed yet.

  - 

### SIGNED

public static final JWSObject.State SIGNED
The JWS secured object is signed but its signature is not
 verified.

  - 

### VERIFIED

public static final JWSObject.State VERIFIED
The JWS secured object is signed and its signature was
 successfully verified.

- 

## Method Details

  - 

### values

public static JWSObject.State[] values()
Returns an array containing the constants of this enum type, in
the order they are declared.

Returns:
an array containing the constants of this enum type, in the order they are declared

  - 

### valueOf

public static JWSObject.State valueOf(String name)
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