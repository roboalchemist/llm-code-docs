# Class AbstractSockJsSession

java.lang.Object
org.springframework.web.socket.sockjs.transport.session.AbstractSockJsSession

All Implemented Interfaces:
`Closeable, AutoCloseable, SockJsSession, WebSocketSession`

Direct Known Subclasses:
`AbstractHttpSockJsSession, WebSocketServerSockJsSession`

---

public abstract class AbstractSockJsSession
extends Object
implements SockJsSession
An abstract base class for SockJS sessions implementing `SockJsSession`.

Since:
4.0
Author:
Rossen Stoyanchev, Sam Brannen

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`DISCONNECTED_CLIENT_LOG_CATEGORY`

Log category to use for network failure after a client has gone away.

`protected final org.apache.commons.logging.Log`
`logger`
 
`protected final Object`
`responseLock`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`AbstractSockJsSession(String id,
 SockJsServiceConfig config,
 WebSocketHandler handler,
 @Nullable Map<String,Object> attributes)`

Create a new instance.

- 

## Method Summary

Modifier and Type
Method
Description
`protected void`
`cancelHeartbeat()`
 
`final void`
`close()`

Performs cleanup and notify the `WebSocketHandler`.

`final void`
`close(CloseStatus status)`

Performs cleanup and notify the `WebSocketHandler`.

`final void`
`delegateConnectionClosed(CloseStatus status)`

Invoked when the underlying connection is closed.

`void`
`delegateConnectionEstablished()`
 
`void`
`delegateError(Throwable ex)`
 
`void`
`delegateMessages(String... messages)`
 
`void`
`disableHeartbeat()`

Disable the SockJS heartbeat, presumably because a higher-level protocol
has heartbeats enabled for the session already.

`protected abstract void`
`disconnect(CloseStatus status)`

Actually close the underlying WebSocket session or in the case of HTTP
transports complete the underlying request.

`Map<String,Object>`
`getAttributes()`

Return the map with attributes associated with the WebSocket session.

`String`
`getId()`

Return a unique session identifier.

`protected SockJsMessageCodec`
`getMessageCodec()`
 
`SockJsServiceConfig`
`getSockJsServiceConfig()`
 
`long`
`getTimeSinceLastActive()`

Return the time (in ms) since the session was last active, or otherwise
if the session is new, then the time since the session was created.

`abstract boolean`
`isActive()`

Polling and Streaming sessions periodically close the current HTTP request and
wait for the next request to come through.

`boolean`
`isClosed()`
 
`boolean`
`isNew()`
 
`boolean`
`isOpen()`

Whether the underlying connection is open.

`protected void`
`scheduleHeartbeat()`
 
`protected void`
`sendHeartbeat()`
 
`final void`
`sendMessage(WebSocketMessage<?> message)`

Send a WebSocket message: either `TextMessage` or `BinaryMessage`.

`protected abstract void`
`sendMessageInternal(String message)`
 
`String`
`toString()`
 
`void`
`tryCloseWithSockJsTransportError(Throwable error,
 CloseStatus closeStatus)`

Close due to error arising from SockJS transport handling.

`protected void`
`updateLastActiveTime()`

Should be invoked whenever the session becomes inactive.

`protected void`
`writeFrame(SockJsFrame frame)`

For internal use within a TransportHandler and the (TransportHandler-specific)
session class.

`protected abstract void`
`writeFrameInternal(SockJsFrame frame)`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface WebSocketSession

`getAcceptedProtocol, getBinaryMessageSizeLimit, getExtensions, getHandshakeHeaders, getLocalAddress, getPrincipal, getRemoteAddress, getTextMessageSizeLimit, getUri, setBinaryMessageSizeLimit, setTextMessageSizeLimit`

- 

## Field Details

  - 

### DISCONNECTED_CLIENT_LOG_CATEGORY

public static final String DISCONNECTED_CLIENT_LOG_CATEGORY
Log category to use for network failure after a client has gone away.

See Also:

    - `DisconnectedClientHelper`

    - Constant Field Values

  - 

### logger

protected final org.apache.commons.logging.Log logger

  - 

### responseLock

protected final Object responseLock

- 

## Constructor Details

  - 

### AbstractSockJsSession

