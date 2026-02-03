# Source: https://docs.apify.com/api/client/python/reference/class/ListPage.md

# ListPage<!-- -->

A single page of items returned from a list() method.

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md#__init__)

### Properties

* [**count](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md#count)
* [**desc](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md#desc)
* [**items](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md#items)
* [**limit](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md#limit)
* [**offset](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md#offset)
* [**total](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md#total)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/_types.py#L34)\_\_init\_\_

* ****\_\_init\_\_**(data): None

- Initialize a ListPage instance from the API response data.

  ***

  #### Parameters

  * ##### data: dict

  #### Returns None

## Properties<!-- -->[**](#Properties)

### [**](#count)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/_types.py#L19)count

**count: int

Count of the returned objects on this page.

### [**](#desc)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/_types.py#L31)desc

**desc: bool

Whether the listing is descending or not.

### [**](#items)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/_types.py#L16)items

**items: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[[T](https://docs.apify.com/api/client/python/api/client/python/reference.md#T)]

List of returned objects on this page.

### [**](#limit)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/_types.py#L25)limit

**limit: int

The offset of the first object specified in the API call

### [**](#offset)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/_types.py#L22)offset

**offset: int

The limit on the number of returned objects offset specified in the API call.

### [**](#total)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/_types.py#L28)total

**total: int

Total number of objects matching the API call criteria.
