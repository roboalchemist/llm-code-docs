Package org.java_websocket

# Class WebSocketAdapter


java.lang.Object
org.java_websocket.WebSocketAdapter



All Implemented Interfaces:
`WebSocketListener`


Direct Known Subclasses:
`AbstractWebSocket`


---

public abstract class WebSocketAdapter
extends Object
implements WebSocketListener
This class default implements all methods of the WebSocketListener that can be overridden
 optionally when advances functionalities is needed.







- 


## Constructor Summary

Constructors

Constructor
Description
`WebSocketAdapter()`
 





- 


## Method Summary





Modifier and Type
Method
Description
`PingFrame`
`onPreparePing(WebSocket conn)`

Default implementation for onPreparePing, returns a (cached) PingFrame that has no application
 data.

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

This default implementation does not do anything.

`void`
`onWebsocketHandshakeSentAsClient(WebSocket conn,
 ClientHandshake request)`

This default implementation does not do anything which will cause the connections to always
 progress.

`void`
`onWebsocketPing(WebSocket conn,
 Framedata f)`

This default implementation will send a pong in response to the received ping.

`void`
`onWebsocketPong(WebSocket conn,
 Framedata f)`

This default implementation does not do anything.






### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`


### Methods inherited from interface org.java_websocket.WebSocketListener

`getLocalSocketAddress, getRemoteSocketAddress, onWebsocketClose, onWebsocketCloseInitiated, onWebsocketClosing, onWebsocketError, onWebsocketMessage, onWebsocketMessage, onWebsocketOpen, onWriteDemand`










- 


## Constructor Details




  - 


### WebSocketAdapter

public WebSocketAdapter()








- 


## Method Details




  - 


### onWebsocketHandshakeReceivedAsServer

public ServerHandshakeBuilder onWebsocketHandshakeReceivedAsServer(WebSocket conn,
 Draft draft,
 ClientHandshake request)
                                                            throws InvalidDataException
This default implementation does not do anything. Go ahead and overwrite it.

Specified by:
`onWebsocketHandshakeReceivedAsServer` in interface `WebSocketListener`
Parameters:
`conn` - The WebSocket related to this event
`draft` - The protocol draft the client uses to connect
`request` - The opening http message send by the client. Can be used to access additional
                fields like cookies.
Returns:
Returns an incomplete handshake containing all optional fields
Throws:
`InvalidDataException` - Throwing this exception will cause this handshake to be rejected
See Also:




    - `WebSocketListener.onWebsocketHandshakeReceivedAsServer(WebSocket, Draft, ClientHandshake)`







  - 


### onWebsocketHandshakeReceivedAsClient

public void onWebsocketHandshakeReceivedAsClient(WebSocket conn,
 ClientHandshake request,
 ServerHandshake response)
                                          throws InvalidDataException
Description copied from interface: `WebSocketListener`
Called on the client side when the socket connection is first established, and the
 WebSocketImpl handshake response has been received.

Specified by:
`onWebsocketHandshakeReceivedAsClient` in interface `WebSocketListener`
Parameters:
`conn` - The WebSocket related to this event
`request` - The handshake initially send out to the server by this websocket.
`response` - The handshake the server sent in response to the request.
Throws:
`InvalidDataException` - Allows the client to reject the connection with the server in
                              respect of its handshake response.




  - 


### onWebsocketHandshakeSentAsClient

public void onWebsocketHandshakeSentAsClient(WebSocket conn,
 ClientHandshake request)
                                      throws InvalidDataException
This default implementation does not do anything which will cause the connections to always
 progress.

Specified by:
`onWebsocketHandshakeSentAsClient` in interface `WebSocketListener`
Parameters:
`conn` - The WebSocket related to this event
`request` - The handshake sent to the server by this websocket
Throws:
`InvalidDataException` - Allows the client to stop the connection from progressing
See Also:




    - `WebSocketListener.onWebsocketHandshakeSentAsClient(WebSocket, ClientHandshake)`







  - 


### onWebsocketPing

public void onWebsocketPing(WebSocket conn,
 Framedata f)
This default implementation will send a pong in response to the received ping. The pong frame
 will have the same payload as the ping frame.

Specified by:
`onWebsocketPing` in interface `WebSocketListener`
Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`f` - The ping frame. Control frames may contain payload.
See Also:




    - `WebSocketListener.onWebsocketPing(WebSocket, Framedata)`







  - 


### onWebsocketPong

public void onWebsocketPong(WebSocket conn,
 Framedata f)
This default implementation does not do anything. Go ahead and overwrite it.

Specified by:
`onWebsocketPong` in interface `WebSocketListener`
Parameters:
`conn` - The `WebSocket` instance this event is occurring on.
`f` - The pong frame. Control frames may contain payload.
See Also:




    - `WebSocketListener.onWebsocketPong(WebSocket, Framedata)`







  - 


### onPreparePing

public PingFrame onPreparePing(WebSocket conn)
Default implementation for onPreparePing, returns a (cached) PingFrame that has no application
 data.

Specified by:
`onPreparePing` in interface `WebSocketListener`
Parameters:
`conn` - The `WebSocket` connection from which the ping frame will be sent.
Returns:
PingFrame to be sent.
See Also:




    - `WebSocketListener.onPreparePing(WebSocket)`