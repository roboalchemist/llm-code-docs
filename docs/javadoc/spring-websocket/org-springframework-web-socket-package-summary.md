# Package org.springframework.web.socket

---

@NullMarked
package org.springframework.web.socket

Common abstractions and Spring configuration support for WebSocket applications.

- 

Related Packages

Package
Description
org.springframework.web.socket.adapter

Classes adapting Spring's WebSocket API to and from WebSocket providers.

org.springframework.web.socket.client

Client-side abstractions for WebSocket applications.

org.springframework.web.socket.config

Configuration support for WebSocket request handling.

org.springframework.web.socket.handler

Convenient `WebSocketHandler`
implementations and decorators.

org.springframework.web.socket.messaging

WebSocket integration for Spring's messaging module.

org.springframework.web.socket.server

Server-side abstractions for WebSocket interactions.

org.springframework.web.socket.sockjs

Top-level SockJS types.

- 

Class
Description
AbstractWebSocketMessage<T>

A message that can be handled or sent on a WebSocket connection.

BinaryMessage

A binary WebSocket message.

CloseStatus

Represents a WebSocket close status code and reason.

PingMessage

A WebSocket ping message.

PongMessage

A WebSocket pong message.

SubProtocolCapable

An interface for WebSocket handlers that support sub-protocols as defined in RFC 6455.

TextMessage

A text WebSocket message.

WebSocketExtension

Represents a WebSocket extension as defined in the RFC 6455.

WebSocketHandler

A handler for WebSocket messages and lifecycle events.

WebSocketHttpHeaders

An `HttpHeaders` variant that adds support for the HTTP headers defined
by the WebSocket specification RFC 6455.

WebSocketMessage<T>

A message that can be handled or sent on a WebSocket connection.

WebSocketSession

A WebSocket session abstraction.