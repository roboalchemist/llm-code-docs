# Package org.springframework.web.socket.handler

---

@NullMarked
package org.springframework.web.socket.handler

Convenient `WebSocketHandler`
implementations and decorators.

- 

Related Packages

Package
Description
org.springframework.web.socket

Common abstractions and Spring configuration support for WebSocket applications.

- 

Class
Description
AbstractWebSocketHandler

A convenient base class for `WebSocketHandler` implementation with empty methods.

BeanCreatingHandlerProvider<T>

Instantiates a target handler through a Spring `BeanFactory` and also provides
an equivalent destroy method.

BinaryWebSocketHandler

A convenient base class for `WebSocketHandler` implementations
that process binary messages only.

ConcurrentWebSocketSessionDecorator

Wrap a `WebSocketSession`
to guarantee only one thread can send messages at a time.

ConcurrentWebSocketSessionDecorator.OverflowStrategy

Enum for options of what to do when the buffer fills up.

ExceptionWebSocketHandlerDecorator

An exception handling `WebSocketHandlerDecorator`.

LoggingWebSocketHandlerDecorator

A `WebSocketHandlerDecorator` that adds logging to WebSocket lifecycle events.

PerConnectionWebSocketHandler

A `WebSocketHandler` that initializes and destroys a `WebSocketHandler`
instance for each WebSocket connection and delegates all other methods to it.

SessionLimitExceededException

Raised when a WebSocket session has exceeded limits it has been configured
for, for example, timeout, buffer size, etc.

TextWebSocketHandler

A convenient base class for `WebSocketHandler` implementations
that process text messages only.

WebSocketHandlerDecorator

Wraps another `WebSocketHandler`
instance and delegates to it.

WebSocketHandlerDecoratorFactory

A factory for applying decorators to a WebSocketHandler.

WebSocketSessionDecorator

Wraps another `WebSocketSession` instance
and delegates to it.