# Package org.springframework.web.socket.sockjs

---

@NullMarked
package org.springframework.web.socket.sockjs

Top-level SockJS types.

- 

Related Packages

Package
Description
org.springframework.web.socket

Common abstractions and Spring configuration support for WebSocket applications.

org.springframework.web.socket.sockjs.client

SockJS client implementation of
`WebSocketClient`.

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
SockJsException

Base class for exceptions raised while processing SockJS HTTP requests.

SockJsMessageDeliveryException

An exception thrown when a message frame was successfully received over an HTTP POST
and parsed but one or more of the messages it contained could not be delivered to the
WebSocketHandler either because the handler failed or because the connection got
closed.

SockJsService

The main entry point for processing HTTP requests from SockJS clients.

SockJsTransportFailureException

Indicates a serious failure that occurred in the SockJS implementation as opposed to
in user code (for example, IOException while writing to the response).