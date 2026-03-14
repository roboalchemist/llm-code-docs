# Class DefaultSockJsService

java.lang.Object
org.springframework.web.socket.sockjs.support.AbstractSockJsService
org.springframework.web.socket.sockjs.transport.TransportHandlingSockJsService
org.springframework.web.socket.sockjs.transport.handler.DefaultSockJsService

All Implemented Interfaces:
`org.springframework.beans.factory.Aware, org.springframework.context.Lifecycle, org.springframework.web.context.ServletContextAware, org.springframework.web.cors.CorsConfigurationSource, SockJsService, SockJsServiceConfig`

---

public class DefaultSockJsService
extends TransportHandlingSockJsService
implements org.springframework.web.context.ServletContextAware
A default implementation of `SockJsService`
with all default `TransportHandler` implementations pre-registered.

Since:
4.0
Author:
Rossen Stoyanchev, Juergen Hoeller

- 

## Field Summary

### Fields inherited from class AbstractSockJsService

`corsConfiguration, logger`

- 

## Constructor Summary

Constructors

Constructor
Description
`DefaultSockJsService(org.springframework.scheduling.TaskScheduler scheduler)`

Create a DefaultSockJsService with default `handler` types.

`DefaultSockJsService(org.springframework.scheduling.TaskScheduler scheduler,
 Collection<TransportHandler> handlerOverrides)`

Create a DefaultSockJsService with overridden `handler` types
replacing the corresponding default handler implementation.

`DefaultSockJsService(org.springframework.scheduling.TaskScheduler scheduler,
 TransportHandler... handlerOverrides)`

Create a DefaultSockJsService with overridden `handler` types
replacing the corresponding default handler implementation.

- 

## Method Summary

Modifier and Type
Method
Description
`void`
`setServletContext(jakarta.servlet.ServletContext servletContext)`
 

### Methods inherited from class TransportHandlingSockJsService

`getHandshakeInterceptors, getMessageCodec, getTransportHandlers, handleRawWebSocketRequest, handleTransportRequest, isRunning, setHandshakeInterceptors, setMessageCodec, start, stop, validateRequest`

### Methods inherited from class AbstractSockJsService

`addCacheHeaders, addNoCacheHeaders, checkOrigin, getAllowedOriginPatterns, getAllowedOrigins, getCorsConfiguration, getDisconnectDelay, getHeartbeatTime, getHttpMessageCacheSize, getName, getSockJsClientLibraryUrl, getStreamBytesLimit, getTaskScheduler, handleRequest, isSessionCookieNeeded, isWebSocketEnabled, sendMethodNotAllowed, setAllowedOriginPatterns, setAllowedOrigins, setDisconnectDelay, setHeartbeatTime, setHttpMessageCacheSize, setName, setSessionCookieNeeded, setSockJsClientLibraryUrl, setStreamBytesLimit, setSuppressCors, setWebSocketEnabled, shouldSuppressCors`

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface SockJsServiceConfig

`getHeartbeatTime, getHttpMessageCacheSize, getStreamBytesLimit, getTaskScheduler`

- 

## Constructor Details

  - 

### DefaultSockJsService

public DefaultSockJsService(org.springframework.scheduling.TaskScheduler scheduler)
Create a DefaultSockJsService with default `handler` types.

Parameters:
`scheduler` - a task scheduler for heart-beat messages and removing
timed-out sessions; the provided TaskScheduler should be declared as a
Spring bean to ensure it is initialized at start up and shut down when the
application stops.

  - 

### DefaultSockJsService

public DefaultSockJsService(org.springframework.scheduling.TaskScheduler scheduler,
 TransportHandler... handlerOverrides)
Create a DefaultSockJsService with overridden `handler` types
replacing the corresponding default handler implementation.

Parameters:
`scheduler` - a task scheduler for heart-beat messages and removing timed-out sessions;
the provided TaskScheduler should be declared as a Spring bean to ensure it gets
initialized at start-up and shuts down when the application stops
`handlerOverrides` - zero or more overrides to the default transport handler types

  - 

### DefaultSockJsService

public DefaultSockJsService(org.springframework.scheduling.TaskScheduler scheduler,
 Collection<TransportHandler> handlerOverrides)
Create a DefaultSockJsService with overridden `handler` types
replacing the corresponding default handler implementation.

Parameters:
`scheduler` - a task scheduler for heart-beat messages and removing timed-out sessions;
the provided TaskScheduler should be declared as a Spring bean to ensure it gets
initialized at start-up and shuts down when the application stops
`handlerOverrides` - zero or more overrides to the default transport handler types

- 

## Method Details

  - 

### setServletContext

public void setServletContext(jakarta.servlet.ServletContext servletContext)

Specified by:
`setServletContext` in interface `org.springframework.web.context.ServletContextAware`