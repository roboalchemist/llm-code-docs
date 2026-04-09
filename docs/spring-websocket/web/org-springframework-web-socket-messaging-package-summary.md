# Package org.springframework.web.socket.messaging

---

@NullMarked
package org.springframework.web.socket.messaging

WebSocket integration for Spring's messaging module.

- 

Related Packages

Package
Description
org.springframework.web.socket

Common abstractions and Spring configuration support for WebSocket applications.

- 

Class
Description
AbstractSubProtocolEvent

A base class for events for a message received from a WebSocket client and
parsed into a higher-level sub-protocol (for example, STOMP).

DefaultSimpUserRegistry

A default implementation of `SimpUserRegistry` that relies on
`AbstractSubProtocolEvent` application context events to keep
track of connected users and their subscriptions.

SessionConnectedEvent

A connected event represents the server response to a client's connect request.

SessionConnectEvent

Event raised when a new WebSocket client using a Simple Messaging Protocol
(for example, STOMP) as the WebSocket sub-protocol issues a connect request.

SessionDisconnectEvent

Event raised when the session of a WebSocket client using a Simple Messaging
Protocol (for example, STOMP) as the WebSocket sub-protocol is closed.

SessionSubscribeEvent

Event raised when a new WebSocket client using a Simple Messaging Protocol
(for example, STOMP) sends a subscription request.

SessionUnsubscribeEvent

Event raised when a new WebSocket client using a Simple Messaging Protocol
(for example, STOMP) sends a request to remove a subscription.

StompSubProtocolErrorHandler

A `SubProtocolErrorHandler` for use with STOMP.

StompSubProtocolHandler

A `SubProtocolHandler` for STOMP that supports versions 1.0, 1.1, and 1.2
of the STOMP specification.

StompSubProtocolHandler.Stats

Contract for access to session counters.

SubProtocolErrorHandler<P>

A contract for handling sub-protocol errors sent to clients.

SubProtocolHandler

A contract for handling WebSocket messages as part of a higher level protocol,
referred to as "sub-protocol" in the WebSocket RFC specification.

SubProtocolWebSocketHandler

An implementation of `WebSocketHandler` that delegates incoming WebSocket
messages to a `SubProtocolHandler` along with a `MessageChannel` to which
the sub-protocol handler can send messages from WebSocket clients to the application.

SubProtocolWebSocketHandler.Stats

Contract for access to session counters.

WebSocketAnnotationMethodMessageHandler

A subclass of `SimpAnnotationMethodMessageHandler` to provide support
for `ControllerAdvice` with global `@MessageExceptionHandler` methods.

WebSocketStompClient

A STOMP over WebSocket client that connects using an implementation of
`WebSocketClient`
including `SockJsClient`.