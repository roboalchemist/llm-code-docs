# Source: https://crawlee.dev/js/api/types/interface/RequestQueueClient.md

# RequestQueueClient<!-- -->

## Index[**](#Index)

### Methods

* [**addRequest](#addRequest)
* [**batchAddRequests](#batchAddRequests)
* [**delete](#delete)
* [**deleteRequest](#deleteRequest)
* [**deleteRequestLock](#deleteRequestLock)
* [**get](#get)
* [**getRequest](#getRequest)
* [**listAndLockHead](#listAndLockHead)
* [**listHead](#listHead)
* [**prolongRequestLock](#prolongRequestLock)
* [**update](#update)
* [**updateRequest](#updateRequest)

## Methods<!-- -->[**](#Methods)

### [**](#addRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L308)addRequest

* ****addRequest**(request, options): Promise<[QueueOperationInfo](https://crawlee.dev/js/api/core/interface/QueueOperationInfo.md)>

- #### Parameters

  * ##### request: [RequestSchema](https://crawlee.dev/js/api/types/interface/RequestSchema.md)
  * ##### optionaloptions: [RequestOptions](https://crawlee.dev/js/api/types/interface/RequestOptions.md)

  #### Returns Promise<[QueueOperationInfo](https://crawlee.dev/js/api/core/interface/QueueOperationInfo.md)>

### [**](#batchAddRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L309)batchAddRequests

* ****batchAddRequests**(requests, options): Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

- #### Parameters

  * ##### requests: [RequestSchema](https://crawlee.dev/js/api/types/interface/RequestSchema.md)\[]
  * ##### optionaloptions: [RequestOptions](https://crawlee.dev/js/api/types/interface/RequestOptions.md)

  #### Returns Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

### [**](#delete)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L306)delete

* ****delete**(): Promise\<void>

- #### Returns Promise\<void>

### [**](#deleteRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L312)deleteRequest

* ****deleteRequest**(id): Promise\<unknown>

- #### Parameters

  * ##### id: string

  #### Returns Promise\<unknown>

### [**](#deleteRequestLock)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L315)deleteRequestLock

* ****deleteRequestLock**(id, options): Promise\<void>

- #### Parameters

  * ##### id: string
  * ##### optionaloptions: [DeleteRequestLockOptions](https://crawlee.dev/js/api/types/interface/DeleteRequestLockOptions.md)

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L304)get

* ****get**(): Promise\<undefined | [RequestQueueInfo](https://crawlee.dev/js/api/types/interface/RequestQueueInfo.md)>

- #### Returns Promise\<undefined | [RequestQueueInfo](https://crawlee.dev/js/api/types/interface/RequestQueueInfo.md)>

### [**](#getRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L310)getRequest

* ****getRequest**(id): Promise\<undefined | [RequestOptions](https://crawlee.dev/js/api/types/interface/RequestOptions.md)>

- #### Parameters

  * ##### id: string

  #### Returns Promise\<undefined | [RequestOptions](https://crawlee.dev/js/api/types/interface/RequestOptions.md)>

### [**](#listAndLockHead)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L313)listAndLockHead

* ****listAndLockHead**(options): Promise<[ListAndLockHeadResult](https://crawlee.dev/js/api/types/interface/ListAndLockHeadResult.md)>

- #### Parameters

  * ##### options: [ListAndLockOptions](https://crawlee.dev/js/api/types/interface/ListAndLockOptions.md)

  #### Returns Promise<[ListAndLockHeadResult](https://crawlee.dev/js/api/types/interface/ListAndLockHeadResult.md)>

### [**](#listHead)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L307)listHead

* ****listHead**(options): Promise<[QueueHead](https://crawlee.dev/js/api/types/interface/QueueHead.md)>

- #### Parameters

  * ##### optionaloptions: [ListOptions](https://crawlee.dev/js/api/types/interface/ListOptions.md)

  #### Returns Promise<[QueueHead](https://crawlee.dev/js/api/types/interface/QueueHead.md)>

### [**](#prolongRequestLock)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L314)prolongRequestLock

* ****prolongRequestLock**(id, options): Promise<[ProlongRequestLockResult](https://crawlee.dev/js/api/types/interface/ProlongRequestLockResult.md)>

- #### Parameters

  * ##### id: string
  * ##### options: [ProlongRequestLockOptions](https://crawlee.dev/js/api/types/interface/ProlongRequestLockOptions.md)

  #### Returns Promise<[ProlongRequestLockResult](https://crawlee.dev/js/api/types/interface/ProlongRequestLockResult.md)>

### [**](#update)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L305)update

* ****update**(newFields): Promise\<undefined | Partial<[RequestQueueInfo](https://crawlee.dev/js/api/types/interface/RequestQueueInfo.md)>>

- #### Parameters

  * ##### newFields: { name?<!-- -->: string }
    * ##### optionalname: string

  #### Returns Promise\<undefined | Partial<[RequestQueueInfo](https://crawlee.dev/js/api/types/interface/RequestQueueInfo.md)>>

### [**](#updateRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L311)updateRequest

* ****updateRequest**(request, options): Promise<[QueueOperationInfo](https://crawlee.dev/js/api/core/interface/QueueOperationInfo.md)>

- #### Parameters

  * ##### request: [UpdateRequestSchema](https://crawlee.dev/js/api/types/interface/UpdateRequestSchema.md)
  * ##### optionaloptions: [RequestOptions](https://crawlee.dev/js/api/types/interface/RequestOptions.md)

  #### Returns Promise<[QueueOperationInfo](https://crawlee.dev/js/api/core/interface/QueueOperationInfo.md)>
