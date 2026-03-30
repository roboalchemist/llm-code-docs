Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class TyrusExtension

java.lang.Object
org.glassfish.tyrus.core.TyrusExtension

All Implemented Interfaces:
`jakarta.websocket.Extension`, `Serializable`

---

public class TyrusExtension
extends Object
implements jakarta.websocket.Extension, Serializable
WebSocket `Extension` implementation.

Author:
Pavel Bucek
See Also:

- Serialized Form

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static class`
`TyrusExtension.TyrusParameter`

WebSocket `Extension.Parameter` implementation.

## Nested classes/interfaces inherited from interface jakarta.websocket.Extension

`jakarta.websocket.Extension.Parameter`

-

## Constructor Summary

Constructors

Constructor
Description
`TyrusExtension(String name)`

Create `Extension` with specific name.

`TyrusExtension(String name,
 List<jakarta.websocket.Extension.Parameter> parameters)`

Create `Extension` with name and parameters.

-

## Method Summary

Modifier and Type
Method
Description
`boolean`
`equals(Object o)`

`static List<jakarta.websocket.Extension>`
`fromHeaders(List<String> extensionHeaders)`

Parse `Extension` from headers (represented as `List` of strings).

`static List<jakarta.websocket.Extension>`
`fromString(List<String> s)`

Parsing of one `Extension`.

`String`
`getName()`

`List<jakarta.websocket.Extension.Parameter>`
`getParameters()`

`int`
`hashCode()`

`String`
`toString()`

### Methods inherited from class java.lang.Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

-

## Constructor Details

-

### TyrusExtension

public TyrusExtension(String name)
Create `Extension` with specific name.

Parameters:
`name` - extension name.
Throws:
`IllegalArgumentException` - when name is null or empty string.

-

### TyrusExtension

public TyrusExtension(String name,
 List<jakarta.websocket.Extension.Parameter> parameters)
Create `Extension` with name and parameters.

Parameters:
`name` - extension name.
`parameters` - extension parameters.

-

## Method Details

-

### getName

public String getName()

Specified by:
`getName` in interface `jakarta.websocket.Extension`

-

### getParameters

public List<jakarta.websocket.Extension.Parameter> getParameters()

Specified by:
`getParameters` in interface `jakarta.websocket.Extension`

-

### toString

public String toString()

Overrides:
`toString` in class `Object`

-

### equals

public boolean equals(Object o)

Overrides:
`equals` in class `Object`

-

### hashCode

public int hashCode()

Overrides:
`hashCode` in class `Object`

-

### fromString

public static List<jakarta.websocket.Extension> fromString(List<String> s)
Parsing of one `Extension`.

Parameters:
`s` - `List` of `String` containing `Extensions`.
Returns:
List of extensions represented as `TyrusExtension`.

-

### fromHeaders

public static List<jakarta.websocket.Extension> fromHeaders(List<String> extensionHeaders)
Parse `Extension` from headers (represented as `List` of strings).

Parameters:
`extensionHeaders` - Http Extension headers.
Returns:
list of parsed `Extensions`.
