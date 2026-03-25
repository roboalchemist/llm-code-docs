# Package org.springframework.web.socket.adapter.jetty

---

@NullMarked
package org.springframework.web.socket.adapter.jetty

Adapter classes for the Jetty WebSocket API.

- 

Related Packages

Package
Description
org.springframework.web.socket.adapter

Classes adapting Spring's WebSocket API to and from WebSocket providers.

org.springframework.web.socket.adapter.standard

Adapter classes for the standard Jakarta WebSocket API.

- 

Classes

Class
Description
JettyWebSocketHandlerAdapter

Adapts `WebSocketHandler` to the Jetty WebSocket API `Session.Listener`.

JettyWebSocketSession

A `WebSocketSession` for use with the Jetty WebSocket API.

WebSocketToJettyExtensionConfigAdapter

Adapter class to convert a `WebSocketExtension` to a Jetty
`ExtensionConfig`.