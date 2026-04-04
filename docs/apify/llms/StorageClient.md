# Source: https://docs.apify.com/sdk/python/reference/class/StorageClient.md

# StorageClient<!-- -->

Base class for storage clients.

The `StorageClient` serves as an abstract base class that defines the interface for accessing Crawlee's storage types: datasets, key-value stores, and request queues. It provides methods to open clients for each of these storage types and handles common functionality.

Storage clients implementations can be provided for various backends (file system, memory, databases, various cloud providers, etc.) to support different use cases from development to production environments.

Each storage client implementation is responsible for ensuring proper initialization, data persistence (where applicable), and consistent access patterns across all storage types it supports.

### Hierarchy

* *StorageClient*

  * [SqlStorageClient](https://crawlee.dev/python/api/class/SqlStorageClient)
  * [FileSystemStorageClient](https://crawlee.dev/python/api/class/FileSystemStorageClient)
  * [MemoryStorageClient](https://crawlee.dev/python/api/class/MemoryStorageClient)
  * [RedisStorageClient](https://crawlee.dev/python/api/class/RedisStorageClient)

## Index[**](#Index)

### Methods

* [](https://crawlee.dev/python/api/class/StorageClient#create_dataset_client)
* [](https://crawlee.dev/python/api/class/StorageClient#create_kvs_client)
* [](https://crawlee.dev/python/api/class/StorageClient#create_rq_client)
* [**get\_rate\_limit\_errors](https://docs.apify.com/sdk/python/sdk/python/reference/class/StorageClient.md#get_rate_limit_errors)
* [](https://crawlee.dev/python/api/class/StorageClient#get_storage_client_cache_key)

## Methods<!-- -->[**](#Methods)

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/crawlee/storage_clients/_base/_storage_client.py#L42)

:

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/crawlee/storage_clients/_base/_storage_client.py#L53)

:

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/crawlee/storage_clients/_base/_storage_client.py#L64)

:

### [**](#get_rate_limit_errors)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/_base/_storage_client.py#L74)get\_rate\_limit\_errors

* ****get\_rate\_limit\_errors**(): dict\[int, int]

- Return statistics about rate limit errors encountered by the HTTP client in storage client.

  ***

  #### Returns dict\[int, int]

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/crawlee/storage_clients/_base/_storage_client.py#L33)

:
