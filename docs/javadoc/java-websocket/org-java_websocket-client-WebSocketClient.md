Package org.java_websocket.client

# Class WebSocketClient


java.lang.Object
org.java_websocket.WebSocketAdapter
org.java_websocket.AbstractWebSocket
org.java_websocket.client.WebSocketClient





All Implemented Interfaces:
`Runnable`, `WebSocket`, `WebSocketListener`


---

public abstract class WebSocketClient
extends AbstractWebSocket
implements Runnable, WebSocket
A subclass must implement at least onOpen, onClose, and
 onMessage to be useful. At runtime the user is expected to establish a connection via
 `connect()`, then receive events like `onMessage(String)` via the overloaded
 methods and to `send(String)` data to the server.






- 


## Field Summary

Fields

Modifier and Type
Field
Description
`protected URI`
`uri`

The URI this channel is supposed to connect to.




### Fields inherited from class org.java_websocket.AbstractWebSocket

`DEFAULT_READ_BUFFER_SIZE`




- 


## Constructor Summary

Constructors

Constructor
Description
`WebSocketClient(URI serverUri)`

Constructs a WebSocketClient instance and sets it to the connect to the specified URI.

`WebSocketClient(URI serverUri,
 Map<String,String> httpHeaders)`

Constructs a WebSocketClient instance and sets it to the connect to the specified URI.

`WebSocketClient(URI serverUri,
 Draft protocolDraft)`

Constructs a WebSocketClient instance and sets it to the connect to the specified URI.

`WebSocketClient(URI serverUri,
 Draft protocolDraft,
 Map<String,String> httpHeaders)`

Constructs a WebSocketClient instance and sets it to the connect to the specified URI.

`WebSocketClient(URI serverUri,
 Draft protocolDraft,
 Map<String,String> httpHeaders,
 int connectTimeout)`

Constructs a WebSocketClient instance and sets it to the connect to the specified URI.






- 


## Method Summary





Modifier and Type
Method
Description
`void`
`addHeader(String key,
 String value)`
 
`void`
`clearHeaders()`
 
`void`
`close()`

Initiates the websocket close handshake.

`void`
`close(int code)`

sends the closing handshake. may be send in response to an other handshake.

`void`
`close(int code,
 String message)`

sends the closing handshake. may be send in response to an other handshake.

`void`
`closeBlocking()`

Same as `close` but blocks until the websocket closed or failed to do so.


`void`
`closeConnection(int code,
 String message)`

This will close the connection immediately without a proper close handshake.

`void`
`connect()`

Initiates the websocket connection.

`boolean`
`connectBlocking()`

Same as `connect` but blocks until the websocket connected or failed to do so.


`boolean`
`connectBlocking(long timeout,
 TimeUnit timeUnit)`

Same as `connect` but blocks with a timeout until the websocket connected or failed
 to do so.


`<T> T`
`getAttachment()`

Getter for the connection attachment.

`WebSocket`
`getConnection()`

Getter for the engine

`protected Collection<WebSocket>`
`getConnections()`

Getter to get all the currently available connections

`Draft`
`getDraft()`

Returns the protocol version this channel uses.
 For more infos see
 https://github.com/TooTallNate/Java-WebSocket/wiki/Drafts

`InetSocketAddress`
`getLocalSocketAddress()`

Returns the address of the endpoint this socket is bound to, or `null` if it is not
 bound.

`InetSocketAddress`
`getLocalSocketAddress(WebSocket conn)`
 
`IProtocol`
`getProtocol()`

Returns the used Sec-WebSocket-Protocol for this websocket connection

`ReadyState`
`getReadyState()`

This represents the state of the connection.

`InetSocketAddress`
`getRemoteSocketAddress()`

Returns the address of the endpoint this socket is connected to, or `null` if it is
 unconnected.

`InetSocketAddress`
`getRemoteSocketAddress(WebSocket conn)`
 
`String`
`getResourceDescriptor()`

Returns the HTTP Request-URI as defined by http://tools.ietf.org/html/rfc2616#section-5.1.2

 If the opening handshake has not yet happened it will return null.

