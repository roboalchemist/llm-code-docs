# Crate fastwebsockets

Source

## Modules§

handshake`upgrade`Client handshake.upgrade`upgrade`HTTP upgrades.

## Structs§

FragmentCollectorCollects fragmented messages over a WebSocket connection and returns the completed message once all fragments have been received.FrameRepresents a WebSocket frame.WebSocketWebSocket protocol implementation over an async stream.

## Enums§

CloseCodeStatus code used to indicate why an endpoint is closing the WebSocket connection.OpCodePayloadRoleWebSocketError

## Functions§

unmaskUnmask a payload using the given 4-byte mask.
