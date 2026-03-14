# spring-websocket 7.0.5 API

Packages

Package
Description
org.springframework.web.socket

Common abstractions and Spring configuration support for WebSocket applications.

org.springframework.web.socket.adapter

Classes adapting Spring's WebSocket API to and from WebSocket providers.

org.springframework.web.socket.adapter.jetty

Adapter classes for the Jetty WebSocket API.

org.springframework.web.socket.adapter.standard

Adapter classes for the standard Jakarta WebSocket API.

org.springframework.web.socket.client

Client-side abstractions for WebSocket applications.

org.springframework.web.socket.client.standard

Client-side classes for use with standard Jakarta WebSocket endpoints.

org.springframework.web.socket.config

Configuration support for WebSocket request handling.

org.springframework.web.socket.config.annotation

Support for annotation-based WebSocket setup in configuration classes.

org.springframework.web.socket.handler

Convenient `WebSocketHandler`
implementations and decorators.

org.springframework.web.socket.messaging

WebSocket integration for Spring's messaging module.

org.springframework.web.socket.server

Server-side abstractions for WebSocket interactions.

org.springframework.web.socket.server.jetty

Server-side support for the Jetty WebSocket API.

org.springframework.web.socket.server.standard

Server-side classes for use with standard JSR-356 WebSocket endpoints.

org.springframework.web.socket.server.support

Server-side support classes including container-specific strategies
for upgrading a request.

org.springframework.web.socket.sockjs

Top-level SockJS types.

org.springframework.web.socket.sockjs.client

SockJS client implementation of
`WebSocketClient`.

org.springframework.web.socket.sockjs.frame

Support classes for creating SockJS frames including the encoding and decoding
of SockJS message frames.

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

org.springframework.web.socket.sockjs.transport.handler

`TransportHandler`
implementation classes as well as a concrete
`SockJsService`.

org.springframework.web.socket.sockjs.transport.session

SockJS specific implementations of
`WebSocketSession`.