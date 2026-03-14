Package org.java_websocket

# Interface WebSocketServerFactory




All Superinterfaces:
`WebSocketFactory`


All Known Implementing Classes:
`CustomSSLWebSocketServerFactory`, `DefaultSSLWebSocketServerFactory`, `DefaultWebSocketServerFactory`, `SSLParametersWebSocketServerFactory`


---

public interface WebSocketServerFactory
extends WebSocketFactory
Interface to encapsulate the required methods for a websocket factory






- 


## Method Summary





Modifier and Type
Method
Description
`void`
`close()`

Allows to shutdown the websocket factory for a clean shutdown

`WebSocketImpl`
`createWebSocket(WebSocketAdapter a,
 List<Draft> drafts)`

Create a new Websocket with the provided listener, drafts and socket

`WebSocketImpl`
`createWebSocket(WebSocketAdapter a,
 Draft d)`

Create a new Websocket with the provided listener, drafts and socket

`ByteChannel`
`wrapChannel(SocketChannel channel,
 SelectionKey key)`

Allows to wrap the SocketChannel( key.channel() ) to insert a protocol layer( like ssl or proxy
 authentication) beyond the ws layer.














- 


## Method Details




  - 


### createWebSocket

WebSocketImpl createWebSocket(WebSocketAdapter a,
 Draft d)
Description copied from interface: `WebSocketFactory`
Create a new Websocket with the provided listener, drafts and socket

Specified by:
`createWebSocket` in interface `WebSocketFactory`
Parameters:
`a` - The Listener for the WebsocketImpl
`d` - The draft which should be used
Returns:
A WebsocketImpl




  - 


### createWebSocket

WebSocketImpl createWebSocket(WebSocketAdapter a,
 List<Draft> drafts)
Description copied from interface: `WebSocketFactory`
Create a new Websocket with the provided listener, drafts and socket

Specified by:
`createWebSocket` in interface `WebSocketFactory`
Parameters:
`a` - The Listener for the WebsocketImpl
`drafts` - The drafts which should be used
Returns:
A WebsocketImpl




  - 


### wrapChannel

ByteChannel wrapChannel(SocketChannel channel,
 SelectionKey key)
                 throws IOException
Allows to wrap the SocketChannel( key.channel() ) to insert a protocol layer( like ssl or proxy
 authentication) beyond the ws layer.

Parameters:
`channel` - The SocketChannel to wrap
`key` - a SelectionKey of an open SocketChannel.
Returns:
The channel on which the read and write operations will be performed.

Throws:
`IOException` - may be thrown while writing on the channel




  - 


### close

void close()
Allows to shutdown the websocket factory for a clean shutdown