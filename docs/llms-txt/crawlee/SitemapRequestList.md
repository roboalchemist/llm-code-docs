# Source: https://crawlee.dev/js/api/core/class/SitemapRequestList.md

# SitemapRequestList<!-- -->

A list of URLs to crawl parsed from a sitemap.

The loading of the sitemap is performed in the background so that crawling can start before the sitemap is fully loaded.

### Implements

* [IRequestList](https://crawlee.dev/js/api/core/interface/IRequestList.md)

## Index[**](#Index)

### Methods

* [**\[asyncIterator\]](#\[asyncIterator])
* [**fetchNextRequest](#fetchNextRequest)
* [**handledCount](#handledCount)
* [**isEmpty](#isEmpty)
* [**isFinished](#isFinished)
* [**isSitemapFullyLoaded](#isSitemapFullyLoaded)
* [**length](#length)
* [**markRequestHandled](#markRequestHandled)
* [**persistState](#persistState)
* [**reclaimRequest](#reclaimRequest)
* [**teardown](#teardown)
* [**open](#open)

## Methods<!-- -->[**](#Methods)

### [**](#\[asyncIterator])[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L574)\[asyncIterator]

* ****\[asyncIterator]**(): AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, void, unknown>

- Implementation of IRequestList.\[asyncIterator]

  Can be used to iterate over the `RequestList` instance in a `for await .. of` loop. Provides an alternative for the repeated use of `fetchNextRequest`.

  ***

  #### Returns AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, void, unknown>

### [**](#fetchNextRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L553)fetchNextRequest

* ****fetchNextRequest**(): Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>

- Implementation of IRequestList.fetchNextRequest

  Gets the next [Request](https://crawlee.dev/js/api/core/class/Request.md) to process. First, the function gets a request previously reclaimed using the [RequestList.reclaimRequest](https://crawlee.dev/js/api/core/class/RequestList.md#reclaimRequest) function, if there is any. Otherwise it gets the next request from sources.

  The function's `Promise` resolves to `null` if there are no more requests to process.

  ***

  #### Returns Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>

### [**](#handledCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L467)handledCount

* ****handledCount**(): number

- Implementation of IRequestList.handledCount

  Returns number of handled requests.

  ***

  #### Returns number

### [**](#isEmpty)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L460)isEmpty

* ****isEmpty**(): Promise\<boolean>

- Implementation of IRequestList.isEmpty

  Resolves to `true` if the next call to [IRequestList.fetchNextRequest](https://crawlee.dev/js/api/core/interface/IRequestList.md#fetchNextRequest) function would return `null`, otherwise it resolves to `false`. Note that even if the list is empty, there might be some pending requests currently being processed.

  ***

  #### Returns Promise\<boolean>

### [**](#isFinished)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L451)isFinished

* ****isFinished**(): Promise\<boolean>

- Implementation of IRequestList.isFinished

  Returns `true` if all requests were already handled and there are no more left.

  ***

  #### Returns Promise\<boolean>

### [**](#isSitemapFullyLoaded)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L358)isSitemapFullyLoaded

* ****isSitemapFullyLoaded**(): boolean

- Indicates whether the background processing of sitemap contents has successfully finished.

  If this is `false`, the background processing is either still in progress or was aborted.

  ***

  #### Returns boolean

### [**](#length)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L444)length

* ****length**(): number

- Implementation of IRequestList.length

  Returns the total number of unique requests present in the list.

  ***

  #### Returns number

### [**](#markRequestHandled)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L609)markRequestHandled

* ****markRequestHandled**(request): Promise\<void>

- Implementation of IRequestList.markRequestHandled

  Marks request as handled after successful processing.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

  #### Returns Promise\<void>

### [**](#persistState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L474)persistState

* ****persistState**(): Promise\<void>

- Implementation of IRequestList.persistState

  Persists the current state of the `IRequestList` into the default [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md). The state is persisted automatically in regular intervals, but calling this method manually is useful in cases where you want to have the most current state available after you pause or stop fetching its requests. For example after you pause or abort a crawl. Or just before a server migration.

  ***

  #### Returns Promise\<void>

### [**](#reclaimRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L586)reclaimRequest

* ****reclaimRequest**(request): Promise\<void>

- Implementation of IRequestList.reclaimRequest

  Reclaims request to the list if its processing failed. The request will become available in the next `this.fetchNextRequest()`.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

  #### Returns Promise\<void>

### [**](#teardown)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L597)teardown

* ****teardown**(): Promise\<void>

- Aborts the internal sitemap loading, stops the processing of the sitemap contents and drops all the pending URLs.

  Calling `fetchNextRequest()` after this method will always return `null`.

  ***

  #### Returns Promise\<void>

### [**](#open)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L416)staticopen

* ****open**(options): Promise<[SitemapRequestList](https://crawlee.dev/js/api/core/class/SitemapRequestList.md)>

- Open a sitemap and start processing it.

  Resolves to a new instance of `SitemapRequestList`, which **might not be fully loaded yet** - i.e. the sitemap might still be loading in the background.

  Track the loading progress using the `isSitemapFullyLoaded` property.

  ***

  #### Parameters

  * ##### options: [SitemapRequestListOptions](https://crawlee.dev/js/api/core/interface/SitemapRequestListOptions.md)

  #### Returns Promise<[SitemapRequestList](https://crawlee.dev/js/api/core/class/SitemapRequestList.md)>
