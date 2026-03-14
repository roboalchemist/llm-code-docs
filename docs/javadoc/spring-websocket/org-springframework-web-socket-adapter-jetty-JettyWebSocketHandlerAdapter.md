# Class JettyWebSocketHandlerAdapter

java.lang.Object
org.springframework.web.socket.adapter.jetty.JettyWebSocketHandlerAdapter

All Implemented Interfaces:
`org.eclipse.jetty.websocket.api.Session.Listener`

---

public class JettyWebSocketHandlerAdapter
extends Object
implements org.eclipse.jetty.websocket.api.Session.Listener
Adapts `WebSocketHandler` to the Jetty WebSocket API `Session.Listener`.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Nested Class Summary

### Nested classes/interfaces inherited from interface org.eclipse.jetty.websocket.api.Session.Listener

`org.eclipse.jetty.websocket.api.Session.Listener.Abstract, org.eclipse.jetty.websocket.api.Session.Listener.AbstractAutoDemanding, org.eclipse.jetty.websocket.api.Session.Listener.AutoDemanding`

- 

## Constructor Summary

Constructors

Constructor
Description
`JettyWebSocketHandlerAdapter(WebSocketHandler webSocketHandler,
 JettyWebSocketSession wsSession)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`onWebSocketBinary(ByteBuffer payload,
 org.eclipse.jetty.websocket.api.Callback callback)`
 
`void`
`onWebSocketClose(int statusCode,
 String reason,
 org.eclipse.jetty.websocket.api.Callback callback)`
 
`void`
`onWebSocketError(Throwable cause)`
 
`void`
`onWebSocketOpen(org.eclipse.jetty.websocket.api.Session session)`
 
`void`
`onWebSocketPong(ByteBuffer payload)`
 
`void`
`onWebSocketText(String payload)`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface org.eclipse.jetty.websocket.api.Session.Listener

`onWebSocketClose, onWebSocketFrame, onWebSocketPartialBinary, onWebSocketPartialText, onWebSocketPing`

- 

## Constructor Details

  - 

### JettyWebSocketHandlerAdapter

public JettyWebSocketHandlerAdapter(WebSocketHandler webSocketHandler,
 JettyWebSocketSession wsSession)

- 

## Method Details

  - 

### onWebSocketOpen

public void onWebSocketOpen(org.eclipse.jetty.websocket.api.Session session)

Specified by:
`onWebSocketOpen` in interface `org.eclipse.jetty.websocket.api.Session.Listener`

  - 

### onWebSocketText

public void onWebSocketText(String payload)

Specified by:
`onWebSocketText` in interface `org.eclipse.jetty.websocket.api.Session.Listener`

  - 

### onWebSocketBinary

public void onWebSocketBinary(ByteBuffer payload,
 org.eclipse.jetty.websocket.api.Callback callback)

Specified by:
`onWebSocketBinary` in interface `org.eclipse.jetty.websocket.api.Session.Listener`

  - 

### onWebSocketPong

public void onWebSocketPong(ByteBuffer payload)

Specified by:
`onWebSocketPong` in interface `org.eclipse.jetty.websocket.api.Session.Listener`

  - 

### onWebSocketClose

public void onWebSocketClose(int statusCode,
 String reason,
 org.eclipse.jetty.websocket.api.Callback callback)

Specified by:
`onWebSocketClose` in interface `org.eclipse.jetty.websocket.api.Session.Listener`

  - 

### onWebSocketError

public void onWebSocketError(Throwable cause)

Specified by:
`onWebSocketError` in interface `org.eclipse.jetty.websocket.api.Session.Listener`