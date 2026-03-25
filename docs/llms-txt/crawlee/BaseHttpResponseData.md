# Source: https://crawlee.dev/js/api/core/interface/BaseHttpResponseData.md

# BaseHttpResponseData<!-- -->

HTTP response data, without a body, as returned by [BaseHttpClient](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md) methods.

## Index[**](#Index)

### Properties

* [**complete](#complete)
* [**headers](#headers)
* [**ip](#ip)
* [**redirectUrls](#redirectUrls)
* [**statusCode](#statusCode)
* [**statusMessage](#statusMessage)
* [**trailers](#trailers)
* [**url](#url)

## Properties<!-- -->[**](#Properties)

### [**](#complete)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L141)complete

**complete: boolean

### [**](#headers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L138)headers

**headers: SimpleHeaders

### [**](#ip)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L134)optionalip

**ip?

<!-- -->

: string

### [**](#redirectUrls)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L131)redirectUrls

**redirectUrls: URL\[]

### [**](#statusCode)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L135)statusCode

**statusCode: number

### [**](#statusMessage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L136)optionalstatusMessage

**statusMessage?

<!-- -->

: string

### [**](#trailers)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L139)trailers

**trailers: SimpleHeaders

### [**](#url)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L132)url

**url: string
