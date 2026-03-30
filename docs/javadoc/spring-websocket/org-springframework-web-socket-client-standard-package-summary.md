# Package org.springframework.web.socket.client.standard

---

@NullMarked
package org.springframework.web.socket.client.standard

Client-side classes for use with standard Jakarta WebSocket endpoints.

- 

Related Packages

Package
Description
org.springframework.web.socket.client

Client-side abstractions for WebSocket applications.

- 

Classes

Class
Description
AnnotatedEndpointConnectionManager

WebSocket `connection manager` that connects
to the server via `WebSocketContainer` and handles the session with an
`@ClientEndpoint` endpoint.

EndpointConnectionManager

WebSocket `connection manager` that connects
to the server via `WebSocketContainer` and handles the session with an
`Endpoint`.

StandardWebSocketClient

A WebSocketClient based on the standard Jakarta WebSocket API.

WebSocketContainerFactoryBean

A FactoryBean for creating and configuring a `WebSocketContainer`
through Spring XML configuration.