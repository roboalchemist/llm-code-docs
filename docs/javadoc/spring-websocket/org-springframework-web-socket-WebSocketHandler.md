# Interface WebSocketHandler

All Known Implementing Classes:
`AbstractWebSocketHandler, BinaryWebSocketHandler, ExceptionWebSocketHandlerDecorator, LoggingWebSocketHandlerDecorator, PerConnectionWebSocketHandler, SockJsWebSocketHandler, SubProtocolWebSocketHandler, TextWebSocketHandler, WebSocketHandlerDecorator`

---

public interface WebSocketHandler
A handler for WebSocket messages and lifecycle events.

Implementations of this interface are encouraged to handle exceptions locally where
it makes sense or alternatively let the exception bubble up in which case by default
the exception is logged and the session closed with
`SERVER_ERROR(1011)`. The exception handling
strategy is provided by
`ExceptionWebSocketHandlerDecorator` and it can be customized or replaced by decorating
the `WebSocketHandler` with a different decorator.

Since:
4.0
Author:
Rossen Stoyanchev, Phillip Webb

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`afterConnectionClosed(WebSocketSession session,
 CloseStatus closeStatus)`

Invoked after the WebSocket connection has been closed by either side, or after a
transport error has occurred.

`void`
`afterConnectionEstablished(WebSocketSession session)`

Invoked after WebSocket negotiation has succeeded and the WebSocket connection is
opened and ready for use.

`void`
`handleMessage(WebSocketSession session,
 WebSocketMessage<?> message)`

Invoked when a new WebSocket message arrives.

`void`
`handleTransportError(WebSocketSession session,
 Throwable exception)`

Handle an error from the underlying WebSocket message transport.

`boolean`
`supportsPartialMessages()`

Whether the WebSocketHandler handles partial messages.

- 

## Method Details

  - 

### afterConnectionEstablished

void afterConnectionEstablished(WebSocketSession session)
                         throws Exception
Invoked after WebSocket negotiation has succeeded and the WebSocket connection is
opened and ready for use.

Throws:
`Exception` - this method can handle or propagate exceptions; see class-level
Javadoc for details.

  - 

### handleMessage

void handleMessage(WebSocketSession session,
 WebSocketMessage<?> message)
            throws Exception
Invoked when a new WebSocket message arrives.

Throws:
`Exception` - this method can handle or propagate exceptions; see class-level
Javadoc for details.

  - 

### handleTransportError

void handleTransportError(WebSocketSession session,
 Throwable exception)
                   throws Exception
Handle an error from the underlying WebSocket message transport.

Throws:
`Exception` - this method can handle or propagate exceptions; see class-level
Javadoc for details.

  - 

### afterConnectionClosed

void afterConnectionClosed(WebSocketSession session,
 CloseStatus closeStatus)
                    throws Exception
Invoked after the WebSocket connection has been closed by either side, or after a
transport error has occurred. Although the session may technically still be open,
depending on the underlying implementation, sending messages at this point is
discouraged and most likely will not succeed.

Throws:
`Exception` - this method can handle or propagate exceptions; see class-level
Javadoc for details.

  - 

### supportsPartialMessages

boolean supportsPartialMessages()
Whether the WebSocketHandler handles partial messages. If this flag is set to
`true` and the underlying WebSocket server supports partial messages,
then a large WebSocket message, or one of an unknown size may be split and
maybe received over multiple calls to
`handleMessage(WebSocketSession, WebSocketMessage)`. The flag
`WebSocketMessage.isLast()` indicates if
the message is partial and whether it is the last part.