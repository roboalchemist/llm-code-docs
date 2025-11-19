# Source: https://docs.apify.com/sdk/python/reference/class/DatasetItemsListPage.md

# DatasetItemsListPage<!-- -->

Model for a single page of dataset items returned from a collection list method.

## Index[**](#Index)

### Properties

* [**count](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetItemsListPage.md#count)
* [**desc](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetItemsListPage.md#desc)
* [**items](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetItemsListPage.md#items)
* [**limit](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetItemsListPage.md#limit)
* [**model\_config](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetItemsListPage.md#model_config)
* [**offset](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetItemsListPage.md#offset)
* [**total](https://docs.apify.com/sdk/python/sdk/python/reference/class/DatasetItemsListPage.md#total)

## Properties<!-- -->[**](#Properties)

### [**](#count)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L115)count

**count: int

The number of objects returned on this page.

### [**](#desc)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L127)desc

**desc: bool

Indicates if the returned list is in descending order.

### [**](#items)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L130)items

**items: list\[dict]

The list of dataset items returned on this page.

### [**](#limit)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L121)limit

**limit: int

The maximum number of objects to return, as specified in the API call.

### [**](#model_config)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L113)model\_config

**model\_config: Undefined

### [**](#offset)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L118)offset

**offset: int

The starting position of the first object returned, as specified in the API call.

### [**](#total)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L124)total

**total: int

The total number of objects that match the criteria of the API call.
