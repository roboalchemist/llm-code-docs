# Package org.springframework.web.socket.sockjs.support

---

@NullMarked
package org.springframework.web.socket.sockjs.support

Support classes for SockJS including an
`AbstractSockJsService`
implementation.

- 

Related Packages

Package
Description
org.springframework.web.socket.sockjs

Top-level SockJS types.

org.springframework.web.socket.sockjs.client

SockJS client implementation of
`WebSocketClient`.

org.springframework.web.socket.sockjs.frame

Support classes for creating SockJS frames including the encoding and decoding
of SockJS message frames.

org.springframework.web.socket.sockjs.transport

Server-side support for SockJS transports including
`TransportHandler` implementations
for processing incoming requests, their
`session`
counterparts for sending messages over the various transports, and
`DefaultSockJsService`.

- 

Classes

Class
Description
AbstractSockJsService

An abstract base class for `SockJsService` implementations that provides SockJS
path resolution and handling of static SockJS requests (for example, "/info", "/iframe.html",
etc).

SockJsHttpRequestHandler

An `HttpRequestHandler` that allows mapping a `SockJsService` to requests
in a Servlet container.