# Source: https://crawlee.dev/js/api/core/class/GotScrapingHttpClient.md

# GotScrapingHttpClient<!-- -->

A HTTP client implementation based on the `got-scraping` library.

### Implements

* [BaseHttpClient](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**sendRequest](#sendRequest)
* [**stream](#stream)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)constructor

* ****new GotScrapingHttpClient**(): [GotScrapingHttpClient](https://crawlee.dev/js/api/core/class/GotScrapingHttpClient.md)

- #### Returns [GotScrapingHttpClient](https://crawlee.dev/js/api/core/class/GotScrapingHttpClient.md)

## Methods<!-- -->[**](#Methods)

### [**](#sendRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/got-scraping-http-client.ts#L21)sendRequest

* ****sendRequest**\<TResponseType>(request): Promise<[HttpResponse](https://crawlee.dev/js/api/core/interface/HttpResponse.md)\<TResponseType>>

- Implementation of BaseHttpClient.sendRequest

  Perform an HTTP Request and return the complete response.

  ***

  #### Parameters

  * ##### request: [HttpRequest](https://crawlee.dev/js/api/core/interface/HttpRequest.md)\<TResponseType>

  #### Returns Promise<[HttpResponse](https://crawlee.dev/js/api/core/interface/HttpResponse.md)\<TResponseType>>

### [**](#stream)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/got-scraping-http-client.ts#L45)stream

* ****stream**(request, handleRedirect): Promise<[StreamingHttpResponse](https://crawlee.dev/js/api/core/interface/StreamingHttpResponse.md)>

- Implementation of BaseHttpClient.stream

  Perform an HTTP Request and return after the response headers are received. The body may be read from a stream contained in the response.

  ***

  #### Parameters

  * ##### request: [HttpRequest](https://crawlee.dev/js/api/core/interface/HttpRequest.md)\<text>
  * ##### optionalhandleRedirect: [RedirectHandler](https://crawlee.dev/js/api/core.md#RedirectHandler)

  #### Returns Promise<[StreamingHttpResponse](https://crawlee.dev/js/api/core/interface/StreamingHttpResponse.md)>
