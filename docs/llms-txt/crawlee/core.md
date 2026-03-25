# Source: https://crawlee.dev/js/api/core.md

# @crawlee/core<!-- -->

Core set of classes required for Crawlee.

The [`crawlee`](https://www.npmjs.com/package/crawlee) package consists of several smaller packages, released separately under `@crawlee` namespace:

* [`@crawlee/core`](https://crawlee.dev/js/api/core.md): the base for all the crawler implementations, also contains things like `Request`, `RequestQueue`, `RequestList` or `Dataset` classes
* [`@crawlee/cheerio`](https://crawlee.dev/js/api/cheerio-crawler.md): exports `CheerioCrawler`
* [`@crawlee/playwright`](https://crawlee.dev/js/api/playwright-crawler.md): exports `PlaywrightCrawler`
* [`@crawlee/puppeteer`](https://crawlee.dev/js/api/puppeteer-crawler.md): exports `PuppeteerCrawler`
* [`@crawlee/linkedom`](https://crawlee.dev/js/api/linkedom-crawler.md): exports `LinkeDOMCrawler`
* [`@crawlee/jsdom`](https://crawlee.dev/js/api/jsdom-crawler.md): exports `JSDOMCrawler`
* [`@crawlee/basic`](https://crawlee.dev/js/api/basic-crawler.md): exports `BasicCrawler`
* [`@crawlee/http`](https://crawlee.dev/js/api/http-crawler.md): exports `HttpCrawler` (which is used for creating [`@crawlee/jsdom`](https://crawlee.dev/js/api/jsdom-crawler.md) and [`@crawlee/cheerio`](https://crawlee.dev/js/api/cheerio-crawler.md))
* [`@crawlee/browser`](https://crawlee.dev/js/api/browser-crawler.md): exports `BrowserCrawler` (which is used for creating [`@crawlee/playwright`](https://crawlee.dev/js/api/playwright-crawler.md) and [`@crawlee/puppeteer`](https://crawlee.dev/js/api/puppeteer-crawler.md))
* [`@crawlee/memory-storage`](https://crawlee.dev/js/api/memory-storage.md): [`@apify/storage-local`](https://npmjs.com/package/@apify/storage-local) alternative
* [`@crawlee/browser-pool`](https://crawlee.dev/js/api/browser-pool.md): previously [`browser-pool`](https://npmjs.com/package/browser-pool) package
* [`@crawlee/utils`](https://crawlee.dev/js/api/utils.md): utility methods
* [`@crawlee/types`](https://crawlee.dev/js/api/types.md): holds TS interfaces mainly about the [`StorageClient`](https://crawlee.dev/js/api/core/interface/StorageClient.md)

## Installing Crawlee[​](#installing-crawlee "Direct link to Installing Crawlee")

Most of the Crawlee packages are extending and reexporting each other, so it's enough to install just the one you plan on using, e.g. `@crawlee/playwright` if you plan on using `playwright` - it already contains everything from the `@crawlee/browser` package, which includes everything from `@crawlee/basic`, which includes everything from `@crawlee/core`.

If we don't care much about additional code being pulled in, we can just use the `crawlee` meta-package, which contains (re-exports) most of the `@crawlee/*` packages, and therefore contains all the crawler classes.

```
npm install crawlee
```

Or if all we need is cheerio support, we can install only `@crawlee/cheerio`.

```
npm install @crawlee/cheerio
```

When using `playwright` or `puppeteer`, we still need to install those dependencies explicitly - this allows the users to be in control of which version will be used.

```
npm install crawlee playwright
# or npm install @crawlee/playwright playwright
```

Alternatively we can also use the `crawlee` meta-package which contains (re-exports) most of the `@crawlee/*` packages, and therefore contains all the crawler classes.

> Sometimes you might want to use some utility methods from `@crawlee/utils`, so you might want to install that as well. This package contains some utilities that were previously available under `Apify.utils`. Browser related utilities can be also found in the crawler packages (e.g. `@crawlee/playwright`).

## Index[**](#Index)

### Crawlers

* [**Statistics](https://crawlee.dev/js/api/core/class/Statistics.md)

### Result Stores

* [**Dataset](https://crawlee.dev/js/api/core/class/Dataset.md)
* [**KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)

### Scaling

* [**AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md)
* [**ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md)
* [**Session](https://crawlee.dev/js/api/core/class/Session.md)
* [**SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md)
* [**Snapshotter](https://crawlee.dev/js/api/core/class/Snapshotter.md)
* [**SystemStatus](https://crawlee.dev/js/api/core/class/SystemStatus.md)

### Sources

* [**PseudoUrl](https://crawlee.dev/js/api/core/class/PseudoUrl.md)
* [**Request](https://crawlee.dev/js/api/core/class/Request.md)
* [**RequestList](https://crawlee.dev/js/api/core/class/RequestList.md)
* [**RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md)
* [**RequestQueueV1](https://crawlee.dev/js/api/core/class/RequestQueueV1.md)

### Other

* [**RequestQueueV2](https://crawlee.dev/js/api/core.md#RequestQueueV2)
* [**EnqueueStrategy](https://crawlee.dev/js/api/core/enum/EnqueueStrategy.md)
* [**EventType](https://crawlee.dev/js/api/core/enum/EventType.md)
* [**LogLevel](https://crawlee.dev/js/api/core/enum/LogLevel.md)
* [**RequestState](https://crawlee.dev/js/api/core/enum/RequestState.md)
* [**Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)
* [**CriticalError](https://crawlee.dev/js/api/core/class/CriticalError.md)
* [**ErrorSnapshotter](https://crawlee.dev/js/api/core/class/ErrorSnapshotter.md)
* [**ErrorTracker](https://crawlee.dev/js/api/core/class/ErrorTracker.md)
* [**EventManager](https://crawlee.dev/js/api/core/class/EventManager.md)
* [**GotScrapingHttpClient](https://crawlee.dev/js/api/core/class/GotScrapingHttpClient.md)
* [**LocalEventManager](https://crawlee.dev/js/api/core/class/LocalEventManager.md)
* [**Log](https://crawlee.dev/js/api/core/class/Log.md)
* [**Logger](https://crawlee.dev/js/api/core/class/Logger.md)
* [**LoggerJson](https://crawlee.dev/js/api/core/class/LoggerJson.md)
* [**LoggerText](https://crawlee.dev/js/api/core/class/LoggerText.md)
* [**NonRetryableError](https://crawlee.dev/js/api/core/class/NonRetryableError.md)
* [**RecoverableState](https://crawlee.dev/js/api/core/class/RecoverableState.md)
* [**RequestHandlerResult](https://crawlee.dev/js/api/core/class/RequestHandlerResult.md)
* [**RequestManagerTandem](https://crawlee.dev/js/api/core/class/RequestManagerTandem.md)
* [**RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)
* [**RetryRequestError](https://crawlee.dev/js/api/core/class/RetryRequestError.md)
* [**Router](https://crawlee.dev/js/api/core/class/Router.md)
* [**SessionError](https://crawlee.dev/js/api/core/class/SessionError.md)
* [**SitemapRequestList](https://crawlee.dev/js/api/core/class/SitemapRequestList.md)
* [**AddRequestsBatchedOptions](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedOptions.md)
* [**AddRequestsBatchedResult](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedResult.md)
* [**AutoscaledPoolOptions](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md)
* [**BaseHttpClient](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md)
* [**BaseHttpResponseData](https://crawlee.dev/js/api/core/interface/BaseHttpResponseData.md)
* [**ClientInfo](https://crawlee.dev/js/api/core/interface/ClientInfo.md)
* [**ConfigurationOptions](https://crawlee.dev/js/api/core/interface/ConfigurationOptions.md)
* [**Cookie](https://crawlee.dev/js/api/core/interface/Cookie.md)
* [**CrawlingContext](https://crawlee.dev/js/api/core/interface/CrawlingContext.md)
* [**CreateSession](https://crawlee.dev/js/api/core/interface/CreateSession.md)
* [**DatasetConsumer](https://crawlee.dev/js/api/core/interface/DatasetConsumer.md)
* [**DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)
* [**DatasetDataOptions](https://crawlee.dev/js/api/core/interface/DatasetDataOptions.md)
* [**DatasetExportOptions](https://crawlee.dev/js/api/core/interface/DatasetExportOptions.md)
* [**DatasetExportToOptions](https://crawlee.dev/js/api/core/interface/DatasetExportToOptions.md)
* [**DatasetIteratorOptions](https://crawlee.dev/js/api/core/interface/DatasetIteratorOptions.md)
* [**DatasetMapper](https://crawlee.dev/js/api/core/interface/DatasetMapper.md)
* [**DatasetOptions](https://crawlee.dev/js/api/core/interface/DatasetOptions.md)
* [**DatasetReducer](https://crawlee.dev/js/api/core/interface/DatasetReducer.md)
* [**EnqueueLinksOptions](https://crawlee.dev/js/api/core/interface/EnqueueLinksOptions.md)
* [**ErrnoException](https://crawlee.dev/js/api/core/interface/ErrnoException.md)
* [**ErrorTrackerOptions](https://crawlee.dev/js/api/core/interface/ErrorTrackerOptions.md)
* [**FinalStatistics](https://crawlee.dev/js/api/core/interface/FinalStatistics.md)
* [**HttpRequest](https://crawlee.dev/js/api/core/interface/HttpRequest.md)
* [**HttpRequestOptions](https://crawlee.dev/js/api/core/interface/HttpRequestOptions.md)
* [**HttpResponse](https://crawlee.dev/js/api/core/interface/HttpResponse.md)
* [**IRequestList](https://crawlee.dev/js/api/core/interface/IRequestList.md)
* [**IRequestManager](https://crawlee.dev/js/api/core/interface/IRequestManager.md)
* [**IStorage](https://crawlee.dev/js/api/core/interface/IStorage.md)
* [**KeyConsumer](https://crawlee.dev/js/api/core/interface/KeyConsumer.md)
* [**KeyValueStoreIteratorOptions](https://crawlee.dev/js/api/core/interface/KeyValueStoreIteratorOptions.md)
* [**KeyValueStoreOptions](https://crawlee.dev/js/api/core/interface/KeyValueStoreOptions.md)
* [**LoggerOptions](https://crawlee.dev/js/api/core/interface/LoggerOptions.md)
* [**PersistenceOptions](https://crawlee.dev/js/api/core/interface/PersistenceOptions.md)
* [**ProxyConfigurationFunction](https://crawlee.dev/js/api/core/interface/ProxyConfigurationFunction.md)
* [**ProxyConfigurationOptions](https://crawlee.dev/js/api/core/interface/ProxyConfigurationOptions.md)
* [**ProxyInfo](https://crawlee.dev/js/api/core/interface/ProxyInfo.md)
* [**PushErrorMessageOptions](https://crawlee.dev/js/api/core/interface/PushErrorMessageOptions.md)
* [**QueueOperationInfo](https://crawlee.dev/js/api/core/interface/QueueOperationInfo.md)
* [**RecordOptions](https://crawlee.dev/js/api/core/interface/RecordOptions.md)
* [**RecoverableStateOptions](https://crawlee.dev/js/api/core/interface/RecoverableStateOptions.md)
* [**RecoverableStatePersistenceOptions](https://crawlee.dev/js/api/core/interface/RecoverableStatePersistenceOptions.md)
* [**RequestListOptions](https://crawlee.dev/js/api/core/interface/RequestListOptions.md)
* [**RequestListState](https://crawlee.dev/js/api/core/interface/RequestListState.md)
* [**RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)
* [**RequestProviderOptions](https://crawlee.dev/js/api/core/interface/RequestProviderOptions.md)
* [**RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)
* [**RequestQueueOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOptions.md)
* [**RequestTransform](https://crawlee.dev/js/api/core/interface/RequestTransform.md)
* [**ResponseLike](https://crawlee.dev/js/api/core/interface/ResponseLike.md)
* [**ResponseTypes](https://crawlee.dev/js/api/core/interface/ResponseTypes.md)
* [**RestrictedCrawlingContext](https://crawlee.dev/js/api/core/interface/RestrictedCrawlingContext.md)
* [**RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)
* [**SessionOptions](https://crawlee.dev/js/api/core/interface/SessionOptions.md)
* [**SessionPoolOptions](https://crawlee.dev/js/api/core/interface/SessionPoolOptions.md)
* [**SessionState](https://crawlee.dev/js/api/core/interface/SessionState.md)
* [**SitemapRequestListOptions](https://crawlee.dev/js/api/core/interface/SitemapRequestListOptions.md)
* [**SnapshotResult](https://crawlee.dev/js/api/core/interface/SnapshotResult.md)
* [**SnapshotterOptions](https://crawlee.dev/js/api/core/interface/SnapshotterOptions.md)
* [**StatisticPersistedState](https://crawlee.dev/js/api/core/interface/StatisticPersistedState.md)
* [**StatisticsOptions](https://crawlee.dev/js/api/core/interface/StatisticsOptions.md)
* [**StatisticState](https://crawlee.dev/js/api/core/interface/StatisticState.md)
* [**StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md)
* [**StorageManagerOptions](https://crawlee.dev/js/api/core/interface/StorageManagerOptions.md)
* [**StreamingHttpResponse](https://crawlee.dev/js/api/core/interface/StreamingHttpResponse.md)
* [**SystemInfo](https://crawlee.dev/js/api/core/interface/SystemInfo.md)
* [**SystemStatusOptions](https://crawlee.dev/js/api/core/interface/SystemStatusOptions.md)
* [**TieredProxy](https://crawlee.dev/js/api/core/interface/TieredProxy.md)
* [**UseStateOptions](https://crawlee.dev/js/api/core/interface/UseStateOptions.md)
* [**EventTypeName](https://crawlee.dev/js/api/core.md#EventTypeName)
* [**GetUserDataFromRequest](https://crawlee.dev/js/api/core.md#GetUserDataFromRequest)
* [**GlobInput](https://crawlee.dev/js/api/core.md#GlobInput)
* [**GlobObject](https://crawlee.dev/js/api/core.md#GlobObject)
* [**LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)
* [**PseudoUrlInput](https://crawlee.dev/js/api/core.md#PseudoUrlInput)
* [**PseudoUrlObject](https://crawlee.dev/js/api/core.md#PseudoUrlObject)
* [**RedirectHandler](https://crawlee.dev/js/api/core.md#RedirectHandler)
* [**RegExpInput](https://crawlee.dev/js/api/core.md#RegExpInput)
* [**RegExpObject](https://crawlee.dev/js/api/core.md#RegExpObject)
* [**RequestListSourcesFunction](https://crawlee.dev/js/api/core.md#RequestListSourcesFunction)
* [**RequestsLike](https://crawlee.dev/js/api/core.md#RequestsLike)
* [**RouterRoutes](https://crawlee.dev/js/api/core.md#RouterRoutes)
* [**SkippedRequestCallback](https://crawlee.dev/js/api/core.md#SkippedRequestCallback)
* [**SkippedRequestReason](https://crawlee.dev/js/api/core.md#SkippedRequestReason)
* [**Source](https://crawlee.dev/js/api/core.md#Source)
* [**UrlPatternObject](https://crawlee.dev/js/api/core.md#UrlPatternObject)
* [**BLOCKED\_STATUS\_CODES](https://crawlee.dev/js/api/core.md#BLOCKED_STATUS_CODES)
* [**log](https://crawlee.dev/js/api/core.md#log)
* [**MAX\_POOL\_SIZE](https://crawlee.dev/js/api/core.md#MAX_POOL_SIZE)
* [**PERSIST\_STATE\_KEY](https://crawlee.dev/js/api/core.md#PERSIST_STATE_KEY)
* [**checkStorageAccess](https://crawlee.dev/js/api/core/function/checkStorageAccess.md)
* [**enqueueLinks](https://crawlee.dev/js/api/core/function/enqueueLinks.md)
* [**filterRequestsByPatterns](https://crawlee.dev/js/api/core/function/filterRequestsByPatterns.md)
* [**processHttpRequestOptions](https://crawlee.dev/js/api/core/function/processHttpRequestOptions.md)
* [**purgeDefaultStorages](https://crawlee.dev/js/api/core/function/purgeDefaultStorages.md)
* [**tryAbsoluteURL](https://crawlee.dev/js/api/core/function/tryAbsoluteURL.md)
* [**useState](https://crawlee.dev/js/api/core/function/useState.md)
* [**withCheckedStorageAccess](https://crawlee.dev/js/api/core/function/withCheckedStorageAccess.md)

## Other<!-- -->[**](#__CATEGORY__)

### [**](#RequestQueueV2)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/index.ts#L8)RequestQueueV2

Renames and re-exports

<!-- -->

[RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md)

### [**](#EventTypeName)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L17)EventTypeName

**EventTypeName: [EventType](https://crawlee.dev/js/api/core/enum/EventType.md) | systemInfo | persistState | migrating | aborting | exit

### [**](#GetUserDataFromRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/router.ts#L15)GetUserDataFromRequest

**GetUserDataFromRequest\<T>: T extends [Request](https://crawlee.dev/js/api/core/class/Request.md)\<infer

<!-- -->

Y> ? Y : never

#### Type parameters

* **T**

### [**](#GlobInput)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L41)GlobInput

**GlobInput: string | [GlobObject](https://crawlee.dev/js/api/core.md#GlobObject)

### [**](#GlobObject)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L36)GlobObject

**GlobObject: { glob: string } & Pick<[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md), method | payload | label | userData | headers>

### [**](#LoadedRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L21)LoadedRequest

**LoadedRequest\<R>: WithRequired\<R, id | loadedUrl>

#### Type parameters

* **R**: [Request](https://crawlee.dev/js/api/core/class/Request.md)

### [**](#PseudoUrlInput)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L34)PseudoUrlInput

**PseudoUrlInput: string | [PseudoUrlObject](https://crawlee.dev/js/api/core.md#PseudoUrlObject)

### [**](#PseudoUrlObject)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L29)PseudoUrlObject

**PseudoUrlObject: { purl: string } & Pick<[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md), method | payload | label | userData | headers>

### [**](#RedirectHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L171)RedirectHandler

**RedirectHandler: (redirectResponse, updatedRequest) => void

Type of a function called when an HTTP redirect takes place. It is allowed to mutate the `updatedRequest` argument.

***

#### Type declaration

* * **(redirectResponse, updatedRequest): void

  - #### Parameters

    * ##### redirectResponse: [BaseHttpResponseData](https://crawlee.dev/js/api/core/interface/BaseHttpResponseData.md)
    * ##### updatedRequest: { headers: SimpleHeaders; url?<!-- -->: string | URL }
      * ##### headers: SimpleHeaders
      * ##### optionalurl: string | URL

    #### Returns void

### [**](#RegExpInput)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L48)RegExpInput

**RegExpInput: RegExp | [RegExpObject](https://crawlee.dev/js/api/core.md#RegExpObject)

### [**](#RegExpObject)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L43)RegExpObject

**RegExpObject: { regexp: RegExp } & Pick<[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md), method | payload | label | userData | headers>

### [**](#RequestListSourcesFunction)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L1002)RequestListSourcesFunction

**RequestListSourcesFunction: () => Promise\<RequestListSource\[]>

#### Type declaration

* * **(): Promise\<RequestListSource\[]>

  - #### Returns Promise\<RequestListSource\[]>

### [**](#RequestsLike)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L39)RequestsLike

**RequestsLike: AsyncIterable<[Source](https://crawlee.dev/js/api/core.md#Source) | string> | Iterable<[Source](https://crawlee.dev/js/api/core.md#Source) | string> | ([Source](https://crawlee.dev/js/api/core.md#Source) | string)\[]

### [**](#RouterRoutes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/router.ts#L17)RouterRoutes

**RouterRoutes\<Context, UserData>: { \[ label in string | symbol ]: (ctx) => Awaitable\<void> }

#### Type parameters

* **Context**
* **UserData**: Dictionary

### [**](#SkippedRequestCallback)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L52)SkippedRequestCallback

**SkippedRequestCallback: (args) => Awaitable\<void>

#### Type declaration

* * **(args): Awaitable\<void>

  - #### Parameters

    * ##### args: { reason: [SkippedRequestReason](https://crawlee.dev/js/api/core.md#SkippedRequestReason); url: string }
      * ##### reason: [SkippedRequestReason](https://crawlee.dev/js/api/core.md#SkippedRequestReason)
      * ##### url: string

    #### Returns Awaitable\<void>

### [**](#SkippedRequestReason)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L50)SkippedRequestReason

**SkippedRequestReason: robotsTxt | limit | enqueueLimit | filters | redirect | depth

### [**](#Source)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L583)Source

**Source: (Partial<[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)> & { regex?

<!-- -->

: RegExp; requestsFromUrl?

<!-- -->

: string }) | [Request](https://crawlee.dev/js/api/core/class/Request.md)

### [**](#UrlPatternObject)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L24)UrlPatternObject

**UrlPatternObject: { glob?

<!-- -->

: string; regexp?

<!-- -->

: RegExp } & Pick<[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md), method | payload | label | userData | headers>

### [**](#BLOCKED_STATUS_CODES)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/consts.ts#L1)constBLOCKED\_STATUS\_CODES

**BLOCKED\_STATUS\_CODES: number\[] =

<!-- -->

...

### [**](#log)[**](https://undefined/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/node_modules/@apify/log/src/index.d.ts#L296)externalconstlog

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

### [**](#MAX_POOL_SIZE)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/consts.ts#L3)constMAX\_POOL\_SIZE

**MAX\_POOL\_SIZE: 1000 =

<!-- -->

1000

### [**](#PERSIST_STATE_KEY)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/consts.ts#L2)constPERSIST\_STATE\_KEY

**PERSIST\_STATE\_KEY: SDK\_SESSION\_POOL\_STATE =

<!-- -->

'SDK\_SESSION\_POOL\_STATE'
