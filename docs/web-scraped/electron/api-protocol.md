# Source: https://www.electronjs.org/docs/latest/api/protocol

On this page

# protocol

> Register a custom protocol and intercept existing protocol requests.

Process: [Main](/docs/latest/glossary#main-process)

An example of implementing a protocol that has the same effect as the `file://` protocol:

``` 
const  = require('electron')

const path = require('node:path')
const url = require('node:url')

app.whenReady().then(() => )
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

All methods unless specified can only be used after the `ready` event of the `app` module gets emitted.

## Using `protocol` with a custom `partition` or `session`[â€‹](#using-protocol-with-a-custom-partition-or-session "Direct link to using-protocol-with-a-custom-partition-or-session") 

A protocol is registered to a specific Electron [`session`](/docs/latest/api/session) object. If you don\'t specify a session, then your `protocol` will be applied to the default session that Electron uses. However, if you define a `partition` or `session` on your `browserWindow`\'s `webPreferences`, then that window will use a different session and your custom protocol will not work if you just use `electron.protocol.XXX`.

To have your custom protocol work in combination with a custom session, you need to register it to that session explicitly.

``` 
const  = require('electron')

const path = require('node:path')
const url = require('node:url')

app.whenReady().then(() => )

  const mainWindow = new BrowserWindow( })
})
```

## Methods[â€‹](#methods "Direct link to Methods") 

The `protocol` module has the following methods:

### `protocol.registerSchemesAsPrivileged(customSchemes)`[â€‹](#protocolregisterschemesasprivilegedcustomschemes "Direct link to protocolregisterschemesasprivilegedcustomschemes") 

- `customSchemes` [CustomScheme\[\]](/docs/latest/api/structures/custom-scheme)

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

This method can only be used before the `ready` event of the `app` module gets emitted and can be called only once.

Registers the `scheme` as standard, secure, bypasses content security policy for resources, allows registering ServiceWorker, supports fetch API, streaming video/audio, and V8 code cache. Specify a privilege with the value of `true` to enable the capability.

An example of registering a privileged scheme, that bypasses Content Security Policy:

``` 
const  = require('electron')

protocol.registerSchemesAsPrivileged([
   }
])
```

A standard scheme adheres to what RFC 3986 calls [generic URI syntax](https://tools.ietf.org/html/rfc3986#section-3). For example `http` and `https` are standard schemes, while `file` is not.

Registering a scheme as standard allows relative and absolute resources to be resolved correctly when served. Otherwise the scheme will behave like the `file` protocol, but without the ability to resolve relative URLs.

For example when you load following page with custom protocol without registering it as standard scheme, the image will not be loaded because non-standard schemes can not recognize relative URLs:

``` 
<body>
  <img src='test.png'>
</body>
```

Registering a scheme as standard will allow access to files through the [FileSystem API](https://developer.mozilla.org/en-US/docs/Web/API/LocalFileSystem). Otherwise the renderer will throw a security error for the scheme.

By default web storage apis (localStorage, sessionStorage, webSQL, indexedDB, cookies) are disabled for non standard schemes. So in general if you want to register a custom protocol to replace the `http` protocol, you have to register it as a standard scheme.

Protocols that use streams (http and stream protocols) should set `stream: true`. The `<video>` and `<audio>` HTML elements expect protocols to buffer their responses by default. The `stream` flag configures those elements to correctly expect streaming responses.

### `protocol.handle(scheme, handler)`[â€‹](#protocolhandlescheme-handler "Direct link to protocolhandlescheme-handler") 

- `scheme` string - scheme to handle, for example `https` or `my-app`. This is the bit before the `:` in a URL.
- `handler` Function\<[GlobalResponse](https://nodejs.org/api/globals.html#response) \| Promise\<GlobalResponse\>\>
  - `request` [GlobalRequest](https://nodejs.org/api/globals.html#request)

Register a protocol handler for `scheme`. Requests made to URLs with this scheme will delegate to this handler to determine what response should be sent.

Either a `Response` or a `Promise<Response>` can be returned.

Example:

``` 
const  = require('electron')

const path = require('node:path')
const  = require('node:url')

protocol.registerSchemesAsPrivileged([
  
  }
])

