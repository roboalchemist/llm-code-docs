Package org.jsoup.helper

# Class HttpConnection.Request

java.lang.Object
org.jsoup.helper.HttpConnection.Request

All Implemented Interfaces:
`Connection.Base<Connection.Request>`, `Connection.Request`

Enclosing class:
HttpConnection

---

public static class HttpConnection.Request
extends Object
implements Connection.Request

- 

## Method Summary

Modifier and Type
Method
Description
`Connection.Request`
`addHeader(String name,
 @Nullable String value)`

Add a header.

`@Nullable RequestAuthenticator`
`auth()`

Get the RequestAuthenticator, if any, that will be used on this request.

`Connection.Request`
`auth(@Nullable RequestAuthenticator authenticator)`

Set the authenticator to use for this request.

`String`
`cookie(String name)`

Get a cookie value by name from this request/response.

`Connection.Request`
`cookie(String name,
 String value)`

Set a cookie in this request/response.

`Map<String,String>`
`cookies()`

Retrieve the request/response cookies as a map.

`Collection<Connection.KeyVal>`
`data()`

Get all of the request's data parameters

`HttpConnection.Request`
`data(Connection.KeyVal keyval)`

Add a data parameter to the request

`boolean`
`followRedirects()`

Get the current followRedirects configuration.

`Connection.Request`
`followRedirects(boolean followRedirects)`

Configures the request to (not) follow server redirects.

`boolean`
`hasCookie(String name)`

Check if a cookie is present

`boolean`
`hasHeader(String name)`

Check if a header is present

`boolean`
`hasHeaderWithValue(String name,
 String value)`

Test if the request has a header with this value (case-insensitive).

`@Nullable String`
`header(String name)`

Get the value of a header.

`Connection.Request`
`header(String name,
 String value)`

Set a header.

`Map<String,String>`
`headers()`

Retrieve all of the request/response header names and corresponding values as a map.

`List<String>`
`headers(String name)`

Get the values of a header.

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

`Connection.Method`
`method()`

Get the request method, which defaults to `GET`

`Connection.Request`
`method(Connection.Method method)`

Set the request method

`Map<String,List<String>>`
`multiHeaders()`

Retreive all of the headers, keyed by the header name, and with a list of values per header.

`Parser`
`parser()`

Get the current parser to use when parsing the document.

`HttpConnection.Request`
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

`HttpConnection.Request`
`proxy(@Nullable Proxy proxy)`

Update the proxy for this request.

`HttpConnection.Request`
`proxy(String host,
 int port)`

Set the HTTP proxy to use for this request.

`Connection.Request`
`removeCookie(String name)`

Remove a cookie by name

`Connection.Request`
`removeHeader(String name)`

Remove headers by name.

`@Nullable String`
`requestBody()`

Get the current request body.

`Connection.Request`
`requestBody(@Nullable String body)`

Set a POST (or PUT) request body.

`Connection.Request`
`requestBodyStream(InputStream stream)`

Set the request body.

`@Nullable SSLContext`
`sslContext()`

Get the current custom SSL context, if any.

`Connection.Request`
`sslContext(SSLContext sslContext)`

Set a custom SSL context for HTTPS connections.

`@Nullable SSLSocketFactory`
`sslSocketFactory()`

Get the current custom SSL socket factory, if any.

`void`
`sslSocketFactory(SSLSocketFactory sslSocketFactory)`

Set a custom SSL socket factory for HTTPS connections.

`int`
`timeout()`

Get the request timeout, in milliseconds.

`HttpConnection.Request`
`timeout(int millis)`

Update the request timeout.

`URL`
`url()`

Get the URL of this Request or Response.

`Connection.Request`
`url(URL url)`

Set the URL

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface org.jsoup.Connection.Base

`addHeader, cookie, cookie, cookies, hasCookie, hasHeader, hasHeaderWithValue, header, header, headers, headers, method, method, multiHeaders, removeCookie, removeHeader, url, url`

