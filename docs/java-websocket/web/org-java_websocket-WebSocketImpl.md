Package org.java_websocket

# Class WebSocketImpl


java.lang.Object
org.java_websocket.WebSocketImpl



All Implemented Interfaces:
`WebSocket`


---

public class WebSocketImpl
extends Object
implements WebSocket
Represents one end (client or server) of a single WebSocketImpl connection. Takes care of the
 "handshake" phase, then allows for easy sending of text frames, and receiving frames through an
 event-based model.






- 


## Field Summary

Fields

Modifier and Type
Field
Description
`static final int`
`DEFAULT_PORT`

The default port of WebSockets, as defined in the spec.

`static final int`
`DEFAULT_WSS_PORT`

The default wss port of WebSockets, as defined in the spec.

`final BlockingQueue<ByteBuffer>`
`inQueue`

Queue of buffers that need to be processed

`final BlockingQueue<ByteBuffer>`
`outQueue`

Queue of buffers that need to be sent to the client.






- 


## Constructor Summary

Constructors

Constructor
Description
`WebSocketImpl(WebSocketListener listener,
 List<Draft> drafts)`

Creates a websocket with server role

`WebSocketImpl(WebSocketListener listener,
 Draft draft)`

creates a websocket with client role






- 


## Method Summary





Modifier and Type
Method
Description
`void`
`close()`

Convenience function which behaves like close(CloseFrame.NORMAL)

`void`
`close(int code)`

sends the closing handshake. may be send in response to an other handshake.

`void`
`close(int code,
 String message)`

sends the closing handshake. may be send in response to an other handshake.

`void`
`close(int code,
 String message,
 boolean remote)`
 
`void`
`close(InvalidDataException e)`
 
`void`
`closeConnection()`
 
`protected void`
`closeConnection(int code,
 boolean remote)`
 
`void`
`closeConnection(int code,
 String message)`

This will close the connection immediately without a proper close handshake.

`void`
`closeConnection(int code,
 String message,
 boolean remote)`

This will close the connection immediately without a proper close handshake.

`void`
`decode(ByteBuffer socketBuffer)`

Method to decode the provided ByteBuffer

`void`
`eot()`
 
`void`
`flushAndClose(int code,
 String message,
 boolean remote)`
 
`<T> T`
`getAttachment()`

Getter for the connection attachment.

`ByteChannel`
`getChannel()`
 
`Draft`
`getDraft()`

Getter for the draft

`InetSocketAddress`
`getLocalSocketAddress()`

Returns the address of the endpoint this socket is bound to, or `null` if it is not
 bound.

`IProtocol`
`getProtocol()`

Returns the used Sec-WebSocket-Protocol for this websocket connection

`ReadyState`
`getReadyState()`

Retrieve the WebSocket 'ReadyState'.

`InetSocketAddress`
`getRemoteSocketAddress()`

Returns the address of the endpoint this socket is connected to, or `null` if it is
 unconnected.

`String`
`getResourceDescriptor()`

Returns the HTTP Request-URI as defined by http://tools.ietf.org/html/rfc2616#section-5.1.2

 If the opening handshake has not yet happened it will return null.

`SelectionKey`
`getSelectionKey()`
 
`SSLSession`
`getSSLSession()`

Returns the ssl session of websocket, if ssl/wss is used for this instance.

`WebSocketListener`
`getWebSocketListener()`

Getter for the websocket listener

`WebSocketServer.WebSocketWorker`
`getWorkerThread()`
 
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

`void`
`send(byte[] bytes)`

Send Binary data (plain bytes) to the other end.

`void`
`send(String text)`

Send Text data to the other end.

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
`setChannel(ByteChannel channel)`
 
`void`
`setSelectionKey(SelectionKey key)`
 
`void`
`setWorkerThread(WebSocketServer.WebSocketWorker workerThread)`
 
`void`
`startHandshake(ClientHandshakeBuilder handshakedata)`
 
`String`
`toString()`
 
`void`
`updateLastPong()`

Update the timestamp when the last pong was received






### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`










- 


## Field Details




  - 


### DEFAULT_PORT

public static final int DEFAULT_PORT
The default port of WebSockets, as defined in the spec. If the nullary constructor is used,
 DEFAULT_PORT will be the port the WebSocketServer is binded to. Note that ports under 1024
 usually require root permissions.

See Also:




    - Constant Field Values







  - 


### DEFAULT_WSS_PORT

public static final int DEFAULT_WSS_PORT
The default wss port of WebSockets, as defined in the spec. If the nullary constructor is used,
 DEFAULT_WSS_PORT will be the port the WebSocketServer is binded to. Note that ports under 1024
 usually require root permissions.

See Also:




    - Constant Field Values







  - 


### outQueue

public final BlockingQueue<ByteBuffer> outQueue
Queue of buffers that need to be sent to the client.



  - 


### inQueue

public final BlockingQueue<ByteBuffer> inQueue
Queue of buffers that need to be processed








- 


## Constructor Details




  - 


