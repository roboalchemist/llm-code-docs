# Source: https://docs.apify.com/sdk/python/reference/class/MemoryStorageClient.md

# MemoryStorageClient<!-- -->

Memory implementation of the storage client.

This storage client provides access to datasets, key-value stores, and request queues that store all data in memory using Python data structures (lists and dictionaries). No data is persisted between process runs, meaning all stored data is lost when the program terminates.

The memory implementation provides fast access to data but is limited by available memory and does not support data sharing across different processes. All storage operations happen entirely in memory with no disk operations.

The memory storage client is useful for testing and development environments, or short-lived crawler operations where persistence is not required.

### Hierarchy

* [StorageClient](https://crawlee.dev/python/api/class/StorageClient)
  * *MemoryStorageClient*

## Index[**](#Index)

### Methods

* [**create\_dataset\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/MemoryStorageClient.md#create_dataset_client)
* [**create\_kvs\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/MemoryStorageClient.md#create_kvs_client)
* [**create\_rq\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/MemoryStorageClient.md#create_rq_client)
* [**get\_rate\_limit\_errors](https://docs.apify.com/sdk/python/sdk/python/reference/class/MemoryStorageClient.md#get_rate_limit_errors)
* [**get\_storage\_client\_cache\_key](https://docs.apify.com/sdk/python/sdk/python/reference/class/MemoryStorageClient.md#get_storage_client_cache_key)

## Methods<!-- -->[**](#Methods)

### [**](#create_dataset_client)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/_memory/_storage_client.py#L31)create\_dataset\_client

* **async **create\_dataset\_client**(\*, id, name, alias, configuration): [DatasetClient](https://crawlee.dev/python/api/class/DatasetClient)

- Overrides [StorageClient.create\_dataset\_client](https://crawlee.dev/python/api/class/StorageClient#create_dataset_client)

  Create a dataset client.

  ***

  #### Parameters

  * ##### optionalkeyword-onlyid: str | None = <!-- -->None
  * ##### optionalkeyword-onlyname: str | None = <!-- -->None
  * ##### optionalkeyword-onlyalias: str | None = <!-- -->None
  * ##### optionalkeyword-onlyconfiguration: [Configuration](https://crawlee.dev/python/api/class/Configuration) | None = <!-- -->None

  #### Returns [DatasetClient](https://crawlee.dev/python/api/class/DatasetClient)

### [**](#create_kvs_client)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/_memory/_storage_client.py#L45)create\_kvs\_client

* **async **create\_kvs\_client**(\*, id, name, alias, configuration): [KeyValueStoreClient](https://crawlee.dev/python/api/class/KeyValueStoreClient)

- Overrides [StorageClient.create\_kvs\_client](https://crawlee.dev/python/api/class/StorageClient#create_kvs_client)

  Create a key-value store client.

  ***

  #### Parameters

  * ##### optionalkeyword-onlyid: str | None = <!-- -->None
  * ##### optionalkeyword-onlyname: str | None = <!-- -->None
  * ##### optionalkeyword-onlyalias: str | None = <!-- -->None
  * ##### optionalkeyword-onlyconfiguration: [Configuration](https://crawlee.dev/python/api/class/Configuration) | None = <!-- -->None

  #### Returns [KeyValueStoreClient](https://crawlee.dev/python/api/class/KeyValueStoreClient)

### [**](#create_rq_client)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/_memory/_storage_client.py#L59)create\_rq\_client

* **async **create\_rq\_client**(\*, id, name, alias, configuration): [RequestQueueClient](https://crawlee.dev/python/api/class/RequestQueueClient)

- Overrides [StorageClient.create\_rq\_client](https://crawlee.dev/python/api/class/StorageClient#create_rq_client)

  Create a request queue client.

  ***

  #### Parameters

  * ##### optionalkeyword-onlyid: str | None = <!-- -->None
  * ##### optionalkeyword-onlyname: str | None = <!-- -->None
  * ##### optionalkeyword-onlyalias: str | None = <!-- -->None
  * ##### optionalkeyword-onlyconfiguration: [Configuration](https://crawlee.dev/python/api/class/Configuration) | None = <!-- -->None

  #### Returns [RequestQueueClient](https://crawlee.dev/python/api/class/RequestQueueClient)

### [**](#get_rate_limit_errors)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/_base/_storage_client.py#L74)get\_rate\_limit\_errors

* ****get\_rate\_limit\_errors**(): dict\[int, int]

- Inherited from [StorageClient.get\_rate\_limit\_errors](https://crawlee.dev/python/api/class/StorageClient#get_rate_limit_errors)

  Return statistics about rate limit errors encountered by the HTTP client in storage client.

  ***

  #### Returns dict\[int, int]

### [**](#get_storage_client_cache_key)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/_base/_storage_client.py#L33)get\_storage\_client\_cache\_key

* ****get\_storage\_client\_cache\_key**(configuration): Hashable

- Inherited from [StorageClient.get\_storage\_client\_cache\_key](https://crawlee.dev/python/api/class/StorageClient#get_storage_client_cache_key)

  Return a cache key that can differentiate between different storages of this and other clients.

  Can be based on configuration or on the client itself. By default, returns a module and name of the client class.

  ***

  #### Parameters

  * ##### configuration: [Configuration](https://crawlee.dev/python/api/class/Configuration)

  #### Returns Hashable
