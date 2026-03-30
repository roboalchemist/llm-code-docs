# Package org.springframework.web.socket.server.support

---

@NullMarked
package org.springframework.web.socket.server.support

Server-side support classes including container-specific strategies
for upgrading a request.

- 

Related Packages

Package
Description
org.springframework.web.socket.server

Server-side abstractions for WebSocket interactions.

org.springframework.web.socket.server.jetty

Server-side support for the Jetty WebSocket API.

org.springframework.web.socket.server.standard

Server-side classes for use with standard JSR-356 WebSocket endpoints.

- 

Classes

Class
Description
AbstractHandshakeHandler

A base class for `HandshakeHandler` implementations, independent of the Servlet API.

DefaultHandshakeHandler

A default `HandshakeHandler` implementation,
extending `AbstractHandshakeHandler` with Servlet-specific initialization support.

HandshakeInterceptorChain

A helper class that assists with invoking a list of handshake interceptors.

HttpSessionHandshakeInterceptor

An interceptor to copy information from the HTTP session to the "handshake
attributes" map to be made available via `WebSocketSession.getAttributes()`.

OriginHandshakeInterceptor

An interceptor to check request `Origin` header value against a
collection of allowed origins.

WebSocketHandlerMapping

Extension of `SimpleUrlHandlerMapping` with support for more
precise mapping of WebSocket handshake requests to handlers of type
`WebSocketHttpRequestHandler`.

WebSocketHttpRequestHandler

A `HttpRequestHandler` for processing WebSocket handshake requests.