- 

## Method Details

  - 

### proxy

public @Nullable Proxy proxy()
Description copied from interface: `Connection.Request`
Get the proxy used for this request.

Specified by:
`proxy` in interface `Connection.Request`
Returns:
the proxy; `null` if not enabled.

  - 

### proxy

public HttpConnection.Request proxy(@Nullable Proxy proxy)
Description copied from interface: `Connection.Request`
Update the proxy for this request.

Specified by:
`proxy` in interface `Connection.Request`
Parameters:
`proxy` - the proxy ot use; `null` to disable.
Returns:
this Request, for chaining

  - 

### proxy

public HttpConnection.Request proxy(String host,
 int port)
Description copied from interface: `Connection.Request`
Set the HTTP proxy to use for this request.

Specified by:
`proxy` in interface `Connection.Request`
Parameters:
`host` - the proxy hostname
`port` - the proxy port
Returns:
this Connection, for chaining

  - 

### timeout

public int timeout()
Description copied from interface: `Connection.Request`
Get the request timeout, in milliseconds.

Specified by:
`timeout` in interface `Connection.Request`
Returns:
the timeout in milliseconds.

  - 

### timeout

public HttpConnection.Request timeout(int millis)
Description copied from interface: `Connection.Request`
Update the request timeout.

Specified by:
`timeout` in interface `Connection.Request`
Parameters:
`millis` - timeout, in milliseconds
Returns:
this Request, for chaining

  - 

### maxBodySize

public int maxBodySize()
Description copied from interface: `Connection.Request`
Get the maximum body size, in bytes.

Specified by:
`maxBodySize` in interface `Connection.Request`
Returns:
the maximum body size, in bytes.

  - 

### maxBodySize

public Connection.Request maxBodySize(int bytes)
Description copied from interface: `Connection.Request`
Update the maximum body size, in bytes.

Specified by:
`maxBodySize` in interface `Connection.Request`
Parameters:
`bytes` - maximum body size, in bytes.
Returns:
this Request, for chaining

  - 

### followRedirects

public boolean followRedirects()
Description copied from interface: `Connection.Request`
Get the current followRedirects configuration.

Specified by:
`followRedirects` in interface `Connection.Request`
Returns:
true if followRedirects is enabled.

  - 

### followRedirects

public Connection.Request followRedirects(boolean followRedirects)
Description copied from interface: `Connection.Request`
Configures the request to (not) follow server redirects. By default this is **true**.

Specified by:
`followRedirects` in interface `Connection.Request`
Parameters:
`followRedirects` - true if server redirects should be followed.
Returns:
this Request, for chaining

  - 

### ignoreHttpErrors

public boolean ignoreHttpErrors()
Description copied from interface: `Connection.Request`
Get the current ignoreHttpErrors configuration.

Specified by:
`ignoreHttpErrors` in interface `Connection.Request`
Returns:
true if errors will be ignored; false (default) if HTTP errors will cause an IOException to be
 thrown.

  - 

### sslSocketFactory

public @Nullable SSLSocketFactory sslSocketFactory()
Description copied from interface: `Connection.Request`
Get the current custom SSL socket factory, if any.

Specified by:
`sslSocketFactory` in interface `Connection.Request`
Returns:
custom SSL socket factory if set, null otherwise

  - 

### sslSocketFactory

public void sslSocketFactory(SSLSocketFactory sslSocketFactory)
Description copied from interface: `Connection.Request`
Set a custom SSL socket factory for HTTPS connections.
         

Note: if set, the legacy `HttpURLConnection` will be used instead of the JVM's
         `HttpClient`.

Specified by:
`sslSocketFactory` in interface `Connection.Request`
Parameters:
`sslSocketFactory` - SSL socket factory
See Also:

    - `Connection.Request.sslContext(SSLContext)`

  - 

### sslContext

