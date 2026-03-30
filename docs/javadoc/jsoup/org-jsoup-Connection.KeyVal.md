Package org.jsoup

# Interface Connection.KeyVal

All Known Implementing Classes:
`HttpConnection.KeyVal`

Enclosing interface:
Connection

---

public static interface Connection.KeyVal
A Key:Value tuple(+), used for form data.

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

`boolean`
`hasInputStream()`

Does this keyval have an input stream?

`@Nullable InputStream`
`inputStream()`

Get the input stream associated with this keyval, if any

`Connection.KeyVal`
`inputStream(InputStream inputStream)`

Add or update an input stream to this keyVal

`String`
`key()`

Get the key of a keyval

`Connection.KeyVal`
`key(String key)`

Update the key of a keyval

`String`
`value()`

Get the value of a keyval

`Connection.KeyVal`
`value(String value)`

Update the value of a keyval

- 

## Method Details

  - 

### key

Connection.KeyVal key(String key)
Update the key of a keyval

Parameters:
`key` - new key
Returns:
this KeyVal, for chaining

  - 

### key

String key()
Get the key of a keyval

Returns:
the key

  - 

### value

Connection.KeyVal value(String value)
Update the value of a keyval

Parameters:
`value` - the new value
Returns:
this KeyVal, for chaining

  - 

### value

String value()
Get the value of a keyval

Returns:
the value

  - 

### inputStream

Connection.KeyVal inputStream(InputStream inputStream)
Add or update an input stream to this keyVal

Parameters:
`inputStream` - new input stream
Returns:
this KeyVal, for chaining

  - 

### inputStream

@Nullable InputStream inputStream()
Get the input stream associated with this keyval, if any

Returns:
input stream if set, or null

  - 

### hasInputStream

boolean hasInputStream()
Does this keyval have an input stream?

Returns:
true if this keyval does indeed have an input stream

  - 

### contentType

Connection.KeyVal contentType(String contentType)
Set the Content Type header used in the MIME body (aka mimetype) when uploading files.
 Only useful if `inputStream(InputStream)` is set.
 

Will default to `application/octet-stream`.

Parameters:
`contentType` - the new content type
Returns:
this KeyVal

  - 

### contentType

@Nullable String contentType()
Get the current Content Type, or `null` if not set.

Returns:
the current Content Type.