# Class TextMessage

java.lang.Object
org.springframework.web.socket.AbstractWebSocketMessage<String>
org.springframework.web.socket.TextMessage

All Implemented Interfaces:
`WebSocketMessage<String>`

---

public final class TextMessage
extends AbstractWebSocketMessage<String>
A text WebSocket message.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Constructor Summary

Constructors

Constructor
Description
`TextMessage(byte[] payload)`

Create a new text WebSocket message from the given byte[].

`TextMessage(CharSequence payload)`

Create a new text WebSocket message from the given CharSequence payload.

`TextMessage(CharSequence payload,
 boolean isLast)`

Create a new text WebSocket message with the given payload representing the
full or partial message content.

- 

## Method Summary

Modifier and Type
Method
Description
`byte[]`
`asBytes()`
 
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

### TextMessage

public TextMessage(CharSequence payload)
Create a new text WebSocket message from the given CharSequence payload.

Parameters:
`payload` - the non-null payload

  - 

### TextMessage

public TextMessage(byte[] payload)
Create a new text WebSocket message from the given byte[]. It is assumed
the byte array can be encoded into an UTF-8 String.

Parameters:
`payload` - the non-null payload

  - 

### TextMessage

public TextMessage(CharSequence payload,
 boolean isLast)
Create a new text WebSocket message with the given payload representing the
full or partial message content. When the `isLast` boolean flag is set
to `false` the message is sent as partial content and more partial
messages will be expected until the boolean flag is set to `true`.

Parameters:
`payload` - the non-null payload
`isLast` - whether this the last part of a series of partial messages

- 

## Method Details

  - 

### getPayloadLength

public int getPayloadLength()
Description copied from interface: `WebSocketMessage`
Return the number of bytes contained in the message.

  - 

### asBytes

public byte[] asBytes()

  - 

### toStringPayload

protected String toStringPayload()

Specified by:
`toStringPayload` in class `AbstractWebSocketMessage<String>`