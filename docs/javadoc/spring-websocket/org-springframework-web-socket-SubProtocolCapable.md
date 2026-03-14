# Interface SubProtocolCapable

All Known Implementing Classes:
`SockJsWebSocketHandler, SubProtocolWebSocketHandler`

---

public interface SubProtocolCapable
An interface for WebSocket handlers that support sub-protocols as defined in RFC 6455.

Since:
4.0
Author:
Rossen Stoyanchev
See Also:

- `WebSocketHandler`

- RFC-6455 section 1.9

- 

## Method Summary

Modifier and Type
Method
Description
`List<String>`
`getSubProtocols()`

Return the list of supported sub-protocols.

- 

## Method Details

  - 

### getSubProtocols

List<String> getSubProtocols()
Return the list of supported sub-protocols.