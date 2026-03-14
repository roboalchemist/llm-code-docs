# Class WebSocketExtension

java.lang.Object
org.springframework.web.socket.WebSocketExtension

Direct Known Subclasses:
`StandardToWebSocketExtensionAdapter`

---

public class WebSocketExtension
extends Object
Represents a WebSocket extension as defined in the RFC 6455.
WebSocket extensions add protocol features to the WebSocket protocol. The extensions
used within a session are negotiated during the handshake phase as follows:

- the client may ask for specific extensions in the HTTP handshake request

- the server responds with the final list of extensions to use in the current session

WebSocket Extension HTTP headers may include parameters and follow
RFC 7230 section 3.2

Note that the order of extensions in HTTP headers defines their order of execution,
for example, extensions "foo, bar" will be executed as "bar(foo(message))".

Since:
4.0
Author:
Brian Clozel, Juergen Hoeller
See Also:

- WebSocket Protocol Extensions, RFC 6455 - Section 9

- 

## Constructor Summary

Constructors

Constructor
Description
`WebSocketExtension(String name)`

Create a WebSocketExtension with the given name.

`WebSocketExtension(String name,
 @Nullable Map<String,String> parameters)`

Create a WebSocketExtension with the given name and parameters.

- 

## Method Summary

Modifier and Type
Method
Description
`boolean`
`equals(@Nullable Object other)`
 
`String`
`getName()`

Return the name of the extension (never `null` or empty).

`Map<String,String>`
`getParameters()`

Return the parameters of the extension (never `null`).

`int`
`hashCode()`
 
`static List<WebSocketExtension>`
`parseExtensions(String extensions)`

Parse the given, comma-separated string into a list of `WebSocketExtension` objects.

`String`
`toString()`
 

### Methods inherited from class Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### WebSocketExtension

public WebSocketExtension(String name)
Create a WebSocketExtension with the given name.

Parameters:
`name` - the name of the extension

  - 

### WebSocketExtension

public WebSocketExtension(String name,
 @Nullable Map<String,String> parameters)
Create a WebSocketExtension with the given name and parameters.

Parameters:
`name` - the name of the extension
`parameters` - the parameters

- 

## Method Details

  - 

### getName

public String getName()
Return the name of the extension (never `null` or empty).

  - 

### getParameters

public Map<String,String> getParameters()
Return the parameters of the extension (never `null`).

  - 

### equals

public boolean equals(@Nullable Object other)

Overrides:
`equals` in class `Object`

  - 

### hashCode

public int hashCode()

Overrides:
`hashCode` in class `Object`

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`

  - 

### parseExtensions

public static List<WebSocketExtension> parseExtensions(String extensions)
Parse the given, comma-separated string into a list of `WebSocketExtension` objects.

This method can be used to parse a "Sec-WebSocket-Extension" header.

Parameters:
`extensions` - the string to parse
Returns:
the list of extensions
Throws:
`IllegalArgumentException` - if the string cannot be parsed