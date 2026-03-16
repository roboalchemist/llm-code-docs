Package org.jsoup.helper

# Class HttpConnection

java.lang.Object
org.jsoup.helper.HttpConnection

All Implemented Interfaces:
`Connection`

---

public class HttpConnection
extends Object
implements Connection
Implementation of `Connection`.

See Also:

- `Jsoup.connect(String)`

- 

## Nested Class Summary

Nested Classes

Modifier and Type
Class
Description
`static class `
`HttpConnection.KeyVal`
 
`static class `
`HttpConnection.Request`
 
`static class `
`HttpConnection.Response`
 

## Nested classes/interfaces inherited from interface org.jsoup.Connection

`Connection.Method`

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`CONTENT_ENCODING`
 
`static final String`
`CONTENT_TYPE`
 
`static final String`
`DEFAULT_UA`

Many users would get caught by not setting a user-agent and therefore getting different responses on their desktop
 vs in jsoup, which would otherwise default to `Java`.

`static final String`
`FORM_URL_ENCODED`
 
`static final String`
`MULTIPART_FORM_DATA`
 

- 

## Constructor Summary

Constructors

Constructor
Description
`HttpConnection()`

Create a new, empty HttpConnection.

- 

## Method Summary

Modifier and Type
Method
Description
`Connection`
`auth(@Nullable RequestAuthenticator authenticator)`

Set the authenticator to use for this connection, enabling requests to URLs, and via proxies, that require
     authentication credentials.

`static Connection`
`connect(String url)`

Create a new Connection, with the request URL specified.

`static Connection`
`connect(URL url)`

Create a new Connection, with the request URL specified.

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

`Connection`
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

`Connection`
`requestBodyStream(InputStream stream)`

Set the request body.

`Connection.Response`
`response()`

Get the response, once the request has been executed.

`Connection`
`response(Connection.Response response)`

Set the connection's response

`Connection`
`sslContext(SSLContext sslContext)`

Set a custom SSL context for HTTPS connections.

`Connection`
`sslSocketFactory(SSLSocketFactory sslSocketFactory)`

Set a custom SSL socket factory for HTTPS connections.

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

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface org.jsoup.Connection

`newRequest, newRequest`

- 

## Field Details

  - 

### CONTENT_ENCODING

public static final String CONTENT_ENCODING

See Also:

    - Constant Field Values

  - 

### DEFAULT_UA

public static final String DEFAULT_UA
Many users would get caught by not setting a user-agent and therefore getting different responses on their desktop
 vs in jsoup, which would otherwise default to `Java`. So by default, use a desktop UA.

See Also:

    - Constant Field Values

  - 

### CONTENT_TYPE

public static final String CONTENT_TYPE

See Also:

    - Constant Field Values

  - 

### MULTIPART_FORM_DATA

public static final String MULTIPART_FORM_DATA

See Also:

    - Constant Field Values

  - 

### FORM_URL_ENCODED

public static final String FORM_URL_ENCODED

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### HttpConnection

public HttpConnection()
Create a new, empty HttpConnection.

- 

## Method Details

  - 

### connect

public static Connection connect(String url)
Create a new Connection, with the request URL specified.

Parameters:
`url` - the URL to fetch from
Returns:
a new Connection object

  - 

### connect

public static Connection connect(URL url)
Create a new Connection, with the request URL specified.

Parameters:
`url` - the URL to fetch from
Returns:
a new Connection object

  - 

### newRequest

public Connection newRequest()
Description copied from interface: `Connection`
Creates a new request, using this Connection as the session-state and to initialize the connection settings (which
     may then be independently changed on the returned `Connection.Request` object).

Specified by:
`newRequest` in interface `Connection`
Returns:
a new Connection object, with a shared Cookie Store and initialized settings from this Connection and Request

  - 

### url

public Connection url(URL url)
Description copied from interface: `Connection`
Set the request URL to fetch. The protocol must be HTTP or HTTPS.

Specified by:
`url` in interface `Connection`
Parameters:
`url` - URL to connect to
Returns:
this Connection, for chaining

  - 

### url

public Connection url(String url)
Description copied from interface: `Connection`
Set the request URL to fetch. The protocol must be HTTP or HTTPS.

Specified by:
`url` in interface `Connection`
Parameters:
`url` - URL to connect to
Returns:
this Connection, for chaining

  - 

### proxy

