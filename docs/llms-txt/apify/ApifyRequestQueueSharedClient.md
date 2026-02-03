# Source: https://docs.apify.com/sdk/python/reference/class/ApifyRequestQueueSharedClient.md

# ApifyRequestQueueSharedClient<!-- -->

Internal request queue client implementation for multi-consumer scenarios on the Apify platform.

This implementation is optimized for scenarios where multiple clients concurrently fetch and process requests from the same queue. It makes more frequent API calls to ensure consistency across all consumers and uses request locking to prevent duplicate processing.

This class is used internally by `ApifyRequestQueueClient` when `access='shared'` is specified.

Public methods are not individually documented as they implement the interface defined in `RequestQueueClient`.

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSharedClient.md#__init__)
* [**add\_batch\_of\_requests](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSharedClient.md#add_batch_of_requests)
* [**fetch\_next\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSharedClient.md#fetch_next_request)
* [**get\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSharedClient.md#get_request)
* [**is\_empty](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSharedClient.md#is_empty)
* [**mark\_request\_as\_handled](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSharedClient.md#mark_request_as_handled)
* [**reclaim\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSharedClient.md#reclaim_request)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L40)\_\_init\_\_

* ****\_\_init\_\_**(\*, api\_client, metadata, cache\_size, metadata\_getter): None

- Initialize a new shared request queue client instance.

  Use `ApifyRequestQueueClient.open(access='shared')` instead of calling this directly.

  ***

  #### Parameters

  * ##### keyword-onlyapi\_client: RequestQueueClientAsync

    The Apify API client for request queue operations.

  * ##### keyword-onlymetadata: RequestQueueMetadata

    Initial metadata for the request queue.

  * ##### keyword-onlycache\_size: int

    Maximum number of requests to cache locally.

  * ##### keyword-onlymetadata\_getter: Callable\[\[], Coroutine\[Any, Any, [ApifyRequestQueueMetadata](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueMetadata.md)]]

    Async function to fetch current metadata from the API.

  #### Returns None

### [**](#add_batch_of_requests)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L82)add\_batch\_of\_requests

* **async **add\_batch\_of\_requests**(requests, \*, forefront): AddRequestsResponse

- Specific implementation of this method for the RQ shared access mode.

  ***

  #### Parameters

  * ##### requests: Sequence\[Request]
  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

  #### Returns AddRequestsResponse

### [**](#fetch_next_request)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L170)fetch\_next\_request

* **async **fetch\_next\_request**(): Request | None

- Specific implementation of this method for the RQ shared access mode.

  ***

  #### Returns Request | None

### [**](#get_request)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L166)get\_request

* **async **get\_request**(unique\_key): Request | None

- Specific implementation of this method for the RQ shared access mode.

  ***

  #### Parameters

  * ##### unique\_key: str

  #### Returns Request | None

### [**](#is_empty)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L288)is\_empty

* **async **is\_empty**(): bool

- Specific implementation of this method for the RQ shared access mode.

  ***

  #### Returns bool

### [**](#mark_request_as_handled)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L212)mark\_request\_as\_handled

* **async **mark\_request\_as\_handled**(request): ProcessedRequest | None

- Specific implementation of this method for the RQ shared access mode.

  ***

  #### Parameters

  * ##### request: Request

  #### Returns ProcessedRequest | None

### [**](#reclaim_request)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L244)reclaim\_request

* **async **reclaim\_request**(request, \*, forefront): ProcessedRequest | None

- Specific implementation of this method for the RQ shared access mode.

  ***

  #### Parameters

  * ##### request: Request
  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

  #### Returns ProcessedRequest | None
