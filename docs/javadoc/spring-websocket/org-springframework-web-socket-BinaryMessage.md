# Class BinaryMessage

java.lang.Object
org.springframework.web.socket.AbstractWebSocketMessage<ByteBuffer>
org.springframework.web.socket.BinaryMessage

All Implemented Interfaces:
`WebSocketMessage<ByteBuffer>`

---

public final class BinaryMessage
extends AbstractWebSocketMessage<ByteBuffer>
A binary WebSocket message.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Constructor Summary

Constructors

Constructor
Description
`BinaryMessage(byte[] payload)`

Create a new binary WebSocket message with the given byte[] payload.

`BinaryMessage(byte[] payload,
 boolean isLast)`

Create a new binary WebSocket message with the given byte[] payload representing
the full or partial message content.

`BinaryMessage(byte[] payload,
 int offset,
 int length,
 boolean isLast)`

Create a new binary WebSocket message by wrapping an existing byte array.

`BinaryMessage(ByteBuffer payload)`

Create a new binary WebSocket message with the given ByteBuffer payload.

`BinaryMessage(ByteBuffer payload,
 boolean isLast)`

Create a new binary WebSocket message with the given payload representing the
full or partial message content.

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

### BinaryMessage

public BinaryMessage(ByteBuffer payload)
Create a new binary WebSocket message with the given ByteBuffer payload.

Parameters:
`payload` - the non-null payload

  - 

### BinaryMessage

public BinaryMessage(ByteBuffer payload,
 boolean isLast)
Create a new binary WebSocket message with the given payload representing the
full or partial message content. When the `isLast` boolean flag is set
to `false` the message is sent as partial content and more partial
messages will be expected until the boolean flag is set to `true`.

Parameters:
`payload` - the non-null payload
`isLast` - if the message is the last of a series of partial messages

  - 

### BinaryMessage

public BinaryMessage(byte[] payload)
Create a new binary WebSocket message with the given byte[] payload.

Parameters:
`payload` - a non-null payload; note that this value is not copied so care
must be taken not to modify the array.

  - 

### BinaryMessage

public BinaryMessage(byte[] payload,
 boolean isLast)
Create a new binary WebSocket message with the given byte[] payload representing
the full or partial message content. When the `isLast` boolean flag is set
to `false` the message is sent as partial content and more partial
messages will be expected until the boolean flag is set to `true`.

Parameters:
`payload` - a non-null payload; note that this value is not copied so care
must be taken not to modify the array.
`isLast` - if the message is the last of a series of partial messages

  - 

### BinaryMessage

public BinaryMessage(byte[] payload,
 int offset,
 int length,
 boolean isLast)
Create a new binary WebSocket message by wrapping an existing byte array.

Parameters:
`payload` - a non-null payload; note that this value is not copied so care
must be taken not to modify the array.
`offset` - the offset into the array where the payload starts
`length` - the length of the array considered for the payload
`isLast` - if the message is the last of a series of partial messages

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