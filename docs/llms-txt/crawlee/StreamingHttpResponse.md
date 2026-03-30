# Source: https://crawlee.dev/js/api/core/interface/StreamingHttpResponse.md

# StreamingHttpResponse<!-- -->

HTTP response data as returned by the [BaseHttpClient.stream](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md#stream) method.

### Hierarchy

* HttpResponseWithoutBody
  * *StreamingHttpResponse*

## Index[**](#Index)

### Properties

* [**complete](#complete)
* [**downloadProgress](#downloadProgress)
* [**headers](#headers)
* [**ip](#ip)
* [**redirectUrls](#redirectUrls)
* [**request](#request)
* [**statusCode](#statusCode)
* [**statusMessage](#statusMessage)
* [**stream](#stream)
* [**trailers](#trailers)
* [**uploadProgress](#uploadProgress)
* [**url](#url)

## Properties<!-- -->[**](#Properties)

### [**](#complete)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L141)inheritedcomplete

**complete: boolean

Inherited from HttpResponseWithoutBody.complete

### [**](#downloadProgress)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L164)readonlydownloadProgress

**downloadProgress: Progress

### [**](#headers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L138)inheritedheaders

**headers: SimpleHeaders

Inherited from HttpResponseWithoutBody.headers

### [**](#ip)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L134)optionalinheritedip

**ip?

<!-- -->

: string

Inherited from HttpResponseWithoutBody.ip

### [**](#redirectUrls)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L131)inheritedredirectUrls

**redirectUrls: URL\[]

Inherited from HttpResponseWithoutBody.redirectUrls

### [**](#request)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L146)inheritedrequest

**request: [HttpRequest](https://crawlee.dev/js/api/core/interface/HttpRequest.md)\<keyof

<!-- -->

[ResponseTypes](https://crawlee.dev/js/api/core/interface/ResponseTypes.md)>

Inherited from HttpResponseWithoutBody.request

### [**](#statusCode)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L135)inheritedstatusCode

**statusCode: number

Inherited from HttpResponseWithoutBody.statusCode

### [**](#statusMessage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L136)optionalinheritedstatusMessage

**statusMessage?

<!-- -->

: string

Inherited from HttpResponseWithoutBody.statusMessage

### [**](#stream)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L163)stream

**stream: Readable

### [**](#trailers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L139)inheritedtrailers

**trailers: SimpleHeaders

Inherited from HttpResponseWithoutBody.trailers

### [**](#uploadProgress)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L165)readonlyuploadProgress

**uploadProgress: Progress

### [**](#url)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L132)inheritedurl

**url: string

Inherited from HttpResponseWithoutBody.url