app.whenReady().then(() =>  = new URL(req.url)
    if (host === 'bundle') 
        })
      }
      // NB, this checks for paths that escape the bundle, e.g.
      // app://bundle/../../secret_file.txt
      const pathToServe = path.resolve(__dirname, pathname)
      const relativePath = path.relative(__dirname, pathToServe)
      const isSafe = relativePath && !relativePath.startsWith('..') && !path.isAbsolute(relativePath)
      if (!isSafe) 
        })
      }

      return net.fetch(pathToFileURL(pathToServe).toString())
    } else if (host === 'api') )
    }
  })
})
```

See the MDN docs for [`Request`](https://developer.mozilla.org/en-US/docs/Web/API/Request) and [`Response`](https://developer.mozilla.org/en-US/docs/Web/API/Response) for more details.

### `protocol.unhandle(scheme)`[â€‹](#protocolunhandlescheme "Direct link to protocolunhandlescheme") 

- `scheme` string - scheme for which to remove the handler.

Removes a protocol handler registered with `protocol.handle`.

### `protocol.isProtocolHandled(scheme)`[â€‹](#protocolisprotocolhandledscheme "Direct link to protocolisprotocolhandledscheme") 

- `scheme` string

Returns `boolean` - Whether `scheme` is already handled.

### `protocol.registerFileProtocol(scheme, handler)` *Deprecated*[â€‹](#protocolregisterfileprotocolscheme-handler-deprecated "Direct link to protocolregisterfileprotocolscheme-handler-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string
- `handler` Function
  - `request` [ProtocolRequest](/docs/latest/api/structures/protocol-request)
  - `callback` Function
    - `response` (string \| [ProtocolResponse](/docs/latest/api/structures/protocol-response))

Returns `boolean` - Whether the protocol was successfully registered

Registers a protocol of `scheme` that will send a file as the response. The `handler` will be called with `request` and `callback` where `request` is an incoming request for the `scheme`.

To handle the `request`, the `callback` should be called with either the file\'s path or an object that has a `path` property, e.g. `callback(filePath)` or `callback()`. The `filePath` must be an absolute path.

By default the `scheme` is treated like `http:`, which is parsed differently from protocols that follow the \"generic URI syntax\" like `file:`.

### `protocol.registerBufferProtocol(scheme, handler)` *Deprecated*[â€‹](#protocolregisterbufferprotocolscheme-handler-deprecated "Direct link to protocolregisterbufferprotocolscheme-handler-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string
- `handler` Function
  - `request` [ProtocolRequest](/docs/latest/api/structures/protocol-request)
  - `callback` Function
    - `response` (Buffer \| [ProtocolResponse](/docs/latest/api/structures/protocol-response))

Returns `boolean` - Whether the protocol was successfully registered

Registers a protocol of `scheme` that will send a `Buffer` as a response.

The usage is the same with `registerFileProtocol`, except that the `callback` should be called with either a `Buffer` object or an object that has the `data` property.

Example:

``` 
protocol.registerBufferProtocol('atom', (request, callback) => )
})
```

### `protocol.registerStringProtocol(scheme, handler)` *Deprecated*[â€‹](#protocolregisterstringprotocolscheme-handler-deprecated "Direct link to protocolregisterstringprotocolscheme-handler-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string
- `handler` Function
  - `request` [ProtocolRequest](/docs/latest/api/structures/protocol-request)
  - `callback` Function
    - `response` (string \| [ProtocolResponse](/docs/latest/api/structures/protocol-response))

Returns `boolean` - Whether the protocol was successfully registered

Registers a protocol of `scheme` that will send a `string` as a response.

The usage is the same with `registerFileProtocol`, except that the `callback` should be called with either a `string` or an object that has the `data` property.

### `protocol.registerHttpProtocol(scheme, handler)` *Deprecated*[â€‹](#protocolregisterhttpprotocolscheme-handler-deprecated "Direct link to protocolregisterhttpprotocolscheme-handler-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string
- `handler` Function
  - `request` [ProtocolRequest](/docs/latest/api/structures/protocol-request)
  - `callback` Function
    - `response` [ProtocolResponse](/docs/latest/api/structures/protocol-response)

Returns `boolean` - Whether the protocol was successfully registered

Registers a protocol of `scheme` that will send an HTTP request as a response.

The usage is the same with `registerFileProtocol`, except that the `callback` should be called with an object that has the `url` property.

### `protocol.registerStreamProtocol(scheme, handler)` *Deprecated*[â€‹](#protocolregisterstreamprotocolscheme-handler-deprecated "Direct link to protocolregisterstreamprotocolscheme-handler-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string
- `handler` Function
  - `request` [ProtocolRequest](/docs/latest/api/structures/protocol-request)
  - `callback` Function
    - `response` (ReadableStream \| [ProtocolResponse](/docs/latest/api/structures/protocol-response))

Returns `boolean` - Whether the protocol was successfully registered

Registers a protocol of `scheme` that will send a stream as a response.

The usage is the same with `registerFileProtocol`, except that the `callback` should be called with either a [`ReadableStream`](https://nodejs.org/api/stream.html#stream_class_stream_readable) object or an object that has the `data` property.

Example:

``` 
const  = require('electron')

const  = require('node:stream')

function createStream (text) 

