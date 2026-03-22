Package org.jsoup.helper

# Class HttpConnection.Response

java.lang.Object
org.jsoup.helper.HttpConnection.Response

All Implemented Interfaces:
`Connection.Base<Connection.Response>`, `Connection.Response`

Enclosing class:
HttpConnection

---

public static class HttpConnection.Response
extends Object
implements Connection.Response

- 

## Method Summary

Modifier and Type
Method
Description
`Connection.Response`
`addHeader(String name,
 @Nullable String value)`

Add a header.

`String`
`body()`

Get the body of the response as a plain String.

`byte[]`
`bodyAsBytes()`

Get the body of the response as an array of bytes.

`BufferedInputStream`
`bodyStream()`

Get the body of the response as a (buffered) InputStream.

`Connection.Response`
`bufferUp()`

Read the body of the response into a local buffer, so that `Connection.Response.parse()` may be called repeatedly on the
 same connection response.

`@Nullable String`
`charset()`

Get the character set name of the response, derived from the content-type header.

`HttpConnection.Response`
`charset(String charset)`

Set / override the response character set.

`@Nullable String`
`contentType()`

Get the response content type (e.g.

`String`
`cookie(String name)`

Get a cookie value by name from this request/response.

`Connection.Response`
`cookie(String name,
 String value)`

Set a cookie in this request/response.

`Map<String,String>`
`cookies()`

Retrieve the request/response cookies as a map.

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

`Connection.Response`
`header(String name,
 String value)`

Set a header.

`Map<String,String>`
`headers()`

Retrieve all of the request/response header names and corresponding values as a map.

`List<String>`
`headers(String name)`

Get the values of a header.

`Connection.Method`
`method()`

Get the request method, which defaults to `GET`

`Connection.Response`
`method(Connection.Method method)`

Set the request method

`Map<String,List<String>>`
`multiHeaders()`

Retreive all of the headers, keyed by the header name, and with a list of values per header.

`Document`
`parse()`

Read and parse the body of the response as a Document.

`String`
`readBody()`

Read the response body, and returns it as a plain String.

`Connection.Response`
`readFully()`

Reads the bodyStream into byteData.

`Connection.Response`
`removeCookie(String name)`

Remove a cookie by name

`Connection.Response`
`removeHeader(String name)`

Remove headers by name.

`int`
`statusCode()`

Get the status code of the response.

`String`
`statusMessage()`

Get the status message of the response.

`StreamParser`
`streamParser()`

Returns a `StreamParser` that will parse the Response progressively.

`URL`
`url()`

Get the URL of this Request or Response.

`Connection.Response`
`url(URL url)`

Set the URL

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, toString, wait, wait, wait`

### Methods inherited from interface org.jsoup.Connection.Base

`addHeader, cookie, cookie, cookies, hasCookie, hasHeader, hasHeaderWithValue, header, header, headers, headers, method, method, multiHeaders, removeCookie, removeHeader, url, url`

- 

## Method Details

  - 

### statusCode

public int statusCode()
Description copied from interface: `Connection.Response`
Get the status code of the response.

Specified by:
`statusCode` in interface `Connection.Response`
Returns:
status code

  - 

### statusMessage

public String statusMessage()
Description copied from interface: `Connection.Response`
Get the status message of the response.

Specified by:
`statusMessage` in interface `Connection.Response`
Returns:
status message

  - 

### charset

public @Nullable String charset()
Description copied from interface: `Connection.Response`
Get the character set name of the response, derived from the content-type header.

Specified by:
`charset` in interface `Connection.Response`
Returns:
character set name if set, **null** if not

  - 

### charset

public HttpConnection.Response charset(String charset)
Description copied from interface: `Connection.Response`
Set / override the response character set. When the document body is parsed it will be with this charset.

Specified by:
`charset` in interface `Connection.Response`
Parameters:
`charset` - to decode body as
Returns:
this Response, for chaining

  - 

### contentType

public @Nullable String contentType()
Description copied from interface: `Connection.Response`
Get the response content type (e.g. "text/html");

Specified by:
`contentType` in interface `Connection.Response`
Returns:
the response content type, or **null** if one was not set

  - 

### parse

public Document parse()
               throws IOException
Description copied from interface: `Connection.Response`
Read and parse the body of the response as a Document. If you intend to parse the same response multiple times,
         you should `Connection.Response.readFully()` first, which will buffer the body into memory.

Specified by:
`parse` in interface `Connection.Response`
Returns:
a parsed Document
Throws:
`IOException` - if an IO exception occurs whilst reading the body.
See Also:

    - `Connection.Response.readFully()`

  - 

### streamParser

public StreamParser streamParser()
                          throws IOException
Description copied from interface: `Connection.Response`
Returns a `StreamParser` that will parse the Response progressively.

Specified by:
`streamParser` in interface `Connection.Response`
Returns:
a StreamParser, prepared to parse this response.
Throws:
`IOException` - if an IO exception occurs preparing the parser.

  - 

### readFully

public Connection.Response readFully()
                              throws IOException
Reads the bodyStream into byteData. A no-op if already executed.

Specified by:
`readFully` in interface `Connection.Response`
Returns:
this response, for chaining
Throws:
`IOException` - if an IO exception occurs during buffering.

  - 

### readBody

public String readBody()
                throws IOException
Description copied from interface: `Connection.Response`
Read the response body, and returns it as a plain String.

Specified by:
`readBody` in interface `Connection.Response`
Returns:
body
Throws:
`IOException` - if an IO exception occurs whilst reading the body.

  - 

### body

public String body()
Description copied from interface: `Connection.Response`
Get the body of the response as a plain String.

         

Will throw an UncheckedIOException if the body has not been buffered and an error occurs whilst reading the
         body; use `Connection.Response.readFully()` first to buffer the body and catch any exceptions explicitly. Or more simply,
         `Connection.Response.readBody()`.

Specified by:
`body` in interface `Connection.Response`
Returns:
body
See Also:

    - `Connection.Response.readBody()`

    - `Connection.Response.readFully()`

  - 

### bodyAsBytes

public byte[] bodyAsBytes()
Description copied from interface: `Connection.Response`
Get the body of the response as an array of bytes.

         

Will throw an UncheckedIOException if the body has not been buffered and an error occurs whilst reading the
         body; use `Connection.Response.readFully()` first to buffer the body and catch any exceptions explicitly.

Specified by:
`bodyAsBytes` in interface `Connection.Response`
Returns:
body bytes
See Also:

    - `Connection.Response.readFully()`

  - 

### bufferUp

public Connection.Response bufferUp()
Description copied from interface: `Connection.Response`
Read the body of the response into a local buffer, so that `Connection.Response.parse()` may be called repeatedly on the
 same connection response. Otherwise, once the response is read, its InputStream will have been drained and
 may not be re-read.
 

Calling `Connection.Response.body()` or `Connection.Response.bodyAsBytes()` has the same effect.

Specified by:
`bufferUp` in interface `Connection.Response`
Returns:
this response, for chaining

  - 

### bodyStream

public BufferedInputStream bodyStream()
Description copied from interface: `Connection.Response`
Get the body of the response as a (buffered) InputStream. You should close the input stream when you're done
         with it.
         

Other body methods (like readFully, body, parse, etc) will generally not work in conjunction with this method,
         as it consumes the InputStream.
         

Any configured max size or maximum read timeout applied to the connection will not be applied to this stream,
         unless `Connection.Response.readFully()` is called prior.
         

This method is useful for writing large responses to disk, without buffering them completely into memory
         first.

Specified by:
`bodyStream` in interface `Connection.Response`
Returns:
the response body input stream

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

public Connection.Response url(URL url)
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

public Connection.Response method(Connection.Method method)
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

public Connection.Response addHeader(String name,
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

public Connection.Response header(String name,
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

public Connection.Response removeHeader(String name)
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

public Connection.Response cookie(String name,
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

public Connection.Response removeCookie(String name)
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