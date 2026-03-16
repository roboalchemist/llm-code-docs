Package org.jsoup.helper

# Class HttpConnection.KeyVal

java.lang.Object
org.jsoup.helper.HttpConnection.KeyVal

All Implemented Interfaces:
`Connection.KeyVal`

Enclosing class:
HttpConnection

---

public static class HttpConnection.KeyVal
extends Object
implements Connection.KeyVal

- 

## Method Summary

Modifier and Type
Method
Description
`@Nullable String`
`contentType()`

Get the current Content Type, or `null` if not set.

`Connection.KeyVal`
`contentType(String contentType)`

Set the Content Type header used in the MIME body (aka mimetype) when uploading files.

`static HttpConnection.KeyVal`
`create(String key,
 String value)`
 
`static HttpConnection.KeyVal`
`create(String key,
 String filename,
 InputStream stream)`
 
`boolean`
`hasInputStream()`

Does this keyval have an input stream?

`@Nullable InputStream`
`inputStream()`

Get the input stream associated with this keyval, if any

`HttpConnection.KeyVal`
`inputStream(InputStream inputStream)`

Add or update an input stream to this keyVal

`String`
`key()`

Get the key of a keyval

`HttpConnection.KeyVal`
`key(String key)`

Update the key of a keyval

`String`
`toString()`
 
`String`
`value()`

Get the value of a keyval

`HttpConnection.KeyVal`
`value(String value)`

Update the value of a keyval

### Methods inherited from class java.lang.Object

`clone, equals, finalize, getClass, hashCode, notify, notifyAll, wait, wait, wait`

- 

## Method Details

  - 

### create

public static HttpConnection.KeyVal create(String key,
 String value)

  - 

### create

public static HttpConnection.KeyVal create(String key,
 String filename,
 InputStream stream)

  - 

### key

public HttpConnection.KeyVal key(String key)
Description copied from interface: `Connection.KeyVal`
Update the key of a keyval

Specified by:
`key` in interface `Connection.KeyVal`
Parameters:
`key` - new key
Returns:
this KeyVal, for chaining

  - 

### key

public String key()
Description copied from interface: `Connection.KeyVal`
Get the key of a keyval

Specified by:
`key` in interface `Connection.KeyVal`
Returns:
the key

  - 

### value

public HttpConnection.KeyVal value(String value)
Description copied from interface: `Connection.KeyVal`
Update the value of a keyval

Specified by:
`value` in interface `Connection.KeyVal`
Parameters:
`value` - the new value
Returns:
this KeyVal, for chaining

  - 

### value

public String value()
Description copied from interface: `Connection.KeyVal`
Get the value of a keyval

Specified by:
`value` in interface `Connection.KeyVal`
Returns:
the value

  - 

### inputStream

public HttpConnection.KeyVal inputStream(InputStream inputStream)
Description copied from interface: `Connection.KeyVal`
Add or update an input stream to this keyVal

Specified by:
`inputStream` in interface `Connection.KeyVal`
Parameters:
`inputStream` - new input stream
Returns:
this KeyVal, for chaining

  - 

### inputStream

public @Nullable InputStream inputStream()
Description copied from interface: `Connection.KeyVal`
Get the input stream associated with this keyval, if any

Specified by:
`inputStream` in interface `Connection.KeyVal`
Returns:
input stream if set, or null

  - 

### hasInputStream

public boolean hasInputStream()
Description copied from interface: `Connection.KeyVal`
Does this keyval have an input stream?

Specified by:
`hasInputStream` in interface `Connection.KeyVal`
Returns:
true if this keyval does indeed have an input stream

  - 

### contentType

public Connection.KeyVal contentType(String contentType)
Description copied from interface: `Connection.KeyVal`
Set the Content Type header used in the MIME body (aka mimetype) when uploading files.
 Only useful if `Connection.KeyVal.inputStream(InputStream)` is set.
 

Will default to `application/octet-stream`.

Specified by:
`contentType` in interface `Connection.KeyVal`
Parameters:
`contentType` - the new content type
Returns:
this KeyVal

  - 

### contentType

public @Nullable String contentType()
Description copied from interface: `Connection.KeyVal`
Get the current Content Type, or `null` if not set.

Specified by:
`contentType` in interface `Connection.KeyVal`
Returns:
the current Content Type.

  - 

### toString

public String toString()

Overrides:
`toString` in class `Object`