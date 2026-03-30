# Class WebSocketHttpHeaders

java.lang.Object
org.springframework.http.HttpHeaders
org.springframework.web.socket.WebSocketHttpHeaders

All Implemented Interfaces:
`Serializable`

---

public class WebSocketHttpHeaders
extends org.springframework.http.HttpHeaders
An `HttpHeaders` variant that adds support for the HTTP headers defined
by the WebSocket specification RFC 6455.

Since:
4.0
Author:
Rossen Stoyanchev, Sam Brannen
See Also:

- Serialized Form

- 

## Field Summary

Fields

Modifier and Type
Field
Description
`static final String`
`SEC_WEBSOCKET_ACCEPT`
 
`static final String`
`SEC_WEBSOCKET_EXTENSIONS`
 
`static final String`
`SEC_WEBSOCKET_KEY`
 
`static final String`
`SEC_WEBSOCKET_PROTOCOL`
 
`static final String`
`SEC_WEBSOCKET_VERSION`
 

### Fields inherited from class org.springframework.http.HttpHeaders

`ACCEPT, ACCEPT_CHARSET, ACCEPT_ENCODING, ACCEPT_LANGUAGE, ACCEPT_PATCH, ACCEPT_RANGES, ACCESS_CONTROL_ALLOW_CREDENTIALS, ACCESS_CONTROL_ALLOW_HEADERS, ACCESS_CONTROL_ALLOW_METHODS, ACCESS_CONTROL_ALLOW_ORIGIN, ACCESS_CONTROL_EXPOSE_HEADERS, ACCESS_CONTROL_MAX_AGE, ACCESS_CONTROL_REQUEST_HEADERS, ACCESS_CONTROL_REQUEST_METHOD, AGE, ALLOW, AUTHORIZATION, CACHE_CONTROL, CONNECTION, CONTENT_DISPOSITION, CONTENT_ENCODING, CONTENT_LANGUAGE, CONTENT_LENGTH, CONTENT_LOCATION, CONTENT_RANGE, CONTENT_TYPE, COOKIE, DATE, EMPTY, ETAG, EXPECT, EXPIRES, FROM, HOST, IF_MATCH, IF_MODIFIED_SINCE, IF_NONE_MATCH, IF_RANGE, IF_UNMODIFIED_SINCE, LAST_MODIFIED, LINK, LOCATION, MAX_FORWARDS, ORIGIN, PRAGMA, PROXY_AUTHENTICATE, PROXY_AUTHORIZATION, RANGE, REFERER, RETRY_AFTER, SERVER, SET_COOKIE, SET_COOKIE2, TE, TRAILER, TRANSFER_ENCODING, UPGRADE, USER_AGENT, VARY, VIA, WARNING, WWW_AUTHENTICATE`

- 

## Constructor Summary

Constructors

Constructor
Description
`WebSocketHttpHeaders()`

Construct a new, empty `WebSocketHttpHeaders` instance.

`WebSocketHttpHeaders(org.springframework.http.HttpHeaders httpHeaders)`

Construct a new `WebSocketHttpHeaders` instance backed by the supplied
`HttpHeaders`.

- 

## Method Summary

Modifier and Type
Method
Description
`@Nullable String`
`getSecWebSocketAccept()`

Returns the value of the `Sec-WebSocket-Accept` header.

`List<WebSocketExtension>`
`getSecWebSocketExtensions()`

Returns the value of the `Sec-WebSocket-Extensions` header.

`@Nullable String`
`getSecWebSocketKey()`

Returns the value of the `Sec-WebSocket-Key` header.

`List<String>`
`getSecWebSocketProtocol()`

Returns the value of the `Sec-WebSocket-Protocol` header.

`@Nullable String`
`getSecWebSocketVersion()`

Returns the value of the `Sec-WebSocket-Version` header.

`void`
`setSecWebSocketAccept(@Nullable String secWebSocketAccept)`

Sets the (new) value of the `Sec-WebSocket-Accept` header.

