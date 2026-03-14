# Package org.springframework.web.socket.server

---

@NullMarked
package org.springframework.web.socket.server

Server-side abstractions for WebSocket interactions.

- 

Related Packages

Package
Description
org.springframework.web.socket

Common abstractions and Spring configuration support for WebSocket applications.

org.springframework.web.socket.server.jetty

Server-side support for the Jetty WebSocket API.

org.springframework.web.socket.server.standard

Server-side classes for use with standard JSR-356 WebSocket endpoints.

org.springframework.web.socket.server.support

Server-side support classes including container-specific strategies
for upgrading a request.

- 

Class
Description
HandshakeFailureException

Thrown when handshake processing failed to complete due to an internal, unrecoverable
error.

HandshakeHandler

Contract for processing a WebSocket handshake request.

HandshakeInterceptor

Interceptor for WebSocket handshake requests.

RequestUpgradeStrategy

A server-specific strategy for performing the actual upgrade to a WebSocket exchange.