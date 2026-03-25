# Source: https://crawlee.dev/js/docs/examples/playwright-crawler.md

# Source: https://crawlee.dev/js/api/playwright-crawler.md

# @crawlee/playwright<!-- -->

Provides a simple framework for parallel crawling of web pages using headless Chromium, Firefox and Webkit browsers with [Playwright](https://github.com/microsoft/playwright). The URLs to crawl are fed either from a static list of URLs or from a dynamic queue of URLs enabling recursive crawling of websites.

Since `Playwright` uses headless browser to download web pages and extract data, it is useful for crawling of websites that require to execute JavaScript. If the target website doesn't need JavaScript, consider using [CheerioCrawler](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md), which downloads the pages using raw HTTP requests and is about 10x faster.

The source URLs are represented using [Request](https://crawlee.dev/js/api/core/class/Request.md) objects that are fed from [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) or [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) instances provided by the [PlaywrightCrawlerOptions.requestList](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlerOptions.md#requestList) or [PlaywrightCrawlerOptions.requestQueue](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlerOptions.md#requestQueue) constructor options, respectively.

If both [PlaywrightCrawlerOptions.requestList](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlerOptions.md#requestList) and [PlaywrightCrawlerOptions.requestQueue](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlerOptions.md#requestQueue) are used, the instance first processes URLs from the [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) and automatically enqueues all of them to [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) before it starts their processing. This ensures that a single URL is not crawled multiple times.

The crawler finishes when there are no more [Request](https://crawlee.dev/js/api/core/class/Request.md) objects to crawl.

`PlaywrightCrawler` opens a new Chrome page (i.e. tab) for each [Request](https://crawlee.dev/js/api/core/class/Request.md) object to crawl and then calls the function provided by user as the [PlaywrightCrawlerOptions.requestHandler](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlerOptions.md#requestHandler) option.

New pages are only opened when there is enough free CPU and memory available, using the functionality provided by the [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) class. All [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) configuration options can be passed to the [PlaywrightCrawlerOptions.autoscaledPoolOptions](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlerOptions.md#autoscaledPoolOptions) parameter of the `PlaywrightCrawler` constructor. For user convenience, the `minConcurrency` and `maxConcurrency` [AutoscaledPoolOptions](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md) are available directly in the `PlaywrightCrawler` constructor.

Note that the pool of Playwright instances is internally managed by the [BrowserPool](https://github.com/apify/browser-pool) class.

## Example usage[​](#example-usage "Direct link to Example usage")

```
const crawler = new PlaywrightCrawler({
    async requestHandler({ page, request }) {
        // This function is called to extract data from a single web page
        // 'page' is an instance of Playwright.Page with page.goto(request.url) already called
        // 'request' is an instance of Request class with information about the page to load
        await Dataset.pushData({
            title: await page.title(),
            url: request.url,
            succeeded: true,
        })
    },
    async failedRequestHandler({ request }) {
        // This function is called when the crawling of a request failed too many times
        await Dataset.pushData({
            url: request.url,
            succeeded: false,
            errors: request.errorMessages,
        })
    },
});

await crawler.run([
    'http://www.example.com/page-1',
    'http://www.example.com/page-2',
]);
```

## Index[**](#Index)

### Crawlers

* [**PlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md)

### Other

* [**AddRequestsBatchedOptions](https://crawlee.dev/js/api/playwright-crawler.md#AddRequestsBatchedOptions)
* [**AddRequestsBatchedResult](https://crawlee.dev/js/api/playwright-crawler.md#AddRequestsBatchedResult)
* [**AutoscaledPool](https://crawlee.dev/js/api/playwright-crawler.md#AutoscaledPool)
* [**AutoscaledPoolOptions](https://crawlee.dev/js/api/playwright-crawler.md#AutoscaledPoolOptions)
* [**BaseHttpClient](https://crawlee.dev/js/api/playwright-crawler.md#BaseHttpClient)
* [**BaseHttpResponseData](https://crawlee.dev/js/api/playwright-crawler.md#BaseHttpResponseData)
* [**BASIC\_CRAWLER\_TIMEOUT\_BUFFER\_SECS](https://crawlee.dev/js/api/playwright-crawler.md#BASIC_CRAWLER_TIMEOUT_BUFFER_SECS)
* [**BasicCrawler](https://crawlee.dev/js/api/playwright-crawler.md#BasicCrawler)
* [**BasicCrawlerOptions](https://crawlee.dev/js/api/playwright-crawler.md#BasicCrawlerOptions)
* [**BasicCrawlingContext](https://crawlee.dev/js/api/playwright-crawler.md#BasicCrawlingContext)
* [**BLOCKED\_STATUS\_CODES](https://crawlee.dev/js/api/playwright-crawler.md#BLOCKED_STATUS_CODES)
* [**BrowserCrawler](https://crawlee.dev/js/api/playwright-crawler.md#BrowserCrawler)
* [**BrowserCrawlerOptions](https://crawlee.dev/js/api/playwright-crawler.md#BrowserCrawlerOptions)
* [**BrowserCrawlingContext](https://crawlee.dev/js/api/playwright-crawler.md#BrowserCrawlingContext)
* [**BrowserErrorHandler](https://crawlee.dev/js/api/playwright-crawler.md#BrowserErrorHandler)
* [**BrowserHook](https://crawlee.dev/js/api/playwright-crawler.md#BrowserHook)
* [**BrowserLaunchContext](https://crawlee.dev/js/api/playwright-crawler.md#BrowserLaunchContext)
* [**BrowserRequestHandler](https://crawlee.dev/js/api/playwright-crawler.md#BrowserRequestHandler)
* [**checkStorageAccess](https://crawlee.dev/js/api/playwright-crawler.md#checkStorageAccess)
* [**Cheerio](https://crawlee.dev/js/api/playwright-crawler.md#Cheerio)
* [**CheerioAPI](https://crawlee.dev/js/api/playwright-crawler.md#CheerioAPI)
* [**CheerioRoot](https://crawlee.dev/js/api/playwright-crawler.md#CheerioRoot)
* [**ClientInfo](https://crawlee.dev/js/api/playwright-crawler.md#ClientInfo)
* [**Configuration](https://crawlee.dev/js/api/playwright-crawler.md#Configuration)
* [**ConfigurationOptions](https://crawlee.dev/js/api/playwright-crawler.md#ConfigurationOptions)
* [**Cookie](https://crawlee.dev/js/api/playwright-crawler.md#Cookie)
* [**CrawlerAddRequestsOptions](https://crawlee.dev/js/api/playwright-crawler.md#CrawlerAddRequestsOptions)
* [**CrawlerAddRequestsResult](https://crawlee.dev/js/api/playwright-crawler.md#CrawlerAddRequestsResult)
* [**CrawlerExperiments](https://crawlee.dev/js/api/playwright-crawler.md#CrawlerExperiments)
* [**CrawlerRunOptions](https://crawlee.dev/js/api/playwright-crawler.md#CrawlerRunOptions)
* [**CrawlingContext](https://crawlee.dev/js/api/playwright-crawler.md#CrawlingContext)
* [**createBasicRouter](https://crawlee.dev/js/api/playwright-crawler.md#createBasicRouter)
* [**CreateContextOptions](https://crawlee.dev/js/api/playwright-crawler.md#CreateContextOptions)
* [**CreateSession](https://crawlee.dev/js/api/playwright-crawler.md#CreateSession)
* [**CriticalError](https://crawlee.dev/js/api/playwright-crawler.md#CriticalError)
* [**Dataset](https://crawlee.dev/js/api/playwright-crawler.md#Dataset)
* [**DatasetConsumer](https://crawlee.dev/js/api/playwright-crawler.md#DatasetConsumer)
* [**DatasetContent](https://crawlee.dev/js/api/playwright-crawler.md#DatasetContent)
* [**DatasetDataOptions](https://crawlee.dev/js/api/playwright-crawler.md#DatasetDataOptions)
* [**DatasetExportOptions](https://crawlee.dev/js/api/playwright-crawler.md#DatasetExportOptions)
* [**DatasetExportToOptions](https://crawlee.dev/js/api/playwright-crawler.md#DatasetExportToOptions)
* [**DatasetIteratorOptions](https://crawlee.dev/js/api/playwright-crawler.md#DatasetIteratorOptions)
* [**DatasetMapper](https://crawlee.dev/js/api/playwright-crawler.md#DatasetMapper)
* [**DatasetOptions](https://crawlee.dev/js/api/playwright-crawler.md#DatasetOptions)
* [**DatasetReducer](https://crawlee.dev/js/api/playwright-crawler.md#DatasetReducer)
* [**Element](https://crawlee.dev/js/api/playwright-crawler.md#Element)
* [**enqueueLinks](https://crawlee.dev/js/api/playwright-crawler.md#enqueueLinks)
* [**EnqueueLinksOptions](https://crawlee.dev/js/api/playwright-crawler.md#EnqueueLinksOptions)
* [**EnqueueStrategy](https://crawlee.dev/js/api/playwright-crawler.md#EnqueueStrategy)
* [**ErrnoException](https://crawlee.dev/js/api/playwright-crawler.md#ErrnoException)
* [**ErrorHandler](https://crawlee.dev/js/api/playwright-crawler.md#ErrorHandler)
* [**ErrorSnapshotter](https://crawlee.dev/js/api/playwright-crawler.md#ErrorSnapshotter)
* [**ErrorTracker](https://crawlee.dev/js/api/playwright-crawler.md#ErrorTracker)
* [**ErrorTrackerOptions](https://crawlee.dev/js/api/playwright-crawler.md#ErrorTrackerOptions)
* [**EventManager](https://crawlee.dev/js/api/playwright-crawler.md#EventManager)
* [**EventType](https://crawlee.dev/js/api/playwright-crawler.md#EventType)
* [**EventTypeName](https://crawlee.dev/js/api/playwright-crawler.md#EventTypeName)
* [**filterRequestsByPatterns](https://crawlee.dev/js/api/playwright-crawler.md#filterRequestsByPatterns)
* [**FinalStatistics](https://crawlee.dev/js/api/playwright-crawler.md#FinalStatistics)
* [**GetUserDataFromRequest](https://crawlee.dev/js/api/playwright-crawler.md#GetUserDataFromRequest)
* [**GlobInput](https://crawlee.dev/js/api/playwright-crawler.md#GlobInput)
* [**GlobObject](https://crawlee.dev/js/api/playwright-crawler.md#GlobObject)
* [**GotScrapingHttpClient](https://crawlee.dev/js/api/playwright-crawler.md#GotScrapingHttpClient)
* [**HttpRequest](https://crawlee.dev/js/api/playwright-crawler.md#HttpRequest)
* [**HttpRequestOptions](https://crawlee.dev/js/api/playwright-crawler.md#HttpRequestOptions)
* [**HttpResponse](https://crawlee.dev/js/api/playwright-crawler.md#HttpResponse)
* [**IRequestList](https://crawlee.dev/js/api/playwright-crawler.md#IRequestList)
* [**IRequestManager](https://crawlee.dev/js/api/playwright-crawler.md#IRequestManager)
* [**IStorage](https://crawlee.dev/js/api/playwright-crawler.md#IStorage)
* [**KeyConsumer](https://crawlee.dev/js/api/playwright-crawler.md#KeyConsumer)
* [**KeyValueStore](https://crawlee.dev/js/api/playwright-crawler.md#KeyValueStore)
* [**KeyValueStoreIteratorOptions](https://crawlee.dev/js/api/playwright-crawler.md#KeyValueStoreIteratorOptions)
* [**KeyValueStoreOptions](https://crawlee.dev/js/api/playwright-crawler.md#KeyValueStoreOptions)
* [**LoadedRequest](https://crawlee.dev/js/api/playwright-crawler.md#LoadedRequest)
* [**LocalEventManager](https://crawlee.dev/js/api/playwright-crawler.md#LocalEventManager)
* [**log](https://crawlee.dev/js/api/playwright-crawler.md#log)
* [**Log](https://crawlee.dev/js/api/playwright-crawler.md#Log)
* [**Logger](https://crawlee.dev/js/api/playwright-crawler.md#Logger)
* [**LoggerJson](https://crawlee.dev/js/api/playwright-crawler.md#LoggerJson)
* [**LoggerOptions](https://crawlee.dev/js/api/playwright-crawler.md#LoggerOptions)
* [**LoggerText](https://crawlee.dev/js/api/playwright-crawler.md#LoggerText)
* [**LogLevel](https://crawlee.dev/js/api/playwright-crawler.md#LogLevel)
* [**MAX\_POOL\_SIZE](https://crawlee.dev/js/api/playwright-crawler.md#MAX_POOL_SIZE)
* [**NonRetryableError](https://crawlee.dev/js/api/playwright-crawler.md#NonRetryableError)
* [**PERSIST\_STATE\_KEY](https://crawlee.dev/js/api/playwright-crawler.md#PERSIST_STATE_KEY)
* [**PersistenceOptions](https://crawlee.dev/js/api/playwright-crawler.md#PersistenceOptions)
* [**PlaywrightDirectNavigationOptions](https://crawlee.dev/js/api/playwright-crawler.md#PlaywrightDirectNavigationOptions)
* [**processHttpRequestOptions](https://crawlee.dev/js/api/playwright-crawler.md#processHttpRequestOptions)
* [**ProxyConfiguration](https://crawlee.dev/js/api/playwright-crawler.md#ProxyConfiguration)
* [**ProxyConfigurationFunction](https://crawlee.dev/js/api/playwright-crawler.md#ProxyConfigurationFunction)
* [**ProxyConfigurationOptions](https://crawlee.dev/js/api/playwright-crawler.md#ProxyConfigurationOptions)
* [**ProxyInfo](https://crawlee.dev/js/api/playwright-crawler.md#ProxyInfo)
* [**PseudoUrl](https://crawlee.dev/js/api/playwright-crawler.md#PseudoUrl)
* [**PseudoUrlInput](https://crawlee.dev/js/api/playwright-crawler.md#PseudoUrlInput)
* [**PseudoUrlObject](https://crawlee.dev/js/api/playwright-crawler.md#PseudoUrlObject)
* [**purgeDefaultStorages](https://crawlee.dev/js/api/playwright-crawler.md#purgeDefaultStorages)
* [**PushErrorMessageOptions](https://crawlee.dev/js/api/playwright-crawler.md#PushErrorMessageOptions)
* [**QueueOperationInfo](https://crawlee.dev/js/api/playwright-crawler.md#QueueOperationInfo)
* [**RecordOptions](https://crawlee.dev/js/api/playwright-crawler.md#RecordOptions)
* [**RecoverableState](https://crawlee.dev/js/api/playwright-crawler.md#RecoverableState)
* [**RecoverableStateOptions](https://crawlee.dev/js/api/playwright-crawler.md#RecoverableStateOptions)
* [**RecoverableStatePersistenceOptions](https://crawlee.dev/js/api/playwright-crawler.md#RecoverableStatePersistenceOptions)
* [**RedirectHandler](https://crawlee.dev/js/api/playwright-crawler.md#RedirectHandler)
* [**RegExpInput](https://crawlee.dev/js/api/playwright-crawler.md#RegExpInput)
* [**RegExpObject](https://crawlee.dev/js/api/playwright-crawler.md#RegExpObject)
* [**Request](https://crawlee.dev/js/api/playwright-crawler.md#Request)
* [**RequestHandler](https://crawlee.dev/js/api/playwright-crawler.md#RequestHandler)
* [**RequestHandlerResult](https://crawlee.dev/js/api/playwright-crawler.md#RequestHandlerResult)
* [**RequestList](https://crawlee.dev/js/api/playwright-crawler.md#RequestList)
* [**RequestListOptions](https://crawlee.dev/js/api/playwright-crawler.md#RequestListOptions)
* [**RequestListSourcesFunction](https://crawlee.dev/js/api/playwright-crawler.md#RequestListSourcesFunction)
* [**RequestListState](https://crawlee.dev/js/api/playwright-crawler.md#RequestListState)
* [**RequestManagerTandem](https://crawlee.dev/js/api/playwright-crawler.md#RequestManagerTandem)
* [**RequestOptions](https://crawlee.dev/js/api/playwright-crawler.md#RequestOptions)
* [**RequestProvider](https://crawlee.dev/js/api/playwright-crawler.md#RequestProvider)
* [**RequestProviderOptions](https://crawlee.dev/js/api/playwright-crawler.md#RequestProviderOptions)
* [**RequestQueue](https://crawlee.dev/js/api/playwright-crawler.md#RequestQueue)
* [**RequestQueueOperationOptions](https://crawlee.dev/js/api/playwright-crawler.md#RequestQueueOperationOptions)
* [**RequestQueueOptions](https://crawlee.dev/js/api/playwright-crawler.md#RequestQueueOptions)
* [**RequestQueueV1](https://crawlee.dev/js/api/playwright-crawler.md#RequestQueueV1)
* [**RequestQueueV2](https://crawlee.dev/js/api/playwright-crawler.md#RequestQueueV2)
* [**RequestsLike](https://crawlee.dev/js/api/playwright-crawler.md#RequestsLike)
* [**RequestState](https://crawlee.dev/js/api/playwright-crawler.md#RequestState)
* [**RequestTransform](https://crawlee.dev/js/api/playwright-crawler.md#RequestTransform)
* [**ResponseLike](https://crawlee.dev/js/api/playwright-crawler.md#ResponseLike)
* [**ResponseTypes](https://crawlee.dev/js/api/playwright-crawler.md#ResponseTypes)
* [**RestrictedCrawlingContext](https://crawlee.dev/js/api/playwright-crawler.md#RestrictedCrawlingContext)
* [**RetryRequestError](https://crawlee.dev/js/api/playwright-crawler.md#RetryRequestError)
* [**Router](https://crawlee.dev/js/api/playwright-crawler.md#Router)
* [**RouterHandler](https://crawlee.dev/js/api/playwright-crawler.md#RouterHandler)
* [**RouterRoutes](https://crawlee.dev/js/api/playwright-crawler.md#RouterRoutes)
* [**Session](https://crawlee.dev/js/api/playwright-crawler.md#Session)
* [**SessionError](https://crawlee.dev/js/api/playwright-crawler.md#SessionError)
* [**SessionOptions](https://crawlee.dev/js/api/playwright-crawler.md#SessionOptions)
* [**SessionPool](https://crawlee.dev/js/api/playwright-crawler.md#SessionPool)
* [**SessionPoolOptions](https://crawlee.dev/js/api/playwright-crawler.md#SessionPoolOptions)
* [**SessionState](https://crawlee.dev/js/api/playwright-crawler.md#SessionState)
* [**SitemapRequestList](https://crawlee.dev/js/api/playwright-crawler.md#SitemapRequestList)
* [**SitemapRequestListOptions](https://crawlee.dev/js/api/playwright-crawler.md#SitemapRequestListOptions)
* [**SkippedRequestCallback](https://crawlee.dev/js/api/playwright-crawler.md#SkippedRequestCallback)
* [**SkippedRequestReason](https://crawlee.dev/js/api/playwright-crawler.md#SkippedRequestReason)
* [**SnapshotResult](https://crawlee.dev/js/api/playwright-crawler.md#SnapshotResult)
* [**Snapshotter](https://crawlee.dev/js/api/playwright-crawler.md#Snapshotter)
* [**SnapshotterOptions](https://crawlee.dev/js/api/playwright-crawler.md#SnapshotterOptions)
* [**Source](https://crawlee.dev/js/api/playwright-crawler.md#Source)
* [**StatisticPersistedState](https://crawlee.dev/js/api/playwright-crawler.md#StatisticPersistedState)
* [**Statistics](https://crawlee.dev/js/api/playwright-crawler.md#Statistics)
* [**StatisticsOptions](https://crawlee.dev/js/api/playwright-crawler.md#StatisticsOptions)
* [**StatisticState](https://crawlee.dev/js/api/playwright-crawler.md#StatisticState)
* [**StatusMessageCallback](https://crawlee.dev/js/api/playwright-crawler.md#StatusMessageCallback)
* [**StatusMessageCallbackParams](https://crawlee.dev/js/api/playwright-crawler.md#StatusMessageCallbackParams)
* [**StorageClient](https://crawlee.dev/js/api/playwright-crawler.md#StorageClient)
* [**StorageManagerOptions](https://crawlee.dev/js/api/playwright-crawler.md#StorageManagerOptions)
* [**StreamingHttpResponse](https://crawlee.dev/js/api/playwright-crawler.md#StreamingHttpResponse)
* [**SystemInfo](https://crawlee.dev/js/api/playwright-crawler.md#SystemInfo)
* [**SystemStatus](https://crawlee.dev/js/api/playwright-crawler.md#SystemStatus)
* [**SystemStatusOptions](https://crawlee.dev/js/api/playwright-crawler.md#SystemStatusOptions)
* [**TieredProxy](https://crawlee.dev/js/api/playwright-crawler.md#TieredProxy)
* [**tryAbsoluteURL](https://crawlee.dev/js/api/playwright-crawler.md#tryAbsoluteURL)
* [**UrlPatternObject](https://crawlee.dev/js/api/playwright-crawler.md#UrlPatternObject)
* [**useState](https://crawlee.dev/js/api/playwright-crawler.md#useState)
* [**UseStateOptions](https://crawlee.dev/js/api/playwright-crawler.md#UseStateOptions)
* [**withCheckedStorageAccess](https://crawlee.dev/js/api/playwright-crawler.md#withCheckedStorageAccess)
* [**playwrightClickElements](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightClickElements.md)
* [**playwrightUtils](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md)
* [**AdaptivePlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/AdaptivePlaywrightCrawler.md)
* [**RenderingTypePredictor](https://crawlee.dev/js/api/playwright-crawler/class/RenderingTypePredictor.md)
* [**AdaptivePlaywrightCrawlerContext](https://crawlee.dev/js/api/playwright-crawler/interface/AdaptivePlaywrightCrawlerContext.md)
* [**AdaptivePlaywrightCrawlerOptions](https://crawlee.dev/js/api/playwright-crawler/interface/AdaptivePlaywrightCrawlerOptions.md)
* [**PlaywrightCrawlerOptions](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlerOptions.md)
* [**PlaywrightCrawlingContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlingContext.md)
* [**PlaywrightHook](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightHook.md)
* [**PlaywrightLaunchContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightLaunchContext.md)
* [**PlaywrightRequestHandler](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightRequestHandler.md)
* [**PlaywrightGotoOptions](https://crawlee.dev/js/api/playwright-crawler.md#PlaywrightGotoOptions)
* [**RenderingType](https://crawlee.dev/js/api/playwright-crawler.md#RenderingType)
* [**createAdaptivePlaywrightRouter](https://crawlee.dev/js/api/playwright-crawler/function/createAdaptivePlaywrightRouter.md)
* [**createPlaywrightRouter](https://crawlee.dev/js/api/playwright-crawler/function/createPlaywrightRouter.md)
* [**launchPlaywright](https://crawlee.dev/js/api/playwright-crawler/function/launchPlaywright.md)

## Other<!-- -->[**](#__CATEGORY__)

### [**](#AddRequestsBatchedOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L967)AddRequestsBatchedOptions

Re-exports

<!-- -->

[AddRequestsBatchedOptions](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedOptions.md)

### [**](#AddRequestsBatchedResult)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L985)AddRequestsBatchedResult

Re-exports

<!-- -->

[AddRequestsBatchedResult](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedResult.md)

### [**](#AutoscaledPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L180)AutoscaledPool

Re-exports

<!-- -->

[AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md)

### [**](#AutoscaledPoolOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/autoscaled_pool.ts#L16)AutoscaledPoolOptions

Re-exports

<!-- -->

[AutoscaledPoolOptions](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md)

### [**](#BaseHttpClient)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L179)BaseHttpClient

Re-exports

<!-- -->

[BaseHttpClient](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md)

### [**](#BaseHttpResponseData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L130)BaseHttpResponseData

Re-exports

<!-- -->

[BaseHttpResponseData](https://crawlee.dev/js/api/core/interface/BaseHttpResponseData.md)

### [**](#BASIC_CRAWLER_TIMEOUT_BUFFER_SECS)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/constants.ts#L6)BASIC\_CRAWLER\_TIMEOUT\_BUFFER\_SECS

Re-exports

<!-- -->

[BASIC\_CRAWLER\_TIMEOUT\_BUFFER\_SECS](https://crawlee.dev/js/api/basic-crawler.md#BASIC_CRAWLER_TIMEOUT_BUFFER_SECS)

### [**](#BasicCrawler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L490)BasicCrawler

Re-exports

<!-- -->

[BasicCrawler](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md)

### [**](#BasicCrawlerOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L135)BasicCrawlerOptions

Re-exports

<!-- -->

[BasicCrawlerOptions](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md)

### [**](#BasicCrawlingContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L73)BasicCrawlingContext

Re-exports

<!-- -->

[BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md)

### [**](#BLOCKED_STATUS_CODES)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/consts.ts#L1)BLOCKED\_STATUS\_CODES

Re-exports

<!-- -->

[BLOCKED\_STATUS\_CODES](https://crawlee.dev/js/api/core.md#BLOCKED_STATUS_CODES)

### [**](#BrowserCrawler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L314)BrowserCrawler

Re-exports

<!-- -->

[BrowserCrawler](https://crawlee.dev/js/api/browser-crawler/class/BrowserCrawler.md)

### [**](#BrowserCrawlerOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L75)BrowserCrawlerOptions

Re-exports

<!-- -->

[BrowserCrawlerOptions](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlerOptions.md)

### [**](#BrowserCrawlingContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L52)BrowserCrawlingContext

Re-exports

<!-- -->

[BrowserCrawlingContext](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlingContext.md)

### [**](#BrowserErrorHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L67)BrowserErrorHandler

Re-exports

<!-- -->

[BrowserErrorHandler](https://crawlee.dev/js/api/browser-crawler.md#BrowserErrorHandler)

### [**](#BrowserHook)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L70)BrowserHook

Re-exports

<!-- -->

[BrowserHook](https://crawlee.dev/js/api/browser-crawler.md#BrowserHook)

### [**](#BrowserLaunchContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-launcher.ts#L14)BrowserLaunchContext

Re-exports

<!-- -->

[BrowserLaunchContext](https://crawlee.dev/js/api/browser-crawler/interface/BrowserLaunchContext.md)

### [**](#BrowserRequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L64)BrowserRequestHandler

Re-exports

<!-- -->

[BrowserRequestHandler](https://crawlee.dev/js/api/browser-crawler.md#BrowserRequestHandler)

### [**](#checkStorageAccess)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/access_checking.ts#L10)checkStorageAccess

Re-exports

<!-- -->

[checkStorageAccess](https://crawlee.dev/js/api/core/function/checkStorageAccess.md)

### [**](#Cheerio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/index.ts#L4)Cheerio

Re-exports

<!-- -->

[Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)

### [**](#CheerioAPI)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/index.ts#L4)CheerioAPI

Re-exports

<!-- -->

[CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)

### [**](#CheerioRoot)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/index.ts#L4)CheerioRoot

Re-exports

<!-- -->

[CheerioRoot](https://crawlee.dev/js/api/basic-crawler.md#CheerioRoot)

### [**](#ClientInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L79)ClientInfo

Re-exports

<!-- -->

[ClientInfo](https://crawlee.dev/js/api/core/interface/ClientInfo.md)

### [**](#Configuration)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L247)Configuration

Re-exports

<!-- -->

[Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)

### [**](#ConfigurationOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/configuration.ts#L16)ConfigurationOptions

Re-exports

<!-- -->

[ConfigurationOptions](https://crawlee.dev/js/api/core/interface/ConfigurationOptions.md)

### [**](#Cookie)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/index.ts#L19)Cookie

Re-exports

<!-- -->

[Cookie](https://crawlee.dev/js/api/core/interface/Cookie.md)

### [**](#CrawlerAddRequestsOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L2111)CrawlerAddRequestsOptions

Re-exports

<!-- -->

[CrawlerAddRequestsOptions](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerAddRequestsOptions.md)

### [**](#CrawlerAddRequestsResult)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L2113)CrawlerAddRequestsResult

Re-exports

<!-- -->

[CrawlerAddRequestsResult](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerAddRequestsResult.md)

### [**](#CrawlerExperiments)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L416)CrawlerExperiments

Re-exports

<!-- -->

[CrawlerExperiments](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerExperiments.md)

### [**](#CrawlerRunOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L2115)CrawlerRunOptions

Re-exports

<!-- -->

[CrawlerRunOptions](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerRunOptions.md)

### [**](#CrawlingContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L112)CrawlingContext

Re-exports

<!-- -->

[CrawlingContext](https://crawlee.dev/js/api/core/interface/CrawlingContext.md)

### [**](#createBasicRouter)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L2157)createBasicRouter

Re-exports

<!-- -->

[createBasicRouter](https://crawlee.dev/js/api/basic-crawler/function/createBasicRouter.md)

### [**](#CreateContextOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L2105)CreateContextOptions

Re-exports

<!-- -->

[CreateContextOptions](https://crawlee.dev/js/api/basic-crawler/interface/CreateContextOptions.md)

### [**](#CreateSession)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L22)CreateSession

Re-exports

<!-- -->

[CreateSession](https://crawlee.dev/js/api/core/interface/CreateSession.md)

### [**](#CriticalError)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/errors.ts#L10)CriticalError

Re-exports

<!-- -->

[CriticalError](https://crawlee.dev/js/api/core/class/CriticalError.md)

### [**](#Dataset)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L232)Dataset

Re-exports

<!-- -->

[Dataset](https://crawlee.dev/js/api/core/class/Dataset.md)

### [**](#DatasetConsumer)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L775)DatasetConsumer

Re-exports

<!-- -->

[DatasetConsumer](https://crawlee.dev/js/api/core/interface/DatasetConsumer.md)

### [**](#DatasetContent)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L814)DatasetContent

Re-exports

<!-- -->

[DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)

### [**](#DatasetDataOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L92)DatasetDataOptions

Re-exports

<!-- -->

[DatasetDataOptions](https://crawlee.dev/js/api/core/interface/DatasetDataOptions.md)

### [**](#DatasetExportOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L144)DatasetExportOptions

Re-exports

<!-- -->

[DatasetExportOptions](https://crawlee.dev/js/api/core/interface/DatasetExportOptions.md)

### [**](#DatasetExportToOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L176)DatasetExportToOptions

Re-exports

<!-- -->

[DatasetExportToOptions](https://crawlee.dev/js/api/core/interface/DatasetExportToOptions.md)

### [**](#DatasetIteratorOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L152)DatasetIteratorOptions

Re-exports

<!-- -->

[DatasetIteratorOptions](https://crawlee.dev/js/api/core/interface/DatasetIteratorOptions.md)

### [**](#DatasetMapper)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L786)DatasetMapper

Re-exports

<!-- -->

[DatasetMapper](https://crawlee.dev/js/api/core/interface/DatasetMapper.md)

### [**](#DatasetOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L807)DatasetOptions

Re-exports

<!-- -->

[DatasetOptions](https://crawlee.dev/js/api/core/interface/DatasetOptions.md)

### [**](#DatasetReducer)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L798)DatasetReducer

Re-exports

<!-- -->

[DatasetReducer](https://crawlee.dev/js/api/core/interface/DatasetReducer.md)

### [**](#Element)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/index.ts#L4)Element

Re-exports

<!-- -->

[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)

### [**](#enqueueLinks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L274)enqueueLinks

Re-exports

<!-- -->

[enqueueLinks](https://crawlee.dev/js/api/core/function/enqueueLinks.md)

### [**](#EnqueueLinksOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L34)EnqueueLinksOptions

Re-exports

<!-- -->

[EnqueueLinksOptions](https://crawlee.dev/js/api/core/interface/EnqueueLinksOptions.md)

### [**](#EnqueueStrategy)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/enqueue_links.ts#L216)EnqueueStrategy

Re-exports

<!-- -->

[EnqueueStrategy](https://crawlee.dev/js/api/core/enum/EnqueueStrategy.md)

### [**](#ErrnoException)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L9)ErrnoException

Re-exports

<!-- -->

[ErrnoException](https://crawlee.dev/js/api/core/interface/ErrnoException.md)

### [**](#ErrorHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L116)ErrorHandler

Re-exports

<!-- -->

[ErrorHandler](https://crawlee.dev/js/api/basic-crawler.md#ErrorHandler)

### [**](#ErrorSnapshotter)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_snapshotter.ts#L42)ErrorSnapshotter

Re-exports

<!-- -->

[ErrorSnapshotter](https://crawlee.dev/js/api/core/class/ErrorSnapshotter.md)

### [**](#ErrorTracker)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L286)ErrorTracker

Re-exports

<!-- -->

[ErrorTracker](https://crawlee.dev/js/api/core/class/ErrorTracker.md)

### [**](#ErrorTrackerOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_tracker.ts#L17)ErrorTrackerOptions

Re-exports

<!-- -->

[ErrorTrackerOptions](https://crawlee.dev/js/api/core/interface/ErrorTrackerOptions.md)

### [**](#EventManager)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L24)EventManager

Re-exports

<!-- -->

[EventManager](https://crawlee.dev/js/api/core/class/EventManager.md)

### [**](#EventType)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L9)EventType

Re-exports

<!-- -->

[EventType](https://crawlee.dev/js/api/core/enum/EventType.md)

### [**](#EventTypeName)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/event_manager.ts#L17)EventTypeName

Re-exports

<!-- -->

[EventTypeName](https://crawlee.dev/js/api/core.md#EventTypeName)

### [**](#filterRequestsByPatterns)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L214)filterRequestsByPatterns

Re-exports

<!-- -->

[filterRequestsByPatterns](https://crawlee.dev/js/api/core/function/filterRequestsByPatterns.md)

### [**](#FinalStatistics)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L85)FinalStatistics

Re-exports

<!-- -->

[FinalStatistics](https://crawlee.dev/js/api/core/interface/FinalStatistics.md)

### [**](#GetUserDataFromRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/router.ts#L15)GetUserDataFromRequest

Re-exports

<!-- -->

[GetUserDataFromRequest](https://crawlee.dev/js/api/core.md#GetUserDataFromRequest)

### [**](#GlobInput)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L41)GlobInput

Re-exports

<!-- -->

[GlobInput](https://crawlee.dev/js/api/core.md#GlobInput)

### [**](#GlobObject)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L36)GlobObject

Re-exports

<!-- -->

[GlobObject](https://crawlee.dev/js/api/core.md#GlobObject)

### [**](#GotScrapingHttpClient)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/got-scraping-http-client.ts#L17)GotScrapingHttpClient

Re-exports

<!-- -->

[GotScrapingHttpClient](https://crawlee.dev/js/api/core/class/GotScrapingHttpClient.md)

### [**](#HttpRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L78)HttpRequest

Re-exports

<!-- -->

[HttpRequest](https://crawlee.dev/js/api/core/interface/HttpRequest.md)

### [**](#HttpRequestOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L111)HttpRequestOptions

Re-exports

<!-- -->

[HttpRequestOptions](https://crawlee.dev/js/api/core/interface/HttpRequestOptions.md)

### [**](#HttpResponse)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L152)HttpResponse

Re-exports

<!-- -->

[HttpResponse](https://crawlee.dev/js/api/core/interface/HttpResponse.md)

### [**](#IRequestList)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L26)IRequestList

Re-exports

<!-- -->

[IRequestList](https://crawlee.dev/js/api/core/interface/IRequestList.md)

### [**](#IRequestManager)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L44)IRequestManager

Re-exports

<!-- -->

[IRequestManager](https://crawlee.dev/js/api/core/interface/IRequestManager.md)

### [**](#IStorage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/storage_manager.ts#L14)IStorage

Re-exports

<!-- -->

[IStorage](https://crawlee.dev/js/api/core/interface/IStorage.md)

### [**](#KeyConsumer)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L814)KeyConsumer

Re-exports

<!-- -->

[KeyConsumer](https://crawlee.dev/js/api/core/interface/KeyConsumer.md)

### [**](#KeyValueStore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L108)KeyValueStore

Re-exports

<!-- -->

[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)

### [**](#KeyValueStoreIteratorOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L848)KeyValueStoreIteratorOptions

Re-exports

<!-- -->

[KeyValueStoreIteratorOptions](https://crawlee.dev/js/api/core/interface/KeyValueStoreIteratorOptions.md)

### [**](#KeyValueStoreOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L824)KeyValueStoreOptions

Re-exports

<!-- -->

[KeyValueStoreOptions](https://crawlee.dev/js/api/core/interface/KeyValueStoreOptions.md)

### [**](#LoadedRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L21)LoadedRequest

Re-exports

<!-- -->

[LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)

### [**](#LocalEventManager)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/events/local_event_manager.ts#L11)LocalEventManager

Re-exports

<!-- -->

[LocalEventManager](https://crawlee.dev/js/api/core/class/LocalEventManager.md)

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/log.ts#L4)log

Re-exports

<!-- -->

[log](https://crawlee.dev/js/api/core.md#log)

### [**](#Log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/log.ts#L4)Log

Re-exports

<!-- -->

[Log](https://crawlee.dev/js/api/core/class/Log.md)

### [**](#Logger)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/log.ts#L4)Logger

Re-exports

<!-- -->

[Logger](https://crawlee.dev/js/api/core/class/Logger.md)

### [**](#LoggerJson)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/log.ts#L4)LoggerJson

Re-exports

<!-- -->

[LoggerJson](https://crawlee.dev/js/api/core/class/LoggerJson.md)

### [**](#LoggerOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/log.ts#L5)LoggerOptions

Re-exports

<!-- -->

[LoggerOptions](https://crawlee.dev/js/api/core/interface/LoggerOptions.md)

### [**](#LoggerText)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/log.ts#L4)LoggerText

Re-exports

<!-- -->

[LoggerText](https://crawlee.dev/js/api/core/class/LoggerText.md)

### [**](#LogLevel)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/log.ts#L4)LogLevel

Re-exports

<!-- -->

[LogLevel](https://crawlee.dev/js/api/core/enum/LogLevel.md)

### [**](#MAX_POOL_SIZE)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/consts.ts#L3)MAX\_POOL\_SIZE

Re-exports

<!-- -->

[MAX\_POOL\_SIZE](https://crawlee.dev/js/api/core.md#MAX_POOL_SIZE)

### [**](#NonRetryableError)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/errors.ts#L4)NonRetryableError

Re-exports

<!-- -->

[NonRetryableError](https://crawlee.dev/js/api/core/class/NonRetryableError.md)

### [**](#PERSIST_STATE_KEY)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/consts.ts#L2)PERSIST\_STATE\_KEY

Re-exports

<!-- -->

[PERSIST\_STATE\_KEY](https://crawlee.dev/js/api/core.md#PERSIST_STATE_KEY)

### [**](#PersistenceOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L41)PersistenceOptions

Re-exports

<!-- -->

[PersistenceOptions](https://crawlee.dev/js/api/core/interface/PersistenceOptions.md)

### [**](#PlaywrightDirectNavigationOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/index.ts#L9)PlaywrightDirectNavigationOptions

Renames and re-exports

<!-- -->

[DirectNavigationOptions](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#DirectNavigationOptions)

### [**](#processHttpRequestOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L196)processHttpRequestOptions

Re-exports

<!-- -->

[processHttpRequestOptions](https://crawlee.dev/js/api/core/function/processHttpRequestOptions.md)

### [**](#ProxyConfiguration)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L203)ProxyConfiguration

Re-exports

<!-- -->

[ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md)

### [**](#ProxyConfigurationFunction)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L9)ProxyConfigurationFunction

Re-exports

<!-- -->

[ProxyConfigurationFunction](https://crawlee.dev/js/api/core/interface/ProxyConfigurationFunction.md)

### [**](#ProxyConfigurationOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L15)ProxyConfigurationOptions

Re-exports

<!-- -->

[ProxyConfigurationOptions](https://crawlee.dev/js/api/core/interface/ProxyConfigurationOptions.md)

### [**](#ProxyInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L80)ProxyInfo

Re-exports

<!-- -->

[ProxyInfo](https://crawlee.dev/js/api/core/interface/ProxyInfo.md)

### [**](#PseudoUrl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/index.ts#L18)PseudoUrl

Re-exports

<!-- -->

[PseudoUrl](https://crawlee.dev/js/api/core/class/PseudoUrl.md)

### [**](#PseudoUrlInput)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L34)PseudoUrlInput

Re-exports

<!-- -->

[PseudoUrlInput](https://crawlee.dev/js/api/core.md#PseudoUrlInput)

### [**](#PseudoUrlObject)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L29)PseudoUrlObject

Re-exports

<!-- -->

[PseudoUrlObject](https://crawlee.dev/js/api/core.md#PseudoUrlObject)

### [**](#purgeDefaultStorages)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/utils.ts#L33)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/utils.ts#L45)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/utils.ts#L46)purgeDefaultStorages

Re-exports

<!-- -->

[purgeDefaultStorages](https://crawlee.dev/js/api/core/function/purgeDefaultStorages.md)

### [**](#PushErrorMessageOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L567)PushErrorMessageOptions

Re-exports

<!-- -->

[PushErrorMessageOptions](https://crawlee.dev/js/api/core/interface/PushErrorMessageOptions.md)

### [**](#QueueOperationInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/index.ts#L19)QueueOperationInfo

Re-exports

<!-- -->

[QueueOperationInfo](https://crawlee.dev/js/api/core/interface/QueueOperationInfo.md)

### [**](#RecordOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L831)RecordOptions

Re-exports

<!-- -->

[RecordOptions](https://crawlee.dev/js/api/core/interface/RecordOptions.md)

### [**](#RecoverableState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L75)RecoverableState

Re-exports

<!-- -->

[RecoverableState](https://crawlee.dev/js/api/core/class/RecoverableState.md)

### [**](#RecoverableStateOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L33)RecoverableStateOptions

Re-exports

<!-- -->

[RecoverableStateOptions](https://crawlee.dev/js/api/core/interface/RecoverableStateOptions.md)

### [**](#RecoverableStatePersistenceOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/recoverable_state.ts#L6)RecoverableStatePersistenceOptions

Re-exports

<!-- -->

[RecoverableStatePersistenceOptions](https://crawlee.dev/js/api/core/interface/RecoverableStatePersistenceOptions.md)

### [**](#RedirectHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L171)RedirectHandler

Re-exports

<!-- -->

[RedirectHandler](https://crawlee.dev/js/api/core.md#RedirectHandler)

### [**](#RegExpInput)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L48)RegExpInput

Re-exports

<!-- -->

[RegExpInput](https://crawlee.dev/js/api/core.md#RegExpInput)

### [**](#RegExpObject)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L43)RegExpObject

Re-exports

<!-- -->

[RegExpObject](https://crawlee.dev/js/api/core.md#RegExpObject)

### [**](#Request)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L84)Request

Re-exports

<!-- -->

[Request](https://crawlee.dev/js/api/core/class/Request.md)

### [**](#RequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L112)RequestHandler

Re-exports

<!-- -->

[RequestHandler](https://crawlee.dev/js/api/basic-crawler.md#RequestHandler)

### [**](#RequestHandlerResult)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L175)RequestHandlerResult

Re-exports

<!-- -->

[RequestHandlerResult](https://crawlee.dev/js/api/core/class/RequestHandlerResult.md)

### [**](#RequestList)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L300)RequestList

Re-exports

<!-- -->

[RequestList](https://crawlee.dev/js/api/core/class/RequestList.md)

### [**](#RequestListOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L91)RequestListOptions

Re-exports

<!-- -->

[RequestListOptions](https://crawlee.dev/js/api/core/interface/RequestListOptions.md)

### [**](#RequestListSourcesFunction)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L1002)RequestListSourcesFunction

Re-exports

<!-- -->

[RequestListSourcesFunction](https://crawlee.dev/js/api/core.md#RequestListSourcesFunction)

### [**](#RequestListState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L990)RequestListState

Re-exports

<!-- -->

[RequestListState](https://crawlee.dev/js/api/core/interface/RequestListState.md)

### [**](#RequestManagerTandem)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_manager_tandem.ts#L22)RequestManagerTandem

Re-exports

<!-- -->

[RequestManagerTandem](https://crawlee.dev/js/api/core/class/RequestManagerTandem.md)

### [**](#RequestOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L451)RequestOptions

Re-exports

<!-- -->

[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)

### [**](#RequestProvider)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L102)RequestProvider

Re-exports

<!-- -->

[RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)

### [**](#RequestProviderOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L909)RequestProviderOptions

Re-exports

<!-- -->

[RequestProviderOptions](https://crawlee.dev/js/api/core/interface/RequestProviderOptions.md)

### [**](#RequestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/index.ts#L7)RequestQueue

Re-exports

<!-- -->

[RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md)

### [**](#RequestQueueOperationOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L936)RequestQueueOperationOptions

Re-exports

<!-- -->

[RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)

### [**](#RequestQueueOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L925)RequestQueueOptions

Re-exports

<!-- -->

[RequestQueueOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOptions.md)

### [**](#RequestQueueV1)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/index.ts#L6)RequestQueueV1

Re-exports

<!-- -->

[RequestQueueV1](https://crawlee.dev/js/api/core/class/RequestQueueV1.md)

### [**](#RequestQueueV2)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/index.ts#L8)RequestQueueV2

Re-exports

<!-- -->

[RequestQueueV2](https://crawlee.dev/js/api/core.md#RequestQueueV2)

### [**](#RequestsLike)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L39)RequestsLike

Re-exports

<!-- -->

[RequestsLike](https://crawlee.dev/js/api/core.md#RequestsLike)

### [**](#RequestState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L42)RequestState

Re-exports

<!-- -->

[RequestState](https://crawlee.dev/js/api/core/enum/RequestState.md)

### [**](#RequestTransform)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L299)RequestTransform

Re-exports

<!-- -->

[RequestTransform](https://crawlee.dev/js/api/core/interface/RequestTransform.md)

### [**](#ResponseLike)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/cookie_utils.ts#L7)ResponseLike

Re-exports

<!-- -->

[ResponseLike](https://crawlee.dev/js/api/core/interface/ResponseLike.md)

### [**](#ResponseTypes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L39)ResponseTypes

Re-exports

<!-- -->

[ResponseTypes](https://crawlee.dev/js/api/core/interface/ResponseTypes.md)

### [**](#RestrictedCrawlingContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L31)RestrictedCrawlingContext

Re-exports

<!-- -->

[RestrictedCrawlingContext](https://crawlee.dev/js/api/core/interface/RestrictedCrawlingContext.md)

### [**](#RetryRequestError)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/errors.ts#L22)RetryRequestError

Re-exports

<!-- -->

[RetryRequestError](https://crawlee.dev/js/api/core/class/RetryRequestError.md)

### [**](#Router)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/router.ts#L86)Router

Re-exports

<!-- -->

[Router](https://crawlee.dev/js/api/core/class/Router.md)

### [**](#RouterHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/router.ts#L10)RouterHandler

Re-exports

<!-- -->

[RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)

### [**](#RouterRoutes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/router.ts#L17)RouterRoutes

Re-exports

<!-- -->

[RouterRoutes](https://crawlee.dev/js/api/core.md#RouterRoutes)

### [**](#Session)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L100)Session

Re-exports

<!-- -->

[Session](https://crawlee.dev/js/api/core/class/Session.md)

### [**](#SessionError)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/errors.ts#L33)SessionError

Re-exports

<!-- -->

[SessionError](https://crawlee.dev/js/api/core/class/SessionError.md)

### [**](#SessionOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L37)SessionOptions

Re-exports

<!-- -->

[SessionOptions](https://crawlee.dev/js/api/core/interface/SessionOptions.md)

### [**](#SessionPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L137)SessionPool

Re-exports

<!-- -->

[SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md)

### [**](#SessionPoolOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session_pool.ts#L30)SessionPoolOptions

Re-exports

<!-- -->

[SessionPoolOptions](https://crawlee.dev/js/api/core/interface/SessionPoolOptions.md)

### [**](#SessionState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/session_pool/session.ts#L24)SessionState

Re-exports

<!-- -->

[SessionState](https://crawlee.dev/js/api/core/interface/SessionState.md)

### [**](#SitemapRequestList)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L128)SitemapRequestList

Re-exports

<!-- -->

[SitemapRequestList](https://crawlee.dev/js/api/core/class/SitemapRequestList.md)

### [**](#SitemapRequestListOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/sitemap_request_list.ts#L60)SitemapRequestListOptions

Re-exports

<!-- -->

[SitemapRequestListOptions](https://crawlee.dev/js/api/core/interface/SitemapRequestListOptions.md)

### [**](#SkippedRequestCallback)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L52)SkippedRequestCallback

Re-exports

<!-- -->

[SkippedRequestCallback](https://crawlee.dev/js/api/core.md#SkippedRequestCallback)

### [**](#SkippedRequestReason)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L50)SkippedRequestReason

Re-exports

<!-- -->

[SkippedRequestReason](https://crawlee.dev/js/api/core.md#SkippedRequestReason)

### [**](#SnapshotResult)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/error_snapshotter.ts#L16)SnapshotResult

Re-exports

<!-- -->

[SnapshotResult](https://crawlee.dev/js/api/core/interface/SnapshotResult.md)

### [**](#Snapshotter)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L118)Snapshotter

Re-exports

<!-- -->

[Snapshotter](https://crawlee.dev/js/api/core/class/Snapshotter.md)

### [**](#SnapshotterOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/snapshotter.ts#L19)SnapshotterOptions

Re-exports

<!-- -->

[SnapshotterOptions](https://crawlee.dev/js/api/core/interface/SnapshotterOptions.md)

### [**](#Source)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/request.ts#L583)Source

Re-exports

<!-- -->

[Source](https://crawlee.dev/js/api/core.md#Source)

### [**](#StatisticPersistedState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L482)StatisticPersistedState

Re-exports

<!-- -->

[StatisticPersistedState](https://crawlee.dev/js/api/core/interface/StatisticPersistedState.md)

### [**](#Statistics)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L59)Statistics

Re-exports

<!-- -->

[Statistics](https://crawlee.dev/js/api/core/class/Statistics.md)

### [**](#StatisticsOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L436)StatisticsOptions

Re-exports

<!-- -->

[StatisticsOptions](https://crawlee.dev/js/api/core/interface/StatisticsOptions.md)

### [**](#StatisticState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/statistics.ts#L496)StatisticState

Re-exports

<!-- -->

[StatisticState](https://crawlee.dev/js/api/core/interface/StatisticState.md)

### [**](#StatusMessageCallback)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L130)StatusMessageCallback

Re-exports

<!-- -->

[StatusMessageCallback](https://crawlee.dev/js/api/basic-crawler.md#StatusMessageCallback)

### [**](#StatusMessageCallbackParams)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L120)StatusMessageCallbackParams

Re-exports

<!-- -->

[StatusMessageCallbackParams](https://crawlee.dev/js/api/basic-crawler/interface/StatusMessageCallbackParams.md)

### [**](#StorageClient)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/index.ts#L19)StorageClient

Re-exports

<!-- -->

[StorageClient](https://crawlee.dev/js/api/core/interface/StorageClient.md)

### [**](#StorageManagerOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/storage_manager.ts#L158)StorageManagerOptions

Re-exports

<!-- -->

[StorageManagerOptions](https://crawlee.dev/js/api/core/interface/StorageManagerOptions.md)

### [**](#StreamingHttpResponse)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L162)StreamingHttpResponse

Re-exports

<!-- -->

[StreamingHttpResponse](https://crawlee.dev/js/api/core/interface/StreamingHttpResponse.md)

### [**](#SystemInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L10)SystemInfo

Re-exports

<!-- -->

[SystemInfo](https://crawlee.dev/js/api/core/interface/SystemInfo.md)

### [**](#SystemStatus)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L120)SystemStatus

Re-exports

<!-- -->

[SystemStatus](https://crawlee.dev/js/api/core/class/SystemStatus.md)

### [**](#SystemStatusOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/autoscaling/system_status.ts#L35)SystemStatusOptions

Re-exports

<!-- -->

[SystemStatusOptions](https://crawlee.dev/js/api/core/interface/SystemStatusOptions.md)

### [**](#TieredProxy)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/proxy_configuration.ts#L45)TieredProxy

Re-exports

<!-- -->

[TieredProxy](https://crawlee.dev/js/api/core/interface/TieredProxy.md)

### [**](#tryAbsoluteURL)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L12)tryAbsoluteURL

Re-exports

<!-- -->

[tryAbsoluteURL](https://crawlee.dev/js/api/core/function/tryAbsoluteURL.md)

### [**](#UrlPatternObject)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/enqueue_links/shared.ts#L24)UrlPatternObject

Re-exports

<!-- -->

[UrlPatternObject](https://crawlee.dev/js/api/core.md#UrlPatternObject)

### [**](#useState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/utils.ts#L87)useState

Re-exports

<!-- -->

[useState](https://crawlee.dev/js/api/core/function/useState.md)

### [**](#UseStateOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/utils.ts#L69)UseStateOptions

Re-exports

<!-- -->

[UseStateOptions](https://crawlee.dev/js/api/core/interface/UseStateOptions.md)

### [**](#withCheckedStorageAccess)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/access_checking.ts#L18)withCheckedStorageAccess

Re-exports

<!-- -->

[withCheckedStorageAccess](https://crawlee.dev/js/api/core/function/withCheckedStorageAccess.md)

### [**](#PlaywrightGotoOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/playwright-crawler.ts#L26)PlaywrightGotoOptions

**PlaywrightGotoOptions: Dictionary & Parameters\<Page\[goto]>\[1]

### [**](#RenderingType)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/rendering-type-prediction.ts#L7)RenderingType

**RenderingType: clientOnly | static
