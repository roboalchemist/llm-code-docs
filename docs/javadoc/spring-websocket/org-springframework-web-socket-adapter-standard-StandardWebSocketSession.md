# Class StandardWebSocketSession

java.lang.Object
org.springframework.web.socket.adapter.AbstractWebSocketSession<jakarta.websocket.Session>
org.springframework.web.socket.adapter.standard.StandardWebSocketSession

All Implemented Interfaces:
`Closeable, AutoCloseable, NativeWebSocketSession, WebSocketSession`

---

public class StandardWebSocketSession
extends AbstractWebSocketSession<jakarta.websocket.Session>
A `WebSocketSession` for use with the standard WebSocket for Java API.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Field Summary

### Fields inherited from class AbstractWebSocketSession

`idGenerator, logger`

- 

## Constructor Summary

Constructors

Constructor
Description
`StandardWebSocketSession(@Nullable org.springframework.http.HttpHeaders headers,
 @Nullable Map<String,Object> attributes,
 @Nullable InetSocketAddress localAddress,
 @Nullable InetSocketAddress remoteAddress)`

Constructor for a standard WebSocket session.

`StandardWebSocketSession(@Nullable org.springframework.http.HttpHeaders headers,
 @Nullable Map<String,Object> attributes,
 @Nullable InetSocketAddress localAddress,
 @Nullable InetSocketAddress remoteAddress,
 @Nullable Principal user)`

Constructor that associates a user with the WebSocket session.

- 

## Method Summary

Modifier and Type
Method
Description
`protected void`
`closeInternal(CloseStatus status)`
 
`@Nullable String`
`getAcceptedProtocol()`

Return the negotiated sub-protocol.

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

`void`
`initializeNativeSession(jakarta.websocket.Session session)`
 
`boolean`
`isOpen()`

Whether the underlying connection is open.

`protected void`
`sendBinaryMessage(BinaryMessage message)`
 
`protected void`
`sendPingMessage(PingMessage message)`
 
`protected void`
`sendPongMessage(PongMessage message)`
 
`protected void`
`sendTextMessage(TextMessage message)`
 
`void`
`setBinaryMessageSizeLimit(int messageSizeLimit)`

Configure the maximum size for an incoming binary message.

`void`
`setTextMessageSizeLimit(int messageSizeLimit)`

Configure the maximum size for an incoming text message.

### Methods inherited from class AbstractWebSocketSession

`checkNativeSessionInitialized, close, close, getAttributes, getNativeSession, getNativeSession, sendMessage, toString`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### StandardWebSocketSession

public StandardWebSocketSession(@Nullable org.springframework.http.HttpHeaders headers,
 @Nullable Map<String,Object> attributes,
 @Nullable InetSocketAddress localAddress,
 @Nullable InetSocketAddress remoteAddress)
Constructor for a standard WebSocket session.

Parameters:
`headers` - the headers of the handshake request
`attributes` - the attributes from the HTTP handshake to associate with the WebSocket
session; the provided attributes are copied, the original map is not used.
`localAddress` - the address on which the request was received
`remoteAddress` - the address of the remote client

  - 

### StandardWebSocketSession

public StandardWebSocketSession(@Nullable org.springframework.http.HttpHeaders headers,
 @Nullable Map<String,Object> attributes,
 @Nullable InetSocketAddress localAddress,
 @Nullable InetSocketAddress remoteAddress,
 @Nullable Principal user)
Constructor that associates a user with the WebSocket session.

Parameters:
`headers` - the headers of the handshake request
`attributes` - the attributes from the HTTP handshake to associate with the WebSocket session
`localAddress` - the address on which the request was received
`remoteAddress` - the address of the remote client
`user` - the user associated with the session; if `null` we'll
fall back on the user available in the underlying WebSocket session

- 

## Method Details

  - 

### getId

public String getId()
Description copied from interface: `WebSocketSession`
Return a unique session identifier.

  - 

