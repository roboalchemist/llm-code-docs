# Source: https://docs.apify.com/sdk/python/reference/class/ApifyRequestQueueSingleClient.md

# ApifyRequestQueueSingleClient<!-- -->

An Apify platform implementation of the request queue client with limited capability.

This client is designed to use as little resources as possible, but has to be used in constrained context. Constraints:

* Only one client is consuming the request queue at the time.
* Multiple producers can put requests to the queue, but their forefront requests are not guaranteed to be handled so quickly as this client does not aggressively fetch the forefront and relies on local head estimation.
* Requests are only added to the queue, never deleted. (Marking as handled is ok.)
* Other producers can add new requests, but not modify existing ones (otherwise caching can miss the updates)

If the constraints are not met, the client might work in an unpredictable way.

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

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_single_client.py#L41)\_\_init\_\_

* ****\_\_init\_\_**(\*, api\_client, metadata, cache\_size): None

- Initialize a new instance.

  Preferably use the `ApifyRequestQueueClient.open` class method to create a new instance.

  ***

  #### Parameters

  * ##### keyword-onlyapi\_client: RequestQueueClientAsync
  * ##### keyword-onlymetadata: RequestQueueMetadata
  * ##### keyword-onlycache\_size: int

  #### Returns None

### [**](#add_batch_of_requests)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_single_client.py#L84)add\_batch\_of\_requests

* **async **add\_batch\_of\_requests**(requests, \*, forefront): AddRequestsResponse

- Add a batch of requests to the queue.

  ***

  #### Parameters

  * ##### requests: Sequence\[Request]

    The requests to add.

  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

    Whether to add the requests to the beginning of the queue.

  #### Returns AddRequestsResponse

### [**](#fetch_next_request)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_single_client.py#L220)fetch\_next\_request

* **async **fetch\_next\_request**(): Request | None

- Return the next request in the queue to be processed.

  Once you successfully finish processing of the request, you need to call `mark_request_as_handled` to mark the request as handled in the queue. If there was some error in processing the request, call `reclaim_request` instead, so that the queue will give the request to some other consumer in another call to the `fetch_next_request` method.

  ***

  #### Returns Request | None

### [**](#get_request)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_single_client.py#L177)get\_request

* **async **get\_request**(unique\_key): Request | None

- Get a request by unique key.

  ***

  #### Parameters

  * ##### unique\_key: str

    Unique key of the request to get.

  #### Returns Request | None

### [**](#is_empty)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_single_client.py#L369)is\_empty

* **async **is\_empty**(): bool

- Check if the queue is empty.

  ***

  #### Returns bool

### [**](#mark_request_as_handled)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_single_client.py#L276)mark\_request\_as\_handled

* **async **mark\_request\_as\_handled**(request): ProcessedRequest | None

- Mark a request as handled after successful processing.

  Handled requests will never again be returned by the `fetch_next_request` method.

  ***

  #### Parameters

  * ##### request: Request

    The request to mark as handled.

  #### Returns ProcessedRequest | None

### [**](#reclaim_request)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_single_client.py#L316)reclaim\_request

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
