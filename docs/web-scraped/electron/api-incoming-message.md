# Source: https://www.electronjs.org/docs/latest/api/incoming-message

On this page

# Class: IncomingMessage

## Class: IncomingMessage[â€‹](#class-incomingmessage "Direct link to Class: IncomingMessage") 

> Handle responses to HTTP/HTTPS requests.

Process: [Main](/docs/latest/glossary#main-process), [Utility](/docs/latest/glossary#utility-process)\
*This class is not exported from the `'electron'` module. It is only available as a return value of other methods in the Electron API.*

`IncomingMessage` implements the [Readable Stream](https://nodejs.org/api/stream.html#stream_readable_streams) interface and is therefore an [EventEmitter](https://nodejs.org/api/events.html#events_class_eventemitter).

### Instance Events[â€‹](#instance-events "Direct link to Instance Events") 

#### Event: \'data\'[â€‹](#event-data "Direct link to Event: 'data'") 

Returns:

- `chunk` Buffer - A chunk of response body\'s data.

The `data` event is the usual method of transferring response data into applicative code.

#### Event: \'end\'[â€‹](#event-end "Direct link to Event: 'end'") 

Indicates that response body has ended. Must be placed before \'data\' event.

#### Event: \'aborted\'[â€‹](#event-aborted "Direct link to Event: 'aborted'") 

Emitted when a request has been canceled during an ongoing HTTP transaction.

#### Event: \'error\'[â€‹](#event-error "Direct link to Event: 'error'") 

Returns:

- `error` Error - Typically holds an error string identifying failure root cause.

Emitted when an error was encountered while streaming response data events. For instance, if the server closes the underlying while the response is still streaming, an `error` event will be emitted on the response object and a `close` event will subsequently follow on the request object.

### Instance Properties[â€‹](#instance-properties "Direct link to Instance Properties") 

An `IncomingMessage` instance has the following readable properties:

#### `response.statusCode`[â€‹](#responsestatuscode "Direct link to responsestatuscode") 

An `Integer` indicating the HTTP response status code.

#### `response.statusMessage`[â€‹](#responsestatusmessage "Direct link to responsestatusmessage") 

A `string` representing the HTTP status message.

#### `response.headers`[â€‹](#responseheaders "Direct link to responseheaders") 

A `Record<string, string | string[]>` representing the HTTP response headers. The `headers` object is formatted as follows:

- All header names are lowercased.
- Duplicates of `age`, `authorization`, `content-length`, `content-type`, `etag`, `expires`, `from`, `host`, `if-modified-since`, `if-unmodified-since`, `last-modified`, `location`, `max-forwards`, `proxy-authorization`, `referer`, `retry-after`, `server`, or `user-agent` are discarded.
- `set-cookie` is always an array. Duplicates are added to the array.
- For duplicate `cookie` headers, the values are joined together with \'; \'.
- For all other headers, the values are joined together with \', \'.

#### `response.httpVersion`[â€‹](#responsehttpversion "Direct link to responsehttpversion") 

A `string` indicating the HTTP protocol version number. Typical values are \'1.0\' or \'1.1\'. Additionally `httpVersionMajor` and `httpVersionMinor` are two Integer-valued readable properties that return respectively the HTTP major and minor version numbers.

#### `response.httpVersionMajor`[â€‹](#responsehttpversionmajor "Direct link to responsehttpversionmajor") 

An `Integer` indicating the HTTP protocol major version number.

#### `response.httpVersionMinor`[â€‹](#responsehttpversionminor "Direct link to responsehttpversionminor") 

An `Integer` indicating the HTTP protocol minor version number.

#### `response.rawHeaders`[â€‹](#responserawheaders "Direct link to responserawheaders") 

A `string[]` containing the raw HTTP response headers exactly as they were received. The keys and values are in the same list. It is not a list of tuples. So, the even-numbered offsets are key values, and the odd-numbered offsets are the associated values. Header names are not lowercased, and duplicates are not merged.

``` 
// Prints something like:
//
// [ 'user-agent',
//   'this is invalid because there can be only one',
//   'User-Agent',
//   'curl/7.22.0',
//   'Host',
//   '127.0.0.1:8000',
//   'ACCEPT',
//   '*/*' ]
console.log(response.rawHeaders)
```

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/incoming-message.md)