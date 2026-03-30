# Source: https://crawlee.dev/js/api/types/interface/KeyValueStoreCollectionClient.md

# KeyValueStoreCollectionClient<!-- -->

Key-value store collection client.

## Index[**](#Index)

### Methods

* [**getOrCreate](#getOrCreate)
* [**list](#list)

## Methods<!-- -->[**](#Methods)

### [**](#getOrCreate)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L121)getOrCreate

* ****getOrCreate**(name): Promise<[KeyValueStoreInfo](https://crawlee.dev/js/api/types/interface/KeyValueStoreInfo.md)>

- #### Parameters

  * ##### optionalname: string

  #### Returns Promise<[KeyValueStoreInfo](https://crawlee.dev/js/api/types/interface/KeyValueStoreInfo.md)>

### [**](#list)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L120)list

* ****list**(): Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)<[KeyValueStoreInfo](https://crawlee.dev/js/api/types/interface/KeyValueStoreInfo.md)>>

- #### Returns Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)<[KeyValueStoreInfo](https://crawlee.dev/js/api/types/interface/KeyValueStoreInfo.md)>>
