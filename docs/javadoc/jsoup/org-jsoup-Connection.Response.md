Package org.jsoup

# Interface Connection.Response

All Superinterfaces:
`Connection.Base<Connection.Response>`

All Known Implementing Classes:
`HttpConnection.Response`

Enclosing interface:
Connection

---

public static interface Connection.Response
extends Connection.Base<Connection.Response>
Represents a HTTP response.

- 

## Method Summary

Modifier and Type
Method
Description
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

Deprecated.
use `readFully()` instead (for the checked exception).

`@Nullable String`
`charset()`

Get the character set name of the response, derived from the content-type header.

`Connection.Response`
`charset(String charset)`

Set / override the response character set.

`@Nullable String`
`contentType()`

Get the response content type (e.g.

`Document`
`parse()`

Read and parse the body of the response as a Document.

`default String`
`readBody()`

Read the response body, and returns it as a plain String.

`default Connection.Response`
`readFully()`

Read the body of the response into a local buffer, so that `parse()` may be called repeatedly on the same
         connection response.

`int`
`statusCode()`

Get the status code of the response.

`String`
`statusMessage()`

Get the status message of the response.

`default StreamParser`
`streamParser()`

Returns a `StreamParser` that will parse the Response progressively.

### Methods inherited from interface org.jsoup.Connection.Base

`addHeader, cookie, cookie, cookies, hasCookie, hasHeader, hasHeaderWithValue, header, header, headers, headers, method, method, multiHeaders, removeCookie, removeHeader, url, url`

- 

## Method Details

  - 

### statusCode

int statusCode()
Get the status code of the response.

Returns:
status code

  - 

### statusMessage

String statusMessage()
Get the status message of the response.

Returns:
status message

  - 

### charset

@Nullable String charset()
Get the character set name of the response, derived from the content-type header.

Returns:
character set name if set, **null** if not

  - 

### charset

Connection.Response charset(String charset)
Set / override the response character set. When the document body is parsed it will be with this charset.

Parameters:
`charset` - to decode body as
Returns:
this Response, for chaining

  - 

### contentType

@Nullable String contentType()
Get the response content type (e.g. "text/html");

Returns:
the response content type, or **null** if one was not set

  - 

### parse

Document parse()
        throws IOException
Read and parse the body of the response as a Document. If you intend to parse the same response multiple times,
         you should `readFully()` first, which will buffer the body into memory.

Returns:
a parsed Document
Throws:
`IOException` - if an IO exception occurs whilst reading the body.
See Also:

    - `readFully()`

  - 

### readBody

default String readBody()
                 throws IOException
Read the response body, and returns it as a plain String.

Returns:
body
Throws:
`IOException` - if an IO exception occurs whilst reading the body.
Since:
1.21.1

  - 

### body

String body()
Get the body of the response as a plain String.

         

Will throw an UncheckedIOException if the body has not been buffered and an error occurs whilst reading the
         body; use `readFully()` first to buffer the body and catch any exceptions explicitly. Or more simply,
         `readBody()`.

Returns:
body
Throws:
`UncheckedIOException` - if an IO exception occurs whilst reading the body.
See Also:

    - `readBody()`

    - `readFully()`

  - 

### bodyAsBytes

byte[] bodyAsBytes()
Get the body of the response as an array of bytes.

         

Will throw an UncheckedIOException if the body has not been buffered and an error occurs whilst reading the
         body; use `readFully()` first to buffer the body and catch any exceptions explicitly.

Returns:
body bytes
Throws:
`UncheckedIOException` - if an IO exception occurs whilst reading the body.
See Also:

    - `readFully()`

  - 

### readFully

default Connection.Response readFully()
                               throws IOException
Read the body of the response into a local buffer, so that `parse()` may be called repeatedly on the same
         connection response. Otherwise, once the response is read, its InputStream will have been drained and may not be
         re-read.

         

Subsequent calls methods than consume the body, such as `parse()`, `body()`,
         `bodyAsBytes()`, will not need to read the body again, and will not throw exceptions.
         

Calling `readBody()`} has the same effect.

Returns:
this response, for chaining
Throws:
`IOException` - if an IO exception occurs during buffering.
Since:
1.21.1

  - 

### bufferUp

@Deprecated
Connection.Response bufferUp()
Deprecated.
use `readFully()` instead (for the checked exception). Will be removed in jsoup 1.24.1.

Read the body of the response into a local buffer, so that `parse()` may be called repeatedly on the
 same connection response. Otherwise, once the response is read, its InputStream will have been drained and
 may not be re-read.
 

Calling `body()` or `bodyAsBytes()` has the same effect.

Returns:
this response, for chaining
Throws:
`UncheckedIOException` - if an IO exception occurs during buffering.

  - 

### bodyStream

BufferedInputStream bodyStream()
Get the body of the response as a (buffered) InputStream. You should close the input stream when you're done
         with it.
         

Other body methods (like readFully, body, parse, etc) will generally not work in conjunction with this method,
         as it consumes the InputStream.
         

Any configured max size or maximum read timeout applied to the connection will not be applied to this stream,
         unless `readFully()` is called prior.
         

This method is useful for writing large responses to disk, without buffering them completely into memory
         first.

Returns:
the response body input stream

  - 

### streamParser

default StreamParser streamParser()
                           throws IOException
Returns a `StreamParser` that will parse the Response progressively.

Returns:
a StreamParser, prepared to parse this response.
Throws:
`IOException` - if an IO exception occurs preparing the parser.