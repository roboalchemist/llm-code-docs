# Package org.springframework.web.socket.sockjs.transport.handler

---

@NullMarked
package org.springframework.web.socket.sockjs.transport.handler

`TransportHandler`
implementation classes as well as a concrete
`SockJsService`.

- 

Related Packages

Package
Description
org.springframework.web.socket.sockjs.transport

Server-side support for SockJS transports including
`TransportHandler` implementations
for processing incoming requests, their
`session`
counterparts for sending messages over the various transports, and
`DefaultSockJsService`.

org.springframework.web.socket.sockjs.transport.session

SockJS specific implementations of
`WebSocketSession`.

- 

Classes

Class
Description
AbstractHttpReceivingTransportHandler

Base class for HTTP transport handlers that receive messages via HTTP POST.

AbstractHttpSendingTransportHandler

Base class for HTTP transport handlers that push messages to connected clients.

AbstractTransportHandler

Common base class for `TransportHandler` implementations.

DefaultSockJsService

A default implementation of `SockJsService`
with all default `TransportHandler` implementations pre-registered.

EventSourceTransportHandler

A TransportHandler for sending messages via Server-Sent Events:
Server-Sent Events.

HtmlFileTransportHandler

An HTTP `TransportHandler` that uses a famous browser
`document.domain` technique.

SockJsWebSocketHandler

An implementation of `WebSocketHandler` that adds SockJS messages frames, sends
SockJS heartbeat messages, and delegates lifecycle events and messages to a target
`WebSocketHandler`.

WebSocketTransportHandler

WebSocket-based `TransportHandler`.

XhrPollingTransportHandler

A `TransportHandler` based on XHR (long) polling.

XhrReceivingTransportHandler

A `TransportHandler` that receives messages over HTTP.

XhrStreamingTransportHandler

A `TransportHandler` that sends messages over an HTTP streaming request.