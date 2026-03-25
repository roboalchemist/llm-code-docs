# Source: https://crawlee.dev/js/api/impit-client/class/ImpitHttpClient.md

# ImpitHttpClient<!-- -->

A HTTP client implementation based on the \`impit library.

### Implements

* [BaseHttpClient](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**sendRequest](#sendRequest)
* [**stream](#stream)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/impit-client/src/index.ts#L54)constructor

* ****new ImpitHttpClient**(options): [ImpitHttpClient](https://crawlee.dev/js/api/impit-client/class/ImpitHttpClient.md)

- #### Parameters

  * ##### optionaloptions: Omit\<ImpitOptions, proxyUrl> & { maxRedirects?<!-- -->: number }

  #### Returns [ImpitHttpClient](https://crawlee.dev/js/api/impit-client/class/ImpitHttpClient.md)

## Methods<!-- -->[**](#Methods)

### [**](#sendRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/impit-client/src/index.ts#L174)sendRequest

* ****sendRequest**\<TResponseType>(request): Promise<[HttpResponse](https://crawlee.dev/js/api/core/interface/HttpResponse.md)\<TResponseType>>

- Implementation of BaseHttpClient.sendRequest

  Perform an HTTP Request and return the complete response.

  ***

  #### Parameters

  * ##### request: [HttpRequest](https://crawlee.dev/js/api/core/interface/HttpRequest.md)\<TResponseType>

  #### Returns Promise<[HttpResponse](https://crawlee.dev/js/api/core/interface/HttpResponse.md)\<TResponseType>>

### [**](#stream)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/impit-client/src/index.ts#L236)stream

* ****stream**(request): Promise<[StreamingHttpResponse](https://crawlee.dev/js/api/core/interface/StreamingHttpResponse.md)>

- Implementation of BaseHttpClient.stream

  Perform an HTTP Request and return after the response headers are received. The body may be read from a stream contained in the response.

  ***

  #### Parameters

  * ##### request: [HttpRequest](https://crawlee.dev/js/api/core/interface/HttpRequest.md)\<text>

  #### Returns Promise<[StreamingHttpResponse](https://crawlee.dev/js/api/core/interface/StreamingHttpResponse.md)>
