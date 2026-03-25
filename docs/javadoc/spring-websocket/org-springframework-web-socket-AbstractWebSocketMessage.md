# Class AbstractWebSocketMessage<T>

java.lang.Object
org.springframework.web.socket.AbstractWebSocketMessage<T>

Type Parameters:
`T` - the payload type

All Implemented Interfaces:
`WebSocketMessage<T>`

Direct Known Subclasses:
`BinaryMessage, PingMessage, PongMessage, TextMessage`

---

public abstract class AbstractWebSocketMessage<T>
extends Object
implements WebSocketMessage<T>
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
`boolean`
`equals(@Nullable Object other)`
 
`T`
`getPayload()`

Return the message payload (never `null`).

`int`
`hashCode()`
 
`boolean`
`isLast()`

Whether this is the last part of a message sent as a series of partial messages.

`String`
`toString()`
 
`protected abstract String`
`toStringPayload()`
 

### Methods inherited from class Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

### Methods inherited from interface WebSocketMessage

`getPayloadLength`

- 

## Method Details

  - 

### getPayload

public T getPayload()
Return the message payload (never `null`).

Specified by:
`getPayload` in interface `WebSocketMessage<T>`

  - 

### isLast

public boolean isLast()
Whether this is the last part of a message sent as a series of partial messages.

Specified by:
`isLast` in interface `WebSocketMessage<T>`

  - 

### equals

public boolean equals(@Nullable Object other)

Overrides:
`equals` in class `Object`

  - 

### hashCode

public int hashCode()

Overrides:
`hashCode` in class `Object`

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`

  - 

### toStringPayload

protected abstract String toStringPayload()