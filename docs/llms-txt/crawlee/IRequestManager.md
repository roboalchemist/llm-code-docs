# Source: https://crawlee.dev/js/api/core/interface/IRequestManager.md

# IRequestManager<!-- -->

Represents a provider of requests/URLs to crawl.

### Implemented by

* [RequestManagerTandem](https://crawlee.dev/js/api/core/class/RequestManagerTandem.md)
* [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)

## Index[**](#Index)

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

## Methods<!-- -->[**](#Methods)

### [**](#\[asyncIterator])[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L84)\[asyncIterator]

* ****\[asyncIterator]**(): AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, any, any>

- Can be used to iterate over the `RequestManager` instance in a `for await .. of` loop. Provides an alternative for the repeated use of `fetchNextRequest`.

  ***

  #### Returns AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, any, any>

### [**](#addRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L97)addRequest

* ****addRequest**(requestLike, options): Promise\<RequestQueueOperationInfo>

- #### Parameters

  * ##### requestLike: [Source](https://crawlee.dev/js/api/core.md#Source)
  * ##### optionaloptions: [RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)

  #### Returns Promise\<RequestQueueOperationInfo>

### [**](#addRequestsBatched)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L99)addRequestsBatched

* ****addRequestsBatched**(requests, options): Promise<[AddRequestsBatchedResult](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedResult.md)>

- #### Parameters

  * ##### requests: [RequestsLike](https://crawlee.dev/js/api/core.md#RequestsLike)
  * ##### optionaloptions: [AddRequestsBatchedOptions](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedOptions.md)

  #### Returns Promise<[AddRequestsBatchedResult](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedResult.md)>

### [**](#fetchNextRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L78)fetchNextRequest

* ****fetchNextRequest**\<T>(): Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<T>>

- Gets the next [Request](https://crawlee.dev/js/api/core/class/Request.md) to process.

  The function's `Promise` resolves to `null` if there are no more requests to process.

  ***

  #### Returns Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<T>>

### [**](#getPendingCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L70)getPendingCount

* ****getPendingCount**(): number

- Get an offline approximation of the number of pending requests.

  ***

  #### Returns number

### [**](#getTotalCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L65)getTotalCount

* ****getTotalCount**(): number

- Get the total number of requests known to the request manager.

  ***

  #### Returns number

### [**](#handledCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L60)handledCount

* ****handledCount**(): Promise\<number>

- Returns number of handled requests.

  ***

  #### Returns Promise\<number>

### [**](#isEmpty)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L55)isEmpty

* ****isEmpty**(): Promise\<boolean>

- Resolves to `true` if the next call to [IRequestManager.fetchNextRequest](https://crawlee.dev/js/api/core/interface/IRequestManager.md#fetchNextRequest) function would return `null`, otherwise it resolves to `false`. Note that even if the provider is empty, there might be some pending requests currently being processed.

  ***

  #### Returns Promise\<boolean>

### [**](#isFinished)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L48)isFinished

* ****isFinished**(): Promise\<boolean>

- Returns `true` if all requests were already handled and there are no more left.

  ***

  #### Returns Promise\<boolean>

### [**](#markRequestHandled)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L89)markRequestHandled

* ****markRequestHandled**(request): Promise\<null | void | RequestQueueOperationInfo>

- Marks request as handled after successful processing.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

  #### Returns Promise\<null | void | RequestQueueOperationInfo>

### [**](#reclaimRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L95)reclaimRequest

* ****reclaimRequest**(request, options): Promise\<null | RequestQueueOperationInfo>

- Reclaims request to the provider if its processing failed. The request will become available in the next `fetchNextRequest()`.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>
  * ##### optionaloptions: [RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)

  #### Returns Promise\<null | RequestQueueOperationInfo>