### WebSocketImpl

public WebSocketImpl(WebSocketListener listener,
 List<Draft> drafts)
Creates a websocket with server role

Parameters:
`listener` - The listener for this instance
`drafts` - The drafts which should be used




  - 


### WebSocketImpl

public WebSocketImpl(WebSocketListener listener,
 Draft draft)
creates a websocket with client role

Parameters:
`listener` - The listener for this instance
`draft` - The draft which should be used









- 


## Method Details




  - 


### decode

public void decode(ByteBuffer socketBuffer)
Method to decode the provided ByteBuffer

Parameters:
`socketBuffer` - the ByteBuffer to decode




  - 


### close

public void close(int code,
 String message,
 boolean remote)



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
 String message,
 boolean remote)
This will close the connection immediately without a proper close handshake. The code and the
 message therefore won't be transferred over the wire also they will be forwarded to
 onClose/onWebsocketClose.

Parameters:
`code` - the closing code
`message` - the closing message
`remote` - Indicates who "generated" `code`.

                `true` means that this endpoint received the `code` from
                the other endpoint.
 false means this endpoint decided to send the given
                code,

                `remote` may also be true if this endpoint started the closing
                handshake since the other endpoint may not simply echo the `code` but
                close the connection the same time this endpoint does do but with an other
                `code`. 





  - 


### closeConnection

protected void closeConnection(int code,
 boolean remote)



  - 


### closeConnection

public void closeConnection()



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


### flushAndClose

public void flushAndClose(int code,
 String message,
 boolean remote)



  - 


### eot

public void eot()



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

public void close(InvalidDataException e)



  - 


### send

public void send(String text)
Send Text data to the other end.

Specified by:
`send` in interface `WebSocket`
Parameters:
`text` - the text data to send
Throws:
`WebsocketNotConnectedException` - websocket is not yet connected




  - 


### send

public void send(ByteBuffer bytes)
Send Binary data (plain bytes) to the other end.

Specified by:
`send` in interface `WebSocket`
Parameters:
`bytes` - the binary data to send
Throws:
`IllegalArgumentException` - the data is null
`WebsocketNotConnectedException` - websocket is not yet connected




  - 


### send

public void send(byte[] bytes)
Description copied from interface: `WebSocket`
Send Binary data (plain bytes) to the other end.

Specified by:
`send` in interface `WebSocket`
Parameters:
`bytes` - the byte array to send




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


### sendFrame

public void sendFrame(Collection<Framedata> frames)
Description copied from interface: `WebSocket`
Send a collection of frames to the other end

Specified by:
`sendFrame` in interface `WebSocket`
Parameters:
`frames` - the frames to send to the other end




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


### sendPing

public void sendPing()
              throws NullPointerException
Description copied from interface: `WebSocket`
Send a ping to the other end

Specified by:
`sendPing` in interface `WebSocket`
Throws:
`NullPointerException`




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


### startHandshake

public void startHandshake(ClientHandshakeBuilder handshakedata)
                    throws InvalidHandshakeException

Throws:
`InvalidHandshakeException`




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


### isClosing

public boolean isClosing()
Description copied from interface: `WebSocket`
Is the websocket in the state CLOSING

Specified by:
`isClosing` in interface `WebSocket`
Returns:
state equals ReadyState.CLOSING




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


### getReadyState

public ReadyState getReadyState()
Description copied from interface: `WebSocket`
Retrieve the WebSocket 'ReadyState'. This represents the state of the connection. It returns a
 numerical value, as per W3C WebSockets specs.

Specified by:
`getReadyState` in interface `WebSocket`
Returns:
Returns '0 = CONNECTING', '1 = OPEN', '2 = CLOSING' or '3 = CLOSED'




  - 


### setSelectionKey

public void setSelectionKey(SelectionKey key)

Parameters:
`key` - the selection key of this implementation




  - 


### getSelectionKey

public SelectionKey getSelectionKey()

Returns:
the selection key of this implementation




  - 


### toString

public String toString()

Overrides:
`toString` in class `Object`




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


### getDraft

public Draft getDraft()
Description copied from interface: `WebSocket`
Getter for the draft

Specified by:
`getDraft` in interface `WebSocket`
Returns:
the used draft




  - 


### close

public void close()
Description copied from interface: `WebSocket`
Convenience function which behaves like close(CloseFrame.NORMAL)

Specified by:
`close` in interface `WebSocket`




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


### updateLastPong

public void updateLastPong()
Update the timestamp when the last pong was received



  - 


### getWebSocketListener

public WebSocketListener getWebSocketListener()
Getter for the websocket listener

Returns:
the websocket listener associated with this instance




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


### getChannel

public ByteChannel getChannel()



  - 


### setChannel

public void setChannel(ByteChannel channel)



  - 


### getWorkerThread

public WebSocketServer.WebSocketWorker getWorkerThread()



  - 


### setWorkerThread

public void setWorkerThread(WebSocketServer.WebSocketWorker workerThread)