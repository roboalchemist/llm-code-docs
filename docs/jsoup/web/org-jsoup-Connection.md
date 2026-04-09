Package org.jsoup

# Interface Connection

All Known Implementing Classes:
`HttpConnection`

---

public interface Connection
The Connection interface is a convenient HTTP client and session object to fetch content from the web, and parse them
 into Documents.
 

To start a new session, use either `Jsoup.newSession()` or `Jsoup.connect(String)`.
 Connections contain `Connection.Request` and `Connection.Response` objects (once executed). Configuration
 settings (URL, timeout, useragent, etc) set on a session will be applied by default to each subsequent request.
 

To start a new request from the session, use `newRequest()`.
 

Cookies are stored in memory for the duration of the session. For that reason, do not use one single session for all
 requests in a long-lived application, or you are likely to run out of memory, unless care is taken to clean up the
 cookie store. The cookie store for the session is available via `cookieStore()`. You may provide your own
 implementation via `cookieStore(java.net.CookieStore)` before making requests.
 

Request configuration can be made using either the shortcut methods in Connection (e.g. `userAgent(String)`),
 or by methods in the `Connection.Request` object directly. All request configuration must be made before the request is
 executed. When used as an ongoing session, initialize all defaults prior to making multi-threaded `newRequest()`s.
 

Note that the term "Connection" used here does not mean that a long-lived connection is held against a server for
 the lifetime of the Connection object. A socket connection is only made at the point of request execution (`execute()`, `get()`, or `post()`), and the server's response consumed.
 

For multi-threaded implementations, it is important to use a `newRequest()` for each request. The session may
 be shared across concurrent threads, but a not a specific request.
 

**HTTP/2** support: On JVM 11 and above, requests use `HttpClient`, which supports
 HTTP/2. To use the legacy `HttpURLConnection` instead, set
 `System.setProperty("jsoup.useHttpClient", "false")`.

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Interface
Description
`static interface `
`Connection.Base<T extends Connection.Base<T>>`

Common methods for Requests and Responses

`static interface `
`Connection.KeyVal`

A Key:Value tuple(+), used for form data.

`static enum `
`Connection.Method`

GET and POST http methods.

`static interface `
`Connection.Request`

Represents a HTTP request.

`static interface `
`Connection.Response`

Represents a HTTP response.

- 

## Method Summary

Modifier and Type
Method
Description
`default Connection`
`auth(@Nullable RequestAuthenticator authenticator)`

Set the authenticator to use for this connection, enabling requests to URLs, and via proxies, that require
     authentication credentials.

`Connection`
`cookie(String name,
 String value)`

Set a cookie to be sent in the request.

`Connection`
`cookies(Map<String,String> cookies)`

Adds each of the supplied cookies to the request.

`CookieStore`
`cookieStore()`

Get the cookie store used by this Connection.

`Connection`
`cookieStore(CookieStore cookieStore)`

Provide a custom or pre-filled CookieStore to be used on requests made by this Connection.

`@Nullable Connection.KeyVal`
`data(String key)`

Get the data KeyVal for this key, if any

`Connection`
`data(String... keyvals)`

Add one or more request `key, val` data parameter pairs.

`Connection`
`data(String key,
 String value)`

Add a request data parameter.

`Connection`
`data(String key,
 String filename,
 InputStream inputStream)`

Add an input stream as a request data parameter.

`Connection`
`data(String key,
 String filename,
 InputStream inputStream,
 String contentType)`

Add an input stream as a request data parameter.

`Connection`
`data(Collection<Connection.KeyVal> data)`

Adds all of the supplied data to the request data parameters

`Connection`
`data(Map<String,String> data)`

Adds all of the supplied data to the request data parameters

`Connection.Response`
`execute()`

Execute the request.

`Connection`
`followRedirects(boolean followRedirects)`

Configures the connection to (not) follow server redirects.

`Document`
`get()`

Execute the request as a GET, and parse the result.

`Connection`
`header(String name,
 String value)`

Set a request header.

`Connection`
`headers(Map<String,String> headers)`

Sets each of the supplied headers on the request.

`Connection`
`ignoreContentType(boolean ignoreContentType)`

Ignore the document's Content-Type when parsing the response.

`Connection`
`ignoreHttpErrors(boolean ignoreHttpErrors)`

Configures the connection to not throw exceptions when an HTTP error occurs. (4xx - 5xx, e.g. 404 or 500).

`Connection`
`maxBodySize(int bytes)`

Set the maximum bytes to read from the (uncompressed) connection into the body, before the connection is closed,
 and the input truncated (i.e. the body content will be trimmed).

