# Package org.springframework.web.socket.adapter

---

@NullMarked
package org.springframework.web.socket.adapter

Classes adapting Spring's WebSocket API to and from WebSocket providers.

- 

Related Packages

Package
Description
org.springframework.web.socket

Common abstractions and Spring configuration support for WebSocket applications.

org.springframework.web.socket.adapter.jetty

Adapter classes for the Jetty WebSocket API.

org.springframework.web.socket.adapter.standard

Adapter classes for the standard Jakarta WebSocket API.

- 

Class
Description
AbstractWebSocketSession<T>

An abstract base class for implementations of `WebSocketSession`.

NativeWebSocketSession

A `WebSocketSession` that exposes the underlying, native WebSocketSession
through a getter.