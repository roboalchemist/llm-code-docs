# Source: https://www.electronjs.org/docs/latest/api/net

On this page

# net

> Issue HTTP/HTTPS requests using Chromium\'s native networking library

Process: [Main](/docs/latest/glossary#main-process), [Utility](/docs/latest/glossary#utility-process)

The `net` module is a client-side API for issuing HTTP(S) requests. It is similar to the [HTTP](https://nodejs.org/api/http.html) and [HTTPS](https://nodejs.org/api/https.html) modules of Node.js but uses Chromium\'s native networking library instead of the Node.js implementation, offering better support for web proxies. It also supports checking network status.

The following is a non-exhaustive list of why you may consider using the `net` module instead of the native Node.js modules:

- Automatic management of system proxy configuration, support of the wpad protocol and proxy pac configuration files.
- Automatic tunneling of HTTPS requests.
- Support for authenticating proxies using basic, digest, NTLM, Kerberos or negotiate authentication schemes.
- Support for traffic monitoring proxies: Fiddler-like proxies used for access control and monitoring.

The API components (including classes, methods, properties and event names) are similar to those used in Node.js.

Example usage:

``` 
const  = require('electron')

app.whenReady().then(() =>  = require('electron')
  const request = net.request('https://github.com')
  request.on('response', (response) => `)
    console.log(`HEADERS: $`)
    response.on('data', (chunk) => `)
    })
    response.on('end', () => )
  })
  request.end()
})
```

The `net` API can be used only after the application emits the `ready` event. Trying to use the module before the `ready` event will throw an error.

## Methods[â€‹](#methods "Direct link to Methods") 

The `net` module has the following methods:

### `net.request(options)`[â€‹](#netrequestoptions "Direct link to netrequestoptions") 

- `options` ([ClientRequestConstructorOptions](/docs/latest/api/client-request#new-clientrequestoptions) \| string) - The `ClientRequest` constructor options.

Returns [`ClientRequest`](/docs/latest/api/client-request)

Creates a [`ClientRequest`](/docs/latest/api/client-request) instance using the provided `options` which are directly forwarded to the `ClientRequest` constructor. The `net.request` method would be used to issue both secure and insecure HTTP requests according to the specified protocol scheme in the `options` object.

### `net.fetch(input[, init])`[â€‹](#netfetchinput-init "Direct link to netfetchinput-init") 

- `input` string \| [GlobalRequest](https://nodejs.org/api/globals.html#request)
- `init` [RequestInit](https://developer.mozilla.org/en-US/docs/Web/API/fetch#options) &  (optional)

Returns `Promise<GlobalResponse>` - see [Response](https://developer.mozilla.org/en-US/docs/Web/API/Response).

Sends a request, similarly to how `fetch()` works in the renderer, using Chrome\'s network stack. This differs from Node\'s `fetch()`, which uses Node.js\'s HTTP stack.

Example:

``` 
async function example () 
}
```

This method will issue requests from the [default session](/docs/latest/api/session#sessiondefaultsession). To send a `fetch` request from another session, use [ses.fetch()](/docs/latest/api/session#sesfetchinput-init).

See the MDN documentation for [`fetch()`](https://developer.mozilla.org/en-US/docs/Web/API/fetch) for more details.

Limitations:

- `net.fetch()` does not support the `data:` or `blob:` schemes.
- The value of the `integrity` option is ignored.
- The `.type` and `.url` values of the returned `Response` object are incorrect.

By default, requests made with `net.fetch` can be made to [custom protocols](/docs/latest/api/protocol) as well as `file:`, and will trigger [webRequest](/docs/latest/api/web-request) handlers if present. When the non-standard `bypassCustomProtocolHandlers` option is set in RequestInit, custom protocol handlers will not be called for this request. This allows forwarding an intercepted request to the built-in handler. [webRequest](/docs/latest/api/web-request) handlers will still be triggered when bypassing custom protocols.

``` 
protocol.handle('https', (req) =>  else )
  }
})
```

[![](data:image/svg+xml;base64,PHN2ZyB2aWV3Ym94PSIwIDAgMTQgMTYiPjxwYXRoIGZpbGwtcnVsZT0iZXZlbm9kZCIgZD0iTTYuMyA1LjY5YS45NDIuOTQyIDAgMCAxLS4yOC0uN2MwLS4yOC4wOS0uNTIuMjgtLjcuMTktLjE4LjQyLS4yOC43LS4yOC4yOCAwIC41Mi4wOS43LjI4LjE4LjE5LjI4LjQyLjI4LjcgMCAuMjgtLjA5LjUyLS4yOC43YTEgMSAwIDAgMS0uNy4zYy0uMjggMC0uNTItLjExLS43LS4zek04IDcuOTljLS4wMi0uMjUtLjExLS40OC0uMzEtLjY5LS4yLS4xOS0uNDItLjMtLjY5LS4zMUg2Yy0uMjcuMDItLjQ4LjEzLS42OS4zMS0uMi4yLS4zLjQ0LS4zMS42OWgxdjNjLjAyLjI3LjExLjUuMzEuNjkuMi4yLjQyLjMxLjY5LjMxaDFjLjI3IDAgLjQ4LS4xMS42OS0uMzEuMi0uMTkuMy0uNDIuMzEtLjY5SDhWNy45OHYuMDF6TTcgMi4zYy0zLjE0IDAtNS43IDIuNTQtNS43IDUuNjggMCAzLjE0IDIuNTYgNS43IDUuNyA1LjdzNS43LTIuNTUgNS43LTUuN2MwLTMuMTUtMi41Ni01LjY5LTUuNy01LjY5di4wMXpNNyAuOThjMy44NiAwIDcgMy4xNCA3IDdzLTMuMTQgNy03IDctNy0zLjEyLTctNyAzLjE0LTcgNy03eiIgLz48L3N2Zz4=)]note

In the [utility process](/docs/latest/glossary#utility-process), custom protocols are not supported.

### `net.isOnline()`[â€‹](#netisonline "Direct link to netisonline") 

Returns `boolean` - Whether there is currently internet connection.

A return value of `false` is a pretty strong indicator that the user won\'t be able to connect to remote sites. However, a return value of `true` is inconclusive; even if some link is up, it is uncertain whether a particular connection attempt to a particular remote site will be successful.

### `net.resolveHost(host, [options])`[â€‹](#netresolvehosthost-options "Direct link to netresolvehosthost-options") 

- `host` string - Hostname to resolve.
- `options` Object (optional)
  - `queryType` string (optional) - Requested DNS query type. If unspecified, resolver will pick A or AAAA (or both) based on IPv4/IPv6 settings:
    - `A` - Fetch only A records
    - `AAAA` - Fetch only AAAA records.
  - `source` string (optional) - The source to use for resolved addresses. Default allows the resolver to pick an appropriate source. Only affects use of big external sources (e.g. calling the system for resolution or using DNS). Even if a source is specified, results can still come from cache, resolving \"localhost\" or IP literals, etc. One of the following values:
    - `any` (default) - Resolver will pick an appropriate source. Results could come from DNS, MulticastDNS, HOSTS file, etc
    - `system` - Results will only be retrieved from the system or OS, e.g. via the `getaddrinfo()` system call
    - `dns` - Results will only come from DNS queries
    - `mdns` - Results will only come from Multicast DNS queries
    - `localOnly` - No external sources will be used. Results will only come from fast local sources that are available no matter the source setting, e.g. cache, hosts file, IP literal resolution, etc.
  - `cacheUsage` string (optional) - Indicates what DNS cache entries, if any, can be used to provide a response. One of the following values:
    - `allowed` (default) - Results may come from the host cache if non-stale
    - `staleAllowed` - Results may come from the host cache even if stale (by expiration or network changes)
    - `disallowed` - Results will not come from the host cache.
  - `secureDnsPolicy` string (optional) - Controls the resolver\'s Secure DNS behavior for this request. One of the following values:
    - `allow` (default)
    - `disable`

Returns [Promise\<ResolvedHost\>](/docs/latest/api/structures/resolved-host) - Resolves with the resolved IP addresses for the `host`.

This method will resolve hosts from the [default session](/docs/latest/api/session#sessiondefaultsession). To resolve a host from another session, use [ses.resolveHost()](/docs/latest/api/session#sesresolvehosthost-options).

## Properties[â€‹](#properties "Direct link to Properties") 

### `net.online` *Readonly*[â€‹](#netonline-readonly "Direct link to netonline-readonly") 

A `boolean` property. Whether there is currently internet connection.

A return value of `false` is a pretty strong indicator that the user won\'t be able to connect to remote sites. However, a return value of `true` is inconclusive; even if some link is up, it is uncertain whether a particular connection attempt to a particular remote site will be successful.

[![](data:image/svg+xml;base64,PHN2ZyBmaWxsPSJjdXJyZW50Q29sb3IiIGhlaWdodD0iMjAiIHdpZHRoPSIyMCIgdmlld2JveD0iMCAwIDQwIDQwIiBjbGFzcz0iaWNvbkVkaXRfWjlTdyIgYXJpYS1oaWRkZW49InRydWUiPjxnPjxwYXRoIGQ9Im0zNC41IDExLjdsLTMgMy4xLTYuMy02LjMgMy4xLTNxMC41LTAuNSAxLjItMC41dDEuMSAwLjVsMy45IDMuOXEwLjUgMC40IDAuNSAxLjF0LTAuNSAxLjJ6IG0tMjkuNSAxNy4xbDE4LjQtMTguNSA2LjMgNi4zLTE4LjQgMTguNGgtNi4zdi02LjJ6IiAvPjwvZz48L3N2Zz4=)Edit this page](https://github.com/electron/electron/edit/main/docs/api/net.md)