`Connection`
`method(Connection.Method method)`

Set the request method to use, GET or POST.

`Connection`
`newRequest()`

Creates a new request, using this Connection as the session-state and to initialize the connection settings (which
     may then be independently changed on the returned `Connection.Request` object).

`default Connection`
`newRequest(String url)`

Creates a new request, using this Connection as the session-state and to initialize the connection settings (which
     may then be independently changed on the returned `Connection.Request` object).

`default Connection`
`newRequest(URL url)`

Creates a new request, using this Connection as the session-state and to initialize the connection settings (which
     may then be independently changed on the returned `Connection.Request` object).

`default Connection`
`onResponseProgress(Progress<Connection.Response> handler)`

Set the response progress handler, which will be called periodically as the response body is downloaded.

`Connection`
`parser(Parser parser)`

Provide a specific parser to use when parsing the response to a Document.

`Document`
`post()`

Execute the request as a POST, and parse the result.

`Connection`
`postDataCharset(String charset)`

Set the character-set used to encode the request body.

`Connection`
`proxy(@Nullable Proxy proxy)`

Set the proxy to use for this request.

`Connection`
`proxy(String host,
 int port)`

Set the HTTP proxy to use for this request.

`Connection`
`referrer(String referrer)`

Set the request referrer (aka "referer") header.

`Connection.Request`
`request()`

Get the request object associated with this connection

`Connection`
`request(Connection.Request request)`

Set the connection's request

`Connection`
`requestBody(String body)`

Set a POST (or PUT) request body.

`default Connection`
`requestBodyStream(InputStream stream)`

Set the request body.

`Connection.Response`
`response()`

Get the response, once the request has been executed.

`Connection`
`response(Connection.Response response)`

Set the connection's response

`default Connection`
`sslContext(SSLContext sslContext)`

Set a custom SSL context for HTTPS connections.

`Connection`
`sslSocketFactory(SSLSocketFactory sslSocketFactory)`

Deprecated.
use `sslContext(SSLContext)` instead; will be removed in jsoup 1.24.1.

`Connection`
`timeout(int millis)`

Set the total maximum request duration.

`Connection`
`url(String url)`

Set the request URL to fetch.

`Connection`
`url(URL url)`

Set the request URL to fetch.

`Connection`
`userAgent(String userAgent)`

Set the request user-agent header.

- 

## Method Details

  - 

### newRequest

Connection newRequest()
Creates a new request, using this Connection as the session-state and to initialize the connection settings (which
     may then be independently changed on the returned `Connection.Request` object).

Returns:
a new Connection object, with a shared Cookie Store and initialized settings from this Connection and Request
Since:
1.14.1

  - 

### newRequest

default Connection newRequest(String url)
Creates a new request, using this Connection as the session-state and to initialize the connection settings (which
     may then be independently changed on the returned `Connection.Request` object).

Parameters:
`url` - URL for the new request
Returns:
a new Connection object, with a shared Cookie Store and initialized settings from this Connection and Request
Since:
1.17.1

  - 

### newRequest

default Connection newRequest(URL url)
Creates a new request, using this Connection as the session-state and to initialize the connection settings (which
     may then be independently changed on the returned `Connection.Request` object).

Parameters:
`url` - URL for the new request
Returns:
a new Connection object, with a shared Cookie Store and initialized settings from this Connection and Request
Since:
1.17.1

  - 

### url

Connection url(URL url)
Set the request URL to fetch. The protocol must be HTTP or HTTPS.

Parameters:
`url` - URL to connect to
Returns:
this Connection, for chaining

  - 

### url

Connection url(String url)
Set the request URL to fetch. The protocol must be HTTP or HTTPS.

Parameters:
`url` - URL to connect to
Returns:
this Connection, for chaining

  - 

### proxy

Connection proxy(@Nullable Proxy proxy)
Set the proxy to use for this request. Set to `null` to disable a previously set proxy.

Parameters:
`proxy` - proxy to use
Returns:
this Connection, for chaining

  - 

### proxy

Connection proxy(String host,
 int port)
Set the HTTP proxy to use for this request.

Parameters:
`host` - the proxy hostname
`port` - the proxy port
Returns:
this Connection, for chaining

  - 

### userAgent

Connection userAgent(String userAgent)
Set the request user-agent header.

Parameters:
`userAgent` - user-agent to use
Returns:
this Connection, for chaining
See Also:

    - `HttpConnection.DEFAULT_UA`

  - 

### timeout

