Package org.jsoup

# Interface Connection.Request

All Superinterfaces:
`Connection.Base<Connection.Request>`

All Known Implementing Classes:
`HttpConnection.Request`

Enclosing interface:
Connection

---

public static interface Connection.Request
extends Connection.Base<Connection.Request>
Represents a HTTP request.

- 

## Method Summary

Modifier and Type
Method
Description
`default @Nullable RequestAuthenticator`
`auth()`

Get the RequestAuthenticator, if any, that will be used on this request.

`default Connection.Request`
`auth(@Nullable RequestAuthenticator authenticator)`

Set the authenticator to use for this request.

`Collection<Connection.KeyVal>`
`data()`

Get all of the request's data parameters

`Connection.Request`
`data(Connection.KeyVal keyval)`

Add a data parameter to the request

`boolean`
`followRedirects()`

Get the current followRedirects configuration.

`Connection.Request`
`followRedirects(boolean followRedirects)`

Configures the request to (not) follow server redirects.

`boolean`
`ignoreContentType()`

Get the current ignoreContentType configuration.

`Connection.Request`
`ignoreContentType(boolean ignoreContentType)`

Configures the request to ignore the Content-Type of the response.

`boolean`
`ignoreHttpErrors()`

Get the current ignoreHttpErrors configuration.

`Connection.Request`
`ignoreHttpErrors(boolean ignoreHttpErrors)`

Configures the request to ignore HTTP errors in the response.

`int`
`maxBodySize()`

Get the maximum body size, in bytes.

`Connection.Request`
`maxBodySize(int bytes)`

Update the maximum body size, in bytes.

`Parser`
`parser()`

Get the current parser to use when parsing the document.

`Connection.Request`
`parser(Parser parser)`

Specify the parser to use when parsing the document.

`String`
`postDataCharset()`

Gets the post data character set for x-www-form-urlencoded post data

`Connection.Request`
`postDataCharset(String charset)`

Sets the post data character set for x-www-form-urlencoded post data

`@Nullable Proxy`
`proxy()`

Get the proxy used for this request.

`Connection.Request`
`proxy(@Nullable Proxy proxy)`

Update the proxy for this request.

`Connection.Request`
`proxy(String host,
 int port)`

Set the HTTP proxy to use for this request.

`@Nullable String`
`requestBody()`

Get the current request body.

`Connection.Request`
`requestBody(@Nullable String body)`

Set a POST (or PUT) request body.

`default Connection.Request`
`requestBodyStream(InputStream stream)`

Set the request body.

`default @Nullable SSLContext`
`sslContext()`

Get the current custom SSL context, if any.

`default Connection.Request`
`sslContext(SSLContext sslContext)`

Set a custom SSL context for HTTPS connections.

`@Nullable SSLSocketFactory`
`sslSocketFactory()`

Get the current custom SSL socket factory, if any.

`void`
`sslSocketFactory(SSLSocketFactory sslSocketFactory)`

Deprecated.
use `sslContext(SSLContext)` instead; will be removed in jsoup 1.24.1.

`int`
`timeout()`

Get the request timeout, in milliseconds.

`Connection.Request`
`timeout(int millis)`

Update the request timeout.

### Methods inherited from interface org.jsoup.Connection.Base

`addHeader, cookie, cookie, cookies, hasCookie, hasHeader, hasHeaderWithValue, header, header, headers, headers, method, method, multiHeaders, removeCookie, removeHeader, url, url`

- 

## Method Details

  - 

### proxy

@Nullable Proxy proxy()
Get the proxy used for this request.

Returns:
the proxy; `null` if not enabled.

  - 

### proxy

Connection.Request proxy(@Nullable Proxy proxy)
Update the proxy for this request.

Parameters:
`proxy` - the proxy ot use; `null` to disable.
Returns:
this Request, for chaining

  - 

### proxy

Connection.Request proxy(String host,
 int port)
Set the HTTP proxy to use for this request.

Parameters:
`host` - the proxy hostname
`port` - the proxy port
Returns:
this Connection, for chaining

  - 

### timeout

int timeout()
Get the request timeout, in milliseconds.

Returns:
the timeout in milliseconds.

  - 

### timeout

Connection.Request timeout(int millis)
Update the request timeout.

Parameters:
`millis` - timeout, in milliseconds
Returns:
this Request, for chaining

  - 

### maxBodySize

int maxBodySize()
Get the maximum body size, in bytes.

Returns:
the maximum body size, in bytes.

  - 

### maxBodySize

Connection.Request maxBodySize(int bytes)
Update the maximum body size, in bytes.

Parameters:
`bytes` - maximum body size, in bytes.
Returns:
this Request, for chaining

  - 

### followRedirects

boolean followRedirects()
Get the current followRedirects configuration.

Returns:
true if followRedirects is enabled.

  - 

### followRedirects

Connection.Request followRedirects(boolean followRedirects)
Configures the request to (not) follow server redirects. By default this is **true**.

Parameters:
`followRedirects` - true if server redirects should be followed.
Returns:
this Request, for chaining

  - 