`Socket`
`getSocket()`

Returns the socket to allow Hostname Verification

`SSLSession`
`getSSLSession()`

Returns the ssl session of websocket, if ssl/wss is used for this instance.

`URI`
`getURI()`

Returns the URI that this WebSocketClient is connected to.

`boolean`
`hasBufferedData()`

Checks if the websocket has buffered data

`boolean`
`hasSSLSupport()`

Does this websocket use an encrypted (wss/ssl) or unencrypted (ws) connection

`boolean`
`isClosed()`

Is the websocket in the state CLOSED

`boolean`
`isClosing()`

Is the websocket in the state CLOSING

`boolean`
`isFlushAndClose()`

Returns true when no further frames may be submitted
 This happens before the socket
 connection is closed.

`boolean`
`isOpen()`

Is the websocket in the state OPEN

`abstract void`
`onClose(int code,
 String reason,
 boolean remote)`

Called after the websocket connection has been closed.

`void`
`onCloseInitiated(int code,
 String reason)`

Send when this peer sends a close handshake

`void`
`onClosing(int code,
 String reason,
 boolean remote)`

Called as soon as no further frames are accepted

`abstract void`
`onError(Exception ex)`

Called when errors occurs.

`abstract void`
`onMessage(String message)`

Callback for string messages received from the remote host

`void`
`onMessage(ByteBuffer bytes)`

Callback for binary messages received from the remote host

`abstract void`
`onOpen(ServerHandshake handshakedata)`

Called after an opening handshake has been performed and the given websocket is ready to be
 written on.

`protected void`
`onSetSSLParameters(SSLParameters sslParameters)`

Apply specific SSLParameters If you override this method make sure to always call
 super.onSetSSLParameters() to ensure the hostname validation is active

`final void`
`onWebsocketClose(WebSocket conn,
 int code,
 String reason,
 boolean remote)`

Calls subclass' implementation of onClose.

`void`
`onWebsocketCloseInitiated(WebSocket conn,
 int code,
 String reason)`

send when this peer sends a close handshake

`void`
`onWebsocketClosing(WebSocket conn,
 int code,
 String reason,
 boolean remote)`

Called as soon as no further frames are accepted

`final void`
`onWebsocketError(WebSocket conn,
 Exception ex)`

Calls subclass' implementation of onIOError.

`final void`
`onWebsocketMessage(WebSocket conn,
 String message)`

Calls subclass' implementation of onMessage.

`final void`
`onWebsocketMessage(WebSocket conn,
 ByteBuffer blob)`

Called when an entire binary frame has been received.

`final void`
`onWebsocketOpen(WebSocket conn,
 Handshakedata handshake)`

Calls subclass' implementation of onOpen.

`final void`
`onWriteDemand(WebSocket conn)`

This method is used to inform the selector thread that there is data queued to be written to
 the socket.

`void`
`reconnect()`

Reinitiates the websocket connection.

`boolean`
`reconnectBlocking()`

Same as `reconnect` but blocks until the websocket reconnected or failed to do
 so.


`String`
`removeHeader(String key)`
 
`void`
`run()`
 
`void`
`send(byte[] data)`

Sends binary  data to the connected webSocket server.

`void`
`send(String text)`

Sends text to the connected websocket server.

`void`
`send(ByteBuffer bytes)`

Send Binary data (plain bytes) to the other end.

`void`
`sendFragmentedFrame(Opcode op,
 ByteBuffer buffer,
 boolean fin)`

Allows to send continuous/fragmented frames conveniently.

`void`
`sendFrame(Collection<Framedata> frames)`

Send a collection of frames to the other end

`void`
`sendFrame(Framedata framedata)`

Send a frame to the other end

`void`
`sendPing()`

Send a ping to the other end

`<T> void`
`setAttachment(T attachment)`

Setter for an attachment on the socket connection.

`void`
`setDnsResolver(DnsResolver dnsResolver)`

Sets a custom DNS resolver.

`void`
`setProxy(Proxy proxy)`

Method to set a proxy for this connection