public @Nullable SSLContext sslContext()
Description copied from interface: `Connection.Request`
Get the current custom SSL context, if any.

Specified by:
`sslContext` in interface `Connection.Request`
Returns:
custom SSL context if set, null otherwise

  - 

### sslContext

public Connection.Request sslContext(SSLContext sslContext)
Description copied from interface: `Connection.Request`
Set a custom SSL context for HTTPS connections.
         

Note: when using the legacy `HttpURLConnection`, only the `SSLSocketFactory` from the
         context will be used.

Specified by:
`sslContext` in interface `Connection.Request`
Parameters:
`sslContext` - SSL context
Returns:
this Request, for chaining

  - 

### ignoreHttpErrors

public Connection.Request ignoreHttpErrors(boolean ignoreHttpErrors)
Description copied from interface: `Connection.Request`
Configures the request to ignore HTTP errors in the response.

Specified by:
`ignoreHttpErrors` in interface `Connection.Request`
Parameters:
`ignoreHttpErrors` - set to true to ignore HTTP errors.
Returns:
this Request, for chaining

  - 

### ignoreContentType

public boolean ignoreContentType()
Description copied from interface: `Connection.Request`
Get the current ignoreContentType configuration.

Specified by:
`ignoreContentType` in interface `Connection.Request`
Returns:
true if invalid content-types will be ignored; false (default) if they will cause an IOException to
 be thrown.

  - 

### ignoreContentType

public Connection.Request ignoreContentType(boolean ignoreContentType)
Description copied from interface: `Connection.Request`
Configures the request to ignore the Content-Type of the response.

Specified by:
`ignoreContentType` in interface `Connection.Request`
Parameters:
`ignoreContentType` - set to true to ignore the content type.
Returns:
this Request, for chaining

  - 

### data

public HttpConnection.Request data(Connection.KeyVal keyval)
Description copied from interface: `Connection.Request`
Add a data parameter to the request

Specified by:
`data` in interface `Connection.Request`
Parameters:
`keyval` - data to add.
Returns:
this Request, for chaining

  - 

### data

public Collection<Connection.KeyVal> data()
Description copied from interface: `Connection.Request`
Get all of the request's data parameters

Specified by:
`data` in interface `Connection.Request`
Returns:
collection of keyvals

  - 

### requestBody

public Connection.Request requestBody(@Nullable String body)
Description copied from interface: `Connection.Request`
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

Specified by:
`requestBody` in interface `Connection.Request`
Parameters:
`body` - to use as the request body. Set to null to clear a previously set body.
Returns:
this Request, for chaining
See Also:

    - `Connection.Request.requestBodyStream(InputStream)`

  - 

### requestBody

public @Nullable String requestBody()
Description copied from interface: `Connection.Request`
Get the current request body.

Specified by:
`requestBody` in interface `Connection.Request`
Returns:
null if not set.

  - 

### requestBodyStream

public Connection.Request requestBodyStream(InputStream stream)
Description copied from interface: `Connection.Request`
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

Specified by:
`requestBodyStream` in interface `Connection.Request`
Parameters:
`stream` - the input stream to send.
Returns:
this Request, for chaining
See Also:

    - `Connection.Request.requestBody(String)`

  - 

### parser

public HttpConnection.Request parser(Parser parser)
Description copied from interface: `Connection.Request`
Specify the parser to use when parsing the document.

Specified by:
`parser` in interface `Connection.Request`
Parameters:
`parser` - parser to use.
Returns:
this Request, for chaining

  - 

### parser

public Parser parser()
Description copied from interface: `Connection.Request`
Get the current parser to use when parsing the document.

Specified by:
`parser` in interface `Connection.Request`
Returns:
current Parser

  - 

### postDataCharset

public Connection.Request postDataCharset(String charset)
Description copied from interface: `Connection.Request`
Sets the post data character set for x-www-form-urlencoded post data

