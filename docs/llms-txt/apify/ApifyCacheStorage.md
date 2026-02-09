# Source: https://docs.apify.com/sdk/python/reference/class/ApifyCacheStorage.md

# ApifyCacheStorage<!-- -->

A Scrapy cache storage that uses the Apify `KeyValueStore` to store responses.

It can be set as a storage for Scrapy's built-in `HttpCacheMiddleware`, which caches responses to requests. See HTTPCache middleware settings (prefixed with `HTTPCACHE_`) in the Scrapy documentation for more information. Requires the asyncio Twisted reactor to be installed.

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyCacheStorage.md#__init__)
* [**close\_spider](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyCacheStorage.md#close_spider)
* [**open\_spider](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyCacheStorage.md#open_spider)
* [**retrieve\_response](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyCacheStorage.md#retrieve_response)
* [**store\_response](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyCacheStorage.md#store_response)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/extensions/_httpcache.py#L38)\_\_init\_\_

* ****\_\_init\_\_**(settings): None

- #### Parameters

  * ##### settings: BaseSettings

  #### Returns None

### [**](#close_spider)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/extensions/_httpcache.py#L69)close\_spider

* ****close\_spider**(\_, current\_time): None

- Close the cache storage for a spider.

  ***

  #### Parameters

  * ##### \_: Spider
  * ##### optionalcurrent\_time: int | None = <!-- -->None

  #### Returns None

### [**](#open_spider)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/extensions/_httpcache.py#L46)open\_spider

* ****open\_spider**(spider): None

- Open the cache storage for a spider.

  ***

  #### Parameters

  * ##### spider: Spider

  #### Returns None

### [**](#retrieve_response)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/extensions/_httpcache.py#L112)retrieve\_response

* ****retrieve\_response**(\_, request, current\_time): Response | None

- Retrieve a response from the cache storage.

  ***

  #### Parameters

  * ##### \_: Spider
  * ##### request: Request
  * ##### optionalcurrent\_time: int | None = <!-- -->None

  #### Returns Response | None

### [**](#store_response)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/scrapy/extensions/_httpcache.py#L144)store\_response

* ****store\_response**(\_, request, response): None

- Store a response in the cache storage.

  ***

  #### Parameters

  * ##### \_: Spider
  * ##### request: Request
  * ##### response: Response

  #### Returns None