`void`
`setSocket(Socket socket)`

Deprecated.
use setSocketFactory


`void`
`setSocketFactory(SocketFactory socketFactory)`

Accepts a SocketFactory.
 This method must be called before `connect`.






### Methods inherited from class org.java_websocket.AbstractWebSocket

`getConnectionLostTimeout, getReceiveBufferSize, isDaemon, isReuseAddr, isTcpNoDelay, setConnectionLostTimeout, setDaemon, setReceiveBufferSize, setReuseAddr, setTcpNoDelay, startConnectionLostTimer, stopConnectionLostTimer`


### Methods inherited from class org.java_websocket.WebSocketAdapter

`onPreparePing, onWebsocketHandshakeReceivedAsClient, onWebsocketHandshakeReceivedAsServer, onWebsocketHandshakeSentAsClient, onWebsocketPing, onWebsocketPong`


### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`










- 


## Field Details




  - 


### uri

protected URI uri
The URI this channel is supposed to connect to.








- 


## Constructor Details




  - 


### WebSocketClient

public WebSocketClient(URI serverUri)
Constructs a WebSocketClient instance and sets it to the connect to the specified URI. The
 channel does not attampt to connect automatically. The connection will be established once you
 call connect.

Parameters:
`serverUri` - the server URI to connect to




  - 


### WebSocketClient

public WebSocketClient(URI serverUri,
 Draft protocolDraft)
Constructs a WebSocketClient instance and sets it to the connect to the specified URI. The
 channel does not attampt to connect automatically. The connection will be established once you
 call connect.

Parameters:
`serverUri` - the server URI to connect to
`protocolDraft` - The draft which should be used for this connection




  - 


### WebSocketClient

public WebSocketClient(URI serverUri,
 Map<String,String> httpHeaders)
Constructs a WebSocketClient instance and sets it to the connect to the specified URI. The
 channel does not attampt to connect automatically. The connection will be established once you
 call connect.

Parameters:
`serverUri` - the server URI to connect to
`httpHeaders` - Additional HTTP-Headers
Since:
1.3.8




  - 


### WebSocketClient

public WebSocketClient(URI serverUri,
 Draft protocolDraft,
 Map<String,String> httpHeaders)
Constructs a WebSocketClient instance and sets it to the connect to the specified URI. The
 channel does not attampt to connect automatically. The connection will be established once you
 call connect.

Parameters:
`serverUri` - the server URI to connect to
`protocolDraft` - The draft which should be used for this connection
`httpHeaders` - Additional HTTP-Headers
Since:
1.3.8




  - 


### WebSocketClient

public WebSocketClient(URI serverUri,
 Draft protocolDraft,
 Map<String,String> httpHeaders,
 int connectTimeout)
Constructs a WebSocketClient instance and sets it to the connect to the specified URI. The
 channel does not attampt to connect automatically. The connection will be established once you
 call connect.

Parameters:
`serverUri` - the server URI to connect to
`protocolDraft` - The draft which should be used for this connection
`httpHeaders` - Additional HTTP-Headers
`connectTimeout` - The Timeout for the connection









- 


## Method Details




  - 


### getURI

public URI getURI()
Returns the URI that this WebSocketClient is connected to.

Returns:
the URI connected to




  - 


### getDraft

public Draft getDraft()
Returns the protocol version this channel uses.
 For more infos see
 https://github.com/TooTallNate/Java-WebSocket/wiki/Drafts

Specified by:
`getDraft` in interface `WebSocket`
Returns:
The draft used for this client




  - 


### getSocket

public Socket getSocket()
Returns the socket to allow Hostname Verification

Returns:
the socket used for this connection




  - 


### addHeader

public void addHeader(String key,
 String value)

Parameters:
`key` - Name of the header to add.
`value` - Value of the header to add.
Since:
1.4.1 Adds an additional header to be sent in the handshake.
 If the connection is
 already made, adding headers has no effect, unless reconnect is called, which then a new
 handshake is sent.
 If a header with the same key already exists, it is overridden.




  - 


### removeHeader

public String removeHeader(String key)

