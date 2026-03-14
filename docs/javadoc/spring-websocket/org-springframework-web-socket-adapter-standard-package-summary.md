# Package org.springframework.web.socket.adapter.standard

---

@NullMarked
package org.springframework.web.socket.adapter.standard

Adapter classes for the standard Jakarta WebSocket API.

- 

Related Packages

Package
Description
org.springframework.web.socket.adapter

Classes adapting Spring's WebSocket API to and from WebSocket providers.

org.springframework.web.socket.adapter.jetty

Adapter classes for the Jetty WebSocket API.

- 

Classes

Class
Description
ConvertingEncoderDecoderSupport<T,M>

Base class that can be used to implement a standard `Encoder`
and/or `Decoder`.

ConvertingEncoderDecoderSupport.BinaryDecoder<T>

A binary `jakarta.websocket.Encoder` that delegates
to Spring's conversion service.

ConvertingEncoderDecoderSupport.BinaryEncoder<T>

A binary `jakarta.websocket.Encoder` that delegates
to Spring's conversion service.

ConvertingEncoderDecoderSupport.TextDecoder<T>

A Text `jakarta.websocket.Encoder` that delegates
to Spring's conversion service.

ConvertingEncoderDecoderSupport.TextEncoder<T>

A text `jakarta.websocket.Encoder` that delegates
to Spring's conversion service.

StandardToWebSocketExtensionAdapter

A subclass of `WebSocketExtension` that can be constructed from a
`Extension`.

StandardWebSocketHandlerAdapter

Adapts a `WebSocketHandler` to the standard WebSocket for Java API.

StandardWebSocketSession

A `WebSocketSession` for use with the standard WebSocket for Java API.

WebSocketToStandardExtensionAdapter

Adapt an instance of `WebSocketExtension` to
the `Extension` interface.