Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class TyrusExtension.TyrusParameter

java.lang.Object
org.glassfish.tyrus.core.TyrusExtension.TyrusParameter

All Implemented Interfaces:
`jakarta.websocket.Extension.Parameter`, `Serializable`

Enclosing class:
`TyrusExtension`

---

public static class TyrusExtension.TyrusParameter
extends Object
implements jakarta.websocket.Extension.Parameter, Serializable
WebSocket `Extension.Parameter` implementation.

See Also:

- Serialized Form

-

## Constructor Summary

Constructors

Constructor
Description
`TyrusParameter(String name,
 String value)`

Create `Extension.Parameter` with name and value.

-

## Method Summary

Modifier and Type
Method
Description
`String`
`getName()`

`String`
`getValue()`

`String`
`toString()`

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

-

## Constructor Details

-

### TyrusParameter

public TyrusParameter(String name,
 String value)
Create `Extension.Parameter` with name and value.

Parameters:
`name` - parameter name.
`value` - parameter value.

-

## Method Details

-

### getName

public String getName()

Specified by:
`getName` in interface `jakarta.websocket.Extension.Parameter`

-

### getValue

public String getValue()

Specified by:
`getValue` in interface `jakarta.websocket.Extension.Parameter`

-

### toString

public String toString()

Overrides:
`toString` in class `Object`
