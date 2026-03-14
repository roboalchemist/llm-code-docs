Package org.java_websocket

# Interface WebSocketListener




All Known Implementing Classes:
`AbstractWebSocket`, `WebSocketAdapter`, `WebSocketClient`, `WebSocketServer`


---

public interface WebSocketListener
Implemented by `WebSocketClient` and `WebSocketServer`. The methods within are
 called by `WebSocket`. Almost every method takes a first parameter conn which represents
 the source of the respective event.






- 


## Method Summary





Modifier and Type
Method
Description
`InetSocketAddress`
`getLocalSocketAddress(WebSocket conn)`
 
`InetSocketAddress`
`getRemoteSocketAddress(WebSocket conn)`
 
`PingFrame`
`onPreparePing(WebSocket conn)`

Called just before a ping frame is sent, in order to allow users to customize their ping frame
 data.

`void`
`onWebsocketClose(WebSocket ws,
 int code,
 String reason,
 boolean remote)`

Called after `WebSocket#close` is explicity called, or when the other end of the
 WebSocket connection is closed.

`void`
`onWebsocketCloseInitiated(WebSocket ws,
 int code,
 String reason)`

send when this peer sends a close handshake

`void`
`onWebsocketClosing(WebSocket ws,
 int code,
 String reason,
 boolean remote)`

Called as soon as no further frames are accepted

`void`
`onWebsocketError(WebSocket conn,
 Exception ex)`

Called if an exception worth noting occurred.

`void`
`onWebsocketHandshakeReceivedAsClient(WebSocket conn,
 ClientHandshake request,
 ServerHandshake response)`

Called on the client side when the socket connection is first established, and the
 WebSocketImpl handshake response has been received.

`ServerHandshakeBuilder`
`onWebsocketHandshakeReceivedAsServer(WebSocket conn,
 Draft draft,
 ClientHandshake request)`

Called on the server side when the socket connection is first established, and the WebSocket
 handshake has been received.

`void`
`onWebsocketHandshakeSentAsClient(WebSocket conn,
 ClientHandshake request)`

Called on the client side when the socket connection is first established, and the
 WebSocketImpl handshake has just been sent.

`void`
`onWebsocketMessage(WebSocket conn,
 String message)`

Called when an entire text frame has been received.

`void`
`onWebsocketMessage(WebSocket conn,
 ByteBuffer blob)`

Called when an entire binary frame has been received.

`void`
`onWebsocketOpen(WebSocket conn,
 Handshakedata d)`

Called after onHandshakeReceived returns true.

`void`
`onWebsocketPing(WebSocket conn,
 Framedata f)`

Called a ping frame has been received.

`void`
`onWebsocketPong(WebSocket conn,
 Framedata f)`

Called when a pong frame is received.

`void`
`onWriteDemand(WebSocket conn)`

This method is used to inform the selector thread that there is data queued to be written to
 the socket.














- 


## Method Details




  - 


### onWebsocketHandshakeReceivedAsServer

ServerHandshakeBuilder onWebsocketHandshakeReceivedAsServer(WebSocket conn,
 Draft draft,
 ClientHandshake request)
                                                     throws InvalidDataException
Called on the server side when the socket connection is first established, and the WebSocket
 handshake has been received. This method allows to deny connections based on the received
 handshake.
 By default this method only requires protocol compliance.

Parameters:
`conn` - The WebSocket related to this event
`draft` - The protocol draft the client uses to connect
`request` - The opening http message send by the client. Can be used to access additional
                fields like cookies.
Returns:
Returns an incomplete handshake containing all optional fields
Throws:
`InvalidDataException` - Throwing this exception will cause this handshake to be rejected




  - 


### onWebsocketHandshakeReceivedAsClient

void onWebsocketHandshakeReceivedAsClient(WebSocket conn,
 ClientHandshake request,
 ServerHandshake response)
                                   throws InvalidDataException
Called on the client side when the socket connection is first established, and the
 WebSocketImpl handshake response has been received.

Parameters:
`conn` - The WebSocket related to this event
`request` - The handshake initially send out to the server by this websocket.
`response` - The handshake the server sent in response to the request.
Throws:
`InvalidDataException` - Allows the client to reject the connection with the server in
                              respect of its handshake response.




  - 


