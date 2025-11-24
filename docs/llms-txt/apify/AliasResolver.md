# Source: https://docs.apify.com/sdk/python/reference/class/AliasResolver.md

# AliasResolver<!-- -->

Class for handling aliases.

The purpose of this is class is to ensure that alias storages are created with correct id. This is achieved by using default kvs as a storage for global mapping of aliases to storage ids. Same mapping is also kept in memory to avoid unnecessary calls to API and also have limited support of alias storages when not running on Apify platform. When on Apify platform, the storages created with alias are accessible by the same alias even after migration or reboot.

## Index[**](#Index)

### Methods

* [**\_\_aenter\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/AliasResolver.md#__aenter__)
* [**\_\_aexit\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/AliasResolver.md#__aexit__)
* [**\_\_init\_\_](https://docs.apify.com/sdk/python/sdk/python/reference/class/AliasResolver.md#__init__)
* [**resolve\_id](https://docs.apify.com/sdk/python/sdk/python/reference/class/AliasResolver.md#resolve_id)
* [**store\_mapping](https://docs.apify.com/sdk/python/sdk/python/reference/class/AliasResolver.md#store_mapping)

## Methods<!-- -->[**](#Methods)

### [**](#__aenter__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_alias_resolving.py#L144)\_\_aenter\_\_

* **async **\_\_aenter\_\_**(): [AliasResolver](https://docs.apify.com/sdk/python/sdk/python/reference/class/AliasResolver.md)

- Context manager to prevent race condition in alias creation.

  ***

  #### Returns [AliasResolver](https://docs.apify.com/sdk/python/sdk/python/reference/class/AliasResolver.md)

### [**](#__aexit__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_alias_resolving.py#L150)\_\_aexit\_\_

* **async **\_\_aexit\_\_**(exc\_type, exc\_value, exc\_traceback): None

- #### Parameters

  * ##### exc\_type: type\[BaseException] | None
  * ##### exc\_value: BaseException | None
  * ##### exc\_traceback: TracebackType | None

  #### Returns None

### [**](#__init__)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_alias_resolving.py#L133)\_\_init\_\_

* ****\_\_init\_\_**(storage\_type, alias, configuration): None

- #### Parameters

  * ##### storage\_type: Literal\[Dataset, KeyValueStore, RequestQueue]
  * ##### alias: str
  * ##### configuration: [Configuration](https://docs.apify.com/sdk/python/sdk/python/reference/class/Configuration.md)

  #### Returns None

### [**](#resolve_id)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_alias_resolving.py#L198)resolve\_id

* **async **resolve\_id**(): str | None

- Get id of the aliased storage.

  ***

  #### Returns str | None

### [**](#store_mapping)[**](https://github.com/apify/apify-sdk-python/blob/f050b2684cf6d5e88bafe381599a3653d220ec14//src/apify/storage_clients/_apify/_alias_resolving.py#L206)store\_mapping

* **async **store\_mapping**(storage\_id): None

- Add alias and related storage id to the mapping in default kvs and local in-memory mapping.

  ***

  #### Parameters

  * ##### storage\_id: str

  #### Returns None
