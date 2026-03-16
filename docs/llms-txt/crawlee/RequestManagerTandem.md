# Source: https://crawlee.dev/js/api/core/class/RequestManagerTandem.md

# RequestManagerTandem<!-- -->

A request manager that combines a RequestList and a RequestQueue. It first reads requests from the RequestList and then, when needed, transfers them in batches to the RequestQueue.

### Implements

* [IRequestManager](https://crawlee.dev/js/api/core/interface/IRequestManager.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Methods

* [**\[asyncIterator\]](#\[asyncIterator])
* [**addRequest](#addRequest)
* [**addRequestsBatched](#addRequestsBatched)
* [**fetchNextRequest](#fetchNextRequest)
* [**getPendingCount](#getPendingCount)
* [**getTotalCount](#getTotalCount)
* [**handledCount](#handledCount)
* [**isEmpty](#isEmpty)
* [**isFinished](#isFinished)
* [**markRequestHandled](#markRequestHandled)
* [**reclaimRequest](#reclaimRequest)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_manager_tandem.ts#L27)constructor

* ****new RequestManagerTandem**(requestList, requestQueue): [RequestManagerTandem](https://crawlee.dev/js/api/core/class/RequestManagerTandem.md)

- #### Parameters

  * ##### requestList: [IRequestList](https://crawlee.dev/js/api/core/interface/IRequestList.md)
  * ##### requestQueue: [IRequestManager](https://crawlee.dev/js/api/core/interface/IRequestManager.md)

  #### Returns [RequestManagerTandem](https://crawlee.dev/js/api/core/class/RequestManagerTandem.md)

## Methods<!-- -->[**](#Methods)

### [**](#\[asyncIterator])[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_manager_tandem.ts#L122)\[asyncIterator]

* ****\[asyncIterator]**(): AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, void, unknown>

- Implementation of IRequestManager.\[asyncIterator]

  Can be used to iterate over the `RequestManager` instance in a `for await .. of` loop. Provides an alternative for the repeated use of `fetchNextRequest`.

  ***

  #### Returns AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, void, unknown>

### [**](#addRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_manager_tandem.ts#L150)addRequest

* ****addRequest**(requestLike, options): Promise\<RequestQueueOperationInfo>

- Implementation of IRequestManager.addRequest

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### requestLike: [Source](https://crawlee.dev/js/api/core.md#Source)
  * ##### optionaloptions: [RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)

  #### Returns Promise\<RequestQueueOperationInfo>

### [**](#addRequestsBatched)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_manager_tandem.ts#L157)addRequestsBatched

* ****addRequestsBatched**(requests, options): Promise<[AddRequestsBatchedResult](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedResult.md)>

- Implementation of IRequestManager.addRequestsBatched

  * **@inheritDoc**

  ***

  #### Parameters

  * ##### requests: [RequestsLike](https://crawlee.dev/js/api/core.md#RequestsLike)
  * ##### optionaloptions: [AddRequestsBatchedOptions](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedOptions.md)

  #### Returns Promise<[AddRequestsBatchedResult](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedResult.md)>

### [**](#fetchNextRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_manager_tandem.ts#L66)fetchNextRequest

* ****fetchNextRequest**\<T>(): Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<T>>

- Implementation of IRequestManager.fetchNextRequest

  Gets the next [Request](https://crawlee.dev/js/api/core/class/Request.md) to process.

  The function's `Promise` resolves to `null` if there are no more requests to process.

  ***

  #### Returns Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<T>>

### [**](#getPendingCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_manager_tandem.ts#L115)getPendingCount

* ****getPendingCount**(): number

- Implementation of IRequestManager.getPendingCount

  Get an offline approximation of the number of pending requests.

  ***

  #### Returns number

### [**](#getTotalCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_manager_tandem.ts#L108)getTotalCount

* ****getTotalCount**(): number

- Implementation of IRequestManager.getTotalCount

  Get the total number of requests known to the request manager.

  ***

  #### Returns number

### [**](#handledCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_manager_tandem.ts#L100)handledCount

* ****handledCount**(): Promise\<number>

- Implementation of IRequestManager.handledCount

  Returns number of handled requests.

  ***

  #### Returns Promise\<number>

### [**](#isEmpty)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_manager_tandem.ts#L92)isEmpty

* ****isEmpty**(): Promise\<boolean>

- Implementation of IRequestManager.isEmpty

  Resolves to `true` if the next call to [IRequestManager.fetchNextRequest](https://crawlee.dev/js/api/core/interface/IRequestManager.md#fetchNextRequest) function would return `null`, otherwise it resolves to `false`. Note that even if the provider is empty, there might be some pending requests currently being processed.

  ***

  #### Returns Promise\<boolean>

### [**](#isFinished)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_manager_tandem.ts#L84)isFinished

* ****isFinished**(): Promise\<boolean>

- Implementation of IRequestManager.isFinished

  Returns `true` if all requests were already handled and there are no more left.

  ***

  #### Returns Promise\<boolean>

### [**](#markRequestHandled)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_manager_tandem.ts#L133)markRequestHandled

* ****markRequestHandled**(request): Promise\<null | void | RequestQueueOperationInfo>

- Implementation of IRequestManager.markRequestHandled

  Marks request as handled after successful processing.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

  #### Returns Promise\<null | void | RequestQueueOperationInfo>

### [**](#reclaimRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_manager_tandem.ts#L140)reclaimRequest

* ****reclaimRequest**(request, options): Promise\<null | RequestQueueOperationInfo>

- Implementation of IRequestManager.reclaimRequest

  Reclaims request to the provider if its processing failed. The request will become available in the next `fetchNextRequest()`.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>
  * ##### optionaloptions: [RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)

  #### Returns Promise\<null | RequestQueueOperationInfo>