public AbstractSockJsSession(String id,
 SockJsServiceConfig config,
 WebSocketHandler handler,
 @Nullable Map<String,Object> attributes)
Create a new instance.

Parameters:
`id` - the session ID
`config` - the SockJS service configuration options
`handler` - the recipient of SockJS messages
`attributes` - the attributes from the HTTP handshake to associate with the WebSocket
session; the provided attributes are copied, the original map is not used.

- 

## Method Details

  - 

### getId

public String getId()
Description copied from interface: `WebSocketSession`
Return a unique session identifier.

Specified by:
`getId` in interface `WebSocketSession`

  - 

### getMessageCodec

protected SockJsMessageCodec getMessageCodec()

  - 

### getSockJsServiceConfig

public SockJsServiceConfig getSockJsServiceConfig()

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

### sendMessageInternal

protected abstract void sendMessageInternal(String message)
                                     throws IOException

Throws:
`IOException`

  - 

### isNew

public boolean isNew()

  - 

### isOpen

public boolean isOpen()
Description copied from interface: `WebSocketSession`
Whether the underlying connection is open.

Specified by:
`isOpen` in interface `WebSocketSession`

  - 

### isClosed

public boolean isClosed()

  - 

### close

public final void close()
                 throws IOException
Performs cleanup and notify the `WebSocketHandler`.

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
Performs cleanup and notify the `WebSocketHandler`.

Specified by:
`close` in interface `WebSocketSession`
Throws:
`IOException`

  - 

### getTimeSinceLastActive

public long getTimeSinceLastActive()
Description copied from interface: `SockJsSession`
Return the time (in ms) since the session was last active, or otherwise
if the session is new, then the time since the session was created.

Specified by:
`getTimeSinceLastActive` in interface `SockJsSession`

  - 

### updateLastActiveTime

protected void updateLastActiveTime()
Should be invoked whenever the session becomes inactive.

  - 

### disableHeartbeat

public void disableHeartbeat()
Description copied from interface: `SockJsSession`
Disable the SockJS heartbeat, presumably because a higher-level protocol
has heartbeats enabled for the session already. It is not recommended to
disable this otherwise, as it helps proxies to know the connection is
not hanging.

Specified by:
`disableHeartbeat` in interface `SockJsSession`

  - 

### sendHeartbeat

protected void sendHeartbeat()
                      throws SockJsTransportFailureException

Throws:
`SockJsTransportFailureException`

  - 

### scheduleHeartbeat

protected void scheduleHeartbeat()

  - 

### cancelHeartbeat

protected void cancelHeartbeat()

  - 

### isActive

public abstract boolean isActive()
Polling and Streaming sessions periodically close the current HTTP request and
wait for the next request to come through. During this "downtime" the session is
still open but inactive and unable to send messages and therefore has to buffer
them temporarily. A WebSocket session by contrast is stateful and remain active
until closed.

  - 

### disconnect

protected abstract void disconnect(CloseStatus status)
                            throws IOException
Actually close the underlying WebSocket session or in the case of HTTP
transports complete the underlying request.

Throws:
`IOException`

  - 

### writeFrame

protected void writeFrame(SockJsFrame frame)
                   throws SockJsTransportFailureException
For internal use within a TransportHandler and the (TransportHandler-specific)
session class.

Throws:
`SockJsTransportFailureException`

  - 

### writeFrameInternal

protected abstract void writeFrameInternal(SockJsFrame frame)
                                    throws IOException

Throws:
`IOException`

  - 

### delegateConnectionEstablished

public void delegateConnectionEstablished()
                                   throws Exception

Throws:
`Exception`

  - 

### delegateMessages

public void delegateMessages(String... messages)
                      throws SockJsMessageDeliveryException

Throws:
`SockJsMessageDeliveryException`

  - 

### delegateConnectionClosed

public final void delegateConnectionClosed(CloseStatus status)
                                    throws Exception
Invoked when the underlying connection is closed.

Throws:
`Exception`

  - 

### tryCloseWithSockJsTransportError

public void tryCloseWithSockJsTransportError(Throwable error,
 CloseStatus closeStatus)
Close due to error arising from SockJS transport handling.

  - 

### delegateError

public void delegateError(Throwable ex)
                   throws Exception

Throws:
`Exception`

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`