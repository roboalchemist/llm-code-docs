# Source: https://docs.apify.com/sdk/python/reference/class/KeyValueStoreRecordMetadata.md

# KeyValueStoreRecordMetadata<!-- -->

Model for a key-value store record metadata.

### Hierarchy

* *KeyValueStoreRecordMetadata*
  * [KeyValueStoreRecord](https://crawlee.dev/python/api/class/KeyValueStoreRecord)

## Index[**](#Index)

### Properties

* [**content\_type](https://docs.apify.com/sdk/python/sdk/python/reference/class/KeyValueStoreRecordMetadata.md#content_type)
* [**key](https://docs.apify.com/sdk/python/sdk/python/reference/class/KeyValueStoreRecordMetadata.md#key)
* [**model\_config](https://docs.apify.com/sdk/python/sdk/python/reference/class/KeyValueStoreRecordMetadata.md#model_config)
* [**size](https://docs.apify.com/sdk/python/sdk/python/reference/class/KeyValueStoreRecordMetadata.md#size)

## Properties<!-- -->[**](#Properties)

### [**](#content_type)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L89)content\_type

**content\_type: str

The MIME type of the record.

Describe the format and type of data stored in the record, following the MIME specification.

### [**](#key)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L83)key

**key: str

The key of the record.

A unique identifier for the record in the key-value store.

### [**](#model_config)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L81)model\_config

**model\_config: Undefined

### [**](#size)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L95)size

**size: int | None

The size of the record in bytes.