### ignoreHttpErrors

boolean ignoreHttpErrors()
Get the current ignoreHttpErrors configuration.

Returns:
true if errors will be ignored; false (default) if HTTP errors will cause an IOException to be
 thrown.

  - 

### ignoreHttpErrors

Connection.Request ignoreHttpErrors(boolean ignoreHttpErrors)
Configures the request to ignore HTTP errors in the response.

Parameters:
`ignoreHttpErrors` - set to true to ignore HTTP errors.
Returns:
this Request, for chaining

  - 

### ignoreContentType

boolean ignoreContentType()
Get the current ignoreContentType configuration.

Returns:
true if invalid content-types will be ignored; false (default) if they will cause an IOException to
 be thrown.

  - 

### ignoreContentType

Connection.Request ignoreContentType(boolean ignoreContentType)
Configures the request to ignore the Content-Type of the response.

Parameters:
`ignoreContentType` - set to true to ignore the content type.
Returns:
this Request, for chaining

  - 

### sslSocketFactory

@Nullable SSLSocketFactory sslSocketFactory()
Get the current custom SSL socket factory, if any.

Returns:
custom SSL socket factory if set, null otherwise

  - 

### sslSocketFactory

@Deprecated
void sslSocketFactory(SSLSocketFactory sslSocketFactory)
Deprecated.
use `sslContext(SSLContext)` instead; will be removed in jsoup 1.24.1.

Set a custom SSL socket factory for HTTPS connections.
         

Note: if set, the legacy `HttpURLConnection` will be used instead of the JVM's
         `HttpClient`.

Parameters:
`sslSocketFactory` - SSL socket factory
See Also:

    - `sslContext(SSLContext)`

  - 

### sslContext

default @Nullable SSLContext sslContext()
Get the current custom SSL context, if any.

Returns:
custom SSL context if set, null otherwise
Since:
1.21.2

  - 

### sslContext

default Connection.Request sslContext(SSLContext sslContext)
Set a custom SSL context for HTTPS connections.
         

Note: when using the legacy `HttpURLConnection`, only the `SSLSocketFactory` from the
         context will be used.

Parameters:
`sslContext` - SSL context
Returns:
this Request, for chaining
Since:
1.21.2

  - 

### data

Connection.Request data(Connection.KeyVal keyval)
Add a data parameter to the request

Parameters:
`keyval` - data to add.
Returns:
this Request, for chaining

  - 

### data

Collection<Connection.KeyVal> data()
Get all of the request's data parameters

Returns:
collection of keyvals

  - 

### requestBody

Connection.Request requestBody(@Nullable String body)
Set a POST (or PUT) request body. Useful when a server expects a plain request body, not a set of URL
 encoded form key/value pairs. E.g.:
 `

```
Jsoup.connect(url)
 .requestBody(json)
 .header("Content-Type", "application/json")
 .post();
```
`
 

If any data key/vals are supplied, they will be sent as URL query params.

Parameters:
`body` - to use as the request body. Set to null to clear a previously set body.
Returns:
this Request, for chaining
See Also:

    - `requestBodyStream(InputStream)`

  - 

### requestBody

@Nullable String requestBody()
Get the current request body.

Returns:
null if not set.

  - 

### requestBodyStream

default Connection.Request requestBodyStream(InputStream stream)
Set the request body. Useful for posting data such as byte arrays or files, and the server expects a single
         request body (and not a multipart upload). E.g.:
         `

```
 Jsoup.connect(url)
         .requestBody(new ByteArrayInputStream(bytes))
         .header("Content-Type", "application/octet-stream")
         .post();
         
```
`
         

Or, use a FileInputStream to data from disk.
         

You should close the stream in a finally block.

Parameters:
`stream` - the input stream to send.
Returns:
this Request, for chaining
Since:
1.20.1
See Also:

    - `requestBody(String)`

  - 

### parser

Connection.Request parser(Parser parser)
Specify the parser to use when parsing the document.

Parameters:
`parser` - parser to use.
Returns:
this Request, for chaining

  - 

### parser

Parser parser()
Get the current parser to use when parsing the document.

Returns:
current Parser

  - 

### postDataCharset

Connection.Request postDataCharset(String charset)
Sets the post data character set for x-www-form-urlencoded post data

Parameters:
`charset` - character set to encode post data
Returns:
this Request, for chaining

  - 

### postDataCharset

String postDataCharset()
Gets the post data character set for x-www-form-urlencoded post data

Returns:
character set to encode post data

  - 

### auth

default Connection.Request auth(@Nullable RequestAuthenticator authenticator)
Set the authenticator to use for this request.
         See `Connection.auth(authenticator)` for examples and
         implementation notes.

Parameters:
`authenticator` - the authenticator
Returns:
this Request, for chaining.
Since:
1.17.1

  - 

### auth

default @Nullable RequestAuthenticator auth()
Get the RequestAuthenticator, if any, that will be used on this request.

Returns:
the RequestAuthenticator, or `null` if not set
Since:
1.17.1