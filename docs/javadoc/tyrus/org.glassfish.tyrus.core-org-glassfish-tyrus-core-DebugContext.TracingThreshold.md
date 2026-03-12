Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Enum Class DebugContext.TracingThreshold

java.lang.Object
java.lang.Enum<DebugContext.TracingThreshold>
org.glassfish.tyrus.core.DebugContext.TracingThreshold

All Implemented Interfaces:
`Serializable`, `Comparable<DebugContext.TracingThreshold>`, `Constable`

Enclosing class:
`DebugContext`

---

public static enum DebugContext.TracingThreshold
extends Enum<DebugContext.TracingThreshold>
Tracing threshold - used for configuration granularity of information that will be sent in tracing headers.

-

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`

-

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`SUMMARY`

A less verbose tracing, an equivalent to `Level.FINER` logging level.

`TRACE`

A more verbose tracing, an equivalent to `Level.FINE` logging level.

-

## Method Summary

Modifier and Type
Method
Description
`static DebugContext.TracingThreshold`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static DebugContext.TracingThreshold[]`
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

### SUMMARY

public static final DebugContext.TracingThreshold SUMMARY
A less verbose tracing, an equivalent to `Level.FINER` logging level.

-

### TRACE

public static final DebugContext.TracingThreshold TRACE
A more verbose tracing, an equivalent to `Level.FINE` logging level.

 The default tracing threshold.

-

## Method Details

-

### values

public static DebugContext.TracingThreshold[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared

-

### valueOf

public static DebugContext.TracingThreshold valueOf(String name)
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