### onWebsocketHandshakeSentAsClient

void onWebsocketHandshakeSentAsClient(WebSocket conn,
 ClientHandshake request)
                               throws InvalidDataException
Called on the client side when the socket connection is first established, and the
 WebSocketImpl handshake has just been sent.

Parameters:
`conn` - The WebSocket related to this event
`request` - The handshake sent to the server by this websocket
Throws:
`InvalidDataException` - Allows the client to stop the connection from progressing




  - 


### onWebsocketMessage

void onWebsocketMessage(WebSocket conn,
 String message)
Called when an entire text frame has been received. Do whatever you want here...

Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`message` - The UTF-8 decoded message that was received.




  - 


### onWebsocketMessage

void onWebsocketMessage(WebSocket conn,
 ByteBuffer blob)
Called when an entire binary frame has been received. Do whatever you want here...

Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`blob` - The binary message that was received.




  - 


### onWebsocketOpen

void onWebsocketOpen(WebSocket conn,
 Handshakedata d)
Called after onHandshakeReceived returns true. Indicates that a complete
 WebSocket connection has been established, and we are ready to send/receive data.

Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`d` - The handshake of the websocket instance




  - 


### onWebsocketClose

void onWebsocketClose(WebSocket ws,
 int code,
 String reason,
 boolean remote)
Called after `WebSocket#close` is explicity called, or when the other end of the
 WebSocket connection is closed.

Parameters:
`ws` - The `WebSocket` instance this event is occurring on.
`code` - The codes can be looked up here: `CloseFrame`
`reason` - Additional information string
`remote` - Returns whether or not the closing of the connection was initiated by the remote
               host.




  - 


### onWebsocketClosing

void onWebsocketClosing(WebSocket ws,
 int code,
 String reason,
 boolean remote)
Called as soon as no further frames are accepted

Parameters:
`ws` - The `WebSocket` instance this event is occurring on.
`code` - The codes can be looked up here: `CloseFrame`
`reason` - Additional information string
`remote` - Returns whether or not the closing of the connection was initiated by the remote
               host.




  - 


### onWebsocketCloseInitiated

void onWebsocketCloseInitiated(WebSocket ws,
 int code,
 String reason)
send when this peer sends a close handshake

Parameters:
`ws` - The `WebSocket` instance this event is occurring on.
`code` - The codes can be looked up here: `CloseFrame`
`reason` - Additional information string




  - 


### onWebsocketError

void onWebsocketError(WebSocket conn,
 Exception ex)
Called if an exception worth noting occurred. If an error causes the connection to fail onClose
 will be called additionally afterwards.

Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`ex` - The exception that occurred. 
 Might be null if the exception is not related to
             any specific connection. For example if the server port could not be bound.




  - 


### onWebsocketPing

void onWebsocketPing(WebSocket conn,
 Framedata f)
Called a ping frame has been received. This method must send a corresponding pong by itself.

Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`f` - The ping frame. Control frames may contain payload.




  - 


### onPreparePing

PingFrame onPreparePing(WebSocket conn)
Called just before a ping frame is sent, in order to allow users to customize their ping frame
 data.

Parameters:
`conn` - The `WebSocket` connection from which the ping frame will be sent.
Returns:
PingFrame to be sent.




  - 


### onWebsocketPong

void onWebsocketPong(WebSocket conn,
 Framedata f)
Called when a pong frame is received.

Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`f` - The pong frame. Control frames may contain payload.




  - 


### onWriteDemand

void onWriteDemand(WebSocket conn)
This method is used to inform the selector thread that there is data queued to be written to
 the socket.

Parameters:
`conn` - The `WebSocket` instance this event is occurring on.




  - 


### getLocalSocketAddress

InetSocketAddress getLocalSocketAddress(WebSocket conn)

Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
Returns:
Returns the address of the endpoint this socket is bound to.
See Also:




    - `WebSocket.getLocalSocketAddress()`







  - 


### getRemoteSocketAddress

InetSocketAddress getRemoteSocketAddress(WebSocket conn)

Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
Returns:
Returns the address of the endpoint this socket is connected to, or`null` if it
 is unconnected.
See Also:




    - `WebSocket.getRemoteSocketAddress()`