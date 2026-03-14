# Class StandardToWebSocketExtensionAdapter

java.lang.Object
org.springframework.web.socket.WebSocketExtension
org.springframework.web.socket.adapter.standard.StandardToWebSocketExtensionAdapter

---

public class StandardToWebSocketExtensionAdapter
extends WebSocketExtension
A subclass of `WebSocketExtension` that can be constructed from a
`Extension`.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Constructor Summary

Constructors

Constructor
Description
`StandardToWebSocketExtensionAdapter(jakarta.websocket.Extension extension)`
 

- 

## Method Summary

### Methods inherited from class WebSocketExtension

`equals, getName, getParameters, hashCode, parseExtensions, toString`

### Methods inherited from class Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### StandardToWebSocketExtensionAdapter

public StandardToWebSocketExtensionAdapter(jakarta.websocket.Extension extension)