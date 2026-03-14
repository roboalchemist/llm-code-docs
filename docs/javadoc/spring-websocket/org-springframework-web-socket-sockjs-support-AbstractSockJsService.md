# Class AbstractSockJsService

java.lang.Object
org.springframework.web.socket.sockjs.support.AbstractSockJsService

All Implemented Interfaces:
`org.springframework.web.cors.CorsConfigurationSource, SockJsService`

Direct Known Subclasses:
`TransportHandlingSockJsService`

---

public abstract class AbstractSockJsService
extends Object
implements SockJsService, org.springframework.web.cors.CorsConfigurationSource
An abstract base class for `SockJsService` implementations that provides SockJS
path resolution and handling of static SockJS requests (for example, "/info", "/iframe.html",
etc). Sub-classes must handle session URLs (i.e. transport-specific requests).

By default, only same origin requests are allowed. Use `setAllowedOrigins(Collection)`
to specify a list of allowed origins (a list containing "*" will allow all origins).

Since:
4.0
Author:
Rossen Stoyanchev, Sebastien Deleuze

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`protected final org.springframework.web.cors.CorsConfiguration`
`corsConfiguration`
 
`protected final org.apache.commons.logging.Log`
`logger`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`AbstractSockJsService(org.springframework.scheduling.TaskScheduler scheduler)`
 

- 

## Method Summary

Modifier and Type
Method
Description
`protected void`
`addCacheHeaders(org.springframework.http.server.ServerHttpResponse response)`
 
`protected void`
`addNoCacheHeaders(org.springframework.http.server.ServerHttpResponse response)`
 
`protected boolean`
`checkOrigin(org.springframework.http.server.ServerHttpRequest request,
 org.springframework.http.server.ServerHttpResponse response,
 org.springframework.http.HttpMethod... httpMethods)`
 
`@Nullable Collection<String>`
`getAllowedOriginPatterns()`

Return `configured` origin patterns.

`@Nullable Collection<String>`
`getAllowedOrigins()`

Return the `configured` allowed origins.

`@Nullable org.springframework.web.cors.CorsConfiguration`
`getCorsConfiguration(jakarta.servlet.http.HttpServletRequest request)`
 
`long`
`getDisconnectDelay()`

Return the amount of time in milliseconds before a client is considered disconnected.

`long`
`getHeartbeatTime()`

Return the amount of time in milliseconds when the server has not sent
any messages.

`int`
`getHttpMessageCacheSize()`

Return the size of the HTTP message cache.

`String`
`getName()`

Return the unique name associated with this service.

`String`
`getSockJsClientLibraryUrl()`

Return he URL to the SockJS JavaScript client library.

`int`
`getStreamBytesLimit()`

Return the minimum number of bytes that can be sent over a single HTTP
streaming request before it will be closed.

`org.springframework.scheduling.TaskScheduler`
`getTaskScheduler()`

A scheduler instance to use for scheduling heart-beat messages.

`protected abstract void`
`handleRawWebSocketRequest(org.springframework.http.server.ServerHttpRequest request,
 org.springframework.http.server.ServerHttpResponse response,
 WebSocketHandler webSocketHandler)`

Handle request for raw WebSocket communication, i.e.

`final void`
`handleRequest(org.springframework.http.server.ServerHttpRequest request,
 org.springframework.http.server.ServerHttpResponse response,
 @Nullable String sockJsPath,
 WebSocketHandler wsHandler)`

This method determines the SockJS path and handles SockJS static URLs.

`protected abstract void`
`handleTransportRequest(org.springframework.http.server.ServerHttpRequest request,
 org.springframework.http.server.ServerHttpResponse response,
 WebSocketHandler webSocketHandler,
 String sessionId,
 String transport)`

