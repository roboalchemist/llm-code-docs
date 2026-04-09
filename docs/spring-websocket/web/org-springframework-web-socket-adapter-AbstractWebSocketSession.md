# Class AbstractWebSocketSession<T>

java.lang.Object
org.springframework.web.socket.adapter.AbstractWebSocketSession<T>

Type Parameters:
`T` - the native session type

All Implemented Interfaces:
`Closeable, AutoCloseable, NativeWebSocketSession, WebSocketSession`

Direct Known Subclasses:
`JettyWebSocketSession, StandardWebSocketSession`

---

public abstract class AbstractWebSocketSession<T>
extends Object
implements NativeWebSocketSession
An abstract base class for implementations of `WebSocketSession`.

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
`protected static final org.springframework.util.IdGenerator`
`idGenerator`
 
`protected static final org.apache.commons.logging.Log`
`logger`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`AbstractWebSocketSession(@Nullable Map<String,Object> attributes)`

Create a new instance and associate the given attributes with it.

- 

## Method Summary

Modifier and Type
Method
Description
`protected final void`
`checkNativeSessionInitialized()`
 
`final void`
`close()`

Close the WebSocket connection with status 1000, i.e.

`final void`
`close(CloseStatus status)`

Close the WebSocket connection with the given close status.

`protected abstract void`
`closeInternal(CloseStatus status)`
 
`Map<String,Object>`
`getAttributes()`

Return the map with attributes associated with the WebSocket session.

`T`
`getNativeSession()`

Return the underlying native WebSocketSession.

`<R> @Nullable R`
`getNativeSession(@Nullable Class<R> requiredType)`

Return the underlying native WebSocketSession, if available.

`void`
`initializeNativeSession(T session)`
 
`protected abstract void`
`sendBinaryMessage(BinaryMessage message)`
 
`final void`
`sendMessage(WebSocketMessage<?> message)`

Send a WebSocket message: either `TextMessage` or `BinaryMessage`.

`protected abstract void`
`sendPingMessage(PingMessage message)`
 
`protected abstract void`
`sendPongMessage(PongMessage message)`
 
`protected abstract void`
`sendTextMessage(TextMessage message)`
 
`String`
`toString()`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface WebSocketSession

`getAcceptedProtocol, getBinaryMessageSizeLimit, getExtensions, getHandshakeHeaders, getId, getLocalAddress, getPrincipal, getRemoteAddress, getTextMessageSizeLimit, getUri, isOpen, setBinaryMessageSizeLimit, setTextMessageSizeLimit`

- 

## Field Details

  - 

### idGenerator

protected static final org.springframework.util.IdGenerator idGenerator

  - 

### logger

protected static final org.apache.commons.logging.Log logger

- 

## Constructor Details

  - 

### AbstractWebSocketSession

public AbstractWebSocketSession(@Nullable Map<String,Object> attributes)
Create a new instance and associate the given attributes with it.

Parameters:
`attributes` - the attributes from the HTTP handshake to associate with the WebSocket
session; the provided attributes are copied, the original map is not used.

- 

## Method Details

  - 

### getAttributes

public Map<String,Object> getAttributes()
Description copied from interface: `WebSocketSession`
Return the map with attributes associated with the WebSocket session.

On the server side the map can be populated initially through a
`HandshakeInterceptor`. On the client side the map can be populated via
`WebSocketClient` handshake methods.

Specified by:
`getAttributes` in interface `WebSocketSession`
Returns:
a Map with the session attributes (never `null`)

  - 

### getNativeSession

public T getNativeSession()
Description copied from interface: `NativeWebSocketSession`
Return the underlying native WebSocketSession.

Specified by:
`getNativeSession` in interface `NativeWebSocketSession`

  - 

### getNativeSession

public <R> @Nullable R getNativeSession(@Nullable Class<R> requiredType)
Description copied from interface: `NativeWebSocketSession`
Return the underlying native WebSocketSession, if available.

Specified by:
`getNativeSession` in interface `NativeWebSocketSession`
Parameters:
`requiredType` - the required type of the session
Returns:
the native session of the required type,
or `null` if not available

  - 

### initializeNativeSession

public void initializeNativeSession(T session)

  - 

### checkNativeSessionInitialized

protected final void checkNativeSessionInitialized()

  - 

### sendMessage

public final void sendMessage(WebSocketMessage<?> message)
                       throws IOException
Description copied from interface: `WebSocketSession`
Send a WebSocket message: either `TextMessage` or `BinaryMessage`.

**Note:** The underlying standard WebSocket session (JSR-356) does
not allow concurrent sending. Therefore, sending must be synchronized. To ensure
that, one option is to wrap the `WebSocketSession` with the
`ConcurrentWebSocketSessionDecorator`.

Specified by:
`sendMessage` in interface `WebSocketSession`
Throws:
`IOException`
See Also:

    - `ConcurrentWebSocketSessionDecorator`

  - 

### sendTextMessage

protected abstract void sendTextMessage(TextMessage message)
                                 throws IOException

Throws:
`IOException`

  - 

### sendBinaryMessage

protected abstract void sendBinaryMessage(BinaryMessage message)
                                   throws IOException

Throws:
`IOException`

  - 

### sendPingMessage

protected abstract void sendPingMessage(PingMessage message)
                                 throws IOException

Throws:
`IOException`

  - 

### sendPongMessage

protected abstract void sendPongMessage(PongMessage message)
                                 throws IOException

Throws:
`IOException`

  - 

### close

public final void close()
                 throws IOException
Description copied from interface: `WebSocketSession`
Close the WebSocket connection with status 1000, i.e. equivalent to:

```

session.close(CloseStatus.NORMAL);

```

Specified by:
`close` in interface `AutoCloseable`
Specified by:
`close` in interface `Closeable`
Specified by:
`close` in interface `WebSocketSession`
Throws:
`IOException`

  - 

### close

public final void close(CloseStatus status)
                 throws IOException
Description copied from interface: `WebSocketSession`
Close the WebSocket connection with the given close status.

Specified by:
`close` in interface `WebSocketSession`
Throws:
`IOException`

  - 

### closeInternal

protected abstract void closeInternal(CloseStatus status)
                               throws IOException

Throws:
`IOException`

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`