Specified by:
`postDataCharset` in interface `Connection.Request`
Parameters:
`charset` - character set to encode post data
Returns:
this Request, for chaining

  - 

### postDataCharset

public String postDataCharset()
Description copied from interface: `Connection.Request`
Gets the post data character set for x-www-form-urlencoded post data

Specified by:
`postDataCharset` in interface `Connection.Request`
Returns:
character set to encode post data

  - 

### auth

public Connection.Request auth(@Nullable RequestAuthenticator authenticator)
Description copied from interface: `Connection.Request`
Set the authenticator to use for this request.
         See `Connection.auth(authenticator)` for examples and
         implementation notes.

Specified by:
`auth` in interface `Connection.Request`
Parameters:
`authenticator` - the authenticator
Returns:
this Request, for chaining.

  - 

### auth

public @Nullable RequestAuthenticator auth()
Description copied from interface: `Connection.Request`
Get the RequestAuthenticator, if any, that will be used on this request.

Specified by:
`auth` in interface `Connection.Request`
Returns:
the RequestAuthenticator, or `null` if not set

  - 

### url

public URL url()
Description copied from interface: `Connection.Base`
Get the URL of this Request or Response. For redirected responses, this will be the final destination URL.

Specified by:
`url` in interface `Connection.Base<T extends Connection.Base<T>>`
Returns:
URL

  - 

### url

public Connection.Request url(URL url)
Description copied from interface: `Connection.Base`
Set the URL

Specified by:
`url` in interface `Connection.Base<T extends Connection.Base<T>>`
Parameters:
`url` - new URL
Returns:
this, for chaining

  - 

### method

public Connection.Method method()
Description copied from interface: `Connection.Base`
Get the request method, which defaults to `GET`

Specified by:
`method` in interface `Connection.Base<T extends Connection.Base<T>>`
Returns:
method

  - 

### method

public Connection.Request method(Connection.Method method)
Description copied from interface: `Connection.Base`
Set the request method

Specified by:
`method` in interface `Connection.Base<T extends Connection.Base<T>>`
Parameters:
`method` - new method
Returns:
this, for chaining

  - 

### header

public @Nullable String header(String name)
Description copied from interface: `Connection.Base`
Get the value of a header. If there is more than one header value with the same name, the headers are returned
 comma separated, per rfc2616-sec4.
 

 Header names are case-insensitive.
 

Specified by:
`header` in interface `Connection.Base<T extends Connection.Base<T>>`
Parameters:
`name` - name of header (case-insensitive)
Returns:
value of header, or null if not set.
See Also:

    - `Connection.Base.hasHeader(String)`

    - `Connection.Base.cookie(String)`

  - 

### addHeader

public Connection.Request addHeader(String name,
 @Nullable String value)
Description copied from interface: `Connection.Base`
Add a header. The header will be added regardless of whether a header with the same name already exists.
 

For compatibility, if the content of the header includes text that cannot be represented by ISO-8859-1,
 then it should be encoded first per RFC 2047.

Specified by:
`addHeader` in interface `Connection.Base<T extends Connection.Base<T>>`
Parameters:
`name` - Name of new header
`value` - Value of new header
Returns:
this, for chaining

  - 

### headers

public List<String> headers(String name)
Description copied from interface: `Connection.Base`
Get the values of a header.

Specified by:
`headers` in interface `Connection.Base<T extends Connection.Base<T>>`
Parameters:
`name` - header name, case-insensitive.
Returns:
a list of values for this header, or an empty list if not set.

  - 

### header

public Connection.Request header(String name,
 String value)
Description copied from interface: `Connection.Base`
Set a header. This method will overwrite any existing header with the same case-insensitive name. If there
 is more than one value for this header, this method will update the first matching header.
 

For compatibility, if the content of the header includes text that cannot be represented by ISO-8859-1,
 then it should be encoded first per RFC 2047.

