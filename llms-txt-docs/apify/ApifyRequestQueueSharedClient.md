# Source: https://docs.apify.com/sdk/python/reference/class/ApifyRequestQueueSharedClient.md

# ApifyRequestQueueSharedClient<!-- -->

An Apify platform implementation of the request queue client.

This implementation supports multiple producers and multiple consumers scenario.

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

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L35)\_\_init\_\_

* ****\_\_init\_\_**(\*, api\_client, metadata, cache\_size, metadata\_getter): None

- Initialize a new instance.

  Preferably use the `ApifyRequestQueueClient.open` class method to create a new instance.

  ***

  #### Parameters

  * ##### keyword-onlyapi\_client: RequestQueueClientAsync
  * ##### keyword-onlymetadata: RequestQueueMetadata
  * ##### keyword-onlycache\_size: int
  * ##### keyword-onlymetadata\_getter: Callable\[\[], Coroutine\[Any, Any, [ApifyRequestQueueMetadata](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueMetadata.md)]]

  #### Returns None

### [**](#add_batch_of_requests)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L83)add\_batch\_of\_requests

* **async **add\_batch\_of\_requests**(requests, \*, forefront): AddRequestsResponse

- Add a batch of requests to the queue.

  ***

  #### Parameters

  * ##### requests: Sequence\[Request]

    The requests to add.

  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

    Whether to add the requests to the beginning of the queue.

  #### Returns AddRequestsResponse

### [**](#fetch_next_request)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L195)fetch\_next\_request

* **async **fetch\_next\_request**(): Request | None

- Return the next request in the queue to be processed.

  Once you successfully finish processing of the request, you need to call `mark_request_as_handled` to mark the request as handled in the queue. If there was some error in processing the request, call `reclaim_request` instead, so that the queue will give the request to some other consumer in another call to the `fetch_next_request` method.

  ***

  #### Returns Request | None

### [**](#get_request)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L176)get\_request

* **async **get\_request**(unique\_key): Request | None

- Get a request by unique key.

  ***

  #### Parameters

  * ##### unique\_key: str

    Unique key of the request to get.

  #### Returns Request | None

### [**](#is_empty)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L341)is\_empty

* **async **is\_empty**(): bool

- Check if the queue is empty.

  ***

  #### Returns bool

### [**](#mark_request_as_handled)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L246)mark\_request\_as\_handled

* **async **mark\_request\_as\_handled**(request): ProcessedRequest | None

- Mark a request as handled after successful processing.

  Handled requests will never again be returned by the `fetch_next_request` method.

  ***

  #### Parameters

  * ##### request: Request

    The request to mark as handled.

  #### Returns ProcessedRequest | None

### [**](#reclaim_request)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_shared_client.py#L287)reclaim\_request

* **async **reclaim\_request**(request, \*, forefront): ProcessedRequest | None

- Reclaim a failed request back to the queue.

  The request will be returned for processing later again by another call to `fetch_next_request`.

  ***

  #### Parameters

  * ##### request: Request

    The request to return to the queue.

  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

    Whether to add the request to the head or the end of the queue.

  #### Returns ProcessedRequest | None
