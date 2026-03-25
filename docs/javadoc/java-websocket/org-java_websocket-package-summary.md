# Package org.java_websocket



---

package org.java_websocket




- 

Related Packages

Package
Description
org.java_websocket.client

This package encapsulates all implementations in relation with the WebSocketClient.

org.java_websocket.drafts

This package encapsulates all implementations in relation with the WebSocket drafts.

org.java_websocket.enums

This package encapsulates all enums.

org.java_websocket.exceptions

This package encapsulates all implementations in relation with the exceptions thrown in this
 lib.

org.java_websocket.extensions

This package encapsulates all interfaces and implementations in relation with the WebSocket
 Sec-WebSocket-Extensions.

org.java_websocket.framing

This package encapsulates all interfaces and implementations in relation with the WebSocket
 frames.

org.java_websocket.handshake

This package encapsulates all interfaces and implementations in relation with the WebSocket
 handshake.

org.java_websocket.interfaces

This package encapsulates all new interfaces.

org.java_websocket.protocols

This package encapsulates all interfaces and implementations in relation with the WebSocket
 Sec-WebSocket-Protocol.

org.java_websocket.server

This package encapsulates all implementations in relation with the WebSocketServer.

org.java_websocket.util

This package encapsulates the utility classes.





- 




Class
Description
AbstractWebSocket

Base class for additional implementations for the server as well as the client

AbstractWrappedByteChannel
Deprecated. 
SocketChannelIOHelper
 
SSLSocketChannel

A class that represents an SSL/TLS peer, and can be extended to create a client or a server.

SSLSocketChannel2

Implements the relevant portions of the SocketChannel interface with the SSLEngine wrapper.

WebSocket
 
WebSocketAdapter

This class default implements all methods of the WebSocketListener that can be overridden
 optionally when advances functionalities is needed.


WebSocketFactory
 
WebSocketImpl

Represents one end (client or server) of a single WebSocketImpl connection.

WebSocketListener

Implemented by `WebSocketClient` and `WebSocketServer`.

WebSocketServerFactory

Interface to encapsulate the required methods for a websocket factory

WrappedByteChannel