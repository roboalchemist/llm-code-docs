# Source: https://docs.apify.com/sdk/python/reference/class/StorageMetadata.md

# StorageMetadata<!-- -->

Represents the base model for storage metadata.

It contains common fields shared across all specific storage types.

### Hierarchy

* *StorageMetadata*

  * [DatasetMetadata](https://crawlee.dev/python/api/class/DatasetMetadata)
  * [KeyValueStoreMetadata](https://crawlee.dev/python/api/class/KeyValueStoreMetadata)
  * [RequestQueueMetadata](https://crawlee.dev/python/api/class/RequestQueueMetadata)

## Index[**](#Index)

### Properties

* [**accessed\_at](https://docs.apify.com/sdk/python/sdk/python/reference/class/StorageMetadata.md#accessed_at)
* [**created\_at](https://docs.apify.com/sdk/python/sdk/python/reference/class/StorageMetadata.md#created_at)
* [**id](https://docs.apify.com/sdk/python/sdk/python/reference/class/StorageMetadata.md#id)
* [**model\_config](https://docs.apify.com/sdk/python/sdk/python/reference/class/StorageMetadata.md#model_config)
* [**modified\_at](https://docs.apify.com/sdk/python/sdk/python/reference/class/StorageMetadata.md#modified_at)
* [**name](https://docs.apify.com/sdk/python/sdk/python/reference/class/StorageMetadata.md#name)

## Properties<!-- -->[**](#Properties)

### [**](#accessed_at)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L31)accessed\_at

**accessed\_at: datetime

The timestamp when the storage was last accessed.

### [**](#created_at)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L34)created\_at

**created\_at: datetime

The timestamp when the storage was created.

### [**](#id)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L25)id

**id: str

The unique identifier of the storage.

### [**](#model_config)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L23)model\_config

**model\_config: Undefined

### [**](#modified_at)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L37)modified\_at

**modified\_at: datetime

The timestamp when the storage was last modified.

### [**](#name)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L28)name

**name: str | None

The name of the storage.