Specified by:
`header` in interface `Connection.Base<T extends Connection.Base<T>>`
Parameters:
`name` - Name of header
`value` - Value of header
Returns:
this, for chaining
See Also:

    - `Connection.Base.addHeader(String, String)`

  - 

### hasHeader

public boolean hasHeader(String name)
Description copied from interface: `Connection.Base`
Check if a header is present

Specified by:
`hasHeader` in interface `Connection.Base<T extends Connection.Base<T>>`
Parameters:
`name` - name of header (case-insensitive)
Returns:
if the header is present in this request/response

  - 

### hasHeaderWithValue

public boolean hasHeaderWithValue(String name,
 String value)
Test if the request has a header with this value (case-insensitive).

Specified by:
`hasHeaderWithValue` in interface `Connection.Base<T extends Connection.Base<T>>`
Parameters:
`name` - header name (case-insensitive)
`value` - value (case-insensitive)
Returns:
if the header and value pair are set in this req/res

  - 

### removeHeader

public Connection.Request removeHeader(String name)
Description copied from interface: `Connection.Base`
Remove headers by name. If there is more than one header with this name, they will all be removed.

Specified by:
`removeHeader` in interface `Connection.Base<T extends Connection.Base<T>>`
Parameters:
`name` - name of header to remove (case-insensitive)
Returns:
this, for chaining

  - 

### headers

public Map<String,String> headers()
Description copied from interface: `Connection.Base`
Retrieve all of the request/response header names and corresponding values as a map. For headers with multiple
 values, only the first header is returned.
 

Note that this is a view of the headers only, and changes made to this map will not be reflected in the
 request/response object.

Specified by:
`headers` in interface `Connection.Base<T extends Connection.Base<T>>`
Returns:
headers
See Also:

    - `Connection.Base.multiHeaders()`

  - 

### multiHeaders

public Map<String,List<String>> multiHeaders()
Description copied from interface: `Connection.Base`
Retreive all of the headers, keyed by the header name, and with a list of values per header.

Specified by:
`multiHeaders` in interface `Connection.Base<T extends Connection.Base<T>>`
Returns:
a list of multiple values per header.

  - 

### cookie

public String cookie(String name)
Description copied from interface: `Connection.Base`
Get a cookie value by name from this request/response.

Specified by:
`cookie` in interface `Connection.Base<T extends Connection.Base<T>>`
Parameters:
`name` - name of cookie to retrieve.
Returns:
value of cookie, or null if not set

  - 

### cookie

public Connection.Request cookie(String name,
 String value)
Description copied from interface: `Connection.Base`
Set a cookie in this request/response.

Specified by:
`cookie` in interface `Connection.Base<T extends Connection.Base<T>>`
Parameters:
`name` - name of cookie
`value` - value of cookie
Returns:
this, for chaining

  - 

### hasCookie

public boolean hasCookie(String name)
Description copied from interface: `Connection.Base`
Check if a cookie is present

Specified by:
`hasCookie` in interface `Connection.Base<T extends Connection.Base<T>>`
Parameters:
`name` - name of cookie
Returns:
if the cookie is present in this request/response

  - 

### removeCookie

public Connection.Request removeCookie(String name)
Description copied from interface: `Connection.Base`
Remove a cookie by name

Specified by:
`removeCookie` in interface `Connection.Base<T extends Connection.Base<T>>`
Parameters:
`name` - name of cookie to remove
Returns:
this, for chaining

  - 

### cookies

public Map<String,String> cookies()
Description copied from interface: `Connection.Base`
Retrieve the request/response cookies as a map. For response cookies, if duplicate cookie names were sent, the
         last one set will be the one included. For session management, rather than using these response cookies, prefer
         to use `Jsoup.newSession()` and related methods.

Specified by:
`cookies` in interface `Connection.Base<T extends Connection.Base<T>>`
Returns:
simple cookie map
See Also:

    - `Connection.cookieStore()`