# Source: https://docs.apify.com/sdk/python/reference/class/DatasetMetadata.md

# DatasetMetadata<!-- -->

Model for a dataset metadata.

### Hierarchy

* [StorageMetadata](https://crawlee.dev/python/api/class/StorageMetadata)
  * *DatasetMetadata*

## Index[**](#Index)

### Properties

* [**accessed\_at](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetMetadata.md#accessed_at)
* [**created\_at](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetMetadata.md#created_at)
* [**id](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetMetadata.md#id)
* [**item\_count](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetMetadata.md#item_count)
* [**model\_config](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetMetadata.md#model_config)
* [**modified\_at](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetMetadata.md#modified_at)
* [**name](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetMetadata.md#name)

## Properties<!-- -->[**](#Properties)

### [**](#accessed_at)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L31)accessed\_at

**accessed\_at: Annotated\[datetime, Field(alias='accessedAt')]

Inherited from [StorageMetadata.accessed\_at](https://crawlee.dev/python/api/class/StorageMetadata#accessed_at)

The timestamp when the storage was last accessed.

### [**](#created_at)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L34)created\_at

**created\_at: Annotated\[datetime, Field(alias='createdAt')]

Inherited from [StorageMetadata.created\_at](https://crawlee.dev/python/api/class/StorageMetadata#created_at)

The timestamp when the storage was created.

### [**](#id)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L25)id

**id: Annotated\[str, Field(alias='id')]

Inherited from [StorageMetadata.id](https://crawlee.dev/python/api/class/StorageMetadata#id)

The unique identifier of the storage.

### [**](#item_count)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L47)item\_count

**item\_count: int

The number of items in the dataset.

### [**](#model_config)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L45)model\_config

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
