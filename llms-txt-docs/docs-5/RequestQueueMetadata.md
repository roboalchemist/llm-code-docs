# Source: https://docs.apify.com/sdk/python/reference/class/RequestQueueMetadata.md

# RequestQueueMetadata<!-- -->

Model for a request queue metadata.

### Hierarchy

* [StorageMetadata](https://crawlee.dev/python/api/class/StorageMetadata)
  * *RequestQueueMetadata*

## Index[**](#Index)

### Properties

* [**accessed\_at](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueMetadata.md#accessed_at)
* [**created\_at](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueMetadata.md#created_at)
* [**had\_multiple\_clients](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueMetadata.md#had_multiple_clients)
* [**handled\_request\_count](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueMetadata.md#handled_request_count)
* [**id](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueMetadata.md#id)
* [**model\_config](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueMetadata.md#model_config)
* [**modified\_at](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueMetadata.md#modified_at)
* [**name](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueMetadata.md#name)
* [**pending\_request\_count](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueMetadata.md#pending_request_count)
* [**total\_request\_count](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueMetadata.md#total_request_count)

## Properties<!-- -->[**](#Properties)

### [**](#accessed_at)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L31)accessed\_at

**accessed\_at: Annotated\[datetime, Field(alias='accessedAt')]

Inherited from [StorageMetadata.accessed\_at](https://crawlee.dev/python/api/class/StorageMetadata#accessed_at)

The timestamp when the storage was last accessed.

### [**](#created_at)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L34)created\_at

**created\_at: Annotated\[datetime, Field(alias='createdAt')]

Inherited from [StorageMetadata.created\_at](https://crawlee.dev/python/api/class/StorageMetadata#created_at)

The timestamp when the storage was created.

### [**](#had_multiple_clients)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L64)had\_multiple\_clients

**had\_multiple\_clients: bool

Indicates whether the queue has been accessed by multiple clients (consumers).

### [**](#handled_request_count)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L67)handled\_request\_count

**handled\_request\_count: int

The number of requests that have been handled from the queue.

### [**](#id)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L25)id

**id: Annotated\[str, Field(alias='id')]

Inherited from [StorageMetadata.id](https://crawlee.dev/python/api/class/StorageMetadata#id)

The unique identifier of the storage.

### [**](#model_config)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L62)model\_config

**model\_config: Undefined

Overrides [StorageMetadata.model\_config](https://crawlee.dev/python/api/class/StorageMetadata#model_config)

### [**](#modified_at)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L37)modified\_at

**modified\_at: Annotated\[datetime, Field(alias='modifiedAt')]

Inherited from [StorageMetadata.modified\_at](https://crawlee.dev/python/api/class/StorageMetadata#modified_at)

The timestamp when the storage was last modified.

### [**](#name)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L28)name

**name: Annotated\[str | None, Field(alias='name', default=None)]

Inherited from [StorageMetadata.name](https://crawlee.dev/python/api/class/StorageMetadata#name)

The name of the storage.

### [**](#pending_request_count)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L70)pending\_request\_count

**pending\_request\_count: int

The number of requests that are still pending in the queue.

### [**](#total_request_count)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L73)total\_request\_count

**total\_request\_count: int

The total number of requests that have been added to the queue.
