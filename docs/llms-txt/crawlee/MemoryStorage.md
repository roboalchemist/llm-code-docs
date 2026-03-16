# Source: https://crawlee.dev/js/api/memory-storage/class/MemoryStorage.md

# MemoryStorage<!-- -->

Represents a storage capable of working with datasets, KV stores and request queues.

### Implements

* [StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**datasetClientsHandled](#datasetClientsHandled)
* [**datasetsDirectory](#datasetsDirectory)
* [**keyValueStoresDirectory](#keyValueStoresDirectory)
* [**keyValueStoresHandled](#keyValueStoresHandled)
* [**localDataDirectory](#localDataDirectory)
* [**persistStorage](#persistStorage)
* [**requestQueuesDirectory](#requestQueuesDirectory)
* [**requestQueuesHandled](#requestQueuesHandled)
* [**writeMetadata](#writeMetadata)

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

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L52)constructor

* ****new MemoryStorage**(options): [MemoryStorage](https://crawlee.dev/js/api/memory-storage/class/MemoryStorage.md)

- #### Parameters

  * ##### options: [MemoryStorageOptions](https://crawlee.dev/js/api/memory-storage/interface/MemoryStorageOptions.md) = <!-- -->{}

  #### Returns [MemoryStorage](https://crawlee.dev/js/api/memory-storage/class/MemoryStorage.md)

## Properties<!-- -->[**](#Properties)

### [**](#datasetClientsHandled)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L49)readonlydatasetClientsHandled

**datasetClientsHandled: DatasetClient\<Dictionary>\[] =

<!-- -->

\[]

### [**](#datasetsDirectory)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L42)readonlydatasetsDirectory

**datasetsDirectory: string

### [**](#keyValueStoresDirectory)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L43)readonlykeyValueStoresDirectory

**keyValueStoresDirectory: string

### [**](#keyValueStoresHandled)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L48)readonlykeyValueStoresHandled

**keyValueStoresHandled: KeyValueStoreClient\[] =

<!-- -->

\[]

### [**](#localDataDirectory)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L41)readonlylocalDataDirectory

**localDataDirectory: string

### [**](#persistStorage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L46)readonlypersistStorage

**persistStorage: boolean

### [**](#requestQueuesDirectory)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L44)readonlyrequestQueuesDirectory

**requestQueuesDirectory: string

### [**](#requestQueuesHandled)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L50)readonlyrequestQueuesHandled

**requestQueuesHandled: RequestQueueClient\[] =

<!-- -->

\[]

### [**](#writeMetadata)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L45)readonlywriteMetadata

**writeMetadata: boolean

## Methods<!-- -->[**](#Methods)

### [**](#dataset)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L93)dataset

* ****dataset**\<Data>(id): [DatasetClient](https://crawlee.dev/js/api/types/interface/DatasetClient.md)\<Data>

- Implementation of storage.StorageClient.dataset

  #### Parameters

  * ##### id: string

  #### Returns [DatasetClient](https://crawlee.dev/js/api/types/interface/DatasetClient.md)\<Data>

### [**](#datasets)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L86)datasets

* ****datasets**(): [DatasetCollectionClient](https://crawlee.dev/js/api/types/interface/DatasetCollectionClient.md)

- Implementation of storage.StorageClient.datasets

  #### Returns [DatasetCollectionClient](https://crawlee.dev/js/api/types/interface/DatasetCollectionClient.md)

### [**](#keyValueStore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L106)keyValueStore

* ****keyValueStore**(id): [KeyValueStoreClient](https://crawlee.dev/js/api/types/interface/KeyValueStoreClient.md)

- Implementation of storage.StorageClient.keyValueStore

  #### Parameters

  * ##### id: string

  #### Returns [KeyValueStoreClient](https://crawlee.dev/js/api/types/interface/KeyValueStoreClient.md)

### [**](#keyValueStores)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L99)keyValueStores

* ****keyValueStores**(): [KeyValueStoreCollectionClient](https://crawlee.dev/js/api/types/interface/KeyValueStoreCollectionClient.md)

- Implementation of storage.StorageClient.keyValueStores

  #### Returns [KeyValueStoreCollectionClient](https://crawlee.dev/js/api/types/interface/KeyValueStoreCollectionClient.md)

### [**](#purge)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L149)purge

* ****purge**(): Promise\<void>

- Implementation of storage.StorageClient.purge

  Cleans up the default storage directories before the run starts:

  * local directory containing the default dataset;
  * all records from the default key-value store in the local directory, except for the "INPUT" key;
  * local directory containing the default request queue.

  ***

  #### Returns Promise\<void>

### [**](#requestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L119)requestQueue

* ****requestQueue**(id, options): [RequestQueueClient](https://crawlee.dev/js/api/types/interface/RequestQueueClient.md)

- Implementation of storage.StorageClient.requestQueue

  #### Parameters

  * ##### id: string
  * ##### options: [RequestQueueOptions](https://crawlee.dev/js/api/types/interface/RequestQueueOptions.md) = <!-- -->{}

  #### Returns [RequestQueueClient](https://crawlee.dev/js/api/types/interface/RequestQueueClient.md)

### [**](#requestQueues)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L112)requestQueues

* ****requestQueues**(): [RequestQueueCollectionClient](https://crawlee.dev/js/api/types/interface/RequestQueueCollectionClient.md)

- Implementation of storage.StorageClient.requestQueues

  #### Returns [RequestQueueCollectionClient](https://crawlee.dev/js/api/types/interface/RequestQueueCollectionClient.md)

### [**](#setStatusMessage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L134)setStatusMessage

* ****setStatusMessage**(message, options): Promise\<void>

- Implementation of storage.StorageClient.setStatusMessage

  #### Parameters

  * ##### message: string
  * ##### options: [SetStatusMessageOptions](https://crawlee.dev/js/api/types/interface/SetStatusMessageOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#teardown)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/memory-storage/src/memory-storage.ts#L198)teardown

* ****teardown**(): Promise\<void>

- Implementation of storage.StorageClient.teardown

  This method should be called at the end of the process, to ensure all data is saved.

  ***

  #### Returns Promise\<void>