public Connection proxy(@Nullable Proxy proxy)
Description copied from interface: `Connection`
Set the proxy to use for this request. Set to `null` to disable a previously set proxy.

Specified by:
`proxy` in interface `Connection`
Parameters:
`proxy` - proxy to use
Returns:
this Connection, for chaining

  - 

### proxy

public Connection proxy(String host,
 int port)
Description copied from interface: `Connection`
Set the HTTP proxy to use for this request.

Specified by:
`proxy` in interface `Connection`
Parameters:
`host` - the proxy hostname
`port` - the proxy port
Returns:
this Connection, for chaining

  - 

### userAgent

public Connection userAgent(String userAgent)
Description copied from interface: `Connection`
Set the request user-agent header.

Specified by:
`userAgent` in interface `Connection`
Parameters:
`userAgent` - user-agent to use
Returns:
this Connection, for chaining
See Also:

    - `DEFAULT_UA`

  - 

### timeout

public Connection timeout(int millis)
Description copied from interface: `Connection`
Set the total maximum request duration. If a timeout occurs, an `SocketTimeoutException` will be
     thrown.
     

The default timeout is **30 seconds** (30,000 millis). A timeout of zero is treated as an infinite timeout.
     

This timeout specifies the combined maximum duration of the connection time and the time to read
     the full response.
     

Implementation note: when this `Connection` is backed by `HttpURLConnection` (rather than `HttpClient`, as used in JVM 11+), this timeout is implemented by setting both the socket connect and read timeouts to half of the specified value.

Specified by:
`timeout` in interface `Connection`
Parameters:
`millis` - number of milliseconds (thousandths of a second) before timing out connects or reads.
Returns:
this Connection, for chaining
See Also:

    - `Connection.maxBodySize(int)`

  - 

### maxBodySize

public Connection maxBodySize(int bytes)
Description copied from interface: `Connection`
Set the maximum bytes to read from the (uncompressed) connection into the body, before the connection is closed,
 and the input truncated (i.e. the body content will be trimmed). **The default maximum is 2MB**. A max size of
 `0` is treated as an infinite amount (bounded only by your patience and the memory available on your
 machine).

Specified by:
`maxBodySize` in interface `Connection`
Parameters:
`bytes` - number of bytes to read from the input before truncating
Returns:
this Connection, for chaining

  - 

### followRedirects

public Connection followRedirects(boolean followRedirects)
Description copied from interface: `Connection`
Configures the connection to (not) follow server redirects. By default, this is **true**.

Specified by:
`followRedirects` in interface `Connection`
Parameters:
`followRedirects` - true if server redirects should be followed.
Returns:
this Connection, for chaining

  - 

### referrer

public Connection referrer(String referrer)
Description copied from interface: `Connection`
Set the request referrer (aka "referer") header.

Specified by:
`referrer` in interface `Connection`
Parameters:
`referrer` - referrer to use
Returns:
this Connection, for chaining

  - 

### method

public Connection method(Connection.Method method)
Description copied from interface: `Connection`
Set the request method to use, GET or POST. Default is GET.

Specified by:
`method` in interface `Connection`
Parameters:
`method` - HTTP request method
Returns:
this Connection, for chaining

  - 

### ignoreHttpErrors

public Connection ignoreHttpErrors(boolean ignoreHttpErrors)
Description copied from interface: `Connection`
Configures the connection to not throw exceptions when an HTTP error occurs. (4xx - 5xx, e.g. 404 or 500). By
 default, this is **false**; an IOException is thrown if an error is encountered. If set to **true**, the
 response is populated with the error body, and the status message will reflect the error.

Specified by:
`ignoreHttpErrors` in interface `Connection`
Parameters:
`ignoreHttpErrors` - - false (default) if HTTP errors should be ignored.
Returns:
this Connection, for chaining

  - 

### ignoreContentType

public Connection ignoreContentType(boolean ignoreContentType)
Description copied from interface: `Connection`
Ignore the document's Content-Type when parsing the response. By default, this is **false**, an unrecognised
 content-type will cause an IOException to be thrown. (This is to prevent producing garbage by attempting to parse
 a JPEG binary image, for example.) Set to true to force a parse attempt regardless of content type.

Specified by:
`ignoreContentType` in interface `Connection`
Parameters:
`ignoreContentType` - set to true if you would like the content type ignored on parsing the response into a
 Document.
Returns:
this Connection, for chaining

  - 

### data

public Connection data(String key,
 String value)
