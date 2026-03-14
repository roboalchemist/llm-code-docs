# Interface WebSocketClient

All Known Implementing Classes:
`AbstractWebSocketClient, SockJsClient, StandardWebSocketClient`

---

public interface WebSocketClient
Contract for initiating a WebSocket request. As an alternative considering using the
declarative style `WebSocketConnectionManager` that starts a WebSocket connection
to a pre-configured URI when the application starts.

Since:
4.0
Author:
Rossen Stoyanchev
See Also:

- `WebSocketConnectionManager`

- 

## Method Summary

Modifier and Type
Method
Description
`CompletableFuture<WebSocketSession>`
`execute(WebSocketHandler webSocketHandler,
 String uriTemplate,
 @Nullable Object... uriVariables)`

Execute a handshake request to the given url and handle the resulting
WebSocket session with the given handler.

`CompletableFuture<WebSocketSession>`
`execute(WebSocketHandler webSocketHandler,
 @Nullable WebSocketHttpHeaders headers,
 URI uri)`

Execute a handshake request to the given url and handle the resulting
WebSocket session with the given handler.

- 

## Method Details

  - 

### execute

CompletableFuture<WebSocketSession> execute(WebSocketHandler webSocketHandler,
 String uriTemplate,
 @Nullable Object... uriVariables)
Execute a handshake request to the given url and handle the resulting
WebSocket session with the given handler.

Parameters:
`webSocketHandler` - the session handler
`uriTemplate` - the url template
`uriVariables` - the variables to expand the template
Returns:
a future that completes when the session is available
Since:
6.0

  - 

### execute

CompletableFuture<WebSocketSession> execute(WebSocketHandler webSocketHandler,
 @Nullable WebSocketHttpHeaders headers,
 URI uri)
Execute a handshake request to the given url and handle the resulting
WebSocket session with the given handler.

Parameters:
`webSocketHandler` - the session handler
`uri` - the url
Returns:
a future that completes when the session is available
Since:
6.0