Connection timeout(int millis)
Set the total maximum request duration. If a timeout occurs, an `SocketTimeoutException` will be
     thrown.
     

The default timeout is **30 seconds** (30,000 millis). A timeout of zero is treated as an infinite timeout.
     

This timeout specifies the combined maximum duration of the connection time and the time to read
     the full response.
     

Implementation note: when this `Connection` is backed by `HttpURLConnection` (rather than `HttpClient`, as used in JVM 11+), this timeout is implemented by setting both the socket connect and read timeouts to half of the specified value.

Parameters:
`millis` - number of milliseconds (thousandths of a second) before timing out connects or reads.
Returns:
this Connection, for chaining
See Also:

    - `maxBodySize(int)`

  - 

### maxBodySize

Connection maxBodySize(int bytes)
Set the maximum bytes to read from the (uncompressed) connection into the body, before the connection is closed,
 and the input truncated (i.e. the body content will be trimmed). **The default maximum is 2MB**. A max size of
 `0` is treated as an infinite amount (bounded only by your patience and the memory available on your
 machine).

Parameters:
`bytes` - number of bytes to read from the input before truncating
Returns:
this Connection, for chaining

  - 

### referrer

Connection referrer(String referrer)
Set the request referrer (aka "referer") header.

Parameters:
`referrer` - referrer to use
Returns:
this Connection, for chaining

  - 

### followRedirects

Connection followRedirects(boolean followRedirects)
Configures the connection to (not) follow server redirects. By default, this is **true**.

Parameters:
`followRedirects` - true if server redirects should be followed.
Returns:
this Connection, for chaining

  - 

### method

Connection method(Connection.Method method)
Set the request method to use, GET or POST. Default is GET.

Parameters:
`method` - HTTP request method
Returns:
this Connection, for chaining

  - 

### ignoreHttpErrors

Connection ignoreHttpErrors(boolean ignoreHttpErrors)
Configures the connection to not throw exceptions when an HTTP error occurs. (4xx - 5xx, e.g. 404 or 500). By
 default, this is **false**; an IOException is thrown if an error is encountered. If set to **true**, the
 response is populated with the error body, and the status message will reflect the error.

Parameters:
`ignoreHttpErrors` - - false (default) if HTTP errors should be ignored.
Returns:
this Connection, for chaining

  - 

### ignoreContentType

Connection ignoreContentType(boolean ignoreContentType)
Ignore the document's Content-Type when parsing the response. By default, this is **false**, an unrecognised
 content-type will cause an IOException to be thrown. (This is to prevent producing garbage by attempting to parse
 a JPEG binary image, for example.) Set to true to force a parse attempt regardless of content type.

Parameters:
`ignoreContentType` - set to true if you would like the content type ignored on parsing the response into a
 Document.
Returns:
this Connection, for chaining

  - 

### sslSocketFactory

@Deprecated
Connection sslSocketFactory(SSLSocketFactory sslSocketFactory)
Deprecated.
use `sslContext(SSLContext)` instead; will be removed in jsoup 1.24.1.

Set a custom SSL socket factory for HTTPS connections.
     

Note: if set, the legacy `HttpURLConnection` will be used instead of the JVM's
     `HttpClient`.

Parameters:
`sslSocketFactory` - SSL socket factory
Returns:
this Connection, for chaining
See Also:

    - `sslContext(SSLContext)`

  - 

### sslContext

default Connection sslContext(SSLContext sslContext)
Set a custom SSL context for HTTPS connections.
     

Note: when using the legacy `HttpURLConnection`, only the `SSLSocketFactory` from the
     context will be used.

Parameters:
`sslContext` - SSL context
Returns:
this Connection, for chaining
Since:
1.21.2

  - 

### data

Connection data(String key,
 String value)
Add a request data parameter. Request parameters are sent in the request query string for GETs, and in the
 request body for POSTs. A request may have multiple values of the same name.

Parameters:
`key` - data key
`value` - data value
Returns:
this Connection, for chaining

  - 

### data

Connection data(String key,
 String filename,
 InputStream inputStream)
Add an input stream as a request data parameter. For GETs, has no effect, but for POSTS this will upload the
 input stream.
 

Use the `data(String, String, InputStream, String)` method to set the uploaded file's mimetype.

Parameters:
`key` - data key (form item name)
`filename` - the name of the file to present to the remove server. Typically just the name, not path,
 component.
`inputStream` - the input stream to upload, that you probably obtained from a `FileInputStream`.
 You must close the InputStream in a `finally` block.
Returns:
this Connection, for chaining
See Also:

    - `data(String, String, InputStream, String)`

  - 

### data

