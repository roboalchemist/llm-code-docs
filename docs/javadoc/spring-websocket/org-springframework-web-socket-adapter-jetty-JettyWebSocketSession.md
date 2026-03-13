# Class JettyWebSocketSession

java.lang.Object
org.springframework.web.socket.adapter.AbstractWebSocketSession<org.eclipse.jetty.websocket.api.Session>
org.springframework.web.socket.adapter.jetty.JettyWebSocketSession

All Implemented Interfaces:
`Closeable, AutoCloseable, NativeWebSocketSession, WebSocketSession`

---

public class JettyWebSocketSession
extends AbstractWebSocketSession<org.eclipse.jetty.websocket.api.Session>
A `WebSocketSession` for use with the Jetty WebSocket API.

Since:
4.0
Author:
Phillip Webb, Rossen Stoyanchev, Brian Clozel, Juergen Hoeller

- 

## Field Summary

### Fields inherited from class AbstractWebSocketSession

`idGenerator, logger`

- 

## Constructor Summary

Constructors

Constructor
Description
`JettyWebSocketSession(Map<String,Object> attributes)`

Create a new `JettyWebSocketSession` instance.

`JettyWebSocketSession(Map<String,Object> attributes,
 @Nullable Principal user)`

Create a new `JettyWebSocketSession` instance associated with the given user.

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

`InetSocketAddress`
`getLocalAddress()`

Return the address on which the request was received.

`@Nullable Principal`
`getPrincipal()`

Return a `Principal` instance containing the name
of the authenticated user.

`InetSocketAddress`
`getRemoteAddress()`

Return the address of the remote client.

`int`
`getTextMessageSizeLimit()`

Get the configured maximum size for an incoming text message.

`@Nullable URI`
`getUri()`

Return the URI used to open the WebSocket connection.

`void`
`initializeNativeSession(org.eclipse.jetty.websocket.api.Session session)`
 
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

### JettyWebSocketSession

public JettyWebSocketSession(Map<String,Object> attributes)
Create a new `JettyWebSocketSession` instance.

Parameters:
`attributes` - the attributes from the HTTP handshake to associate with the WebSocket session

  - 

### JettyWebSocketSession

public JettyWebSocketSession(Map<String,Object> attributes,
 @Nullable Principal user)
Create a new `JettyWebSocketSession` instance associated with the given user.

Parameters:
`attributes` - the attributes from the HTTP handshake to associate with the WebSocket
session; the provided attributes are copied, the original map is not used.
`user` - the user associated with the session; if `null` we'll fall back on the
user available via `Session.getUpgradeRequest()`

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

public InetSocketAddress getLocalAddress()
Description copied from interface: `WebSocketSession`
Return the address on which the request was received.

**Note:** The localAddress is not always possible to access,
which is the case with the Standard WebSocket client API, and accordingly
`StandardWebSocketClient`
returns `null`.

  - 

### getRemoteAddress

public InetSocketAddress getRemoteAddress()
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

public void initializeNativeSession(org.eclipse.jetty.websocket.api.Session session)

Overrides:
`initializeNativeSession` in class `AbstractWebSocketSession<org.eclipse.jetty.websocket.api.Session>`

  - 

### sendTextMessage

protected void sendTextMessage(TextMessage message)
                        throws IOException

Specified by:
`sendTextMessage` in class `AbstractWebSocketSession<org.eclipse.jetty.websocket.api.Session>`
Throws:
`IOException`

  - 

### sendBinaryMessage

protected void sendBinaryMessage(BinaryMessage message)
                          throws IOException

Specified by:
`sendBinaryMessage` in class `AbstractWebSocketSession<org.eclipse.jetty.websocket.api.Session>`
Throws:
`IOException`

  - 

### sendPingMessage

protected void sendPingMessage(PingMessage message)
                        throws IOException

Specified by:
`sendPingMessage` in class `AbstractWebSocketSession<org.eclipse.jetty.websocket.api.Session>`
Throws:
`IOException`

  - 

### sendPongMessage

protected void sendPongMessage(PongMessage message)
                        throws IOException

Specified by:
`sendPongMessage` in class `AbstractWebSocketSession<org.eclipse.jetty.websocket.api.Session>`
Throws:
`IOException`

  - 

### closeInternal

protected void closeInternal(CloseStatus status)
                      throws IOException

Specified by:
`closeInternal` in class `AbstractWebSocketSession<org.eclipse.jetty.websocket.api.Session>`
Throws:
`IOException`