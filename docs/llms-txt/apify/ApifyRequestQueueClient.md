# Source: https://docs.apify.com/sdk/python/reference/class/ApifyRequestQueueClient.md

# ApifyRequestQueueClient<!-- -->

Base class for Apify platform implementations of the request queue client.

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md#__init__)
* [**add\_batch\_of\_requests](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md#add_batch_of_requests)
* [**drop](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md#drop)
* [**fetch\_next\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md#fetch_next_request)
* [**get\_metadata](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md#get_metadata)
* [**get\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md#get_request)
* [**is\_empty](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md#is_empty)
* [**mark\_request\_as\_handled](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md#mark_request_as_handled)
* [**open](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md#open)
* [**purge](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md#purge)
* [**reclaim\_request](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md#reclaim_request)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_client.py#L33)\_\_init\_\_

* ****\_\_init\_\_**(\*, api\_client, metadata, access): None

- Initialize a new instance.

  Preferably use the `ApifyRequestQueueClient.open` class method to create a new instance.

  ***

  #### Parameters

  * ##### keyword-onlyapi\_client: RequestQueueClientAsync
  * ##### keyword-onlymetadata: RequestQueueMetadata
  * ##### optionalkeyword-onlyaccess: Literal\[single, shared] = <!-- -->'single'

  #### Returns None

### [**](#add_batch_of_requests)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_client.py#L68)add\_batch\_of\_requests

* **async **add\_batch\_of\_requests**(requests, \*, forefront): AddRequestsResponse

- Add a batch of requests to the queue.

  ***

  #### Parameters

  * ##### requests: Sequence\[Request]

    The requests to add.

  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

    Whether to add the requests to the beginning of the queue.

  #### Returns AddRequestsResponse

### [**](#drop)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_client.py#L253)drop

* **async **drop**(): None

- #### Returns None

### [**](#fetch_next_request)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_client.py#L86)fetch\_next\_request

* **async **fetch\_next\_request**(): Request | None

- Return the next request in the queue to be processed.

  Once you successfully finish processing of the request, you need to call `mark_request_as_handled` to mark the request as handled in the queue. If there was some error in processing the request, call `reclaim_request` instead, so that the queue will give the request to some other consumer in another call to the `fetch_next_request` method.

  ***

  #### Returns Request | None

### [**](#get_metadata)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_client.py#L155)get\_metadata

* **async **get\_metadata**(): [ApifyRequestQueueMetadata](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueMetadata.md)

- Get metadata about the request queue.

  ***

  #### Returns [ApifyRequestQueueMetadata](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueMetadata.md)

### [**](#get_request)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_client.py#L114)get\_request

* **async **get\_request**(unique\_key): Request | None

- Get a request by unique key.

  ***

  #### Parameters

  * ##### unique\_key: str

    Unique key of the request to get.

  #### Returns Request | None

### [**](#is_empty)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_client.py#L146)is\_empty

* **async **is\_empty**(): bool

- Check if the queue is empty.

  ***

  #### Returns bool

### [**](#mark_request_as_handled)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_client.py#L100)mark\_request\_as\_handled

* **async **mark\_request\_as\_handled**(request): ProcessedRequest | None

- Mark a request as handled after successful processing.

  Handled requests will never again be returned by the `fetch_next_request` method.

  ***

  #### Parameters

  * ##### request: Request

    The request to mark as handled.

  #### Returns ProcessedRequest | None

### [**](#open)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_client.py#L180)open

* **async **open**(\*, id, name, alias, configuration, access): [ApifyRequestQueueClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md)

- Open an Apify request queue client.

  This method creates and initializes a new instance of the Apify request queue client. It handles authentication, storage lookup/creation, and metadata retrieval, and sets up internal caching and queue management structures.

  ***

  #### Parameters

  * ##### keyword-onlyid: str | None

    The ID of the RQ to open. If provided, searches for existing RQ by ID. Mutually exclusive with name and alias.

  * ##### keyword-onlyname: str | None

    The name of the RQ to open (global scope, persists across runs). Mutually exclusive with id and alias.

  * ##### keyword-onlyalias: str | None

    The alias of the RQ to open (run scope, creates unnamed storage). Mutually exclusive with id and name.

  * ##### keyword-onlyconfiguration: [Configuration](https://docs.apify.com/sdk/python/sdk/python/reference/class/Configuration.md)

    The configuration object containing API credentials and settings. Must include a valid `token` and `api_base_url`. May also contain a `default_request_queue_id` for fallback when neither `id`, `name`, nor `alias` is provided.

  * ##### optionalkeyword-onlyaccess: Literal\[single, shared] = <!-- -->'single'

    Controls the implementation of the request queue client based on expected scenario:

    * 'single' is suitable for single consumer scenarios. It makes less API calls, is cheaper and faster.
    * 'shared' is suitable for multiple consumers scenarios at the cost of higher API usage. Detailed constraints for the 'single' access type:
    * Only one client is consuming the request queue at the time.
    * Multiple producers can put requests to the queue, but their forefront requests are not guaranteed to be handled so quickly as this client does not aggressively fetch the forefront and relies on local head estimation.
    * Requests are only added to the queue, never deleted by other clients. (Marking as handled is ok.)
    * Other producers can add new requests, but not modify existing ones. (Modifications would not be included in local cache)

  #### Returns [ApifyRequestQueueClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md)

### [**](#purge)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_client.py#L246)purge

* **async **purge**(): None

- #### Returns None

### [**](#reclaim_request)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_request_queue_client.py#L126)reclaim\_request

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
