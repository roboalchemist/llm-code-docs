Package org.jsoup

# Interface Connection.Base<T extends Connection.Base<T>>

Type Parameters:
`T` - Type of Base, either Request or Response

All Known Subinterfaces:
`Connection.Request`, `Connection.Response`

All Known Implementing Classes:
`HttpConnection.Request`, `HttpConnection.Response`

Enclosing interface:
Connection

---

public static interface Connection.Base<T extends Connection.Base<T>>
Common methods for Requests and Responses

- 

## Method Summary

Modifier and Type
Method
Description
`T`
`addHeader(String name,
 String value)`

Add a header.

`@Nullable String`
`cookie(String name)`

Get a cookie value by name from this request/response.

`T`
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

Check if a header is present, with the given value

`@Nullable String`
`header(String name)`

Get the value of a header.

`T`
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

`T`
`method(Connection.Method method)`

Set the request method

`Map<String,List<String>>`
`multiHeaders()`

Retreive all of the headers, keyed by the header name, and with a list of values per header.

`T`
`removeCookie(String name)`

Remove a cookie by name

`T`
`removeHeader(String name)`

Remove headers by name.

`URL`
`url()`

Get the URL of this Request or Response.

`T`
`url(URL url)`

Set the URL

- 

## Method Details

  - 

### url

URL url()
Get the URL of this Request or Response. For redirected responses, this will be the final destination URL.

Returns:
URL
Throws:
`IllegalArgumentException` - if called on a Request that was created without a URL.

  - 

### url

T url(URL url)
Set the URL

Parameters:
`url` - new URL
Returns:
this, for chaining

  - 

### method

Connection.Method method()
Get the request method, which defaults to `GET`

Returns:
method

  - 

### method

T method(Connection.Method method)
Set the request method

Parameters:
`method` - new method
Returns:
this, for chaining

  - 

### header

@Nullable String header(String name)
Get the value of a header. If there is more than one header value with the same name, the headers are returned
 comma separated, per rfc2616-sec4.
 

 Header names are case-insensitive.
 

Parameters:
`name` - name of header (case-insensitive)
Returns:
value of header, or null if not set.
See Also:

    - `hasHeader(String)`

    - `cookie(String)`

  - 

### headers

List<String> headers(String name)
Get the values of a header.

Parameters:
`name` - header name, case-insensitive.
Returns:
a list of values for this header, or an empty list if not set.

  - 

### header

T header(String name,
 String value)
Set a header. This method will overwrite any existing header with the same case-insensitive name. If there
 is more than one value for this header, this method will update the first matching header.
 

For compatibility, if the content of the header includes text that cannot be represented by ISO-8859-1,
 then it should be encoded first per RFC 2047.

Parameters:
`name` - Name of header
`value` - Value of header
Returns:
this, for chaining
See Also:

    - `addHeader(String, String)`

  - 

### addHeader

T addHeader(String name,
 String value)
Add a header. The header will be added regardless of whether a header with the same name already exists.
 

For compatibility, if the content of the header includes text that cannot be represented by ISO-8859-1,
 then it should be encoded first per RFC 2047.

Parameters:
`name` - Name of new header
`value` - Value of new header
Returns:
this, for chaining

  - 

### hasHeader

boolean hasHeader(String name)
Check if a header is present

Parameters:
`name` - name of header (case-insensitive)
Returns:
if the header is present in this request/response

  - 

### hasHeaderWithValue

boolean hasHeaderWithValue(String name,
 String value)
Check if a header is present, with the given value

Parameters:
`name` - header name (case-insensitive)
`value` - value (case-insensitive)
Returns:
if the header and value pair are set in this req/res

  - 

### removeHeader

T removeHeader(String name)
Remove headers by name. If there is more than one header with this name, they will all be removed.

Parameters:
`name` - name of header to remove (case-insensitive)
Returns:
this, for chaining

  - 

### headers

Map<String,String> headers()
Retrieve all of the request/response header names and corresponding values as a map. For headers with multiple
 values, only the first header is returned.
 

Note that this is a view of the headers only, and changes made to this map will not be reflected in the
 request/response object.

Returns:
headers
See Also:

    - `multiHeaders()`

  - 

### multiHeaders

Map<String,List<String>> multiHeaders()
Retreive all of the headers, keyed by the header name, and with a list of values per header.

Returns:
a list of multiple values per header.

  - 

### cookie

@Nullable String cookie(String name)
Get a cookie value by name from this request/response.

Parameters:
`name` - name of cookie to retrieve.
Returns:
value of cookie, or null if not set

  - 

### cookie

T cookie(String name,
 String value)
Set a cookie in this request/response.

Parameters:
`name` - name of cookie
`value` - value of cookie
Returns:
this, for chaining

  - 

### hasCookie

boolean hasCookie(String name)
Check if a cookie is present

Parameters:
`name` - name of cookie
Returns:
if the cookie is present in this request/response

  - 

### removeCookie

T removeCookie(String name)
Remove a cookie by name

Parameters:
`name` - name of cookie to remove
Returns:
this, for chaining

  - 

### cookies

Map<String,String> cookies()
Retrieve the request/response cookies as a map. For response cookies, if duplicate cookie names were sent, the
         last one set will be the one included. For session management, rather than using these response cookies, prefer
         to use `Jsoup.newSession()` and related methods.

Returns:
simple cookie map
See Also:

    - `Connection.cookieStore()`