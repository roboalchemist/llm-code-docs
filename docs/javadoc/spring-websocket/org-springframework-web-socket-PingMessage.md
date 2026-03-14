# Class PingMessage

java.lang.Object
org.springframework.web.socket.AbstractWebSocketMessage<ByteBuffer>
org.springframework.web.socket.PingMessage

All Implemented Interfaces:
`WebSocketMessage<ByteBuffer>`

---

public final class PingMessage
extends AbstractWebSocketMessage<ByteBuffer>
A WebSocket ping message.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Constructor Summary

Constructors

Constructor
Description
`PingMessage()`

Create a new ping message with an empty payload.

`PingMessage(ByteBuffer payload)`

Create a new ping message with the given ByteBuffer payload.

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

### PingMessage

public PingMessage()
Create a new ping message with an empty payload.

  - 

### PingMessage

public PingMessage(ByteBuffer payload)
Create a new ping message with the given ByteBuffer payload.

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