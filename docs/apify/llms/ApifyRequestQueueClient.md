# Source: https://docs.apify.com/sdk/python/reference/class/ApifyRequestQueueClient.md

# ApifyRequestQueueClient<!-- -->

Request queue client for the Apify platform.

This client provides access to request queues stored on the Apify platform, supporting both single-consumer and multi-consumer scenarios. It manages local caching, request fetching, and state synchronization with the platform's API.

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

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_client.py#L38)\_\_init\_\_

* ****\_\_init\_\_**(\*, api\_client, metadata, access): None

- Initialize a new instance.

  Preferably use the `ApifyRequestQueueClient.open` class method to create a new instance.

  ***

  #### Parameters

  * ##### keyword-onlyapi\_client: RequestQueueClientAsync
  * ##### keyword-onlymetadata: RequestQueueMetadata
  * ##### optionalkeyword-onlyaccess: Literal\[single, shared] = <!-- -->'single'

  #### Returns None

### [**](#add_batch_of_requests)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_client.py#L168)add\_batch\_of\_requests

* **async **add\_batch\_of\_requests**(requests, \*, forefront): AddRequestsResponse

- #### Parameters

  * ##### requests: Sequence\[Request]
  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

  #### Returns AddRequestsResponse

### [**](#drop)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_client.py#L164)drop

* **async **drop**(): None

- #### Returns None

### [**](#fetch_next_request)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_client.py#L177)fetch\_next\_request

* **async **fetch\_next\_request**(): Request | None

- #### Returns Request | None

### [**](#get_metadata)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_client.py#L70)get\_metadata

* **async **get\_metadata**(): [ApifyRequestQueueMetadata](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueMetadata.md)

- Retrieve current metadata about the request queue.

  This method fetches metadata from the Apify API and merges it with local estimations to provide the most up-to-date statistics. Local estimations are used to compensate for potential delays in API data propagation (typically a few seconds).

  ***

  #### Returns [ApifyRequestQueueMetadata](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueMetadata.md)

### [**](#get_request)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_client.py#L185)get\_request

* **async **get\_request**(unique\_key): Request | None

- #### Parameters

  * ##### unique\_key: str

  #### Returns Request | None

### [**](#is_empty)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_client.py#L198)is\_empty

* **async **is\_empty**(): bool

- #### Returns bool

### [**](#mark_request_as_handled)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_client.py#L181)mark\_request\_as\_handled

* **async **mark\_request\_as\_handled**(request): ProcessedRequest | None

- #### Parameters

  * ##### request: Request

  #### Returns ProcessedRequest | None

### [**](#open)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_client.py#L103)open

* **async **open**(\*, id, name, alias, configuration, access): [ApifyRequestQueueClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md)

- Open an Apify request queue client.

  This method creates and initializes a new request queue client instance, handling authentication, storage lookup or creation, metadata retrieval, and initialization of internal caching structures.

  ***

  #### Parameters

  * ##### keyword-onlyid: str | None

    ID of an existing request queue to open. Mutually exclusive with `name` and `alias`.

  * ##### keyword-onlyname: str | None

    Name of the request queue to open or create (persists across Actor runs). Mutually exclusive with `id` and `alias`.

  * ##### keyword-onlyalias: str | None

    Alias for the request queue (scoped to current Actor run, creates unnamed storage). Mutually exclusive with `id` and `name`.

  * ##### keyword-onlyconfiguration: [Configuration](https://docs.apify.com/sdk/python/sdk/python/reference/class/Configuration.md)

    Configuration object containing API credentials (`token`, `api_base_url`) and optionally a `default_request_queue_id` for fallback when no identifier is provided.

  * ##### optionalkeyword-onlyaccess: Literal\[single, shared] = <!-- -->'single'

    Access mode controlling the client's behavior:

    * `single`: Optimized for single-consumer scenarios (lower API usage, better performance).
    * `shared`: Optimized for multi-consumer scenarios (more API calls, guaranteed consistency).

  #### Returns [ApifyRequestQueueClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md)

### [**](#purge)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_client.py#L157)purge

* **async **purge**(): None

- #### Returns None

### [**](#reclaim_request)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_request_queue_client.py#L189)reclaim\_request

* **async **reclaim\_request**(request, \*, forefront): ProcessedRequest | None

- #### Parameters

  * ##### request: Request
  * ##### optionalkeyword-onlyforefront: bool = <!-- -->False

  #### Returns ProcessedRequest | None