`void`
`setSecWebSocketExtensions(List<WebSocketExtension> extensions)`

Sets the (new) value(s) of the `Sec-WebSocket-Extensions` header.

`void`
`setSecWebSocketKey(@Nullable String secWebSocketKey)`

Sets the (new) value of the `Sec-WebSocket-Key` header.

`void`
`setSecWebSocketProtocol(String secWebSocketProtocol)`

Sets the (new) value of the `Sec-WebSocket-Protocol` header.

`void`
`setSecWebSocketProtocol(List<String> secWebSocketProtocols)`

Sets the (new) value of the `Sec-WebSocket-Protocol` header.

`void`
`setSecWebSocketVersion(@Nullable String secWebSocketVersion)`

Sets the (new) value of the `Sec-WebSocket-Version` header.

### Methods inherited from class org.springframework.http.HttpHeaders

`add, addAll, addAll, asMultiValueMap, asSingleValueMap, clear, clearContentHeaders, containsHeader, containsHeaderValue, copyOf, copyOf, encodeBasicAuth, equals, forEach, formatHeaders, get, getAccept, getAcceptCharset, getAcceptLanguage, getAcceptLanguageAsLocales, getAcceptPatch, getAccessControlAllowCredentials, getAccessControlAllowHeaders, getAccessControlAllowMethods, getAccessControlAllowOrigin, getAccessControlExposeHeaders, getAccessControlMaxAge, getAccessControlRequestHeaders, getAccessControlRequestMethod, getAllow, getCacheControl, getConnection, getContentDisposition, getContentLanguage, getContentLength, getContentType, getDate, getETag, getETagValuesAsList, getExpires, getFieldValues, getFirst, getFirstDate, getFirstZonedDateTime, getHost, getIfMatch, getIfModifiedSince, getIfNoneMatch, getIfUnmodifiedSince, getLastModified, getLocation, getOrDefault, getOrEmpty, getOrigin, getPragma, getRange, getUpgrade, getValuesAsList, getVary, hashCode, hasHeaderValues, headerNames, headerSet, isEmpty, put, putAll, putAll, putIfAbsent, readOnlyHttpHeaders, readOnlyHttpHeaders, remove, set, setAccept, setAcceptCharset, setAcceptLanguage, setAcceptLanguageAsLocales, setAcceptPatch, setAccessControlAllowCredentials, setAccessControlAllowHeaders, setAccessControlAllowMethods, setAccessControlAllowOrigin, setAccessControlExposeHeaders, setAccessControlMaxAge, setAccessControlMaxAge, setAccessControlRequestHeaders, setAccessControlRequestMethod, setAll, setAllow, setBasicAuth, setBasicAuth, setBasicAuth, setBearerAuth, setCacheControl, setCacheControl, setConnection, setConnection, setContentDisposition, setContentDispositionFormData, setContentLanguage, setContentLength, setContentType, setDate, setDate, setDate, setDate, setETag, setExpires, setExpires, setExpires, setHost, setIfMatch, setIfMatch, setIfModifiedSince, setIfModifiedSince, setIfModifiedSince, setIfNoneMatch, setIfNoneMatch, setIfUnmodifiedSince, setIfUnmodifiedSince, setIfUnmodifiedSince, setInstant, setLastModified, setLastModified, setLastModified, setLocation, setOrigin, setPragma, setRange, setUpgrade, setVary, setZonedDateTime, size, toCommaDelimitedString, toSingleValueMap, toString`

### Methods inherited from class Object

`clone, finalize, getClass, notify, notifyAll, wait, wait, wait`

- 

## Field Details

  - 

### SEC_WEBSOCKET_ACCEPT

public static final String SEC_WEBSOCKET_ACCEPT

See Also:

    - Constant Field Values

  - 

### SEC_WEBSOCKET_EXTENSIONS

public static final String SEC_WEBSOCKET_EXTENSIONS

See Also:

    - Constant Field Values

  - 

### SEC_WEBSOCKET_KEY

public static final String SEC_WEBSOCKET_KEY

