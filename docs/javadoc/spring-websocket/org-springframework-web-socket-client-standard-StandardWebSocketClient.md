# Class StandardWebSocketClient

java.lang.Object
org.springframework.web.socket.client.AbstractWebSocketClient
org.springframework.web.socket.client.standard.StandardWebSocketClient

All Implemented Interfaces:
`WebSocketClient`

---

public class StandardWebSocketClient
extends AbstractWebSocketClient
A WebSocketClient based on the standard Jakarta WebSocket API.

Since:
4.0
Author:
Rossen Stoyanchev, Juergen Hoeller

- 

## Field Summary

### Fields inherited from class AbstractWebSocketClient

`logger`

- 

## Constructor Summary

Constructors

Constructor
Description
`StandardWebSocketClient()`

Default constructor that calls `ContainerProvider.getWebSocketContainer()`
to obtain a (new) `WebSocketContainer` instance.

`StandardWebSocketClient(jakarta.websocket.WebSocketContainer webSocketContainer)`

Constructor accepting an existing `WebSocketContainer` instance.

- 

## Method Summary

Modifier and Type
Method
Description
`protected CompletableFuture<WebSocketSession>`
`executeInternal(WebSocketHandler webSocketHandler,
 org.springframework.http.HttpHeaders headers,
 URI uri,
 List<String> protocols,
 List<WebSocketExtension> extensions,
 Map<String,Object> attributes)`

Perform the actual handshake to establish a connection to the server.

`@Nullable SSLContext`
`getSslContext()`

Return the `SSLContext` to use.

`@Nullable org.springframework.core.task.AsyncTaskExecutor`
`getTaskExecutor()`

Return the configured `AsyncTaskExecutor`.

`Map<String,Object>`
`getUserProperties()`

Return the configured user properties.

`void`
`setSslContext(@Nullable SSLContext sslContext)`

Set the `SSLContext` to use for `ClientEndpointConfig.getSSLContext()`.

`void`
`setTaskExecutor(@Nullable org.springframework.core.task.AsyncTaskExecutor taskExecutor)`

Set an `AsyncTaskExecutor` to use when opening connections.

`void`
`setUserProperties(@Nullable Map<String,Object> userProperties)`

The standard Jakarta WebSocket API allows passing "user properties" to the
server via `userProperties`.

### Methods inherited from class AbstractWebSocketClient

`assertUri, execute, execute`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Constructor Details

  - 

### StandardWebSocketClient

public StandardWebSocketClient()
Default constructor that calls `ContainerProvider.getWebSocketContainer()`
to obtain a (new) `WebSocketContainer` instance. Also see constructor
accepting existing `WebSocketContainer` instance.

  - 

### StandardWebSocketClient

public StandardWebSocketClient(jakarta.websocket.WebSocketContainer webSocketContainer)
Constructor accepting an existing `WebSocketContainer` instance.

For XML configuration, see `WebSocketContainerFactoryBean`. For Java
configuration, use `ContainerProvider.getWebSocketContainer()` to obtain
the `WebSocketContainer` instance.

- 

## Method Details

  - 

### setUserProperties

public void setUserProperties(@Nullable Map<String,Object> userProperties)
The standard Jakarta WebSocket API allows passing "user properties" to the
server via `userProperties`.
Use this property to configure one or more properties to be passed on
every handshake.

  - 

### getUserProperties

public Map<String,Object> getUserProperties()
Return the configured user properties.

  - 

### setSslContext

public void setSslContext(@Nullable SSLContext sslContext)
Set the `SSLContext` to use for `ClientEndpointConfig.getSSLContext()`.

Since:
6.1.3

  - 

### getSslContext

public @Nullable SSLContext getSslContext()
Return the `SSLContext` to use.

Since:
6.1.3

  - 

### setTaskExecutor

public void setTaskExecutor(@Nullable org.springframework.core.task.AsyncTaskExecutor taskExecutor)
Set an `AsyncTaskExecutor` to use when opening connections.

If this property is set to `null`, calls to any of the
`doHandshake` methods will block until the connection is established.

By default, an instance of `SimpleAsyncTaskExecutor` is used.

  - 

### getTaskExecutor

public @Nullable org.springframework.core.task.AsyncTaskExecutor getTaskExecutor()
Return the configured `AsyncTaskExecutor`.

  - 

### executeInternal

protected CompletableFuture<WebSocketSession> executeInternal(WebSocketHandler webSocketHandler,
 org.springframework.http.HttpHeaders headers,
 URI uri,
 List<String> protocols,
 List<WebSocketExtension> extensions,
 Map<String,Object> attributes)
Description copied from class: `AbstractWebSocketClient`
Perform the actual handshake to establish a connection to the server.

Specified by:
`executeInternal` in class `AbstractWebSocketClient`
Parameters:
`webSocketHandler` - the client-side handler for WebSocket messages
`headers` - the HTTP headers to use for the handshake, with unwanted (forbidden)
headers filtered out (never `null`)
`uri` - the target URI for the handshake (never `null`)
`protocols` - requested sub-protocols, or an empty list
`extensions` - requested WebSocket extensions, or an empty list
`attributes` - the attributes to associate with the WebSocketSession, i.e. via
`WebSocketSession.getAttributes()`; currently always an empty map
Returns:
the established WebSocket session wrapped in a `CompletableFuture`.