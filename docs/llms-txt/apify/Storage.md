# Source: https://docs.apify.com/sdk/python/reference/class/Storage.md

# Storage<!-- -->

Base class for storages.

### Hierarchy

* *Storage*

  * [KeyValueStore](https://crawlee.dev/python/api/class/KeyValueStore)
  * [Dataset](https://crawlee.dev/python/api/class/Dataset)
  * [RequestQueue](https://crawlee.dev/python/api/class/RequestQueue)

## Index[**](#Index)

### Methods

* [](https://crawlee.dev/python/api/class/Storage#drop)
* [](https://crawlee.dev/python/api/class/Storage#get_metadata)
* [](https://crawlee.dev/python/api/class/Storage#open)
* [](https://crawlee.dev/python/api/class/Storage#purge)

### Properties

* [**id](https://docs.apify.com/sdk/python/sdk/python/reference/class/Storage.md#id)
* [**name](https://docs.apify.com/sdk/python/sdk/python/reference/class/Storage.md#name)

## Methods<!-- -->[**](#Methods)

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/crawlee/storages/_base.py#L57)

:

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/crawlee/storages/_base.py#L29)

:

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/crawlee/storages/_base.py#L34)

:

### [**](#undefined)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/crawlee/storages/_base.py#L61)

:

## Properties<!-- -->[**](#Properties)

### [**](#id)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storages/_base.py#L20)id

**id: str

Get the storage ID.

### [**](#name)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storages/_base.py#L25)name

**name: str | None

Get the storage name.
