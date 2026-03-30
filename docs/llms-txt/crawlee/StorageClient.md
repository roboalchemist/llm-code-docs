# Source: https://crawlee.dev/js/api/core/interface/StorageClient.md

# StorageClient<!-- -->

Represents a storage capable of working with datasets, KV stores and request queues.

### Implemented by

* [MemoryStorage](https://crawlee.dev/js/api/memory-storage/class/MemoryStorage.md)

## Index[**](#Index)

### Properties

* [**stats](#stats)

### Methods

* [**dataset](#dataset)
* [**datasets](#datasets)
* [**keyValueStore](#keyValueStore)
* [**keyValueStores](#keyValueStores)
* [**purge](#purge)
* [**requestQueue](#requestQueue)
* [**requestQueues](#requestQueues)
* [**setStatusMessage](#setStatusMessage)
* [**teardown](#teardown)

## Properties<!-- -->[**](#Properties)

### [**](#stats)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L341)optionalstats

**stats?

<!-- -->

: { rateLimitErrors: number\[] }

#### Type declaration

* ##### rateLimitErrors: number\[]

## Methods<!-- -->[**](#Methods)

### [**](#dataset)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L333)dataset

* ****dataset**(id): [DatasetClient](https://crawlee.dev/js/api/types/interface/DatasetClient.md)\<Dictionary>

- #### Parameters

  * ##### id: string

  #### Returns [DatasetClient](https://crawlee.dev/js/api/types/interface/DatasetClient.md)\<Dictionary>

### [**](#datasets)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L332)datasets

* ****datasets**(): [DatasetCollectionClient](https://crawlee.dev/js/api/types/interface/DatasetCollectionClient.md)

- #### Returns [DatasetCollectionClient](https://crawlee.dev/js/api/types/interface/DatasetCollectionClient.md)

### [**](#keyValueStore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L335)keyValueStore

* ****keyValueStore**(id): [KeyValueStoreClient](https://crawlee.dev/js/api/types/interface/KeyValueStoreClient.md)

- #### Parameters

  * ##### id: string

  #### Returns [KeyValueStoreClient](https://crawlee.dev/js/api/types/interface/KeyValueStoreClient.md)

### [**](#keyValueStores)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L334)keyValueStores

* ****keyValueStores**(): [KeyValueStoreCollectionClient](https://crawlee.dev/js/api/types/interface/KeyValueStoreCollectionClient.md)

- #### Returns [KeyValueStoreCollectionClient](https://crawlee.dev/js/api/types/interface/KeyValueStoreCollectionClient.md)

### [**](#purge)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L338)optionalpurge

* ****purge**(): Promise\<void>

- #### Returns Promise\<void>

### [**](#requestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L337)requestQueue

* ****requestQueue**(id, options): [RequestQueueClient](https://crawlee.dev/js/api/types/interface/RequestQueueClient.md)

- #### Parameters

  * ##### id: string
  * ##### optionaloptions: [RequestQueueOptions](https://crawlee.dev/js/api/types/interface/RequestQueueOptions.md)

  #### Returns [RequestQueueClient](https://crawlee.dev/js/api/types/interface/RequestQueueClient.md)

### [**](#requestQueues)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L336)requestQueues

* ****requestQueues**(): [RequestQueueCollectionClient](https://crawlee.dev/js/api/types/interface/RequestQueueCollectionClient.md)

- #### Returns [RequestQueueCollectionClient](https://crawlee.dev/js/api/types/interface/RequestQueueCollectionClient.md)

### [**](#setStatusMessage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L340)optionalsetStatusMessage

* ****setStatusMessage**(message, options): Promise\<void>

- #### Parameters

  * ##### message: string
  * ##### optionaloptions: [SetStatusMessageOptions](https://crawlee.dev/js/api/types/interface/SetStatusMessageOptions.md)

  #### Returns Promise\<void>

### [**](#teardown)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L339)optionalteardown

* ****teardown**(): Promise\<void>

- #### Returns Promise\<void>
