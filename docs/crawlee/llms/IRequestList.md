# Source: https://crawlee.dev/js/api/core/interface/IRequestList.md

# IRequestList<!-- -->

Represents a static list of URLs to crawl.

### Implemented by

* [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md)
* [SitemapRequestList](https://crawlee.dev/js/api/core/class/SitemapRequestList.md)

## Index[**](#Index)

### Methods

* [**\[asyncIterator\]](#\[asyncIterator])
* [**fetchNextRequest](#fetchNextRequest)
* [**handledCount](#handledCount)
* [**isEmpty](#isEmpty)
* [**isFinished](#isFinished)
* [**length](#length)
* [**markRequestHandled](#markRequestHandled)
* [**persistState](#persistState)
* [**reclaimRequest](#reclaimRequest)

## Methods<!-- -->[**](#Methods)

### [**](#\[asyncIterator])[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L72)\[asyncIterator]

* ****\[asyncIterator]**(): AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, any, any>

- Can be used to iterate over the `RequestList` instance in a `for await .. of` loop. Provides an alternative for the repeated use of `fetchNextRequest`.

  ***

  #### Returns AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, any, any>

### [**](#fetchNextRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L66)fetchNextRequest

* ****fetchNextRequest**(): Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>

- Gets the next [Request](https://crawlee.dev/js/api/core/class/Request.md) to process. First, the function gets a request previously reclaimed using the [RequestList.reclaimRequest](https://crawlee.dev/js/api/core/class/RequestList.md#reclaimRequest) function, if there is any. Otherwise it gets the next request from sources.

  The function's `Promise` resolves to `null` if there are no more requests to process.

  ***

  #### Returns Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>

### [**](#handledCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L47)handledCount

* ****handledCount**(): number

- Returns number of handled requests.

  ***

  #### Returns number

### [**](#isEmpty)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L42)isEmpty

* ****isEmpty**(): Promise\<boolean>

- Resolves to `true` if the next call to [IRequestList.fetchNextRequest](https://crawlee.dev/js/api/core/interface/IRequestList.md#fetchNextRequest) function would return `null`, otherwise it resolves to `false`. Note that even if the list is empty, there might be some pending requests currently being processed.

  ***

  #### Returns Promise\<boolean>

### [**](#isFinished)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L35)isFinished

* ****isFinished**(): Promise\<boolean>

- Returns `true` if all requests were already handled and there are no more left.

  ***

  #### Returns Promise\<boolean>

### [**](#length)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L30)length

* ****length**(): number

- Returns the total number of unique requests present in the list.

  ***

  #### Returns number

### [**](#markRequestHandled)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L83)markRequestHandled

* ****markRequestHandled**(request): Promise\<void>

- Marks request as handled after successful processing.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

  #### Returns Promise\<void>

### [**](#persistState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L56)persistState

* ****persistState**(): Promise\<void>

- Persists the current state of the `IRequestList` into the default [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md). The state is persisted automatically in regular intervals, but calling this method manually is useful in cases where you want to have the most current state available after you pause or stop fetching its requests. For example after you pause or abort a crawl. Or just before a server migration.

  ***

  #### Returns Promise\<void>

### [**](#reclaimRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L78)reclaimRequest

* ****reclaimRequest**(request): Promise\<void>

- Reclaims request to the list if its processing failed. The request will become available in the next `this.fetchNextRequest()`.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

  #### Returns Promise\<void>
