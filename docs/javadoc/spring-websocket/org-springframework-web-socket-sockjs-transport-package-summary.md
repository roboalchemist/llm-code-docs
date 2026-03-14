# Package org.springframework.web.socket.sockjs.transport

---

@NullMarked
package org.springframework.web.socket.sockjs.transport

Server-side support for SockJS transports including
`TransportHandler` implementations
for processing incoming requests, their
`session`
counterparts for sending messages over the various transports, and
`DefaultSockJsService`.

- 

Related Packages

Package
Description
org.springframework.web.socket.sockjs

Top-level SockJS types.

org.springframework.web.socket.sockjs.transport.handler

`TransportHandler`
implementation classes as well as a concrete
`SockJsService`.

org.springframework.web.socket.sockjs.transport.session

SockJS specific implementations of
`WebSocketSession`.

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

- 

Class
Description
SockJsServiceConfig

Provides transport handling code with access to the `SockJsService` configuration
options they need to have access to.

SockJsSession

SockJS extension of Spring's standard `WebSocketSession`.

SockJsSessionFactory

A factory for creating a SockJS session.

TransportHandler

Handle a SockJS session URL, i.e.

TransportHandlingSockJsService

A basic implementation of `SockJsService`
with support for SPI-based transport handling and session management.

TransportType

SockJS transport types.