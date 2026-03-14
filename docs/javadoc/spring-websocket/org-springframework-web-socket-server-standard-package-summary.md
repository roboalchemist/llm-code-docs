# Package org.springframework.web.socket.server.standard

---

@NullMarked
package org.springframework.web.socket.server.standard

Server-side classes for use with standard JSR-356 WebSocket endpoints.

- 

Related Packages

Package
Description
org.springframework.web.socket.server

Server-side abstractions for WebSocket interactions.

org.springframework.web.socket.server.jetty

Server-side support for the Jetty WebSocket API.

org.springframework.web.socket.server.support

Server-side support classes including container-specific strategies
for upgrading a request.

- 

Classes

Class
Description
ServerEndpointExporter

Detects beans of type `ServerEndpointConfig` and registers
with the standard Jakarta WebSocket runtime.

ServerEndpointRegistration

An implementation of `ServerEndpointConfig` for use in
Spring-based applications.

ServletServerContainerFactoryBean

A `FactoryBean` for configuring `ServerContainer`.

SpringConfigurator

A `ServerEndpointConfig.Configurator` for initializing
`ServerEndpoint`-annotated classes through Spring.

StandardWebSocketUpgradeStrategy

A WebSocket `RequestUpgradeStrategy` for the Jakarta WebSocket API 2.1+.