Handle a SockJS session URL (i.e.

`boolean`
`isSessionCookieNeeded()`

Return whether the JSESSIONID cookie is required for the application to function.

`boolean`
`isWebSocketEnabled()`

Return whether WebSocket transport is enabled.

`protected void`
`sendMethodNotAllowed(org.springframework.http.server.ServerHttpResponse response,
 org.springframework.http.HttpMethod... httpMethods)`
 
`void`
`setAllowedOriginPatterns(Collection<String> allowedOriginPatterns)`

Alternative to `setAllowedOrigins(Collection)` that supports more
flexible patterns for specifying the origins for which cross-origin
requests are allowed from a browser.

`void`
`setAllowedOrigins(Collection<String> allowedOrigins)`

Set the origins for which cross-origin requests are allowed from a browser.

`void`
`setDisconnectDelay(long disconnectDelay)`

The amount of time in milliseconds before a client is considered
disconnected after not having a receiving connection, i.e.

`void`
`setHeartbeatTime(long heartbeatTime)`

Specify the amount of time in milliseconds when the server has not sent
any messages and after which the server should send a heartbeat frame
to the client in order to keep the connection from breaking.

`void`
`setHttpMessageCacheSize(int httpMessageCacheSize)`

The number of server-to-client messages that a session can cache while waiting
for the next HTTP polling request from the client.

`void`
`setName(String name)`

Set a unique name for this service (mainly for logging purposes).

`void`
`setSessionCookieNeeded(boolean sessionCookieNeeded)`

The SockJS protocol requires a server to respond to an initial "/info" request from
clients with a "cookie_needed" boolean property that indicates whether the use of a
JSESSIONID cookie is required for the application to function correctly, for example, for
load balancing or in Java Servlet containers for the use of an HTTP session.

`void`
`setSockJsClientLibraryUrl(String clientLibraryUrl)`

Transports with no native cross-domain communication (for example, "eventsource",
"htmlfile") must get a simple page from the "foreign" domain in an invisible
`iframe` so that code in the `iframe` can run from a domain
local to the SockJS server.

`void`
`setStreamBytesLimit(int streamBytesLimit)`

Streaming transports save responses on the client side and don't free
memory used by delivered messages.

`void`
`setSuppressCors(boolean suppressCors)`

This option can be used to disable automatic addition of CORS headers for
SockJS requests.

`void`
`setWebSocketEnabled(boolean webSocketEnabled)`

Some load balancers do not support WebSocket.

`boolean`
`shouldSuppressCors()`

Return if automatic addition of CORS headers has been disabled.

`protected boolean`
`validateRequest(String serverId,
 String sessionId,
 String transport)`
 

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Field Details

  - 

### logger

protected final org.apache.commons.logging.Log logger

  - 

### corsConfiguration

protected final org.springframework.web.cors.CorsConfiguration corsConfiguration

- 

## Constructor Details

  - 

### AbstractSockJsService

public AbstractSockJsService(org.springframework.scheduling.TaskScheduler scheduler)

- 

## Method Details

  - 

### getTaskScheduler

public org.springframework.scheduling.TaskScheduler getTaskScheduler()
A scheduler instance to use for scheduling heart-beat messages.

  - 

### setName

public void setName(String name)
Set a unique name for this service (mainly for logging purposes).

  - 

### getName

public String getName()
Return the unique name associated with this service.

  - 

### setSockJsClientLibraryUrl

public void setSockJsClientLibraryUrl(String clientLibraryUrl)
Transports with no native cross-domain communication (for example, "eventsource",
"htmlfile") must get a simple page from the "foreign" domain in an invisible
`iframe` so that code in the `iframe` can run from a domain
local to the SockJS server. Since the `iframe` needs to load the
SockJS JavaScript client library, this property allows specifying where to
load it from.

By default this is set to point to
"https://cdn.jsdelivr.net/sockjs/1.0.0/sockjs.min.js".
However, it can also be set to point to a URL served by the application.

Note that it's possible to specify a relative URL in which case the URL
must be relative to the `iframe` URL. For example assuming a SockJS endpoint
mapped to "/sockjs", and resulting `iframe` URL "/sockjs/iframe.html", then
the relative URL must start with "../../" to traverse up to the location
above the SockJS mapping. In case of a prefix-based Servlet mapping one more
traversals may be needed.

  - 

### getSockJsClientLibraryUrl

public String getSockJsClientLibraryUrl()
Return he URL to the SockJS JavaScript client library.

  - 

### setStreamBytesLimit

public void setStreamBytesLimit(int streamBytesLimit)
Streaming transports save responses on the client side and don't free
memory used by delivered messages. Such transports need to recycle the
connection once in a while. This property sets a minimum number of bytes
that can be sent over a single HTTP streaming request before it will be
closed. After that client will open a new request. Setting this value to
one effectively disables streaming and will make streaming transports to
behave like polling transports.

The default value is 128K (i.e. 128 * 1024).

  - 

### getStreamBytesLimit

public int getStreamBytesLimit()
Return the minimum number of bytes that can be sent over a single HTTP
streaming request before it will be closed.

  - 

### setSessionCookieNeeded

public void setSessionCookieNeeded(boolean sessionCookieNeeded)
The SockJS protocol requires a server to respond to an initial "/info" request from
clients with a "cookie_needed" boolean property that indicates whether the use of a
JSESSIONID cookie is required for the application to function correctly, for example, for
load balancing or in Java Servlet containers for the use of an HTTP session.

This is especially important for IE 8,9 that support XDomainRequest -- a modified
AJAX/XHR -- that can do requests across domains but does not send any cookies. In
those cases, the SockJS client prefers the "iframe-htmlfile" transport over
"xdr-streaming" in order to be able to send cookies.

The SockJS protocol also expects a SockJS service to echo back the JSESSIONID
cookie when this property is set to true. However, when running in a Servlet
container this is not necessary since the container takes care of it.

The default value is "true" to maximize the chance for applications to work
correctly in IE 8,9 with support for cookies (and the JSESSIONID cookie in
particular). However, an application can choose to set this to "false" if
the use of cookies (and HTTP session) is not required.

  - 

### isSessionCookieNeeded

public boolean isSessionCookieNeeded()
Return whether the JSESSIONID cookie is required for the application to function.

  - 

### setHeartbeatTime

public void setHeartbeatTime(long heartbeatTime)
Specify the amount of time in milliseconds when the server has not sent
any messages and after which the server should send a heartbeat frame
to the client in order to keep the connection from breaking.

The default value is 25,000 (25 seconds).

  - 

### getHeartbeatTime

public long getHeartbeatTime()
Return the amount of time in milliseconds when the server has not sent
any messages.

  - 

### setDisconnectDelay

public void setDisconnectDelay(long disconnectDelay)
The amount of time in milliseconds before a client is considered
disconnected after not having a receiving connection, i.e. an active
connection over which the server can send data to the client.

The default value is 5000.

  - 

### getDisconnectDelay

public long getDisconnectDelay()
Return the amount of time in milliseconds before a client is considered disconnected.

  - 

### setHttpMessageCacheSize

public void setHttpMessageCacheSize(int httpMessageCacheSize)
The number of server-to-client messages that a session can cache while waiting
for the next HTTP polling request from the client. All HTTP transports use this
property since even streaming transports recycle HTTP requests periodically.

The amount of time between HTTP requests should be relatively brief and will
not exceed the allows disconnect delay (see `setDisconnectDelay(long)`);
5 seconds by default.

The default size is 100.

  - 

### getHttpMessageCacheSize

public int getHttpMessageCacheSize()
Return the size of the HTTP message cache.

  - 

### setWebSocketEnabled

public void setWebSocketEnabled(boolean webSocketEnabled)
Some load balancers do not support WebSocket. This option can be used to
disable the WebSocket transport on the server side.

The default value is "true".

  - 

### isWebSocketEnabled

public boolean isWebSocketEnabled()
Return whether WebSocket transport is enabled.

  - 

### setSuppressCors

public void setSuppressCors(boolean suppressCors)
This option can be used to disable automatic addition of CORS headers for
SockJS requests.

The default value is "false".

Since:
4.1.2

  - 

### shouldSuppressCors

public boolean shouldSuppressCors()
Return if automatic addition of CORS headers has been disabled.

Since:
4.1.2
See Also:

    - `setSuppressCors(boolean)`

  - 

### setAllowedOrigins

public void setAllowedOrigins(Collection<String> allowedOrigins)
Set the origins for which cross-origin requests are allowed from a browser.
Please, refer to `CorsConfiguration.setAllowedOrigins(List)` for
format details and considerations, and keep in mind that the CORS spec
does not allow use of `"*"` with `allowCredentials=true`.
For more flexible origin patterns use `setAllowedOriginPatterns(Collection)`
instead.

By default, no origins are allowed. When
`allowedOriginPatterns` is also
set, then that takes precedence over this property.

Note when SockJS is enabled and origins are restricted, transport types
that do not allow to check request origin (Iframe based transports) are
disabled. As a consequence, IE 6 to 9 are not supported when origins are
restricted.

Since:
4.1.2
See Also:

    - `setAllowedOriginPatterns(Collection)`

    - RFC 6454: The Web Origin Concept

    - SockJS supported transports by browser

  - 

### getAllowedOrigins

public @Nullable Collection<String> getAllowedOrigins()
Return the `configured` allowed origins.

Since:
4.1.2

  - 

### setAllowedOriginPatterns

public void setAllowedOriginPatterns(Collection<String> allowedOriginPatterns)
Alternative to `setAllowedOrigins(Collection)` that supports more
flexible patterns for specifying the origins for which cross-origin
requests are allowed from a browser. Please, refer to
`CorsConfiguration.setAllowedOriginPatterns(List)` for format
details and other considerations.

By default this is not set.

Since:
5.2.3

  - 

### getAllowedOriginPatterns

public @Nullable Collection<String> getAllowedOriginPatterns()
Return `configured` origin patterns.

Since:
5.3.2

  - 

### handleRequest

public final void handleRequest(org.springframework.http.server.ServerHttpRequest request,
 org.springframework.http.server.ServerHttpResponse response,
 @Nullable String sockJsPath,
 WebSocketHandler wsHandler)
                         throws SockJsException
This method determines the SockJS path and handles SockJS static URLs.
Session URLs and raw WebSocket requests are delegated to abstract methods.

Specified by:
`handleRequest` in interface `SockJsService`
Parameters:
`request` - the current request
`response` - the current response
`sockJsPath` - the remainder of the path within the SockJS service prefix
`wsHandler` - the handler that will exchange messages with the SockJS client
Throws:
`SockJsException` - raised when request processing fails; generally, failed
attempts to send messages to clients automatically close the SockJS session
and raise `SockJsTransportFailureException`; failed attempts to read
messages from clients do not automatically close the session and may result
in `SockJsMessageDeliveryException` or `SockJsException`;
exceptions from the WebSocketHandler can be handled internally or through
`ExceptionWebSocketHandlerDecorator` or some alternative decorator.
The former is automatically added when using
`SockJsHttpRequestHandler`.

  - 

### validateRequest

protected boolean validateRequest(String serverId,
 String sessionId,
 String transport)

  - 

### checkOrigin

protected boolean checkOrigin(org.springframework.http.server.ServerHttpRequest request,
 org.springframework.http.server.ServerHttpResponse response,
 org.springframework.http.HttpMethod... httpMethods)
                       throws IOException

Throws:
`IOException`

  - 

### getCorsConfiguration

public @Nullable org.springframework.web.cors.CorsConfiguration getCorsConfiguration(jakarta.servlet.http.HttpServletRequest request)

Specified by:
`getCorsConfiguration` in interface `org.springframework.web.cors.CorsConfigurationSource`

  - 

### addCacheHeaders

protected void addCacheHeaders(org.springframework.http.server.ServerHttpResponse response)

  - 

### addNoCacheHeaders

protected void addNoCacheHeaders(org.springframework.http.server.ServerHttpResponse response)

  - 

### sendMethodNotAllowed

protected void sendMethodNotAllowed(org.springframework.http.server.ServerHttpResponse response,
 org.springframework.http.HttpMethod... httpMethods)

  - 

### handleRawWebSocketRequest

protected abstract void handleRawWebSocketRequest(org.springframework.http.server.ServerHttpRequest request,
 org.springframework.http.server.ServerHttpResponse response,
 WebSocketHandler webSocketHandler)
                                           throws IOException
Handle request for raw WebSocket communication, i.e. without any SockJS message framing.

Throws:
`IOException`

  - 

### handleTransportRequest

protected abstract void handleTransportRequest(org.springframework.http.server.ServerHttpRequest request,
 org.springframework.http.server.ServerHttpResponse response,
 WebSocketHandler webSocketHandler,
 String sessionId,
 String transport)
                                        throws SockJsException
Handle a SockJS session URL (i.e. transport-specific request).

Throws:
`SockJsException`