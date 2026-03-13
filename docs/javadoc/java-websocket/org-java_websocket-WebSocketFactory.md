Package org.java_websocket

# Interface WebSocketFactory




All Known Subinterfaces:
`WebSocketServerFactory`


All Known Implementing Classes:
`CustomSSLWebSocketServerFactory`, `DefaultSSLWebSocketServerFactory`, `DefaultWebSocketServerFactory`, `SSLParametersWebSocketServerFactory`


---

public interface WebSocketFactory






- 


## Method Summary





Modifier and Type
Method
Description
`WebSocket`
`createWebSocket(WebSocketAdapter a,
 List<Draft> drafts)`

Create a new Websocket with the provided listener, drafts and socket

`WebSocket`
`createWebSocket(WebSocketAdapter a,
 Draft d)`

Create a new Websocket with the provided listener, drafts and socket














- 


## Method Details




  - 


### createWebSocket

WebSocket createWebSocket(WebSocketAdapter a,
 Draft d)
Create a new Websocket with the provided listener, drafts and socket

Parameters:
`a` - The Listener for the WebsocketImpl
`d` - The draft which should be used
Returns:
A WebsocketImpl




  - 


### createWebSocket

WebSocket createWebSocket(WebSocketAdapter a,
 List<Draft> drafts)
Create a new Websocket with the provided listener, drafts and socket

Parameters:
`a` - The Listener for the WebsocketImpl
`drafts` - The drafts which should be used
Returns:
A WebsocketImpl