Description copied from interface: `Connection`
Add a request data parameter. Request parameters are sent in the request query string for GETs, and in the
 request body for POSTs. A request may have multiple values of the same name.

Specified by:
`data` in interface `Connection`
Parameters:
`key` - data key
`value` - data value
Returns:
this Connection, for chaining

  - 

### sslSocketFactory

public Connection sslSocketFactory(SSLSocketFactory sslSocketFactory)
Description copied from interface: `Connection`
Set a custom SSL socket factory for HTTPS connections.
     

Note: if set, the legacy `HttpURLConnection` will be used instead of the JVM's
     `HttpClient`.

Specified by:
`sslSocketFactory` in interface `Connection`
Parameters:
`sslSocketFactory` - SSL socket factory
Returns:
this Connection, for chaining
See Also:

    - `Connection.sslContext(SSLContext)`

  - 

### sslContext

public Connection sslContext(SSLContext sslContext)
Description copied from interface: `Connection`
Set a custom SSL context for HTTPS connections.
     

Note: when using the legacy `HttpURLConnection`, only the `SSLSocketFactory` from the
     context will be used.

Specified by:
`sslContext` in interface `Connection`
Parameters:
`sslContext` - SSL context
Returns:
this Connection, for chaining

  - 

### data

public Connection data(String key,
 String filename,
 InputStream inputStream)
Description copied from interface: `Connection`
Add an input stream as a request data parameter. For GETs, has no effect, but for POSTS this will upload the
 input stream.
 

Use the `Connection.data(String, String, InputStream, String)` method to set the uploaded file's mimetype.

Specified by:
`data` in interface `Connection`
Parameters:
`key` - data key (form item name)
`filename` - the name of the file to present to the remove server. Typically just the name, not path,
 component.
`inputStream` - the input stream to upload, that you probably obtained from a `FileInputStream`.
 You must close the InputStream in a `finally` block.
Returns:
this Connection, for chaining
See Also:

    - `Connection.data(String, String, InputStream, String)`

  - 

### data

public Connection data(String key,
 String filename,
 InputStream inputStream,
 String contentType)
Description copied from interface: `Connection`
Add an input stream as a request data parameter. For GETs, has no effect, but for POSTS this will upload the
 input stream.

Specified by:
`data` in interface `Connection`
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

public Connection data(Map<String,String> data)
Description copied from interface: `Connection`
Adds all of the supplied data to the request data parameters

Specified by:
`data` in interface `Connection`
Parameters:
`data` - map of data parameters
Returns:
this Connection, for chaining

  - 

### data

public Connection data(String... keyvals)
Description copied from interface: `Connection`
Add one or more request `key, val` data parameter pairs.
     

Multiple parameters may be set at once, e.g.:
     `.data("name", "jsoup", "language", "Java", "language", "English");` creates a query string like:
     `?name=jsoup&language=Java&language=English`
     

For GET requests, data parameters will be sent on the request query string. For POST (and other methods that
     contain a body), they will be sent as body form parameters, unless the body is explicitly set by
     `Connection.requestBody(String)`, in which case they will be query string parameters.

Specified by:
`data` in interface `Connection`
Parameters:
`keyvals` - a set of key value pairs.
Returns:
this Connection, for chaining

  - 

### data

public Connection data(Collection<Connection.KeyVal> data)
Description copied from interface: `Connection`
Adds all of the supplied data to the request data parameters

Specified by:
`data` in interface `Connection`
Parameters:
`data` - collection of data parameters
Returns:
this Connection, for chaining

  - 

### data

public @Nullable Connection.KeyVal data(String key)
Description copied from interface: `Connection`
Get the data KeyVal for this key, if any

Specified by:
`data` in interface `Connection`
Parameters:
`key` - the data key
Returns:
null if not set

  - 

### requestBody

public Connection requestBody(String body)
Description copied from interface: `Connection`
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

Specified by:
`requestBody` in interface `Connection`
Returns:
this Request, for chaining
See Also:

    - `Connection.requestBodyStream(InputStream)`

  - 

### requestBodyStream

public Connection requestBodyStream(InputStream stream)
Description copied from interface: `Connection`
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

Specified by:
`requestBodyStream` in interface `Connection`
Parameters:
`stream` - the input stream to send.
Returns:
this Request, for chaining
See Also:

    - `Connection.requestBody(String)`

  - 

### header

public Connection header(String name,
 String value)
Description copied from interface: `Connection`
Set a request header. Replaces any existing header with the same case-insensitive name.

