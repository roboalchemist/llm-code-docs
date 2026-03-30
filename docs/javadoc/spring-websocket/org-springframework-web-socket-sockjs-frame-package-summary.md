# Package org.springframework.web.socket.sockjs.frame

---

@NullMarked
package org.springframework.web.socket.sockjs.frame

Support classes for creating SockJS frames including the encoding and decoding
of SockJS message frames.

- 

Related Packages

Package
Description
org.springframework.web.socket.sockjs

Top-level SockJS types.

org.springframework.web.socket.sockjs.client

SockJS client implementation of
`WebSocketClient`.

org.springframework.web.socket.sockjs.support

Support classes for SockJS including an
`AbstractSockJsService`
implementation.

org.springframework.web.socket.sockjs.transport

Server-side support for SockJS transports including
`TransportHandler` implementations
for processing incoming requests, their
`session`
counterparts for sending messages over the various transports, and
`DefaultSockJsService`.

- 

Class
Description
AbstractSockJsMessageCodec

A base class for SockJS message codec that provides an implementation of
`AbstractSockJsMessageCodec.encode(String[])`.

DefaultSockJsFrameFormat

A default implementation of
`SockJsFrameFormat` that relies
on `String.format(String, Object...)`..

Jackson2SockJsMessageCodec
Deprecated, for removal: This API element is subject to removal in a future version.
since 7.0 in favor of `JacksonJsonSockJsMessageCodec`

JacksonJsonSockJsMessageCodec

A Jackson 3.x codec for encoding and decoding SockJS messages.

SockJsFrame

Represents a SockJS frame.

SockJsFrameFormat

Applies a transport-specific format to the content of a SockJS frame resulting
in a content that can be written out.

SockJsFrameType

SockJS frame types.

SockJsMessageCodec

Encode and decode messages to and from a SockJS message frame,
essentially an array of JSON-encoded messages.