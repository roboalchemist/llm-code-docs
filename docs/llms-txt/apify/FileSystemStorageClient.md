# Source: https://docs.apify.com/sdk/python/reference/class/FileSystemStorageClient.md

# FileSystemStorageClient<!-- -->

File system implementation of the storage client.

This storage client provides access to datasets, key-value stores, and request queues that persist data to the local file system. Each storage type is implemented with its own specific file system client that stores data in a structured directory hierarchy.

Data is stored in JSON format in predictable file paths, making it easy to inspect and manipulate the stored data outside of the Crawlee application if needed.

All data persists between program runs but is limited to access from the local machine where the files are stored.

Warning: This storage client is not safe for concurrent access from multiple crawler processes. Use it only when running a single crawler process at a time.

### Hierarchy

* [StorageClient](https://crawlee.dev/python/api/class/StorageClient)
  * *FileSystemStorageClient*

## Index[**](#Index)

### Methods

* [**create\_dataset\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/FileSystemStorageClient.md#create_dataset_client)
* [**create\_kvs\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/FileSystemStorageClient.md#create_kvs_client)
* [**create\_rq\_client](https://docs.apify.com/sdk/python/sdk/python/reference/class/FileSystemStorageClient.md#create_rq_client)
* [**get\_rate\_limit\_errors](https://docs.apify.com/sdk/python/sdk/python/reference/class/FileSystemStorageClient.md#get_rate_limit_errors)
* [**get\_storage\_client\_cache\_key](https://docs.apify.com/sdk/python/sdk/python/reference/class/FileSystemStorageClient.md#get_storage_client_cache_key)

## Methods<!-- -->[**](#Methods)

### [**](#create_dataset_client)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/_file_system/_storage_client.py#L43)create\_dataset\_client

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

### [**](#create_kvs_client)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/_file_system/_storage_client.py#L57)create\_kvs\_client

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

### [**](#create_rq_client)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/_file_system/_storage_client.py#L71)create\_rq\_client

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

### [**](#get_storage_client_cache_key)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/_file_system/_storage_client.py#L38)get\_storage\_client\_cache\_key

* ****get\_storage\_client\_cache\_key**(configuration): Hashable

- Overrides [StorageClient.get\_storage\_client\_cache\_key](https://crawlee.dev/python/api/class/StorageClient#get_storage_client_cache_key)

  Return a cache key that can differentiate between different storages of this and other clients.

  Can be based on configuration or on the client itself. By default, returns a module and name of the client class.

  ***

  #### Parameters

  * ##### configuration: [Configuration](https://crawlee.dev/python/api/class/Configuration)

  #### Returns Hashable
