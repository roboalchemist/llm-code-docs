Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Enum Class DebugContext.TracingType

java.lang.Object
java.lang.Enum<DebugContext.TracingType>
org.glassfish.tyrus.core.DebugContext.TracingType

All Implemented Interfaces:
`Serializable`, `Comparable<DebugContext.TracingType>`, `Constable`

Enclosing class:
`DebugContext`

---

public static enum DebugContext.TracingType
extends Enum<DebugContext.TracingType>
Type of tracing - used for tracing configuration.

-

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`

-

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`ALL`

Tracing headers will be present in all handshake responses.

`OFF`

No tracing headers will be ever sent in handshake response.

`ON_DEMAND`

Tracing headers will be sent in handshake response only if X-Tyrus-Tracing-Accept header is present
 in handshake request.

-

## Method Summary

Modifier and Type
Method
Description
`static DebugContext.TracingType`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static DebugContext.TracingType[]`
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

### OFF

public static final DebugContext.TracingType OFF
No tracing headers will be ever sent in handshake response.

-

### ON_DEMAND

public static final DebugContext.TracingType ON_DEMAND
Tracing headers will be sent in handshake response only if X-Tyrus-Tracing-Accept header is present
 in handshake request.

-

### ALL

public static final DebugContext.TracingType ALL
Tracing headers will be present in all handshake responses.

-

## Method Details

-

### values

public static DebugContext.TracingType[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared

-

### valueOf

public static DebugContext.TracingType valueOf(String name)
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
