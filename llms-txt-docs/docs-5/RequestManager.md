# Source: https://docs.apify.com/sdk/python/reference/class/RequestManager.md

# RequestManager<!-- -->

Base class that extends `RequestLoader` with the capability to enqueue new requests and reclaim failed ones.

### Hierarchy

* [RequestLoader](https://crawlee.dev/python/api/class/RequestLoader)

  * *RequestManager*

    * [RequestQueue](https://crawlee.dev/python/api/class/RequestQueue)
    * [RequestManagerTandem](https://crawlee.dev/python/api/class/RequestManagerTandem)

## Index[**](#Index)

### Methods

* [](https://crawlee.dev/python/api/class/RequestManager#add_request)
* [](https://crawlee.dev/python/api/class/RequestManager#add_requests)
* [**drop](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManager.md#drop)
* [](https://crawlee.dev/python/api/class/RequestManager#fetch_next_request)
* [](https://crawlee.dev/python/api/class/RequestManager#get_handled_count)
* [](https://crawlee.dev/python/api/class/RequestManager#get_total_count)
* [](https://crawlee.dev/python/api/class/RequestManager#is_empty)
* [](https://crawlee.dev/python/api/class/RequestManager#is_finished)
* [](https://crawlee.dev/python/api/class/RequestManager#mark_request_as_handled)
* [](https://crawlee.dev/python/api/class/RequestManager#reclaim_request)
* [**to\_tandem](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManager.md#to_tandem)

## Methods<!-- -->[**](#Methods)

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/crawlee/request_loaders/_request_manager.py#L26)

:

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/crawlee/request_loaders/_request_manager.py#L43)

:

### [**](#drop)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_manager.py#L22)drop

* **async **drop**(): None

- Overrides [Storage.drop](https://crawlee.dev/python/api/class/Storage#drop)

  Remove persistent state either from the Apify Cloud storage or from the local database.

  ***

  #### Returns None

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

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/crawlee/request_loaders/_request_manager.py#L70)

:

### [**](#to_tandem)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_loader.py#L56)to\_tandem

* **async **to\_tandem**(request\_manager): [RequestManagerTandem](https://crawlee.dev/python/api/class/RequestManagerTandem)

- Inherited from [RequestLoader.to\_tandem](https://crawlee.dev/python/api/class/RequestLoader#to_tandem)

  Combine the loader with a request manager to support adding and reclaiming requests.

  ***

  #### Parameters

  * ##### optionalrequest\_manager: RequestManager | None = <!-- -->None

    Request manager to combine the loader with. If None is given, the default request queue is used.

  #### Returns [RequestManagerTandem](https://crawlee.dev/python/api/class/RequestManagerTandem)
