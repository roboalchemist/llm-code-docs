# Source: https://docs.apify.com/sdk/python/reference/class/RequestManagerTandem.md

# RequestManagerTandem<!-- -->

Implements a tandem behaviour for a pair of `RequestLoader` and `RequestManager`.

In this scenario, the contents of the "loader" get transferred into the "manager", allowing processing the requests from both sources and also enqueueing new requests (not possible with plain `RequestManager`).

### Hierarchy

* [RequestManager](https://crawlee.dev/python/api/class/RequestManager)
  * *RequestManagerTandem*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManagerTandem.md#__init__)
* [**add\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManagerTandem.md#add_request)
* [**add\_requests](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManagerTandem.md#add_requests)
* [**drop](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManagerTandem.md#drop)
* [**fetch\_next\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManagerTandem.md#fetch_next_request)
* [**get\_handled\_count](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManagerTandem.md#get_handled_count)
* [**get\_total\_count](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManagerTandem.md#get_total_count)
* [**is\_empty](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManagerTandem.md#is_empty)
* [**is\_finished](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManagerTandem.md#is_finished)
* [**mark\_request\_as\_handled](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManagerTandem.md#mark_request_as_handled)
* [**reclaim\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManagerTandem.md#reclaim_request)
* [**to\_tandem](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestManagerTandem.md#to_tandem)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_manager_tandem.py#L31)\_\_init\_\_

* ****\_\_init\_\_**(request\_loader, request\_manager): None

- #### Parameters

  * ##### request\_loader: [RequestLoader](https://crawlee.dev/python/api/class/RequestLoader)
  * ##### request\_manager: [RequestManager](https://crawlee.dev/python/api/class/RequestManager)

  #### Returns None

### [**](#add_request)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_manager_tandem.py#L52)add\_request

* **async **add\_request**(request, \*, forefront): [ProcessedRequest](https://crawlee.dev/python/api/class/ProcessedRequest)

- Overrides [RequestManager.add\_request](https://crawlee.dev/python/api/class/RequestManager#add_request)

  Add a single request to the manager and store it in underlying resource client.

  ***

  #### Parameters

  * ##### request: str | [Request](https://crawlee.dev/python/api/class/Request)

    The request object (or its string representation) to be added to the manager.

  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

    Determines whether the request should be added to the beginning (if True) or the end (if False) of the manager.

  #### Returns [ProcessedRequest](https://crawlee.dev/python/api/class/ProcessedRequest)

### [**](#add_requests)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_manager_tandem.py#L56)add\_requests

* **async **add\_requests**(requests, \*, forefront, batch\_size, wait\_time\_between\_batches, wait\_for\_all\_requests\_to\_be\_added, wait\_for\_all\_requests\_to\_be\_added\_timeout): None

- Overrides [RequestManager.add\_requests](https://crawlee.dev/python/api/class/RequestManager#add_requests)

  Add requests to the manager in batches.

  ***

  #### Parameters

  * ##### requests: Sequence\[str | [Request](https://crawlee.dev/python/api/class/Request)]

    Requests to enqueue.

  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

    If True, add requests to the beginning of the queue.

  * ##### optionalkeyword-onlybatch\_size: int = <!-- -->1000

    The number of requests to add in one batch.

  * ##### optionalkeyword-onlywait\_time\_between\_batches: timedelta = <!-- -->timedelta(seconds=1)

    Time to wait between adding batches.

  * ##### optionalkeyword-onlywait\_for\_all\_requests\_to\_be\_added: bool = <!-- -->False

    If True, wait for all requests to be added before returning.

  * ##### optionalkeyword-onlywait\_for\_all\_requests\_to\_be\_added\_timeout: timedelta | None = <!-- -->None

    Timeout for waiting for all requests to be added.

  #### Returns None

### [**](#drop)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_manager_tandem.py#L107)drop

* **async **drop**(): None

- Overrides [Storage.drop](https://crawlee.dev/python/api/class/Storage#drop)

  Remove persistent state either from the Apify Cloud storage or from the local database.

  ***

  #### Returns None

### [**](#fetch_next_request)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_manager_tandem.py#L76)fetch\_next\_request

* **async **fetch\_next\_request**(): Request | None

- Overrides [RequestManager.fetch\_next\_request](https://crawlee.dev/python/api/class/RequestManager#fetch_next_request)

  Return the next request to be processed, or `None` if there are no more pending requests.

  The method should return `None` if and only if `is_finished` would return `True`. In other cases, the method should wait until a request appears.

  ***

  #### Returns Request | None

### [**](#get_handled_count)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_manager_tandem.py#L36)get\_handled\_count

* **async **get\_handled\_count**(): int

- Overrides [RequestManager.get\_handled\_count](https://crawlee.dev/python/api/class/RequestManager#get_handled_count)

  Get the number of requests in the loader that have been handled.

  ***

  #### Returns int

### [**](#get_total_count)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_manager_tandem.py#L40)get\_total\_count

* **async **get\_total\_count**(): int

- Overrides [RequestManager.get\_total\_count](https://crawlee.dev/python/api/class/RequestManager#get_total_count)

  Get an offline approximation of the total number of requests in the loader (i.e. pending + handled).

  ***

  #### Returns int

### [**](#is_empty)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_manager_tandem.py#L44)is\_empty

* **async **is\_empty**(): bool

- Overrides [RequestManager.is\_empty](https://crawlee.dev/python/api/class/RequestManager#is_empty)

  Return True if there are no more requests in the loader (there might still be unfinished requests).

  ***

  #### Returns bool

### [**](#is_finished)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_manager_tandem.py#L48)is\_finished

* **async **is\_finished**(): bool

- Overrides [RequestManager.is\_finished](https://crawlee.dev/python/api/class/RequestManager#is_finished)

  Return True if all requests have been handled.

  ***

  #### Returns bool

### [**](#mark_request_as_handled)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_manager_tandem.py#L103)mark\_request\_as\_handled

* **async **mark\_request\_as\_handled**(request): ProcessedRequest | None

- Overrides [RequestManager.mark\_request\_as\_handled](https://crawlee.dev/python/api/class/RequestManager#mark_request_as_handled)

  Mark a request as handled after a successful processing (or after giving up retrying).

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/python/api/class/Request)

  #### Returns ProcessedRequest | None

### [**](#reclaim_request)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_manager_tandem.py#L99)reclaim\_request

* **async **reclaim\_request**(request, \*, forefront): [ProcessedRequest](https://crawlee.dev/python/api/class/ProcessedRequest) | None

- Overrides [RequestManager.reclaim\_request](https://crawlee.dev/python/api/class/RequestManager#reclaim_request)

  Reclaims a failed request back to the source, so that it can be returned for processing later again.

  It is possible to modify the request data by supplying an updated request as a parameter.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/python/api/class/Request)
  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

  #### Returns [ProcessedRequest](https://crawlee.dev/python/api/class/ProcessedRequest) | None

### [**](#to_tandem)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/request_loaders/_request_loader.py#L56)to\_tandem

* **async **to\_tandem**(request\_manager): [RequestManagerTandem](https://crawlee.dev/python/api/class/RequestManagerTandem)

- Inherited from [RequestLoader.to\_tandem](https://crawlee.dev/python/api/class/RequestLoader#to_tandem)

  Combine the loader with a request manager to support adding and reclaiming requests.

  ***

  #### Parameters

  * ##### optionalrequest\_manager: RequestManager | None = <!-- -->None

    Request manager to combine the loader with. If None is given, the default request queue is used.

  #### Returns [RequestManagerTandem](https://crawlee.dev/python/api/class/RequestManagerTandem)
