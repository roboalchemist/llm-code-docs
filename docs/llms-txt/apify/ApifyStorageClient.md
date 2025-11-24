# Source: https://docs.apify.com/sdk/python/reference/class/ApifyStorageClient.md

# ApifyStorageClient<!-- -->

Apify platform implementation of the storage client.

This storage client provides access to datasets, key-value stores, and request queues that persist data to the Apify platform. Each storage type is implemented with its own specific Apify client that stores data in the cloud, making it accessible from anywhere.

The communication with the Apify platform is handled via the Apify API client for Python, which is an HTTP API wrapper. For maximum efficiency and performance of the storage clients, various caching mechanisms are used to minimize the number of API calls made to the Apify platform. Data can be inspected and manipulated through the Apify console web interface or via the Apify API.

The request queue client supports two access modes controlled by the `request_queue_access` parameter:

### Single mode

The `single` mode is optimized for scenarios with only one consumer. It minimizes API calls, making it faster and more cost-efficient compared to the `shared` mode. This option is ideal when a single Actor is responsible for consuming the entire request queue. Using multiple consumers simultaneously may lead to inconsistencies or unexpected behavior.

In this mode, multiple producers can safely add new requests, but forefront requests may not be processed immediately, as the client relies on local head estimation instead of frequent forefront fetching. Requests can also be added or marked as handled by other clients, but they must not be deleted or modified, since such changes would not be reflected in the local cache. If a request is already fully cached locally, marking it as handled by another client will be ignored by this client. This does not cause errors but can occasionally result in reprocessing a request that was already handled elsewhere. If the request was not yet cached locally, marking it as handled poses no issue.

### Shared mode

The `shared` mode is designed for scenarios with multiple concurrent consumers. It ensures proper synchronization and consistency across clients, at the cost of higher API usage and slightly worse performance. This mode is safe for concurrent access from multiple processes, including Actors running in parallel on the Apify platform. It should be used when multiple consumers need to process requests from the same queue simultaneously.

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyStorageClient.md#__init__)
* [**create\_dataset\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyStorageClient.md#create_dataset_client)
* [**create\_kvs\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyStorageClient.md#create_kvs_client)
* [**create\_rq\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyStorageClient.md#create_rq_client)
* [**get\_storage\_client\_cache\_key](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyStorageClient.md#get_storage_client_cache_key)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_storage_client.py#L66)\_\_init\_\_

* ****\_\_init\_\_**(\*, request\_queue\_access): None

- Initialize a new instance.

  ***

  #### Parameters

  * ##### optionalkeyword-onlyrequest\_queue\_access: Literal\[single, shared] = <!-- -->'single'

    Defines how the request queue client behaves. Use `single` mode for a single consumer. It has fewer API calls, meaning better performance and lower costs. If you need multiple concurrent consumers use `shared` mode, but expect worse performance and higher costs due to the additional overhead.

  #### Returns None

### [**](#create_dataset_client)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_storage_client.py#L78)create\_dataset\_client

* **async **create\_dataset\_client**(\*, id, name, alias, configuration): [ApifyDatasetClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyDatasetClient.md)

- #### Parameters

  * ##### optionalkeyword-onlyid: str | None = <!-- -->None
  * ##### optionalkeyword-onlyname: str | None = <!-- -->None
  * ##### optionalkeyword-onlyalias: str | None = <!-- -->None
  * ##### optionalkeyword-onlyconfiguration: CrawleeConfiguration | None = <!-- -->None

  #### Returns [ApifyDatasetClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyDatasetClient.md)

### [**](#create_kvs_client)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_storage_client.py#L93)create\_kvs\_client

* **async **create\_kvs\_client**(\*, id, name, alias, configuration): [ApifyKeyValueStoreClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md)

- #### Parameters

  * ##### optionalkeyword-onlyid: str | None = <!-- -->None
  * ##### optionalkeyword-onlyname: str | None = <!-- -->None
  * ##### optionalkeyword-onlyalias: str | None = <!-- -->None
  * ##### optionalkeyword-onlyconfiguration: CrawleeConfiguration | None = <!-- -->None

  #### Returns [ApifyKeyValueStoreClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyKeyValueStoreClient.md)

### [**](#create_rq_client)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_storage_client.py#L108)create\_rq\_client

* **async **create\_rq\_client**(\*, id, name, alias, configuration): [ApifyRequestQueueClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md)

- #### Parameters

  * ##### optionalkeyword-onlyid: str | None = <!-- -->None
  * ##### optionalkeyword-onlyname: str | None = <!-- -->None
  * ##### optionalkeyword-onlyalias: str | None = <!-- -->None
  * ##### optionalkeyword-onlyconfiguration: CrawleeConfiguration | None = <!-- -->None

  #### Returns [ApifyRequestQueueClient](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestQueueClient.md)

### [**](#get_storage_client_cache_key)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_storage_client.py#L125)get\_storage\_client\_cache\_key

* ****get\_storage\_client\_cache\_key**(configuration): Hashable

- #### Parameters

  * ##### configuration: CrawleeConfiguration

  #### Returns Hashable
