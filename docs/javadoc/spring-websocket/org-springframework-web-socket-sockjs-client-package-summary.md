# Package org.springframework.web.socket.sockjs.client

---

@NullMarked
package org.springframework.web.socket.sockjs.client

SockJS client implementation of
`WebSocketClient`.

- 

Related Packages

Package
Description
org.springframework.web.socket.sockjs

Top-level SockJS types.

org.springframework.web.socket.sockjs.frame

Support classes for creating SockJS frames including the encoding and decoding
of SockJS message frames.

org.springframework.web.socket.sockjs.support

Support classes for SockJS including an
`AbstractSockJsService`
implementation.

org.springframework.web.socket.sockjs.transport

Server-side support for SockJS transports including
`TransportHandler` implementations
for processing incoming requests, their
`session`
counterparts for sending messages over the various transports, and
`DefaultSockJsService`.

- 

Class
Description
AbstractClientSockJsSession

Base class for SockJS client implementations of `WebSocketSession`.

AbstractXhrTransport

Abstract base class for XHR transport implementations to extend.

InfoReceiver

A component that can execute the SockJS "Info" request that needs to be
performed before the SockJS session starts in order to check server endpoint
capabilities such as whether the endpoint permits use of WebSocket.

JettyXhrTransport

An XHR transport based on Jetty's `HttpClient`.

RestTemplateXhrTransport

An `XhrTransport` implementation that uses a
`RestTemplate`.

SockJsClient

A SockJS implementation of
`WebSocketClient`
with fallback alternatives that simulate a WebSocket interaction through plain
HTTP streaming and long polling techniques.

SockJsUrlInfo

Container for the base URL of a SockJS endpoint with additional helper methods
to derive related SockJS URLs: specifically, the `info`
and `transport` URLs.

Transport

A client-side implementation for a SockJS transport.

TransportRequest

Exposes information, typically to `Transport` and
`session` implementations, about a request
to connect to a SockJS server endpoint over a given transport.

WebSocketClientSockJsSession

An extension of `AbstractClientSockJsSession` wrapping and delegating
to an actual WebSocket session.

WebSocketTransport

A SockJS `Transport` that uses a
`WebSocketClient`.

XhrClientSockJsSession

An extension of `AbstractClientSockJsSession` for use with HTTP
transports simulating a WebSocket session.

XhrTransport

A SockJS `Transport` that uses HTTP requests to simulate a WebSocket
interaction.