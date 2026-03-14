# Package org.springframework.web.socket.sockjs.transport.session

---

@NullMarked
package org.springframework.web.socket.sockjs.transport.session

SockJS specific implementations of
`WebSocketSession`.

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

org.springframework.web.socket.sockjs.transport.handler

`TransportHandler`
implementation classes as well as a concrete
`SockJsService`.

- 

Classes

Class
Description
AbstractHttpSockJsSession

An abstract base class for use with HTTP transport SockJS sessions.

AbstractSockJsSession

An abstract base class for SockJS sessions implementing `SockJsSession`.

PollingSockJsSession

A SockJS session for use with polling HTTP transports.

StreamingSockJsSession

A SockJS session for use with streaming HTTP transports.

WebSocketServerSockJsSession

A SockJS session for use with the WebSocket transport.