Parameters:
`key` - Name of the header to remove.
Returns:
the previous value associated with key, or null if there was no mapping for key.
Since:
1.4.1 Removes a header from the handshake to be sent, if header key exists.





  - 


### clearHeaders

public void clearHeaders()

Since:
1.4.1 Clears all previously put headers.




  - 


### setDnsResolver

public void setDnsResolver(DnsResolver dnsResolver)
Sets a custom DNS resolver.

Parameters:
`dnsResolver` - The DnsResolver to use.
Since:
1.4.1




  - 


### reconnect

public void reconnect()
Reinitiates the websocket connection. This method does not block.

Since:
1.3.8




  - 


### reconnectBlocking

public boolean reconnectBlocking()
                          throws InterruptedException
Same as `reconnect` but blocks until the websocket reconnected or failed to do
 so.


Returns:
Returns whether it succeeded or not.
Throws:
`InterruptedException` - Thrown when the threads get interrupted
Since:
1.3.8




  - 


### connect

public void connect()
Initiates the websocket connection. This method does not block.



  - 


### connectBlocking

public boolean connectBlocking()
                        throws InterruptedException
Same as `connect` but blocks until the websocket connected or failed to do so.


Returns:
Returns whether it succeeded or not.
Throws:
`InterruptedException` - Thrown when the threads get interrupted




  - 


### connectBlocking

public boolean connectBlocking(long timeout,
 TimeUnit timeUnit)
                        throws InterruptedException
Same as `connect` but blocks with a timeout until the websocket connected or failed
 to do so.


Parameters:
`timeout` - The connect timeout
`timeUnit` - The timeout time unit
Returns:
Returns whether it succeeded or not.
Throws:
`InterruptedException` - Thrown when the threads get interrupted




  - 


### close

public void close()
Initiates the websocket close handshake. This method does not block
 In oder to make sure
 the connection is closed use `closeBlocking`

Specified by:
`close` in interface `WebSocket`




  - 


### closeBlocking

public void closeBlocking()
                   throws InterruptedException
Same as `close` but blocks until the websocket closed or failed to do so.


Throws:
`InterruptedException` - Thrown when the threads get interrupted




  - 


### send

public void send(String text)
Sends text to the connected websocket server.

Specified by:
`send` in interface `WebSocket`
Parameters:
`text` - The string which will be transmitted.




  - 


### send

public void send(byte[] data)
Sends binary  data to the connected webSocket server.

Specified by:
`send` in interface `WebSocket`
Parameters:
`data` - The byte-Array of data to send to the WebSocket server.




  - 


### getAttachment

public <T> T getAttachment()
Description copied from interface: `WebSocket`
Getter for the connection attachment.

Specified by:
`getAttachment` in interface `WebSocket`
Type Parameters:
`T` - The type of the attachment
Returns:
Returns the user attachment




  - 


### setAttachment

public <T> void setAttachment(T attachment)
Description copied from interface: `WebSocket`
Setter for an attachment on the socket connection. The attachment may be of any type.

Specified by:
`setAttachment` in interface `WebSocket`
Type Parameters:
`T` - The type of the attachment
Parameters:
`attachment` - The object to be attached to the user




  - 


### getConnections

protected Collection<WebSocket> getConnections()
Description copied from class: `AbstractWebSocket`
Getter to get all the currently available connections

Specified by:
`getConnections` in class `AbstractWebSocket`
Returns:
the currently available connections




  - 


### sendPing

public void sendPing()
Description copied from interface: `WebSocket`
Send a ping to the other end

Specified by:
`sendPing` in interface `WebSocket`




  - 


### run

public void run()

Specified by:
`run` in interface `Runnable`




  - 


### onSetSSLParameters

protected void onSetSSLParameters(SSLParameters sslParameters)
Apply specific SSLParameters If you override this method make sure to always call
 super.onSetSSLParameters() to ensure the hostname validation is active

Parameters:
`sslParameters` - the SSLParameters which will be used for the SSLSocket




  - 


### getReadyState

public ReadyState getReadyState()
This represents the state of the connection.

