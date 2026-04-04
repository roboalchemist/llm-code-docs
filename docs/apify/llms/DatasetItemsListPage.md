# Source: https://docs.apify.com/sdk/python/reference/class/DatasetItemsListPage.md

# DatasetItemsListPage<!-- -->

Model for a single page of dataset items returned from a collection list method.

## Index[**](#Index)

### Properties

* [**count](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetItemsListPage.md#count)
* [**desc](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetItemsListPage.md#desc)
* [**limit](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetItemsListPage.md#limit)
* [**model\_config](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetItemsListPage.md#model_config)
* [**offset](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetItemsListPage.md#offset)
* [**total](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetItemsListPage.md#total)

## Properties<!-- -->[**](#Properties)

### [**](#count)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L115)count

**count: int

The number of objects returned on this page.

### [**](#desc)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L127)desc

**desc: bool

Indicates if the returned list is in descending order.

### [**](#limit)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L121)limit

**limit: int

The maximum number of objects to return, as specified in the API call.

### [**](#model_config)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L113)model\_config

**model\_config: Undefined

### [**](#offset)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L118)offset

**offset: int

The starting position of the first object returned, as specified in the API call.

### [**](#total)[**](https://github.com/apify/crawlee-python/blob/3e08b24571bbd21f25523e9aa81bc31ba308628d//src/crawlee/storage_clients/models.py#L124)total

**total: int

The total number of objects that match the criteria of the API call.
