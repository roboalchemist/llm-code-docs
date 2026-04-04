# Source: https://docs.apify.com/sdk/python/reference/class/ApifyHttpProxyMiddleware.md

# ApifyHttpProxyMiddleware<!-- -->

Apify HTTP proxy middleware for Scrapy.

This middleware enhances request processing by adding a 'proxy' field to the request's meta and an authentication header. It draws inspiration from the `HttpProxyMiddleware` included by default in Scrapy projects. The proxy URL is sourced from the settings under the `APIFY_PROXY_SETTINGS` key. The value of this key, a dictionary, should be provided by the Actor input. An example of the proxy settings:

proxy\_settings = {'useApifyProxy': true, 'apifyProxyGroups': \[]}

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyHttpProxyMiddleware.md#__init__)
* [**from\_crawler](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyHttpProxyMiddleware.md#from_crawler)
* [**process\_exception](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyHttpProxyMiddleware.md#process_exception)
* [**process\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyHttpProxyMiddleware.md#process_request)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/middlewares/apify_proxy.py#L28)\_\_init\_\_

* ****\_\_init\_\_**(proxy\_settings): None

- Create a new instance.

  ***

  #### Parameters

  * ##### proxy\_settings: dict

    Dictionary containing proxy settings, provided by the Actor input.

  #### Returns None

### [**](#from_crawler)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/middlewares/apify_proxy.py#L39)from\_crawler

* ****from\_crawler**(crawler): [ApifyHttpProxyMiddleware](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyHttpProxyMiddleware.md)

- Create an instance of ApifyHttpProxyMiddleware from a Scrapy Crawler.

  ***

  #### Parameters

  * ##### crawler: Crawler

    Scrapy Crawler object.

  #### Returns [ApifyHttpProxyMiddleware](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyHttpProxyMiddleware.md)

### [**](#process_exception)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/middlewares/apify_proxy.py#L89)process\_exception

* ****process\_exception**(request, exception, spider): None

- Process an exception that occurs during request processing.

  ***

  #### Parameters

  * ##### request: Request

    Scrapy Request object.

  * ##### exception: Exception

    Exception object.

  * ##### spider: Spider

    Scrapy Spider object.

  #### Returns None

### [**](#process_request)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/middlewares/apify_proxy.py#L67)process\_request

* **async **process\_request**(request, spider): None

- Process a Scrapy request by assigning a new proxy.

  ***

  #### Parameters

  * ##### request: Request

    Scrapy Request object.

  * ##### spider: Spider

    Scrapy Spider object.

  #### Returns None