Specified by:
`header` in interface `Connection`
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

public Connection headers(Map<String,String> headers)
Description copied from interface: `Connection`
Sets each of the supplied headers on the request. Existing headers with the same case-insensitive name will be
 replaced with the new value.

Specified by:
`headers` in interface `Connection`
Parameters:
`headers` - map of headers name -> value pairs
Returns:
this Connection, for chaining
See Also:

    - `Connection.Base.headers()`

  - 

### cookie

public Connection cookie(String name,
 String value)
Description copied from interface: `Connection`
Set a cookie to be sent in the request.

Specified by:
`cookie` in interface `Connection`
Parameters:
`name` - name of cookie
`value` - value of cookie
Returns:
this Connection, for chaining

  - 

### cookies

public Connection cookies(Map<String,String> cookies)
Description copied from interface: `Connection`
Adds each of the supplied cookies to the request.

Specified by:
`cookies` in interface `Connection`
Parameters:
`cookies` - map of cookie name -> value pairs
Returns:
this Connection, for chaining

  - 

### cookieStore

public Connection cookieStore(CookieStore cookieStore)
Description copied from interface: `Connection`
Provide a custom or pre-filled CookieStore to be used on requests made by this Connection.

Specified by:
`cookieStore` in interface `Connection`
Parameters:
`cookieStore` - a cookie store to use for subsequent requests
Returns:
this Connection, for chaining

  - 

### cookieStore

public CookieStore cookieStore()
Description copied from interface: `Connection`
Get the cookie store used by this Connection.

Specified by:
`cookieStore` in interface `Connection`
Returns:
the cookie store

  - 

### parser

public Connection parser(Parser parser)
Description copied from interface: `Connection`
Provide a specific parser to use when parsing the response to a Document. If not set, jsoup defaults to the
 `HTML parser`, unless the response content-type is XML, in which case the
 `XML parser` is used.

Specified by:
`parser` in interface `Connection`
Parameters:
`parser` - alternate parser
Returns:
this Connection, for chaining

  - 

### get

public Document get()
             throws IOException
Description copied from interface: `Connection`
Execute the request as a GET, and parse the result.

Specified by:
`get` in interface `Connection`
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

public Document post()
              throws IOException
Description copied from interface: `Connection`
Execute the request as a POST, and parse the result.

Specified by:
`post` in interface `Connection`
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

public Connection.Response execute()
                            throws IOException
Description copied from interface: `Connection`
Execute the request.

Specified by:
`execute` in interface `Connection`
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

public Connection.Request request()
Description copied from interface: `Connection`
Get the request object associated with this connection

Specified by:
`request` in interface `Connection`
Returns:
request

  - 

### request

public Connection request(Connection.Request request)
Description copied from interface: `Connection`
Set the connection's request

Specified by:
`request` in interface `Connection`
Parameters:
`request` - new request object
Returns:
this Connection, for chaining

  - 

### response

public Connection.Response response()
Description copied from interface: `Connection`
Get the response, once the request has been executed.

Specified by:
`response` in interface `Connection`
Returns:
response

  - 

### response

public Connection response(Connection.Response response)
Description copied from interface: `Connection`
Set the connection's response

Specified by:
`response` in interface `Connection`
Parameters:
`response` - new response
Returns:
this Connection, for chaining

  - 

### postDataCharset

public Connection postDataCharset(String charset)
Description copied from interface: `Connection`
Set the character-set used to encode the request body. Defaults to `UTF-8`.

Specified by:
`postDataCharset` in interface `Connection`
Parameters:
`charset` - character set to encode the request body
Returns:
this Connection, for chaining

  - 

### auth

public Connection auth(@Nullable RequestAuthenticator authenticator)
Description copied from interface: `Connection`
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
     

Specified by:
`auth` in interface `Connection`
Parameters:
`authenticator` - the authenticator to use in this connection
Returns:
this Connection, for chaining

  - 

### onResponseProgress

public Connection onResponseProgress(Progress<Connection.Response> handler)
Description copied from interface: `Connection`
Set the response progress handler, which will be called periodically as the response body is downloaded. Since
     documents are parsed as they are downloaded, this is also a good proxy for the parse progress.
     

The Response object is supplied as the progress context, and may be read from to obtain headers etc.

Specified by:
`onResponseProgress` in interface `Connection`
Parameters:
`handler` - the progress handler
Returns:
this Connection, for chaining