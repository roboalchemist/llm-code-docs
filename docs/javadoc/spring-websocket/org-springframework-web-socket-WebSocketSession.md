# Interface WebSocketSession

All Superinterfaces:
`AutoCloseable, Closeable`

All Known Subinterfaces:
`NativeWebSocketSession, SockJsSession`

All Known Implementing Classes:
`AbstractClientSockJsSession, AbstractHttpSockJsSession, AbstractSockJsSession, AbstractWebSocketSession, ConcurrentWebSocketSessionDecorator, JettyWebSocketSession, PollingSockJsSession, StandardWebSocketSession, StreamingSockJsSession, WebSocketClientSockJsSession, WebSocketServerSockJsSession, WebSocketSessionDecorator, XhrClientSockJsSession`

---

public interface WebSocketSession
extends Closeable
A WebSocket session abstraction. Allows sending messages over a WebSocket
connection and closing it.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`close()`

Close the WebSocket connection with status 1000, i.e.

`void`
`close(CloseStatus status)`

Close the WebSocket connection with the given close status.

`@Nullable String`
`getAcceptedProtocol()`

Return the negotiated sub-protocol.

`Map<String,Object>`
`getAttributes()`

Return the map with attributes associated with the WebSocket session.

`int`
`getBinaryMessageSizeLimit()`

Get the configured maximum size for an incoming binary message.

`List<WebSocketExtension>`
`getExtensions()`

Determine the negotiated extensions.

`org.springframework.http.HttpHeaders`
`getHandshakeHeaders()`

Return the headers used in the handshake request (never `null`).

`String`
`getId()`

Return a unique session identifier.

`@Nullable InetSocketAddress`
`getLocalAddress()`

Return the address on which the request was received.

`@Nullable Principal`
`getPrincipal()`

Return a `Principal` instance containing the name
of the authenticated user.

`@Nullable InetSocketAddress`
`getRemoteAddress()`

Return the address of the remote client.

`int`
`getTextMessageSizeLimit()`

Get the configured maximum size for an incoming text message.

`@Nullable URI`
`getUri()`

Return the URI used to open the WebSocket connection.

`boolean`
`isOpen()`

Whether the underlying connection is open.

`void`
`sendMessage(WebSocketMessage<?> message)`

Send a WebSocket message: either `TextMessage` or `BinaryMessage`.

`void`
`setBinaryMessageSizeLimit(int messageSizeLimit)`

Configure the maximum size for an incoming binary message.

`void`
`setTextMessageSizeLimit(int messageSizeLimit)`

Configure the maximum size for an incoming text message.

- 

## Method Details

  - 

### getId

String getId()
Return a unique session identifier.

  - 

### getUri

@Nullable URI getUri()
Return the URI used to open the WebSocket connection.

  - 

### getHandshakeHeaders

org.springframework.http.HttpHeaders getHandshakeHeaders()
Return the headers used in the handshake request (never `null`).

  - 

### getAttributes

Map<String,Object> getAttributes()
Return the map with attributes associated with the WebSocket session.

On the server side the map can be populated initially through a
`HandshakeInterceptor`. On the client side the map can be populated via
`WebSocketClient` handshake methods.

Returns:
a Map with the session attributes (never `null`)

  - 

### getPrincipal

@Nullable Principal getPrincipal()
Return a `Principal` instance containing the name
of the authenticated user.

If the user has not been authenticated, the method returns `null`.

  - 

### getLocalAddress

@Nullable InetSocketAddress getLocalAddress()
Return the address on which the request was received.

**Note:** The localAddress is not always possible to access,
which is the case with the Standard WebSocket client API, and accordingly
`StandardWebSocketClient`
returns `null`.

  - 

### getRemoteAddress

@Nullable InetSocketAddress getRemoteAddress()
Return the address of the remote client.

  - 

### getAcceptedProtocol

@Nullable String getAcceptedProtocol()
Return the negotiated sub-protocol.

Returns:
the protocol identifier, or `null` if no protocol
was specified or negotiated successfully

  - 

### setTextMessageSizeLimit

void setTextMessageSizeLimit(int messageSizeLimit)
Configure the maximum size for an incoming text message.

  - 

### getTextMessageSizeLimit

int getTextMessageSizeLimit()
Get the configured maximum size for an incoming text message.

  - 

### setBinaryMessageSizeLimit

void setBinaryMessageSizeLimit(int messageSizeLimit)
Configure the maximum size for an incoming binary message.

  - 

### getBinaryMessageSizeLimit

int getBinaryMessageSizeLimit()
Get the configured maximum size for an incoming binary message.

  - 

### getExtensions

List<WebSocketExtension> getExtensions()
Determine the negotiated extensions.

Returns:
the list of extensions, or an empty list if no extension
was specified or negotiated successfully

  - 

### sendMessage

void sendMessage(WebSocketMessage<?> message)
          throws IOException
Send a WebSocket message: either `TextMessage` or `BinaryMessage`.

**Note:** The underlying standard WebSocket session (JSR-356) does
not allow concurrent sending. Therefore, sending must be synchronized. To ensure
that, one option is to wrap the `WebSocketSession` with the
`ConcurrentWebSocketSessionDecorator`.

Throws:
`IOException`
See Also:

    - `ConcurrentWebSocketSessionDecorator`

  - 

### isOpen

boolean isOpen()
Whether the underlying connection is open.

  - 

### close

void close()
    throws IOException
Close the WebSocket connection with status 1000, i.e. equivalent to:

```

session.close(CloseStatus.NORMAL);

```

Specified by:
`close` in interface `AutoCloseable`
Specified by:
`close` in interface `Closeable`
Throws:
`IOException`

  - 

### close

void close(CloseStatus status)
    throws IOException
Close the WebSocket connection with the given close status.

Throws:
`IOException`