Specified by:
`getReadyState` in interface `WebSocket`
Returns:
Returns '0 = CONNECTING', '1 = OPEN', '2 = CLOSING' or '3 = CLOSED'




  - 


### onWebsocketMessage

public final void onWebsocketMessage(WebSocket conn,
 String message)
Calls subclass' implementation of onMessage.

Specified by:
`onWebsocketMessage` in interface `WebSocketListener`
Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`message` - The UTF-8 decoded message that was received.




  - 


### onWebsocketMessage

public final void onWebsocketMessage(WebSocket conn,
 ByteBuffer blob)
Description copied from interface: `WebSocketListener`
Called when an entire binary frame has been received. Do whatever you want here...

Specified by:
`onWebsocketMessage` in interface `WebSocketListener`
Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`blob` - The binary message that was received.




  - 


### onWebsocketOpen

public final void onWebsocketOpen(WebSocket conn,
 Handshakedata handshake)
Calls subclass' implementation of onOpen.

Specified by:
`onWebsocketOpen` in interface `WebSocketListener`
Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`handshake` - The handshake of the websocket instance




  - 


### onWebsocketClose

public final void onWebsocketClose(WebSocket conn,
 int code,
 String reason,
 boolean remote)
Calls subclass' implementation of onClose.

Specified by:
`onWebsocketClose` in interface `WebSocketListener`
Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`code` - The codes can be looked up here: `CloseFrame`
`reason` - Additional information string
`remote` - Returns whether or not the closing of the connection was initiated by the remote
               host.




  - 


### onWebsocketError

public final void onWebsocketError(WebSocket conn,
 Exception ex)
Calls subclass' implementation of onIOError.

Specified by:
`onWebsocketError` in interface `WebSocketListener`
Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`ex` - The exception that occurred. 
 Might be null if the exception is not related to
             any specific connection. For example if the server port could not be bound.




  - 


### onWriteDemand

public final void onWriteDemand(WebSocket conn)
Description copied from interface: `WebSocketListener`
This method is used to inform the selector thread that there is data queued to be written to
 the socket.

Specified by:
`onWriteDemand` in interface `WebSocketListener`
Parameters:
`conn` - The `WebSocket` instance this event is occurring on.




  - 


### onWebsocketCloseInitiated

public void onWebsocketCloseInitiated(WebSocket conn,
 int code,
 String reason)
Description copied from interface: `WebSocketListener`
send when this peer sends a close handshake

Specified by:
`onWebsocketCloseInitiated` in interface `WebSocketListener`
Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`code` - The codes can be looked up here: `CloseFrame`
`reason` - Additional information string




  - 


### onWebsocketClosing

public void onWebsocketClosing(WebSocket conn,
 int code,
 String reason,
 boolean remote)
Description copied from interface: `WebSocketListener`
Called as soon as no further frames are accepted

Specified by:
`onWebsocketClosing` in interface `WebSocketListener`
Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`code` - The codes can be looked up here: `CloseFrame`
`reason` - Additional information string
`remote` - Returns whether or not the closing of the connection was initiated by the remote
               host.




  - 


### onCloseInitiated

public void onCloseInitiated(int code,
 String reason)
Send when this peer sends a close handshake

Parameters:
`code` - The codes can be looked up here: `CloseFrame`
`reason` - Additional information string




  - 


### onClosing

public void onClosing(int code,
 String reason,
 boolean remote)
Called as soon as no further frames are accepted

Parameters:
`code` - The codes can be looked up here: `CloseFrame`
`reason` - Additional information string
`remote` - Returns whether or not the closing of the connection was initiated by the remote
               host.




  - 


### getConnection

public WebSocket getConnection()
Getter for the engine

Returns:
the engine




  - 


### getLocalSocketAddress

public InetSocketAddress getLocalSocketAddress(WebSocket conn)

Specified by:
`getLocalSocketAddress` in interface `WebSocketListener`
Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
Returns:
Returns the address of the endpoint this socket is bound to.
See Also:




    - `WebSocket.getLocalSocketAddress()`







  - 


### getRemoteSocketAddress

