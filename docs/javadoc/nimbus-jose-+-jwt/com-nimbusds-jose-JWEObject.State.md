Package com.nimbusds.jose

# Enum JWEObject.State

java.lang.Object
java.lang.Enum<JWEObject.State>
com.nimbusds.jose.JWEObject.State

All Implemented Interfaces:
`Serializable`, `Comparable<JWEObject.State>`, `java.lang.constant.Constable`

Enclosing class:
JWEObject

---

public static enum JWEObject.State
extends Enum<JWEObject.State>
Enumeration of the states of a JSON Web Encryption (JWE) secured
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
`DECRYPTED`

The JWE secured object is decrypted.

`ENCRYPTED`

The JWE secured object is encrypted.

`UNENCRYPTED`

The JWE secured object is created but not encrypted yet.

- 

## Method Summary

Modifier and Type
Method
Description
`static JWEObject.State`
`valueOf(String name)`

Returns the enum constant of this type with the specified name.

`static JWEObject.State[]`
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

### UNENCRYPTED

public static final JWEObject.State UNENCRYPTED
The JWE secured object is created but not encrypted yet.

  - 

### ENCRYPTED

public static final JWEObject.State ENCRYPTED
The JWE secured object is encrypted.

  - 

### DECRYPTED

public static final JWEObject.State DECRYPTED
The JWE secured object is decrypted.

- 

## Method Details

  - 

### values

public static JWEObject.State[] values()
Returns an array containing the constants of this enum type, in
the order they are declared.

Returns:
an array containing the constants of this enum type, in the order they are declared

  - 

### valueOf

public static JWEObject.State valueOf(String name)
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