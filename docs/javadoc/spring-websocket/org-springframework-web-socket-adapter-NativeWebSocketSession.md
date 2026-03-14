# Interface NativeWebSocketSession

All Superinterfaces:
`AutoCloseable, Closeable, WebSocketSession`

All Known Implementing Classes:
`AbstractWebSocketSession, JettyWebSocketSession, StandardWebSocketSession, WebSocketClientSockJsSession, WebSocketServerSockJsSession`

---

public interface NativeWebSocketSession
extends WebSocketSession
A `WebSocketSession` that exposes the underlying, native WebSocketSession
through a getter.

Since:
4.0
Author:
Rossen Stoyanchev

- 

## Method Summary

Modifier and Type
Method
Description
`Object`
`getNativeSession()`

Return the underlying native WebSocketSession.

`<T> @Nullable T`
`getNativeSession(@Nullable Class<T> requiredType)`

Return the underlying native WebSocketSession, if available.

### Methods inherited from interface WebSocketSession

`close, close, getAcceptedProtocol, getAttributes, getBinaryMessageSizeLimit, getExtensions, getHandshakeHeaders, getId, getLocalAddress, getPrincipal, getRemoteAddress, getTextMessageSizeLimit, getUri, isOpen, sendMessage, setBinaryMessageSizeLimit, setTextMessageSizeLimit`

- 

## Method Details

  - 

### getNativeSession

Object getNativeSession()
Return the underlying native WebSocketSession.

  - 

### getNativeSession

<T> @Nullable T getNativeSession(@Nullable Class<T> requiredType)
Return the underlying native WebSocketSession, if available.

Parameters:
`requiredType` - the required type of the session
Returns:
the native session of the required type,
or `null` if not available