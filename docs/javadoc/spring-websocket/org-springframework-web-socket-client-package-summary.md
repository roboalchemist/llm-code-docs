# Package org.springframework.web.socket.client

---

@NullMarked
package org.springframework.web.socket.client

Client-side abstractions for WebSocket applications.

- 

Related Packages

Package
Description
org.springframework.web.socket

Common abstractions and Spring configuration support for WebSocket applications.

org.springframework.web.socket.client.standard

Client-side classes for use with standard Jakarta WebSocket endpoints.

- 

Class
Description
AbstractWebSocketClient

Abstract base class for `WebSocketClient` implementations.

ConnectionManagerSupport

Base class for a connection manager that automates the process of connecting
to a WebSocket server with the Spring ApplicationContext lifecycle.

WebSocketClient

Contract for initiating a WebSocket request.

WebSocketConnectionManager

WebSocket `connection manager` that connects
to the server via `WebSocketClient` and handles the session with a
`WebSocketHandler`.