Module org.glassfish.tyrus.core
Package org.glassfish.tyrus.core

# Class RequestContext.Builder

java.lang.Object
org.glassfish.tyrus.core.RequestContext.Builder

Enclosing class:
`RequestContext`

---

public static final class RequestContext.Builder
extends Object
`RequestContext` builder.

-

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static interface`
`RequestContext.Builder.IsUserInRoleDelegate`

Is user in role delegate.

-

## Constructor Summary

Constructors

Constructor
Description
`Builder()`

-

## Method Summary

Modifier and Type
Method
Description
`RequestContext`
`build()`

Build `RequestContext` from given properties.

`static RequestContext.Builder`
`create()`

Create empty builder.

`static RequestContext.Builder`
`create(RequestContext requestContext)`

Create builder instance based on provided `RequestContext`.

`RequestContext.Builder`
`httpSession(Object httpSession)`

Set http session.

`RequestContext.Builder`
`isUserInRoleDelegate(RequestContext.Builder.IsUserInRoleDelegate isUserInRoleDelegate)`

Set delegate for `RequestContext.isUserInRole(String)` method.

`RequestContext.Builder`
`parameterMap(Map<String,String[]> parameterMap)`

Set parameter map.

`RequestContext.Builder`
`queryString(String queryString)`

Set query string.

`RequestContext.Builder`
`remoteAddr(String remoteAddr)`

Set remote address.

`RequestContext.Builder`
`requestURI(URI requestURI)`

Set request URI.

`RequestContext.Builder`
`secure(boolean secure)`

Set secure state.

`RequestContext.Builder`
`serverAddr(String serverAddr)`

Set server address or hostname.

`RequestContext.Builder`
`serverPort(int serverPort)`

Set server port.

`RequestContext.Builder`
`tyrusProperties(Map<String,Object> tyrusProperties)`

Set properties for Tyrus framework.

`RequestContext.Builder`
`userPrincipal(Principal principal)`

Set `Principal`.

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

-

## Constructor Details

-

### Builder

public Builder()

-

## Method Details

-

### create

public static RequestContext.Builder create()
Create empty builder.

Returns:
empty builder instance.

-

### create

public static RequestContext.Builder create(RequestContext requestContext)
Create builder instance based on provided `RequestContext`.

Parameters:
`requestContext` - request context.
Returns:
builder instance.

-

### requestURI

public RequestContext.Builder requestURI(URI requestURI)
Set request URI.

Parameters:
`requestURI` - request URI to be set.
Returns:
updated `RequestContext.Builder` instance.

-

### queryString

public RequestContext.Builder queryString(String queryString)
Set query string.

Parameters:
`queryString` - query string to be set.
Returns:
updated `RequestContext.Builder` instance.

-

### httpSession

public RequestContext.Builder httpSession(Object httpSession)
Set http session.

Parameters:
`httpSession` - `jakarta.servlet.http.HttpSession` session to be set.
Returns:
updated `RequestContext.Builder` instance.

-

### secure

public RequestContext.Builder secure(boolean secure)
Set secure state.

Parameters:
`secure` - secure state to be set.
Returns:
updated `RequestContext.Builder` instance.

-

### userPrincipal

public RequestContext.Builder userPrincipal(Principal principal)
Set `Principal`.

Parameters:
`principal` - principal to be set.
Returns:
updated `RequestContext.Builder` instance.

-

### isUserInRoleDelegate

public RequestContext.Builder isUserInRoleDelegate(RequestContext.Builder.IsUserInRoleDelegate isUserInRoleDelegate)
Set delegate for `RequestContext.isUserInRole(String)` method.

Parameters:
`isUserInRoleDelegate` - delegate for `RequestContext.isUserInRole(String)`.
Returns:
updated `RequestContext.Builder` instance.

-

### parameterMap

public RequestContext.Builder parameterMap(Map<String,String[]> parameterMap)
Set parameter map.

Parameters:
`parameterMap` - parameter map. Takes map returned from ServletRequest#getParameterMap.
Returns:
updated `RequestContext.Builder` instance.

-

### remoteAddr

public RequestContext.Builder remoteAddr(String remoteAddr)
Set remote address.

Parameters:
`remoteAddr` - remote address to be set.
Returns:
updated `RequestContext.Builder` instance.

-

### serverAddr

public RequestContext.Builder serverAddr(String serverAddr)
Set server address or hostname.

Parameters:
`serverAddr` - server address to be set.
Returns:
updated `RequestContext.Builder` instance.

-

### serverPort

public RequestContext.Builder serverPort(int serverPort)
Set server port.

Parameters:
`serverPort` - server port to be set.
Returns:
updated `RequestContext.Builder` instance.

-

### tyrusProperties

public RequestContext.Builder tyrusProperties(Map<String,Object> tyrusProperties)
Set properties for Tyrus framework.

Parameters:
`tyrusProperties` -

-

### build

public RequestContext build()
Build `RequestContext` from given properties.

Returns:
created `RequestContext`.