public InetSocketAddress getRemoteSocketAddress(WebSocket conn)

Specified by:
`getRemoteSocketAddress` in interface `WebSocketListener`
Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
Returns:
Returns the address of the endpoint this socket is connected to, or`null` if it
 is unconnected.
See Also:




    - `WebSocket.getRemoteSocketAddress()`







  - 


### onOpen

public abstract void onOpen(ServerHandshake handshakedata)
Called after an opening handshake has been performed and the given websocket is ready to be
 written on.

Parameters:
`handshakedata` - The handshake of the websocket instance




  - 


### onMessage

public abstract void onMessage(String message)
Callback for string messages received from the remote host

Parameters:
`message` - The UTF-8 decoded message that was received.
See Also:




    - `onMessage(ByteBuffer)`







  - 


### onClose

public abstract void onClose(int code,
 String reason,
 boolean remote)
Called after the websocket connection has been closed.

Parameters:
`code` - The codes can be looked up here: `CloseFrame`
`reason` - Additional information string
`remote` - Returns whether or not the closing of the connection was initiated by the remote
               host.




  - 


### onError

public abstract void onError(Exception ex)
Called when errors occurs. If an error causes the websocket connection to fail `onClose(int, String, boolean)` will be called additionally.
 This method will be called
 primarily because of IO or protocol errors.
 If the given exception is an RuntimeException
 that probably means that you encountered a bug.


Parameters:
`ex` - The exception causing this error




  - 


### onMessage

public void onMessage(ByteBuffer bytes)
Callback for binary messages received from the remote host

Parameters:
`bytes` - The binary message that was received.
See Also:




    - `onMessage(String)`







  - 


### setProxy

public void setProxy(Proxy proxy)
Method to set a proxy for this connection

Parameters:
`proxy` - the proxy to use for this websocket client




  - 


### setSocket

@Deprecated
public void setSocket(Socket socket)
Deprecated.
use setSocketFactory

Accepts bound and unbound sockets.
 This method must be called before `connect`.
 If the given socket is not yet bound it will be bound to the uri specified in the constructor.

Parameters:
`socket` - The socket which should be used for the connection




  - 


### setSocketFactory

public void setSocketFactory(SocketFactory socketFactory)
Accepts a SocketFactory.
 This method must be called before `connect`. The socket
 will be bound to the uri specified in the constructor.

Parameters:
`socketFactory` - The socket factory which should be used for the connection.




  - 


### sendFragmentedFrame

public void sendFragmentedFrame(Opcode op,
 ByteBuffer buffer,
 boolean fin)
Description copied from interface: `WebSocket`
Allows to send continuous/fragmented frames conveniently. 
 For more into on this frame type
 see http://tools.ietf.org/html/rfc6455#section-5.4

 


 If the first frame you send is also the last then it is not a fragmented frame and will
 received via onMessage instead of onFragmented even though it was send by this method.

Specified by:
`sendFragmentedFrame` in interface `WebSocket`
Parameters:
`op` - This is only important for the first frame in the sequence. Opcode.TEXT,
               Opcode.BINARY are allowed.
`buffer` - The buffer which contains the payload. It may have no bytes remaining.
`fin` - true means the current frame is the last in the sequence.




  - 


### isOpen

public boolean isOpen()
Description copied from interface: `WebSocket`
Is the websocket in the state OPEN

Specified by:
`isOpen` in interface `WebSocket`
Returns:
state equals ReadyState.OPEN




  - 


### isFlushAndClose

public boolean isFlushAndClose()
Description copied from interface: `WebSocket`
Returns true when no further frames may be submitted
 This happens before the socket
 connection is closed.

Specified by:
`isFlushAndClose` in interface `WebSocket`
Returns:
true when no further frames may be submitted




  - 


### isClosed

public boolean isClosed()
Description copied from interface: `WebSocket`
Is the websocket in the state CLOSED

Specified by:
`isClosed` in interface `WebSocket`
Returns:
state equals ReadyState.CLOSED




  - 


### isClosing

