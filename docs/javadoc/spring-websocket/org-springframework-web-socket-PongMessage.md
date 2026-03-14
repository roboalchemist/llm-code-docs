# Class PongMessage

java.lang.Object
org.springframework.web.socket.AbstractWebSocketMessage<ByteBuffer>
org.springframework.web.socket.PongMessage

All Implemented Interfaces:
`WebSocketMessage<ByteBuffer>`

---

public final class PongMessage
extends AbstractWebSocketMessage<ByteBuffer>
A WebSocket pong message.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Constructor Summary

Constructors

Constructor
Description
`PongMessage()`

Create a new pong message with an empty payload.

`PongMessage(ByteBuffer payload)`

Create a new pong message with the given ByteBuffer payload.

- 

## Method Summary

Modifier and Type
Method
Description
`int`
`getPayloadLength()`

Return the number of bytes contained in the message.

`protected String`
`toStringPayload()`
 

### Methods inherited from class AbstractWebSocketMessage

`equals, getPayload, hashCode, isLast, toString`

### Methods inherited from class Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Constructor Details

  - 

### PongMessage

public PongMessage()
Create a new pong message with an empty payload.

  - 

### PongMessage

public PongMessage(ByteBuffer payload)
Create a new pong message with the given ByteBuffer payload.

Parameters:
`payload` - the non-null payload

- 

## Method Details

  - 

### getPayloadLength

public int getPayloadLength()
Description copied from interface: `WebSocketMessage`
Return the number of bytes contained in the message.

  - 

### toStringPayload

protected String toStringPayload()

Specified by:
`toStringPayload` in class `AbstractWebSocketMessage<ByteBuffer>`