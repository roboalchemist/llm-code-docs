# Class WebSocketConnectionManager

java.lang.Object
org.springframework.web.socket.client.ConnectionManagerSupport
org.springframework.web.socket.client.WebSocketConnectionManager

All Implemented Interfaces:
`org.springframework.context.Lifecycle, org.springframework.context.Phased, org.springframework.context.SmartLifecycle`

---

public class WebSocketConnectionManager
extends ConnectionManagerSupport
WebSocket `connection manager` that connects
to the server via `WebSocketClient` and handles the session with a
`WebSocketHandler`.

Since:
4.0
Author:
Rossen Stoyanchev, Sam Brannen

- 

## Field Summary

### Fields inherited from class ConnectionManagerSupport

`logger`

### Fields inherited from interface org.springframework.context.SmartLifecycle

`DEFAULT_PHASE`

- 

## Constructor Summary

Constructors

Constructor
Description
`WebSocketConnectionManager(WebSocketClient client,
 WebSocketHandler webSocketHandler,
 String uriTemplate,
 @Nullable Object... uriVariables)`

Constructor with the client to use and a handler to handle messages with.

`WebSocketConnectionManager(WebSocketClient client,
 WebSocketHandler webSocketHandler,
 URI uri)`

Variant of `WebSocketConnectionManager(WebSocketClient, WebSocketHandler, String, Object...)`
with a prepared `URI`.

- 

## Method Summary

Modifier and Type
Method
Description
`protected void`
`closeConnection()`

Subclasses implement this to close the connection.

`protected WebSocketHandler`
`decorateWebSocketHandler(WebSocketHandler handler)`

Decorate the WebSocketHandler provided to the class constructor.

`org.springframework.http.HttpHeaders`
`getHeaders()`

Return the default headers for the WebSocket handshake request.

`@Nullable String`
`getOrigin()`

Return the configured origin.

`List<String>`
`getSubProtocols()`

Return the configured sub-protocols to use.

`boolean`
`isConnected()`

Whether the connection is open/`true` or closed/`false`.

`protected void`
`openConnection()`

Subclasses implement this to actually establish the connection.

`void`
`setHeaders(org.springframework.http.HttpHeaders headers)`

Provide default headers to add to the WebSocket handshake request.

`void`
`setOrigin(@Nullable String origin)`

Set the origin to use.

`void`
`setSubProtocols(List<String> protocols)`

Set the sub-protocols to use.

`void`
`startInternal()`
 
`void`
`stopInternal()`
 

### Methods inherited from class ConnectionManagerSupport

`getPhase, getUri, isAutoStartup, isRunning, setAutoStartup, setPhase, start, stop, stop`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface org.springframework.context.SmartLifecycle

`isPauseable`

- 

## Constructor Details

  - 

### WebSocketConnectionManager

public WebSocketConnectionManager(WebSocketClient client,
 WebSocketHandler webSocketHandler,
 String uriTemplate,
 @Nullable Object... uriVariables)
Constructor with the client to use and a handler to handle messages with.

  - 

### WebSocketConnectionManager

public WebSocketConnectionManager(WebSocketClient client,
 WebSocketHandler webSocketHandler,
 URI uri)
Variant of `WebSocketConnectionManager(WebSocketClient, WebSocketHandler, String, Object...)`
with a prepared `URI`.

Since:
6.0.5

- 

## Method Details

  - 

### setSubProtocols

public void setSubProtocols(List<String> protocols)
Set the sub-protocols to use. If configured, specified sub-protocols will be
requested in the handshake through the `Sec-WebSocket-Protocol` header. The
resulting WebSocket session will contain the protocol accepted by the server, if
any.

  - 

### getSubProtocols

public List<String> getSubProtocols()
Return the configured sub-protocols to use.

  - 

### setOrigin

public void setOrigin(@Nullable String origin)
Set the origin to use.

  - 

### getOrigin

public @Nullable String getOrigin()
Return the configured origin.

  - 

### setHeaders

public void setHeaders(org.springframework.http.HttpHeaders headers)
Provide default headers to add to the WebSocket handshake request.

  - 

### getHeaders

public org.springframework.http.HttpHeaders getHeaders()
Return the default headers for the WebSocket handshake request.

  - 

### startInternal

public void startInternal()

Overrides:
`startInternal` in class `ConnectionManagerSupport`

  - 

### stopInternal

public void stopInternal()
                  throws Exception

Overrides:
`stopInternal` in class `ConnectionManagerSupport`
Throws:
`Exception`

  - 

### isConnected

public boolean isConnected()
Description copied from class: `ConnectionManagerSupport`
Whether the connection is open/`true` or closed/`false`.

Specified by:
`isConnected` in class `ConnectionManagerSupport`

  - 

### openConnection

protected void openConnection()
Description copied from class: `ConnectionManagerSupport`
Subclasses implement this to actually establish the connection.

Specified by:
`openConnection` in class `ConnectionManagerSupport`

  - 

### closeConnection

protected void closeConnection()
                        throws Exception
Description copied from class: `ConnectionManagerSupport`
Subclasses implement this to close the connection.

Specified by:
`closeConnection` in class `ConnectionManagerSupport`
Throws:
`Exception`

  - 

### decorateWebSocketHandler

protected WebSocketHandler decorateWebSocketHandler(WebSocketHandler handler)
Decorate the WebSocketHandler provided to the class constructor.

By default `LoggingWebSocketHandlerDecorator` is added.