public boolean isClosing()
Description copied from interface: `WebSocket`
Is the websocket in the state CLOSING

Specified by:
`isClosing` in interface `WebSocket`
Returns:
state equals ReadyState.CLOSING




  - 


### hasBufferedData

public boolean hasBufferedData()
Description copied from interface: `WebSocket`
Checks if the websocket has buffered data

Specified by:
`hasBufferedData` in interface `WebSocket`
Returns:
has the websocket buffered data




  - 


### close

public void close(int code)
Description copied from interface: `WebSocket`
sends the closing handshake. may be send in response to an other handshake.

Specified by:
`close` in interface `WebSocket`
Parameters:
`code` - the closing code




  - 


### close

public void close(int code,
 String message)
Description copied from interface: `WebSocket`
sends the closing handshake. may be send in response to an other handshake.

Specified by:
`close` in interface `WebSocket`
Parameters:
`code` - the closing code
`message` - the closing message




  - 


### closeConnection

public void closeConnection(int code,
 String message)
Description copied from interface: `WebSocket`
This will close the connection immediately without a proper close handshake. The code and the
 message therefore won't be transferred over the wire also they will be forwarded to
 onClose/onWebsocketClose.

Specified by:
`closeConnection` in interface `WebSocket`
Parameters:
`code` - the closing code
`message` - the closing message




  - 


### send

public void send(ByteBuffer bytes)
Description copied from interface: `WebSocket`
Send Binary data (plain bytes) to the other end.

Specified by:
`send` in interface `WebSocket`
Parameters:
`bytes` - the binary data to send




  - 


### sendFrame

public void sendFrame(Framedata framedata)
Description copied from interface: `WebSocket`
Send a frame to the other end

Specified by:
`sendFrame` in interface `WebSocket`
Parameters:
`framedata` - the frame to send to the other end




  - 


### sendFrame

public void sendFrame(Collection<Framedata> frames)
Description copied from interface: `WebSocket`
Send a collection of frames to the other end

Specified by:
`sendFrame` in interface `WebSocket`
Parameters:
`frames` - the frames to send to the other end




  - 


### getLocalSocketAddress

public InetSocketAddress getLocalSocketAddress()
Description copied from interface: `WebSocket`
Returns the address of the endpoint this socket is bound to, or `null` if it is not
 bound.

Specified by:
`getLocalSocketAddress` in interface `WebSocket`
Returns:
the local socket address or null, if this socket is not bound




  - 


### getRemoteSocketAddress

public InetSocketAddress getRemoteSocketAddress()
Description copied from interface: `WebSocket`
Returns the address of the endpoint this socket is connected to, or `null` if it is
 unconnected.

Specified by:
`getRemoteSocketAddress` in interface `WebSocket`
Returns:
the remote socket address or null, if this socket is unconnected




  - 


### getResourceDescriptor

public String getResourceDescriptor()
Description copied from interface: `WebSocket`
Returns the HTTP Request-URI as defined by http://tools.ietf.org/html/rfc2616#section-5.1.2

 If the opening handshake has not yet happened it will return null.

Specified by:
`getResourceDescriptor` in interface `WebSocket`
Returns:
Returns the decoded path component of this URI.




  - 


### hasSSLSupport

public boolean hasSSLSupport()
Description copied from interface: `WebSocket`
Does this websocket use an encrypted (wss/ssl) or unencrypted (ws) connection

Specified by:
`hasSSLSupport` in interface `WebSocket`
Returns:
true, if the websocket does use wss and therefore has a SSLSession




  - 


### getSSLSession

public SSLSession getSSLSession()
Description copied from interface: `WebSocket`
Returns the ssl session of websocket, if ssl/wss is used for this instance.

Specified by:
`getSSLSession` in interface `WebSocket`
Returns:
the ssl session of this websocket instance




  - 


### getProtocol

public IProtocol getProtocol()
Description copied from interface: `WebSocket`
Returns the used Sec-WebSocket-Protocol for this websocket connection

Specified by:
`getProtocol` in interface `WebSocket`
Returns:
the Sec-WebSocket-Protocol or null, if no draft available