### getUri

public @Nullable URI getUri()
Description copied from interface: `WebSocketSession`
Return the URI used to open the WebSocket connection.

  - 

### getHandshakeHeaders

public org.springframework.http.HttpHeaders getHandshakeHeaders()
Description copied from interface: `WebSocketSession`
Return the headers used in the handshake request (never `null`).

  - 

### getAcceptedProtocol

public @Nullable String getAcceptedProtocol()
Description copied from interface: `WebSocketSession`
Return the negotiated sub-protocol.

Returns:
the protocol identifier, or `null` if no protocol
was specified or negotiated successfully

  - 

### getExtensions

public List<WebSocketExtension> getExtensions()
Description copied from interface: `WebSocketSession`
Determine the negotiated extensions.

Returns:
the list of extensions, or an empty list if no extension
was specified or negotiated successfully

  - 

### getPrincipal

public @Nullable Principal getPrincipal()
Description copied from interface: `WebSocketSession`
Return a `Principal` instance containing the name
of the authenticated user.

If the user has not been authenticated, the method returns `null`.

  - 

### getLocalAddress

public @Nullable InetSocketAddress getLocalAddress()
Description copied from interface: `WebSocketSession`
Return the address on which the request was received.

**Note:** The localAddress is not always possible to access,
which is the case with the Standard WebSocket client API, and accordingly
`StandardWebSocketClient`
returns `null`.

  - 

### getRemoteAddress

public @Nullable InetSocketAddress getRemoteAddress()
Description copied from interface: `WebSocketSession`
Return the address of the remote client.

  - 

### setTextMessageSizeLimit

public void setTextMessageSizeLimit(int messageSizeLimit)
Description copied from interface: `WebSocketSession`
Configure the maximum size for an incoming text message.

  - 

### getTextMessageSizeLimit

public int getTextMessageSizeLimit()
Description copied from interface: `WebSocketSession`
Get the configured maximum size for an incoming text message.

  - 

### setBinaryMessageSizeLimit

public void setBinaryMessageSizeLimit(int messageSizeLimit)
Description copied from interface: `WebSocketSession`
Configure the maximum size for an incoming binary message.

  - 

### getBinaryMessageSizeLimit

public int getBinaryMessageSizeLimit()
Description copied from interface: `WebSocketSession`
Get the configured maximum size for an incoming binary message.

  - 

### isOpen

public boolean isOpen()
Description copied from interface: `WebSocketSession`
Whether the underlying connection is open.

  - 

### initializeNativeSession

public void initializeNativeSession(jakarta.websocket.Session session)

Overrides:
`initializeNativeSession` in class `AbstractWebSocketSession<jakarta.websocket.Session>`

  - 

### sendTextMessage

protected void sendTextMessage(TextMessage message)
                        throws IOException

Specified by:
`sendTextMessage` in class `AbstractWebSocketSession<jakarta.websocket.Session>`
Throws:
`IOException`

  - 

### sendBinaryMessage

protected void sendBinaryMessage(BinaryMessage message)
                          throws IOException

Specified by:
`sendBinaryMessage` in class `AbstractWebSocketSession<jakarta.websocket.Session>`
Throws:
`IOException`

  - 

### sendPingMessage

protected void sendPingMessage(PingMessage message)
                        throws IOException

Specified by:
`sendPingMessage` in class `AbstractWebSocketSession<jakarta.websocket.Session>`
Throws:
`IOException`

  - 

### sendPongMessage

protected void sendPongMessage(PongMessage message)
                        throws IOException

Specified by:
`sendPongMessage` in class `AbstractWebSocketSession<jakarta.websocket.Session>`
Throws:
`IOException`

  - 

### closeInternal

protected void closeInternal(CloseStatus status)
                      throws IOException

Specified by:
`closeInternal` in class `AbstractWebSocketSession<jakarta.websocket.Session>`
Throws:
`IOException`