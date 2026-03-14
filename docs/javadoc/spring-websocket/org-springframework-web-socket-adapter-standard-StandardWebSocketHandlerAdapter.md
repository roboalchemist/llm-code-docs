# Class StandardWebSocketHandlerAdapter

java.lang.Object
jakarta.websocket.Endpoint
org.springframework.web.socket.adapter.standard.StandardWebSocketHandlerAdapter

---

public class StandardWebSocketHandlerAdapter
extends jakarta.websocket.Endpoint
Adapts a `WebSocketHandler` to the standard WebSocket for Java API.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Constructor Summary

Constructors

Constructor
Description
`StandardWebSocketHandlerAdapter(WebSocketHandler handler,
 StandardWebSocketSession wsSession)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`onClose(jakarta.websocket.Session session,
 jakarta.websocket.CloseReason reason)`
 
`void`
`onError(jakarta.websocket.Session session,
 Throwable exception)`
 
`void`
`onOpen(jakarta.websocket.Session session,
 jakarta.websocket.EndpointConfig config)`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### StandardWebSocketHandlerAdapter

public StandardWebSocketHandlerAdapter(WebSocketHandler handler,
 StandardWebSocketSession wsSession)

- 

## Method Details

  - 

### onOpen

public void onOpen(jakarta.websocket.Session session,
 jakarta.websocket.EndpointConfig config)

Specified by:
`onOpen` in class `jakarta.websocket.Endpoint`

  - 

### onClose

public void onClose(jakarta.websocket.Session session,
 jakarta.websocket.CloseReason reason)

Overrides:
`onClose` in class `jakarta.websocket.Endpoint`

  - 

### onError

public void onError(jakarta.websocket.Session session,
 Throwable exception)

Overrides:
`onError` in class `jakarta.websocket.Endpoint`