# Class AbstractWebSocketClient

java.lang.Object
org.springframework.web.socket.client.AbstractWebSocketClient

All Implemented Interfaces:
`WebSocketClient`

Direct Known Subclasses:
`StandardWebSocketClient`

---

public abstract class AbstractWebSocketClient
extends Object
implements WebSocketClient
Abstract base class for `WebSocketClient` implementations.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`protected final org.apache.commons.logging.Log`
`logger`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`AbstractWebSocketClient()`
 

- 

## Method Summary

Modifier and Type
Method
Description
`protected void`
`assertUri(URI uri)`
 
`CompletableFuture<WebSocketSession>`
`execute(WebSocketHandler webSocketHandler,
 String uriTemplate,
 @Nullable Object... uriVars)`

Execute a handshake request to the given url and handle the resulting
WebSocket session with the given handler.

`final CompletableFuture<WebSocketSession>`
`execute(WebSocketHandler webSocketHandler,
 @Nullable WebSocketHttpHeaders headers,
 URI uri)`

Execute a handshake request to the given url and handle the resulting
WebSocket session with the given handler.

`protected abstract CompletableFuture<WebSocketSession>`
`executeInternal(WebSocketHandler webSocketHandler,
 org.springframework.http.HttpHeaders headers,
 URI uri,
 List<String> subProtocols,
 List<WebSocketExtension> extensions,
 Map<String,Object> attributes)`

Perform the actual handshake to establish a connection to the server.

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### logger

protected final org.apache.commons.logging.Log logger

- 

## Constructor Details

  - 

### AbstractWebSocketClient

public AbstractWebSocketClient()

- 

## Method Details

  - 

### execute

public CompletableFuture<WebSocketSession> execute(WebSocketHandler webSocketHandler,
 String uriTemplate,
 @Nullable Object... uriVars)
Description copied from interface: `WebSocketClient`
Execute a handshake request to the given url and handle the resulting
WebSocket session with the given handler.

Specified by:
`execute` in interface `WebSocketClient`
Parameters:
`webSocketHandler` - the session handler
`uriTemplate` - the url template
`uriVars` - the variables to expand the template
Returns:
a future that completes when the session is available

  - 

### execute

public final CompletableFuture<WebSocketSession> execute(WebSocketHandler webSocketHandler,
 @Nullable WebSocketHttpHeaders headers,
 URI uri)
Description copied from interface: `WebSocketClient`
Execute a handshake request to the given url and handle the resulting
WebSocket session with the given handler.

Specified by:
`execute` in interface `WebSocketClient`
Parameters:
`webSocketHandler` - the session handler
`uri` - the url
Returns:
a future that completes when the session is available

  - 

### assertUri

protected void assertUri(URI uri)

  - 

### executeInternal

protected abstract CompletableFuture<WebSocketSession> executeInternal(WebSocketHandler webSocketHandler,
 org.springframework.http.HttpHeaders headers,
 URI uri,
 List<String> subProtocols,
 List<WebSocketExtension> extensions,
 Map<String,Object> attributes)
Perform the actual handshake to establish a connection to the server.

Parameters:
`webSocketHandler` - the client-side handler for WebSocket messages
`headers` - the HTTP headers to use for the handshake, with unwanted (forbidden)
headers filtered out (never `null`)
`uri` - the target URI for the handshake (never `null`)
`subProtocols` - requested sub-protocols, or an empty list
`extensions` - requested WebSocket extensions, or an empty list
`attributes` - the attributes to associate with the WebSocketSession, i.e. via
`WebSocketSession.getAttributes()`; currently always an empty map
Returns:
the established WebSocket session wrapped in a `CompletableFuture`.