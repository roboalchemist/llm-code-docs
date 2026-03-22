# Source: https://crawlee.dev/js/api/types/interface/RequestQueueCollectionClient.md

# RequestQueueCollectionClient<!-- -->

Request queue collection client.

## Index[**](#Index)

### Methods

* [**getOrCreate](#getOrCreate)
* [**list](#list)

## Methods<!-- -->[**](#Methods)

### [**](#getOrCreate)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L214)getOrCreate

* ****getOrCreate**(name): Promise<[RequestQueueInfo](https://crawlee.dev/js/api/types/interface/RequestQueueInfo.md)>

- #### Parameters

  * ##### name: string

  #### Returns Promise<[RequestQueueInfo](https://crawlee.dev/js/api/types/interface/RequestQueueInfo.md)>

### [**](#list)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L213)list

* ****list**(): Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)<[RequestQueueInfo](https://crawlee.dev/js/api/types/interface/RequestQueueInfo.md)>>

- #### Returns Promise<[PaginatedList](https://crawlee.dev/js/api/types/interface/PaginatedList.md)<[RequestQueueInfo](https://crawlee.dev/js/api/types/interface/RequestQueueInfo.md)>>