Connection data(String key,
 String filename,
 InputStream inputStream,
 String contentType)
Add an input stream as a request data parameter. For GETs, has no effect, but for POSTS this will upload the
 input stream.

Parameters:
`key` - data key (form item name)
`filename` - the name of the file to present to the remove server. Typically just the name, not path,
 component.
`inputStream` - the input stream to upload, that you probably obtained from a `FileInputStream`.
`contentType` - the Content Type (aka mimetype) to specify for this file.
 You must close the InputStream in a `finally` block.
Returns:
this Connection, for chaining

  - 

### data

Connection data(Collection<Connection.KeyVal> data)
Adds all of the supplied data to the request data parameters

Parameters:
`data` - collection of data parameters
Returns:
this Connection, for chaining

  - 

### data

Connection data(Map<String,String> data)
Adds all of the supplied data to the request data parameters

Parameters:
`data` - map of data parameters
Returns:
this Connection, for chaining

  - 

### data

Connection data(String... keyvals)
Add one or more request `key, val` data parameter pairs.
     

Multiple parameters may be set at once, e.g.:
     `.data("name", "jsoup", "language", "Java", "language", "English");` creates a query string like:
     `?name=jsoup&language=Java&language=English`
     

For GET requests, data parameters will be sent on the request query string. For POST (and other methods that
     contain a body), they will be sent as body form parameters, unless the body is explicitly set by
     `requestBody(String)`, in which case they will be query string parameters.

Parameters:
`keyvals` - a set of key value pairs.
Returns:
this Connection, for chaining

  - 

### data

@Nullable Connection.KeyVal data(String key)
Get the data KeyVal for this key, if any

Parameters:
`key` - the data key
Returns:
null if not set

  - 

### requestBody

Connection requestBody(String body)
Set a POST (or PUT) request body. Useful when a server expects a plain request body (such as JSON), and not a set
 of URL encoded form key/value pairs. E.g.:
 `

```
Jsoup.connect(url)
 .requestBody(json)
 .header("Content-Type", "application/json")
 .post();
```
`
 If any data key/vals are supplied, they will be sent as URL query params.

Returns:
this Request, for chaining
See Also:

    - `requestBodyStream(InputStream)`

  - 

### requestBodyStream

default Connection requestBodyStream(InputStream stream)
Set the request body. Useful for posting data such as byte arrays or files, and the server expects a single request
     body (and not a multipart upload). E.g.:
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

### header

Connection header(String name,
 String value)
Set a request header. Replaces any existing header with the same case-insensitive name.

Parameters:
`name` - header name
`value` - header value
Returns:
this Connection, for chaining
See Also:

    - `Connection.Base.header(String, String)`

    - `Connection.Base.headers()`

  - 

### headers

Connection headers(Map<String,String> headers)
Sets each of the supplied headers on the request. Existing headers with the same case-insensitive name will be
 replaced with the new value.

Parameters:
`headers` - map of headers name -> value pairs
Returns:
this Connection, for chaining
See Also:

    - `Connection.Base.headers()`

  - 

### cookie

Connection cookie(String name,
 String value)
Set a cookie to be sent in the request.

Parameters:
`name` - name of cookie
`value` - value of cookie
Returns:
this Connection, for chaining

  - 

### cookies

Connection cookies(Map<String,String> cookies)
Adds each of the supplied cookies to the request.

Parameters:
`cookies` - map of cookie name -> value pairs
Returns:
this Connection, for chaining

  - 

### cookieStore

Connection cookieStore(CookieStore cookieStore)
Provide a custom or pre-filled CookieStore to be used on requests made by this Connection.

Parameters:
`cookieStore` - a cookie store to use for subsequent requests
Returns:
this Connection, for chaining
Since:
1.14.1

  - 

### cookieStore

CookieStore cookieStore()
Get the cookie store used by this Connection.

Returns:
the cookie store
Since:
1.14.1

  - 

### parser

Connection parser(Parser parser)
Provide a specific parser to use when parsing the response to a Document. If not set, jsoup defaults to the
 `HTML parser`, unless the response content-type is XML, in which case the
 `XML parser` is used.

Parameters:
`parser` - alternate parser
Returns:
this Connection, for chaining

  - 

### postDataCharset

Connection postDataCharset(String charset)
Set the character-set used to encode the request body. Defaults to `UTF-8`.

Parameters:
`charset` - character set to encode the request body
Returns:
this Connection, for chaining

  - 

### auth

default Connection auth(@Nullable RequestAuthenticator authenticator)
Set the authenticator to use for this connection, enabling requests to URLs, and via proxies, that require
     authentication credentials.
     

