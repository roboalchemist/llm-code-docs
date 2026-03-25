# Package org.springframework.web.socket.config.annotation

---

@NullMarked
package org.springframework.web.socket.config.annotation

Support for annotation-based WebSocket setup in configuration classes.

- 

Related Packages

Package
Description
org.springframework.web.socket.config

Configuration support for WebSocket request handling.

- 

Class
Description
AbstractWebSocketHandlerRegistration<M>

Base class for `WebSocketHandlerRegistrations` that gathers all the configuration
options but allows subclasses to put together the actual HTTP request mappings.

DelegatingWebSocketConfiguration

A variation of `WebSocketConfigurationSupport` that detects implementations of
`WebSocketConfigurer` in Spring configuration and invokes them in order to
configure WebSocket request handling.

DelegatingWebSocketMessageBrokerConfiguration

A `WebSocketMessageBrokerConfigurationSupport` extension that detects
beans of type `WebSocketMessageBrokerConfigurer` and delegates to all
of them allowing callback style customization of the configuration provided
in `WebSocketMessageBrokerConfigurationSupport`.

EnableWebSocket

Add this annotation to an `@Configuration` class to configure
processing WebSocket requests.

EnableWebSocketMessageBroker

Add this annotation to an `@Configuration` class to enable broker-backed
messaging over WebSocket using a higher-level messaging sub-protocol.

ServletWebSocketHandlerRegistration

A helper class for configuring `WebSocketHandler` request handling
including SockJS fallback options.

ServletWebSocketHandlerRegistry

`WebSocketHandlerRegistry` with Spring MVC handler mappings for the
handshake requests.

SockJsServiceRegistration

A helper class for configuring SockJS fallback options for use with an
`EnableWebSocket` and
`WebSocketConfigurer` setup.

StompEndpointRegistry

A contract for registering STOMP over WebSocket endpoints.

StompWebSocketEndpointRegistration

A contract for configuring a STOMP over WebSocket endpoint.

WebMvcStompEndpointRegistry

A registry for STOMP over WebSocket endpoints that maps the endpoints with a
`HandlerMapping` for use in Spring MVC.

WebMvcStompWebSocketEndpointRegistration

An abstract base class for configuring STOMP over WebSocket/SockJS endpoints.

WebSocketConfigurationSupport

Configuration support for WebSocket request handling.

WebSocketConfigurer

Defines callback methods to configure the WebSocket request handling
via `@EnableWebSocket`.

WebSocketHandlerRegistration

Provides methods for configuring a WebSocket handler.

WebSocketHandlerRegistry

Provides methods for configuring `WebSocketHandler` request mappings.

WebSocketMessageBrokerConfigurationSupport

Extends `AbstractMessageBrokerConfiguration` and adds configuration for
receiving and responding to STOMP messages from WebSocket clients.

WebSocketMessageBrokerConfigurer

Defines methods for configuring message handling with simple messaging
protocols (for example, STOMP) from WebSocket clients.

WebSocketScope

`@WebSocketScope` is a specialization of `@Scope` for a
component whose lifecycle is bound to the current WebSocket lifecycle.

WebSocketTransportRegistration

Configure the processing of messages received from and sent to WebSocket clients.