See Also:

    - Constant Field Values

  - 

### SEC_WEBSOCKET_PROTOCOL

public static final String SEC_WEBSOCKET_PROTOCOL

See Also:

    - Constant Field Values

  - 

### SEC_WEBSOCKET_VERSION

public static final String SEC_WEBSOCKET_VERSION

See Also:

    - Constant Field Values

- 

## Constructor Details

  - 

### WebSocketHttpHeaders

public WebSocketHttpHeaders()
Construct a new, empty `WebSocketHttpHeaders` instance.

  - 

### WebSocketHttpHeaders

public WebSocketHttpHeaders(org.springframework.http.HttpHeaders httpHeaders)
Construct a new `WebSocketHttpHeaders` instance backed by the supplied
`HttpHeaders`.

Changes to the `WebSocketHttpHeaders` created by this constructor
will write through to the supplied `HttpHeaders`. If you wish to copy
an existing `HttpHeaders` or `WebSocketHttpHeaders` instance,
use `HttpHeaders.copyOf(HttpHeaders)` instead. Note, however, that `copyOf()`
does not create an instance of `WebSocketHttpHeaders`.

If the supplied `HttpHeaders` instance is a
read-only
`HttpHeaders` wrapper, it will be unwrapped to ensure that the
`WebSocketHttpHeaders` instance created by this constructor is mutable.
Once the writable instance is mutated, the read-only instance is likely to
be out of sync and should be discarded.

Parameters:
`httpHeaders` - the headers to expose
See Also:

    - `HttpHeaders.copyOf(HttpHeaders)`

- 

## Method Details

  - 

### setSecWebSocketAccept

public void setSecWebSocketAccept(@Nullable String secWebSocketAccept)
Sets the (new) value of the `Sec-WebSocket-Accept` header.

Parameters:
`secWebSocketAccept` - the value of the header

  - 

### getSecWebSocketAccept

public @Nullable String getSecWebSocketAccept()
Returns the value of the `Sec-WebSocket-Accept` header.

Returns:
the value of the header

  - 

### getSecWebSocketExtensions

public List<WebSocketExtension> getSecWebSocketExtensions()
Returns the value of the `Sec-WebSocket-Extensions` header.

Returns:
the value of the header

  - 

### setSecWebSocketExtensions

public void setSecWebSocketExtensions(List<WebSocketExtension> extensions)
Sets the (new) value(s) of the `Sec-WebSocket-Extensions` header.

Parameters:
`extensions` - the values for the header

  - 

### setSecWebSocketKey

public void setSecWebSocketKey(@Nullable String secWebSocketKey)
Sets the (new) value of the `Sec-WebSocket-Key` header.

Parameters:
`secWebSocketKey` - the value of the header

  - 

### getSecWebSocketKey

public @Nullable String getSecWebSocketKey()
Returns the value of the `Sec-WebSocket-Key` header.

Returns:
the value of the header

  - 

### setSecWebSocketProtocol

public void setSecWebSocketProtocol(String secWebSocketProtocol)
Sets the (new) value of the `Sec-WebSocket-Protocol` header.

Parameters:
`secWebSocketProtocol` - the value of the header

  - 

### setSecWebSocketProtocol

public void setSecWebSocketProtocol(List<String> secWebSocketProtocols)
Sets the (new) value of the `Sec-WebSocket-Protocol` header.

Parameters:
`secWebSocketProtocols` - the value of the header

  - 

### getSecWebSocketProtocol

public List<String> getSecWebSocketProtocol()
Returns the value of the `Sec-WebSocket-Protocol` header.

Returns:
the value of the header

  - 

### setSecWebSocketVersion

public void setSecWebSocketVersion(@Nullable String secWebSocketVersion)
Sets the (new) value of the `Sec-WebSocket-Version` header.

Parameters:
`secWebSocketVersion` - the value of the header

  - 

### getSecWebSocketVersion

public @Nullable String getSecWebSocketVersion()
Returns the value of the `Sec-WebSocket-Version` header.

Returns:
the value of the header