protocol.registerStreamProtocol('atom', (request, callback) => ,
    data: createStream('<h5>Response</h5>')
  })
})
```

It is possible to pass any object that implements the readable stream API (emits `data`/`end`/`error` events). For example, here\'s how a file could be returned:

``` 
protocol.registerStreamProtocol('atom', (request, callback) => )
```

### `protocol.unregisterProtocol(scheme)` *Deprecated*[â€‹](#protocolunregisterprotocolscheme-deprecated "Direct link to protocolunregisterprotocolscheme-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string

Returns `boolean` - Whether the protocol was successfully unregistered

Unregisters the custom protocol of `scheme`.

### `protocol.isProtocolRegistered(scheme)` *Deprecated*[â€‹](#protocolisprotocolregisteredscheme-deprecated "Direct link to protocolisprotocolregisteredscheme-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string

Returns `boolean` - Whether `scheme` is already registered.

### `protocol.interceptFileProtocol(scheme, handler)` *Deprecated*[â€‹](#protocolinterceptfileprotocolscheme-handler-deprecated "Direct link to protocolinterceptfileprotocolscheme-handler-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string
- `handler` Function
  - `request` [ProtocolRequest](/docs/latest/api/structures/protocol-request)
  - `callback` Function
    - `response` (string \| [ProtocolResponse](/docs/latest/api/structures/protocol-response))

Returns `boolean` - Whether the protocol was successfully intercepted

Intercepts `scheme` protocol and uses `handler` as the protocol\'s new handler which sends a file as a response.

### `protocol.interceptStringProtocol(scheme, handler)` *Deprecated*[â€‹](#protocolinterceptstringprotocolscheme-handler-deprecated "Direct link to protocolinterceptstringprotocolscheme-handler-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string
- `handler` Function
  - `request` [ProtocolRequest](/docs/latest/api/structures/protocol-request)
  - `callback` Function
    - `response` (string \| [ProtocolResponse](/docs/latest/api/structures/protocol-response))

Returns `boolean` - Whether the protocol was successfully intercepted

Intercepts `scheme` protocol and uses `handler` as the protocol\'s new handler which sends a `string` as a response.

### `protocol.interceptBufferProtocol(scheme, handler)` *Deprecated*[â€‹](#protocolinterceptbufferprotocolscheme-handler-deprecated "Direct link to protocolinterceptbufferprotocolscheme-handler-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string
- `handler` Function
  - `request` [ProtocolRequest](/docs/latest/api/structures/protocol-request)
  - `callback` Function
    - `response` (Buffer \| [ProtocolResponse](/docs/latest/api/structures/protocol-response))

Returns `boolean` - Whether the protocol was successfully intercepted

Intercepts `scheme` protocol and uses `handler` as the protocol\'s new handler which sends a `Buffer` as a response.

### `protocol.interceptHttpProtocol(scheme, handler)` *Deprecated*[â€‹](#protocolintercepthttpprotocolscheme-handler-deprecated "Direct link to protocolintercepthttpprotocolscheme-handler-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string
- `handler` Function
  - `request` [ProtocolRequest](/docs/latest/api/structures/protocol-request)
  - `callback` Function
    - `response` [ProtocolResponse](/docs/latest/api/structures/protocol-response)

Returns `boolean` - Whether the protocol was successfully intercepted

Intercepts `scheme` protocol and uses `handler` as the protocol\'s new handler which sends a new HTTP request as a response.

### `protocol.interceptStreamProtocol(scheme, handler)` *Deprecated*[â€‹](#protocolinterceptstreamprotocolscheme-handler-deprecated "Direct link to protocolinterceptstreamprotocolscheme-handler-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string
- `handler` Function
  - `request` [ProtocolRequest](/docs/latest/api/structures/protocol-request)
  - `callback` Function
    - `response` (ReadableStream \| [ProtocolResponse](/docs/latest/api/structures/protocol-response))

Returns `boolean` - Whether the protocol was successfully intercepted

Same as `protocol.registerStreamProtocol`, except that it replaces an existing protocol handler.

### `protocol.uninterceptProtocol(scheme)` *Deprecated*[â€‹](#protocoluninterceptprotocolscheme-deprecated "Direct link to protocoluninterceptprotocolscheme-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string

Returns `boolean` - Whether the protocol was successfully unintercepted

Remove the interceptor installed for `scheme` and restore its original handler.

### `protocol.isProtocolIntercepted(scheme)` *Deprecated*[â€‹](#protocolisprotocolinterceptedscheme-deprecated "Direct link to protocolisprotocolinterceptedscheme-deprecated") 

History

Version(s)

Changes

    None

[](/docs/latest/breaking-changes#deprecated-protocolunregisterinterceptbufferstringstreamfilehttpprotocol-and-protocolisprotocolregisteredintercepted)

`protocol.register*Protocol` and `protocol.intercept*Protocol` methods have been replaced with `protocol.handle`

- `scheme` string

Returns `boolean` - Whether `scheme` is already intercepted.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/protocol.md)