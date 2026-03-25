# Source: https://crawlee.dev/js/api/core/interface/HttpResponse.md

# HttpResponse<!-- --> \<TResponseType>

HTTP response data as returned by the [BaseHttpClient.sendRequest](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md#sendRequest) method.

### Hierarchy

* HttpResponseWithoutBody\<TResponseType>
  * *HttpResponse*

## Index[**](#Index)

### Properties

* [**body](#body)
* [**complete](#complete)
* [**headers](#headers)
* [**ip](#ip)
* [**redirectUrls](#redirectUrls)
* [**request](#request)
* [**statusCode](#statusCode)
* [**statusMessage](#statusMessage)
* [**trailers](#trailers)
* [**url](#url)

## Properties<!-- -->[**](#Properties)

### [**](#body)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L156)body

**body: [ResponseTypes](https://crawlee.dev/js/api/core/interface/ResponseTypes.md)\[TResponseType]

### [**](#complete)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L141)inheritedcomplete

**complete: boolean

Inherited from HttpResponseWithoutBody.complete

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

**request: [HttpRequest](https://crawlee.dev/js/api/core/interface/HttpRequest.md)\<TResponseType>

Inherited from HttpResponseWithoutBody.request

### [**](#statusCode)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L135)inheritedstatusCode

**statusCode: number

Inherited from HttpResponseWithoutBody.statusCode

### [**](#statusMessage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L136)optionalinheritedstatusMessage

**statusMessage?

<!-- -->

: string

Inherited from HttpResponseWithoutBody.statusMessage

### [**](#trailers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L139)inheritedtrailers

**trailers: SimpleHeaders

Inherited from HttpResponseWithoutBody.trailers

### [**](#url)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L132)inheritedurl

**url: string

Inherited from HttpResponseWithoutBody.url