The authentication scheme used is automatically detected during the request execution.
     Supported schemes (subject to the platform) are `basic`, `digest`, `NTLM`,
     and `Kerberos`.

     

To use, supply a `RequestAuthenticator` function that:
     

     
    - validates the URL that is requesting authentication, and
     
    - returns the appropriate credentials (username and password)
     

     

     

For example, to authenticate both to a proxy and a downstream web server:
     `

```

     Connection session = Jsoup.newSession()
         .proxy("proxy.example.com", 8080)
         .auth(auth -> {
             if (auth.isServer()) { // provide credentials for the request url
                 Validate.isTrue(auth.url().getHost().equals("example.com"));
                 // check that we're sending credentials were we expect, and not redirected out
                 return auth.credentials("username", "password");
             } else { // auth.isProxy()
                 return auth.credentials("proxy-user", "proxy-password");
             }
         });

     Connection.Response response = session.newRequest("https://example.com/adminzone/").execute();
     
```
`
     

     

The system may cache the authentication and use it for subsequent requests to the same resource.

     

**Implementation notes**
     

For compatibility, on a Java 8 platform, authentication is set up via the system-wide default
     `Authenticator.setDefault(Authenticator)` method via a ThreadLocal delegator. Whilst the
     authenticator used is request specific and thread-safe, if you have other calls to `setDefault`, they will be
     incompatible with this implementation.
     

On Java 9 and above, the preceding note does not apply; authenticators are directly set on the request. 
     

If you are attempting to authenticate to a proxy that uses the `basic` scheme and will be fetching HTTPS
     URLs, you need to configure your Java platform to enable that, by setting the
     `jdk.http.auth.tunneling.disabledSchemes` system property to `""`.
     This must be executed prior to any authorization attempts. E.g.:
     `

```

     static {
        System.setProperty("jdk.http.auth.tunneling.disabledSchemes", "");
        // removes Basic, which is otherwise excluded from auth for CONNECT tunnels
     }
```
`
     

Parameters:
`authenticator` - the authenticator to use in this connection
Returns:
this Connection, for chaining
Since:
1.17.1

  - 

### get

Document get()
      throws IOException
Execute the request as a GET, and parse the result.

Returns:
parsed Document
Throws:
`MalformedURLException` - if the request URL is not an HTTP or HTTPS URL, or is otherwise malformed
`HttpStatusException` - if the response is not OK and HTTP response errors are not ignored
`UnsupportedMimeTypeException` - if the response mime type is not supported and those errors are not ignored
`SocketTimeoutException` - if the connection times out
`IOException` - on error

  - 

### post

Document post()
       throws IOException
Execute the request as a POST, and parse the result.

Returns:
parsed Document
Throws:
`MalformedURLException` - if the request URL is not a HTTP or HTTPS URL, or is otherwise malformed
`HttpStatusException` - if the response is not OK and HTTP response errors are not ignored
`UnsupportedMimeTypeException` - if the response mime type is not supported and those errors are not ignored
`SocketTimeoutException` - if the connection times out
`IOException` - on error

  - 

### execute

Connection.Response execute()
                     throws IOException
Execute the request.

Returns:
the executed `Connection.Response`
Throws:
`MalformedURLException` - if the request URL is not a HTTP or HTTPS URL, or is otherwise malformed
`HttpStatusException` - if the response is not OK and HTTP response errors are not ignored
`UnsupportedMimeTypeException` - if the response mime type is not supported and those errors are not ignored
`SocketTimeoutException` - if the connection times out
`IOException` - on error

  - 

### request

Connection.Request request()
Get the request object associated with this connection

Returns:
request

  - 

### request

Connection request(Connection.Request request)
Set the connection's request

Parameters:
`request` - new request object
Returns:
this Connection, for chaining

  - 

### response

Connection.Response response()
Get the response, once the request has been executed.

Returns:
response
Throws:
`IllegalArgumentException` - if called before the response has been executed.

  - 

### response

Connection response(Connection.Response response)
Set the connection's response

Parameters:
`response` - new response
Returns:
this Connection, for chaining

  - 

### onResponseProgress

default Connection onResponseProgress(Progress<Connection.Response> handler)
Set the response progress handler, which will be called periodically as the response body is downloaded. Since
     documents are parsed as they are downloaded, this is also a good proxy for the parse progress.
     

The Response object is supplied as the progress context, and may be read from to obtain headers etc.

Parameters:
`handler` - the progress handler
Returns:
this Connection, for chaining
Since:
1.18.1