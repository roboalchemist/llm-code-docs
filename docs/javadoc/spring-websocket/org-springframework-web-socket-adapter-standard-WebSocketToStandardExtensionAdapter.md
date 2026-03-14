# Class WebSocketToStandardExtensionAdapter

java.lang.Object
org.springframework.web.socket.adapter.standard.WebSocketToStandardExtensionAdapter

All Implemented Interfaces:
`jakarta.websocket.Extension`

---

public class WebSocketToStandardExtensionAdapter
extends Object
implements jakarta.websocket.Extension
Adapt an instance of `WebSocketExtension` to
the `Extension` interface.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Nested Class Summary

### Nested classes/interfaces inherited from interface jakarta.websocket.Extension

`jakarta.websocket.Extension.Parameter`

- 

## Constructor Summary

Constructors

Constructor
Description
`WebSocketToStandardExtensionAdapter(WebSocketExtension extension)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`String`
`getName()`
 
`List<jakarta.websocket.Extension.Parameter>`
`getParameters()`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### WebSocketToStandardExtensionAdapter

public WebSocketToStandardExtensionAdapter(WebSocketExtension extension)

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