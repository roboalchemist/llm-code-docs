# Source: https://docs.apify.com/sdk/python/reference/class/RequestLoader.md

# RequestLoader<!-- -->

An abstract class defining the interface for classes that provide access to a read-only stream of requests.

Request loaders are used to manage and provide access to a storage of crawling requests.

Key responsibilities:

* Fetching the next request to be processed.
* Marking requests as successfully handled after processing.
* Managing state information such as the total and handled request counts.

### Hierarchy

* *RequestLoader*

  * [RequestList](https://crawlee.dev/python/api/class/RequestList)
  * [RequestManager](https://crawlee.dev/python/api/class/RequestManager)
  * [SitemapRequestLoader](https://crawlee.dev/python/api/class/SitemapRequestLoader)

## Index[**](#Index)

### Methods

* [](https://crawlee.dev/python/api/class/RequestLoader#fetch_next_request)
* [](https://crawlee.dev/python/api/class/RequestLoader#get_handled_count)
* [](https://crawlee.dev/python/api/class/RequestLoader#get_total_count)
* [](https://crawlee.dev/python/api/class/RequestLoader#is_empty)
* [](https://crawlee.dev/python/api/class/RequestLoader#is_finished)
* [](https://crawlee.dev/python/api/class/RequestLoader#mark_request_as_handled)
* [**to\_tandem](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestLoader.md#to_tandem)

## Methods<!-- -->[**](#Methods)

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/crawlee/request_loaders/_request_loader.py#L45)

:

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/crawlee/request_loaders/_request_loader.py#L29)

:

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/crawlee/request_loaders/_request_loader.py#L33)

:

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/crawlee/request_loaders/_request_loader.py#L37)

:

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/crawlee/request_loaders/_request_loader.py#L41)

:

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/crawlee/request_loaders/_request_loader.py#L53)

:

### [**](#to_tandem)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_loader.py#L56)to\_tandem

* **async **to\_tandem**(request\_manager): [RequestManagerTandem](https://crawlee.dev/python/api/class/RequestManagerTandem)

- Combine the loader with a request manager to support adding and reclaiming requests.

  ***

  #### Parameters

  * ##### optionalrequest\_manager: [RequestManager](https://crawlee.dev/python/api/class/RequestManager) | None = <!-- -->None

    Request manager to combine the loader with. If None is given, the default request queue is used.

  #### Returns [RequestManagerTandem](https://crawlee.dev/python/api/class/RequestManagerTandem)
