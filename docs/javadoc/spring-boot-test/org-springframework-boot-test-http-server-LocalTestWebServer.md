# Class LocalTestWebServer

java.lang.Object
org.springframework.boot.test.http.server.LocalTestWebServer

---

public final class LocalTestWebServer
extends Object
Provides details of a locally running test web server which may have been started on a
dynamic port.

Since:
4.0.0

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static final record `
`LocalTestWebServer.BaseUriDetails`

Details of the base URI to the local test web server.

`static interface `
`LocalTestWebServer.Provider`

Internal strategy used to provide the running `LocalTestWebServer`.

`static enum `
`LocalTestWebServer.Scheme`

Supported HTTP schemes.

- 

## Method Summary

Modifier and Type
Method
Description
`static @Nullable LocalTestWebServer`
`get(org.springframework.context.ApplicationContext applicationContext)`

Return the `LocalTestWebServer` instance provided from the
`ApplicationContext` or `null` of no local server is started or could
be provided.

`static LocalTestWebServer`
`obtain(org.springframework.context.ApplicationContext applicationContext)`

Obtain the `LocalTestWebServer` instance provided from the
`ApplicationContext`.

`static LocalTestWebServer`
`of(LocalTestWebServer.Scheme scheme,
 int port)`

Factory method to create a new `LocalTestWebServer` instance.

`static LocalTestWebServer`
`of(LocalTestWebServer.Scheme scheme,
 int port,
 @Nullable String contextPath)`

Factory method to create a new `LocalTestWebServer` instance.

`static LocalTestWebServer`
`of(LocalTestWebServer.Scheme scheme,
 Supplier<LocalTestWebServer.BaseUriDetails> baseUriDetailsSupplier)`

Factory method to create a new `LocalTestWebServer` instance.

`LocalTestWebServer.Scheme`
`scheme()`

Return if URI scheme used for the request.

`String`
`uri()`

Return the URI of the running local test server.

`String`
`uri(@Nullable String uri)`

Return the URI of the running local test server taking into account the given
`uri`.

`org.springframework.web.util.UriBuilder`
`uriBuilder(@Nullable String uri)`

Return a new `UriBuilder` with the base URI template initialized from the
local server `uri()`.

`org.springframework.web.util.UriBuilderFactory`
`uriBuilderFactory()`

Return a new `UriBuilderFactory` with the base URI template initialized from
the local server `uri()`.

`LocalTestWebServer`
`withPath(String path)`

Return a new `LocalTestWebServer` instance that applies the given
`path`.

### Methods inherited from class Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

- 

## Method Details

  - 

### scheme

public LocalTestWebServer.Scheme scheme()
Return if URI scheme used for the request. This method can be safely called before
the local test server is fully running.

Returns:
if the web server uses an HTTPS address

  - 

### uri

public String uri()
Return the URI of the running local test server. This method should only be called
once the local test server is fully running.

Returns:
the URI of the server

  - 

### uri

public String uri(@Nullable String uri)
Return the URI of the running local test server taking into account the given
`uri`. This method should only be called once the local test server is fully
running.

Parameters:
`uri` - a URI template for the builder or `null`
Returns:
the URI of the server

  - 

### uriBuilder

public org.springframework.web.util.UriBuilder uriBuilder(@Nullable String uri)
Return a new `UriBuilder` with the base URI template initialized from the
local server `uri()`. This method should only be called once the local test
server is fully running.

Parameters:
`uri` - a URI template for the builder or `null`
Returns:
a new `UriBuilder` instance

  - 

### uriBuilderFactory

public org.springframework.web.util.UriBuilderFactory uriBuilderFactory()
Return a new `UriBuilderFactory` with the base URI template initialized from
the local server `uri()`. Methods of the return UriBuilderFactory should
only be called once the local test server is fully running.

Returns:
a new `UriBuilderFactory`

  - 

### withPath

public LocalTestWebServer withPath(String path)
Return a new `LocalTestWebServer` instance that applies the given
`path`.

Parameters:
`path` - a path to append
Returns:
a new instance with the path added

  - 

### of

public static LocalTestWebServer of(LocalTestWebServer.Scheme scheme,
 int port)
Factory method to create a new `LocalTestWebServer` instance.

Parameters:
`scheme` - the URL scheme
`port` - the port of the running server
Returns:
a new `LocalTestWebServer` instance

  - 

### of

public static LocalTestWebServer of(LocalTestWebServer.Scheme scheme,
 int port,
 @Nullable String contextPath)
Factory method to create a new `LocalTestWebServer` instance.

Parameters:
`scheme` - the URL scheme
`port` - the port of the running server
`contextPath` - the context path of the running server
Returns:
a new `LocalTestWebServer` instance

  - 

### of

public static LocalTestWebServer of(LocalTestWebServer.Scheme scheme,
 Supplier<LocalTestWebServer.BaseUriDetails> baseUriDetailsSupplier)
Factory method to create a new `LocalTestWebServer` instance.

Parameters:
`scheme` - the URL scheme
`baseUriDetailsSupplier` - a supplier to provide the details of the base URI
Returns:
a new `LocalTestWebServer` instance

  - 

### obtain

public static LocalTestWebServer obtain(org.springframework.context.ApplicationContext applicationContext)
Obtain the `LocalTestWebServer` instance provided from the
`ApplicationContext`.

Parameters:
`applicationContext` - the application context
Returns:
the local test web server (never `null`)

  - 

### get

public static @Nullable LocalTestWebServer get(org.springframework.context.ApplicationContext applicationContext)
Return the `LocalTestWebServer` instance provided from the
`ApplicationContext` or `null` of no local server is started or could
be provided.

Parameters:
`applicationContext` - the application context
Returns:
the local test web server or `null`