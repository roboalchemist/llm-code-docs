# Source: https://docs.apify.com/sdk/python/reference/class/ApifyRequestQueueSingleClient.md

# ApifyRequestQueueSingleClient<!-- -->

Internal request queue client implementation for single-consumer scenarios on the Apify platform.

This implementation minimizes API calls and resource usage by leveraging local caching and head estimation. It is designed for scenarios where only one client consumes requests from the queue at a time, though multiple producers may add requests concurrently.

### Usage constraints

This client must operate within the following constraints to function correctly:

* **Single consumer**: Only one client should be consuming (fetching) requests from the queue at any given time.
* **Multiple producers allowed**: Multiple clients can add requests concurrently, but their forefront requests may not be prioritized immediately since this client relies on local head estimation.
* **Append-only queue**: Requests should only be added to the queue, never deleted by other clients. Marking requests as handled is permitted.
* **No external modifications**: Other producers can add new requests but should not modify existing ones, as modifications won't be reflected in the local cache.

If these constraints are not met, the client may exhibit unpredictable behavior.

This class is used internally by `ApifyRequestQueueClient` when `access='single'` is specified.

Public methods are not individually documented as they implement the interface defined in `RequestQueueClient`.

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSingleClient.md#__init__)
* [**add\_batch\_of\_requests](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSingleClient.md#add_batch_of_requests)
* [**fetch\_next\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSingleClient.md#fetch_next_request)
* [**get\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSingleClient.md#get_request)
* [**is\_empty](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSingleClient.md#is_empty)
* [**mark\_request\_as\_handled](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSingleClient.md#mark_request_as_handled)
* [**reclaim\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueSingleClient.md#reclaim_request)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_single_client.py#L52)\_\_init\_\_

* ****\_\_init\_\_**(\*, api\_client, metadata, cache\_size): None

- Initialize a new single-consumer request queue client instance.

  Use `ApifyRequestQueueClient.open(access='single')` instead of calling this directly.

  ***

  #### Parameters

  * ##### keyword-onlyapi\_client: RequestQueueClientAsync

    The Apify API client for request queue operations.

  * ##### keyword-onlymetadata: RequestQueueMetadata

    Initial metadata for the request queue.

  * ##### keyword-onlycache\_size: int

    Maximum number of requests to cache locally.

  #### Returns None

### [**](#add_batch_of_requests)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_single_client.py#L98)add\_batch\_of\_requests

* **async **add\_batch\_of\_requests**(requests, \*, forefront): AddRequestsResponse

- Specific implementation of this method for the RQ single access mode.

  ***

  #### Parameters

  * ##### requests: Sequence\[Request]
  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

  #### Returns AddRequestsResponse

### [**](#fetch_next_request)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_single_client.py#L187)fetch\_next\_request

* **async **fetch\_next\_request**(): Request | None

- Specific implementation of this method for the RQ single access mode.

  ***

  #### Returns Request | None

### [**](#get_request)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_single_client.py#L183)get\_request

* **async **get\_request**(unique\_key): Request | None

- Specific implementation of this method for the RQ single access mode.

  ***

  #### Parameters

  * ##### unique\_key: str

  #### Returns Request | None

### [**](#is_empty)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_single_client.py#L272)is\_empty

* **async **is\_empty**(): bool

- Specific implementation of this method for the RQ single access mode.

  ***

  #### Returns bool

### [**](#mark_request_as_handled)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_single_client.py#L199)mark\_request\_as\_handled

* **async **mark\_request\_as\_handled**(request): ProcessedRequest | None

- Specific implementation of this method for the RQ single access mode.

  ***

  #### Parameters

  * ##### request: Request

  #### Returns ProcessedRequest | None

### [**](#reclaim_request)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_single_client.py#L229)reclaim\_request

* **async **reclaim\_request**(request, \*, forefront): ProcessedRequest | None

- Specific implementation of this method for the RQ single access mode.

  ***

  #### Parameters

  * ##### request: Request
  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

  #### Returns ProcessedRequest | None
