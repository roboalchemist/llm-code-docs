Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class RequestContext

java.lang.Object
org.glassfish.tyrus.spi.UpgradeRequest
org.glassfish.tyrus.core.RequestContext

All Implemented Interfaces:
`jakarta.websocket.server.HandshakeRequest`

---

public final class RequestContext
extends org.glassfish.tyrus.spi.UpgradeRequest
Implementation of all possible request interfaces. Should be the only point of truth.

Author:
Pavel Bucek

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final class`
`RequestContext.Builder`

`RequestContext` builder.

-

## Field Summary

### Fields inherited from class org.glassfish.tyrus.spi.UpgradeRequest

`AUTHORIZATION, CLUSTER_CONNECTION_ID_HEADER, CONNECTION, ENABLE_TRACING_HEADER, HOST, ORIGIN_HEADER, RESPONSE_CODE_MESSAGE, SEC_WS_ORIGIN_HEADER, SERVER_KEY_HASH, TRACING_THRESHOLD, UPGRADE, WEBSOCKET`

### Fields inherited from interface jakarta.websocket.server.HandshakeRequest

`SEC_WEBSOCKET_EXTENSIONS, SEC_WEBSOCKET_KEY, SEC_WEBSOCKET_PROTOCOL, SEC_WEBSOCKET_VERSION`

-

## Method Summary

Modifier and Type
Method
Description
`String`
`getHeader(String name)`

Returns the header value corresponding to the name.

`Map<String,List<String>>`
`getHeaders()`

Get headers.

`Object`
`getHttpSession()`

`Map<String,List<String>>`
`getParameterMap()`

`String`
`getQueryString()`

`String`
`getRemoteAddr()`

Get the Internet Protocol (IP) address of the client or last proxy that sent the request.

`String`
`getRequestUri()`

`URI`
`getRequestURI()`

`String`
`getServerAddr()`

Returns the host name of the server to which the request was sent.

`int`
`getServerPort()`

Get the port of the last client or proxy that sent the request.

`Principal`
`getUserPrincipal()`

`boolean`
`isSecure()`

`boolean`
`isUserInRole(String role)`

`void`
`lock()`

Make headers and parameter map read-only.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Method Details

-

### getHeaders

public Map<String,List<String>> getHeaders()
Get headers.

Returns:
headers map. List items are corresponding to header declaration in HTTP request.

-

### getHeader

public String getHeader(String name)
Returns the header value corresponding to the name.

Specified by:
`getHeader` in class `org.glassfish.tyrus.spi.UpgradeRequest`
Parameters:
`name` - header name.
Returns:
`List` of header values iff found, `null` otherwise.

-

### lock

public void lock()
Make headers and parameter map read-only.

-

### getUserPrincipal

public Principal getUserPrincipal()

-

### getRequestURI

public URI getRequestURI()

-

### isUserInRole

public boolean isUserInRole(String role)

-

### getHttpSession

public Object getHttpSession()

-

### getParameterMap

public Map<String,List<String>> getParameterMap()

-

### getQueryString

public String getQueryString()

-

### getRequestUri

public String getRequestUri()

Specified by:
`getRequestUri` in class `org.glassfish.tyrus.spi.UpgradeRequest`

-

### isSecure

public boolean isSecure()

Specified by:
`isSecure` in class `org.glassfish.tyrus.spi.UpgradeRequest`

-

### getRemoteAddr

public String getRemoteAddr()
Get the Internet Protocol (IP) address of the client or last proxy that sent the request.

Returns:
a `String` containing the IP address of the client that sent the request or `null` when
 method is called on client-side.

-

### getServerAddr

public String getServerAddr()
Returns the host name of the server to which the request was sent.

Returns:
a `String` Returns the host name of the server to which the request was sent or `null` when
 method is called on client-side.

-

### getServerPort

public int getServerPort()
Get the port of the last client or proxy that sent the request.

Returns:
a port of the client that sent the request.
