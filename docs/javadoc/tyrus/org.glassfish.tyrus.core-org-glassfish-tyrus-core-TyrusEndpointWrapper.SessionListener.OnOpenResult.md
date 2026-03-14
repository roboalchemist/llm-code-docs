Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Enum Class TyrusEndpointWrapper.SessionListener.OnOpenResult

java.lang.Object
java.lang.Enum<TyrusEndpointWrapper.SessionListener.OnOpenResult>
org.glassfish.tyrus.core.TyrusEndpointWrapper.SessionListener.OnOpenResult

All Implemented Interfaces:
`Serializable`, `Comparable<TyrusEndpointWrapper.SessionListener.OnOpenResult>`, `Constable`

Enclosing class:
`TyrusEndpointWrapper.SessionListener`

---

public static enum TyrusEndpointWrapper.SessionListener.OnOpenResult
extends Enum<TyrusEndpointWrapper.SessionListener.OnOpenResult>
Result of `TyrusEndpointWrapper.SessionListener.onOpen(TyrusSession)`.

-

## Nested Class Summary

## Nested classes/interfaces inherited from class java.lang.Enum

`Enum.EnumDesc<E extends Enum<E>>`

-

## Enum Constant Summary

Enum Constants

Enum Constant
Description
`MAX_SESSIONS_PER_APP_EXCEEDED`

Session cannot be opened - the maximal number of open session per application exceeded.

`MAX_SESSIONS_PER_REMOTE_ADDR_EXCEEDED`

Session cannot be opened - the maximal number of open session per remote address exceeded.

`SESSION_ALLOWED`

Session can be opened.

-

## Method Summary

Modifier and Type
Method
Description
`static TyrusEndpointWrapper.SessionListener.OnOpenResult`
`valueOf(String name)`

Returns the enum constant of this class with the specified name.

`static TyrusEndpointWrapper.SessionListener.OnOpenResult[]`
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

### SESSION_ALLOWED

public static final TyrusEndpointWrapper.SessionListener.OnOpenResult SESSION_ALLOWED
Session can be opened.

-

### MAX_SESSIONS_PER_APP_EXCEEDED

public static final TyrusEndpointWrapper.SessionListener.OnOpenResult MAX_SESSIONS_PER_APP_EXCEEDED
Session cannot be opened - the maximal number of open session per application exceeded.

-

### MAX_SESSIONS_PER_REMOTE_ADDR_EXCEEDED

public static final TyrusEndpointWrapper.SessionListener.OnOpenResult MAX_SESSIONS_PER_REMOTE_ADDR_EXCEEDED
Session cannot be opened - the maximal number of open session per remote address exceeded.

-

## Method Details

-

### values

public static TyrusEndpointWrapper.SessionListener.OnOpenResult[] values()
Returns an array containing the constants of this enum class, in
the order they are declared.

Returns:
an array containing the constants of this enum class, in the order they are declared

-

### valueOf

public static TyrusEndpointWrapper.SessionListener.OnOpenResult valueOf(String name)
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
