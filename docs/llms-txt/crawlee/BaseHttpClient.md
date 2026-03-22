# Source: https://crawlee.dev/js/api/core/interface/BaseHttpClient.md

# BaseHttpClient<!-- -->

Interface for user-defined HTTP clients to be used for plain HTTP crawling and for sending additional requests during a crawl.

### Implemented by

* [GotScrapingHttpClient](https://crawlee.dev/js/api/core/class/GotScrapingHttpClient.md)
* [ImpitHttpClient](https://crawlee.dev/js/api/impit-client/class/ImpitHttpClient.md)

## Index[**](#Index)

### Methods

* [**sendRequest](#sendRequest)
* [**stream](#stream)

## Methods<!-- -->[**](#Methods)

### [**](#sendRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L183)sendRequest

* ****sendRequest**\<TResponseType>(request): Promise<[HttpResponse](https://crawlee.dev/js/api/core/interface/HttpResponse.md)\<TResponseType>>

- Perform an HTTP Request and return the complete response.

  ***

  #### Parameters

  * ##### request: [HttpRequest](https://crawlee.dev/js/api/core/interface/HttpRequest.md)\<TResponseType>

  #### Returns Promise<[HttpResponse](https://crawlee.dev/js/api/core/interface/HttpResponse.md)\<TResponseType>>

### [**](#stream)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L190)stream

* ****stream**(request, onRedirect): Promise<[StreamingHttpResponse](https://crawlee.dev/js/api/core/interface/StreamingHttpResponse.md)>

- Perform an HTTP Request and return after the response headers are received. The body may be read from a stream contained in the response.

  ***

  #### Parameters

  * ##### request: [HttpRequest](https://crawlee.dev/js/api/core/interface/HttpRequest.md)\<text>
  * ##### optionalonRedirect: [RedirectHandler](https://crawlee.dev/js/api/core.md#RedirectHandler)

  #### Returns Promise<[StreamingHttpResponse](https://crawlee.dev/js/api/core/interface/StreamingHttpResponse.md)>
