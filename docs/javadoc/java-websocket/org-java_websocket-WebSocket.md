Package org.java_websocket

# Interface WebSocket




All Known Implementing Classes:
`WebSocketClient`, `WebSocketImpl`


---

public interface WebSocket






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
`closeConnection(int code,
 String message)`

This will close the connection immediately without a proper close handshake.

`<T> T`
`getAttachment()`

Getter for the connection attachment.

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

`SSLSession`
`getSSLSession()`

Returns the ssl session of websocket, if ssl/wss is used for this instance.

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














- 


## Method Details




  - 


### close

void close(int code,
 String message)
sends the closing handshake. may be send in response to an other handshake.

Parameters:
`code` - the closing code
`message` - the closing message




  - 


### close

void close(int code)
sends the closing handshake. may be send in response to an other handshake.

Parameters:
`code` - the closing code




  - 


### close

void close()
Convenience function which behaves like close(CloseFrame.NORMAL)



  - 


### closeConnection

void closeConnection(int code,
 String message)
This will close the connection immediately without a proper close handshake. The code and the
 message therefore won't be transferred over the wire also they will be forwarded to
 onClose/onWebsocketClose.

Parameters:
`code` - the closing code
`message` - the closing message




  - 


### send

void send(String text)
Send Text data to the other end.

Parameters:
`text` - the text data to send
Throws:
`WebsocketNotConnectedException` - websocket is not yet connected




  - 


### send

void send(ByteBuffer bytes)
Send Binary data (plain bytes) to the other end.

Parameters:
`bytes` - the binary data to send
Throws:
`IllegalArgumentException` - the data is null
`WebsocketNotConnectedException` - websocket is not yet connected




  - 


### send

void send(byte[] bytes)
Send Binary data (plain bytes) to the other end.

Parameters:
`bytes` - the byte array to send
Throws:
`IllegalArgumentException` - the data is null
`WebsocketNotConnectedException` - websocket is not yet connected




  - 


### sendFrame

void sendFrame(Framedata framedata)
Send a frame to the other end

Parameters:
`framedata` - the frame to send to the other end




  - 


### sendFrame

void sendFrame(Collection<Framedata> frames)
Send a collection of frames to the other end

Parameters:
`frames` - the frames to send to the other end




  - 


### sendPing

void sendPing()
Send a ping to the other end

Throws:
`WebsocketNotConnectedException` - websocket is not yet connected




  - 


### sendFragmentedFrame

void sendFragmentedFrame(Opcode op,
 ByteBuffer buffer,
 boolean fin)
Allows to send continuous/fragmented frames conveniently. 
 For more into on this frame type
 see http://tools.ietf.org/html/rfc6455#section-5.4

 


 If the first frame you send is also the last then it is not a fragmented frame and will
 received via onMessage instead of onFragmented even though it was send by this method.

Parameters:
`op` - This is only important for the first frame in the sequence. Opcode.TEXT,
               Opcode.BINARY are allowed.
`buffer` - The buffer which contains the payload. It may have no bytes remaining.
`fin` - true means the current frame is the last in the sequence.




  - 


### hasBufferedData

boolean hasBufferedData()
Checks if the websocket has buffered data

Returns:
has the websocket buffered data




  - 


### getRemoteSocketAddress

InetSocketAddress getRemoteSocketAddress()
Returns the address of the endpoint this socket is connected to, or `null` if it is
 unconnected.

Returns:
the remote socket address or null, if this socket is unconnected




  - 


### getLocalSocketAddress

InetSocketAddress getLocalSocketAddress()
Returns the address of the endpoint this socket is bound to, or `null` if it is not
 bound.

Returns:
the local socket address or null, if this socket is not bound




  - 


### isOpen

boolean isOpen()
Is the websocket in the state OPEN

Returns:
state equals ReadyState.OPEN




  - 


### isClosing

boolean isClosing()
Is the websocket in the state CLOSING

Returns:
state equals ReadyState.CLOSING




  - 


### isFlushAndClose

boolean isFlushAndClose()
Returns true when no further frames may be submitted
 This happens before the socket
 connection is closed.

Returns:
true when no further frames may be submitted




  - 


### isClosed

boolean isClosed()
Is the websocket in the state CLOSED

Returns:
state equals ReadyState.CLOSED




  - 


### getDraft

Draft getDraft()
Getter for the draft

Returns:
the used draft




  - 


### getReadyState

ReadyState getReadyState()
Retrieve the WebSocket 'ReadyState'. This represents the state of the connection. It returns a
 numerical value, as per W3C WebSockets specs.

Returns:
Returns '0 = CONNECTING', '1 = OPEN', '2 = CLOSING' or '3 = CLOSED'




  - 


### getResourceDescriptor

String getResourceDescriptor()
Returns the HTTP Request-URI as defined by http://tools.ietf.org/html/rfc2616#section-5.1.2

 If the opening handshake has not yet happened it will return null.

Returns:
Returns the decoded path component of this URI.




  - 


### setAttachment

<T> void setAttachment(T attachment)
Setter for an attachment on the socket connection. The attachment may be of any type.

Type Parameters:
`T` - The type of the attachment
Parameters:
`attachment` - The object to be attached to the user
Since:
1.3.7




  - 


### getAttachment

<T> T getAttachment()
Getter for the connection attachment.

Type Parameters:
`T` - The type of the attachment
Returns:
Returns the user attachment
Since:
1.3.7




  - 


### hasSSLSupport

boolean hasSSLSupport()
Does this websocket use an encrypted (wss/ssl) or unencrypted (ws) connection

Returns:
true, if the websocket does use wss and therefore has a SSLSession
Since:
1.4.1




  - 


### getSSLSession

SSLSession getSSLSession()
                  throws IllegalArgumentException
Returns the ssl session of websocket, if ssl/wss is used for this instance.

Returns:
the ssl session of this websocket instance
Throws:
`IllegalArgumentException` - the underlying channel does not use ssl (use hasSSLSupport()
                                  to check)
Since:
1.4.1




  - 


### getProtocol

IProtocol getProtocol()
Returns the used Sec-WebSocket-Protocol for this websocket connection

Returns:
the Sec-WebSocket-Protocol or null, if no draft available
Throws:
`IllegalArgumentException` - the underlying draft does not support a Sec-WebSocket-Protocol
Since:
1.5.2