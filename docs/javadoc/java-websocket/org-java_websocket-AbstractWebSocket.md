Package org.java_websocket

# Class AbstractWebSocket


java.lang.Object
org.java_websocket.WebSocketAdapter
org.java_websocket.AbstractWebSocket




All Implemented Interfaces:
`WebSocketListener`


Direct Known Subclasses:
`WebSocketClient`, `WebSocketServer`


---

public abstract class AbstractWebSocket
extends WebSocketAdapter
Base class for additional implementations for the server as well as the client






- 


## Field Summary

Fields

Modifier and Type
Field
Description
`protected static int`
`DEFAULT_READ_BUFFER_SIZE`

Used for internal buffer allocations when the socket buffer size is not specified.






- 


## Constructor Summary

Constructors

Constructor
Description
`AbstractWebSocket()`
 





- 


## Method Summary





Modifier and Type
Method
Description
`int`
`getConnectionLostTimeout()`

Get the interval checking for lost connections Default is 60 seconds

`protected abstract Collection<WebSocket>`
`getConnections()`

Getter to get all the currently available connections

`int`
`getReceiveBufferSize()`

Returns the TCP receive buffer size that will be used for sockets (or zero, if not explicitly set).

`boolean`
`isDaemon()`

Getter for daemon

`boolean`
`isReuseAddr()`

Tests Tests if SO_REUSEADDR is enabled.

`boolean`
`isTcpNoDelay()`

Tests if TCP_NODELAY is enabled.

`void`
`setConnectionLostTimeout(int connectionLostTimeout)`

Setter for the interval checking for lost connections A value lower or equal 0 results in the
 check to be deactivated

`void`
`setDaemon(boolean daemon)`

Setter for daemon

`void`
`setReceiveBufferSize(int receiveBufferSize)`

Sets the TCP receive buffer size that will be used for sockets.

`void`
`setReuseAddr(boolean reuseAddr)`

Setter for soReuseAddr

`void`
`setTcpNoDelay(boolean tcpNoDelay)`

Setter for tcpNoDelay

`protected void`
`startConnectionLostTimer()`

Start the connection lost timer

`protected void`
`stopConnectionLostTimer()`

Stop the connection lost timer






### Methods inherited from class org.java_websocket.WebSocketAdapter

`onPreparePing, onWebsocketHandshakeReceivedAsClient, onWebsocketHandshakeReceivedAsServer, onWebsocketHandshakeSentAsClient, onWebsocketPing, onWebsocketPong`


### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`


### Methods inherited from interface org.java_websocket.WebSocketListener

`getLocalSocketAddress, getRemoteSocketAddress, onWebsocketClose, onWebsocketCloseInitiated, onWebsocketClosing, onWebsocketError, onWebsocketMessage, onWebsocketMessage, onWebsocketOpen, onWriteDemand`










- 


## Field Details




  - 


### DEFAULT_READ_BUFFER_SIZE

protected static int DEFAULT_READ_BUFFER_SIZE
Used for internal buffer allocations when the socket buffer size is not specified.








- 


## Constructor Details




  - 


### AbstractWebSocket

public AbstractWebSocket()








- 


## Method Details




  - 


### getConnectionLostTimeout

public int getConnectionLostTimeout()
Get the interval checking for lost connections Default is 60 seconds

Returns:
the interval in seconds
Since:
1.3.4




  - 


### setConnectionLostTimeout

public void setConnectionLostTimeout(int connectionLostTimeout)
Setter for the interval checking for lost connections A value lower or equal 0 results in the
 check to be deactivated

Parameters:
`connectionLostTimeout` - the interval in seconds
Since:
1.3.4




  - 


### stopConnectionLostTimer

protected void stopConnectionLostTimer()
Stop the connection lost timer

Since:
1.3.4




  - 


### startConnectionLostTimer

protected void startConnectionLostTimer()
Start the connection lost timer

Since:
1.3.4




  - 


### getConnections

protected abstract Collection<WebSocket> getConnections()
Getter to get all the currently available connections

Returns:
the currently available connections
Since:
1.3.4




  - 


### isTcpNoDelay

public boolean isTcpNoDelay()
Tests if TCP_NODELAY is enabled.

Returns:
a boolean indicating whether or not TCP_NODELAY is enabled for new connections.
Since:
1.3.3




  - 


### setTcpNoDelay

public void setTcpNoDelay(boolean tcpNoDelay)
Setter for tcpNoDelay
 


 Enable/disable TCP_NODELAY (disable/enable Nagle's algorithm) for new connections

Parameters:
`tcpNoDelay` - true to enable TCP_NODELAY, false to disable.
Since:
1.3.3




  - 


### isReuseAddr

public boolean isReuseAddr()
Tests Tests if SO_REUSEADDR is enabled.

Returns:
a boolean indicating whether or not SO_REUSEADDR is enabled.
Since:
1.3.5




  - 


### setReuseAddr

public void setReuseAddr(boolean reuseAddr)
Setter for soReuseAddr
 


 Enable/disable SO_REUSEADDR for the socket

Parameters:
`reuseAddr` - whether to enable or disable SO_REUSEADDR
Since:
1.3.5




  - 


### isDaemon

public boolean isDaemon()
Getter for daemon

Returns:
whether internal threads are spawned in daemon mode
Since:
1.5.6




  - 


### setDaemon

public void setDaemon(boolean daemon)
Setter for daemon
 


 Controls whether or not internal threads are spawned in daemon mode

Since:
1.5.6




  - 


### getReceiveBufferSize

public int getReceiveBufferSize()
Returns the TCP receive buffer size that will be used for sockets (or zero, if not explicitly set).

Since:
1.5.7
See Also:




    - `Socket.setReceiveBufferSize(int)`







  - 


### setReceiveBufferSize

public void setReceiveBufferSize(int receiveBufferSize)
Sets the TCP receive buffer size that will be used for sockets.
 If this is not explicitly set (or set to zero), the system default is used.

Since:
1.5.7
See Also:




    - `Socket.setReceiveBufferSize(int)`