# Interface WebSocketMessage<T>

Type Parameters:
`T` - the payload type

All Known Implementing Classes:
`AbstractWebSocketMessage, BinaryMessage, PingMessage, PongMessage, TextMessage`

---

public interface WebSocketMessage<T>
A message that can be handled or sent on a WebSocket connection.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Method Summary

Modifier and Type
Method
Description
`T`
`getPayload()`

Return the message payload (never `null`).

`int`
`getPayloadLength()`

Return the number of bytes contained in the message.

`boolean`
`isLast()`

When partial message support is available and requested via
`WebSocketHandler.supportsPartialMessages()`,
this method returns `true` if the current message is the last part of the
complete WebSocket message sent by the client.

- 

## Method Details

  - 

### getPayload

T getPayload()
Return the message payload (never `null`).

  - 

### getPayloadLength

int getPayloadLength()
Return the number of bytes contained in the message.

  - 

### isLast

boolean isLast()
When partial message support is available and requested via
`WebSocketHandler.supportsPartialMessages()`,
this method returns `true` if the current message is the last part of the
complete WebSocket message sent by the client. Otherwise `false` is returned
if partial message support is either not available or not enabled.