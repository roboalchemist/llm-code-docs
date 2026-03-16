# Source: https://crawlee.dev/js/docs/examples/jsdom-crawler.md

# Source: https://crawlee.dev/js/api/jsdom-crawler.md

# @crawlee/jsdom<!-- -->

Provides a framework for the parallel crawling of web pages using plain HTTP requests and [jsdom](https://www.npmjs.com/package/jsdom) DOM implementation. The URLs to crawl are fed either from a static list of URLs or from a dynamic queue of URLs enabling recursive crawling of websites.

Since `JSDOMCrawler` uses raw HTTP requests to download web pages, it is very fast and efficient on data bandwidth. However, if the target website requires JavaScript to display the content, you might need to use [PuppeteerCrawler](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md) or [PlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md) instead, because it loads the pages using full-featured headless Chrome browser.

`JSDOMCrawler` downloads each URL using a plain HTTP request, parses the HTML content using [JSDOM](https://www.npmjs.com/package/jsdom) and then invokes the user-provided [JSDOMCrawlerOptions.requestHandler](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlerOptions.md#requestHandler) to extract page data using the `window` object.

The source URLs are represented using [Request](https://crawlee.dev/js/api/core/class/Request.md) objects that are fed from [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) or [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) instances provided by the [JSDOMCrawlerOptions.requestList](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlerOptions.md#requestList) or [JSDOMCrawlerOptions.requestQueue](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlerOptions.md#requestQueue) constructor options, respectively.

If both [JSDOMCrawlerOptions.requestList](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlerOptions.md#requestList) and [JSDOMCrawlerOptions.requestQueue](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlerOptions.md#requestQueue) are used, the instance first processes URLs from the [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) and automatically enqueues all of them to [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) before it starts their processing. This ensures that a single URL is not crawled multiple times.

The crawler finishes when there are no more [Request](https://crawlee.dev/js/api/core/class/Request.md) objects to crawl.

We can use the `preNavigationHooks` to adjust `gotOptions`:

```
preNavigationHooks: [
    (crawlingContext, gotOptions) => {
        // ...
    },
]
```

By default, `JSDOMCrawler` only processes web pages with the `text/html` and `application/xhtml+xml` MIME content types (as reported by the `Content-Type` HTTP header), and skips pages with other content types. If you want the crawler to process other content types, use the [JSDOMCrawlerOptions.additionalMimeTypes](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlerOptions.md#additionalMimeTypes) constructor option. Beware that the parsing behavior differs for HTML, XML, JSON and other types of content. For more details, see [JSDOMCrawlerOptions.requestHandler](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlerOptions.md#requestHandler).

New requests are only dispatched when there is enough free CPU and memory available, using the functionality provided by the [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) class. All [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) configuration options can be passed to the `autoscaledPoolOptions` parameter of the `JSDOMCrawler` constructor. For user convenience, the `minConcurrency` and `maxConcurrency` [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) options are available directly in the `JSDOMCrawler` constructor.

## Example usage[​](#example-usage "Direct link to Example usage")

```
const crawler = new JSDOMCrawler({
    async requestHandler({ request, window }) {
        await Dataset.pushData({
            url: request.url,
            title: window.document.title,
        });
    },
});

await crawler.run([
    'http://crawlee.dev',
]);
```

## Index[**](#Index)

### Crawlers

* [**JSDOMCrawler](https://crawlee.dev/js/api/jsdom-crawler/class/JSDOMCrawler.md)

### Other

* [**AddRequestsBatchedOptions](https://crawlee.dev/js/api/jsdom-crawler.md#AddRequestsBatchedOptions)
* [**AddRequestsBatchedResult](https://crawlee.dev/js/api/jsdom-crawler.md#AddRequestsBatchedResult)
* [**AutoscaledPool](https://crawlee.dev/js/api/jsdom-crawler.md#AutoscaledPool)
* [**AutoscaledPoolOptions](https://crawlee.dev/js/api/jsdom-crawler.md#AutoscaledPoolOptions)
* [**BaseHttpClient](https://crawlee.dev/js/api/jsdom-crawler.md#BaseHttpClient)
* [**BaseHttpResponseData](https://crawlee.dev/js/api/jsdom-crawler.md#BaseHttpResponseData)
* [**BASIC\_CRAWLER\_TIMEOUT\_BUFFER\_SECS](https://crawlee.dev/js/api/jsdom-crawler.md#BASIC_CRAWLER_TIMEOUT_BUFFER_SECS)
* [**BasicCrawler](https://crawlee.dev/js/api/jsdom-crawler.md#BasicCrawler)
* [**BasicCrawlerOptions](https://crawlee.dev/js/api/jsdom-crawler.md#BasicCrawlerOptions)
* [**BasicCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler.md#BasicCrawlingContext)
* [**BLOCKED\_STATUS\_CODES](https://crawlee.dev/js/api/jsdom-crawler.md#BLOCKED_STATUS_CODES)
* [**ByteCounterStream](https://crawlee.dev/js/api/jsdom-crawler.md#ByteCounterStream)
* [**checkStorageAccess](https://crawlee.dev/js/api/jsdom-crawler.md#checkStorageAccess)
* [**Cheerio](https://crawlee.dev/js/api/jsdom-crawler.md#Cheerio)
* [**CheerioAPI](https://crawlee.dev/js/api/jsdom-crawler.md#CheerioAPI)
* [**CheerioRoot](https://crawlee.dev/js/api/jsdom-crawler.md#CheerioRoot)
* [**ClientInfo](https://crawlee.dev/js/api/jsdom-crawler.md#ClientInfo)
* [**Configuration](https://crawlee.dev/js/api/jsdom-crawler.md#Configuration)
* [**ConfigurationOptions](https://crawlee.dev/js/api/jsdom-crawler.md#ConfigurationOptions)
* [**Cookie](https://crawlee.dev/js/api/jsdom-crawler.md#Cookie)
* [**CrawlerAddRequestsOptions](https://crawlee.dev/js/api/jsdom-crawler.md#CrawlerAddRequestsOptions)
* [**CrawlerAddRequestsResult](https://crawlee.dev/js/api/jsdom-crawler.md#CrawlerAddRequestsResult)
* [**CrawlerExperiments](https://crawlee.dev/js/api/jsdom-crawler.md#CrawlerExperiments)
* [**CrawlerRunOptions](https://crawlee.dev/js/api/jsdom-crawler.md#CrawlerRunOptions)
* [**CrawlingContext](https://crawlee.dev/js/api/jsdom-crawler.md#CrawlingContext)
* [**createBasicRouter](https://crawlee.dev/js/api/jsdom-crawler.md#createBasicRouter)
* [**CreateContextOptions](https://crawlee.dev/js/api/jsdom-crawler.md#CreateContextOptions)
* [**createFileRouter](https://crawlee.dev/js/api/jsdom-crawler.md#createFileRouter)
* [**createHttpRouter](https://crawlee.dev/js/api/jsdom-crawler.md#createHttpRouter)
* [**CreateSession](https://crawlee.dev/js/api/jsdom-crawler.md#CreateSession)
* [**CriticalError](https://crawlee.dev/js/api/jsdom-crawler.md#CriticalError)
* [**Dataset](https://crawlee.dev/js/api/jsdom-crawler.md#Dataset)
* [**DatasetConsumer](https://crawlee.dev/js/api/jsdom-crawler.md#DatasetConsumer)
* [**DatasetContent](https://crawlee.dev/js/api/jsdom-crawler.md#DatasetContent)
* [**DatasetDataOptions](https://crawlee.dev/js/api/jsdom-crawler.md#DatasetDataOptions)
* [**DatasetExportOptions](https://crawlee.dev/js/api/jsdom-crawler.md#DatasetExportOptions)
* [**DatasetExportToOptions](https://crawlee.dev/js/api/jsdom-crawler.md#DatasetExportToOptions)
* [**DatasetIteratorOptions](https://crawlee.dev/js/api/jsdom-crawler.md#DatasetIteratorOptions)
* [**DatasetMapper](https://crawlee.dev/js/api/jsdom-crawler.md#DatasetMapper)
* [**DatasetOptions](https://crawlee.dev/js/api/jsdom-crawler.md#DatasetOptions)
* [**DatasetReducer](https://crawlee.dev/js/api/jsdom-crawler.md#DatasetReducer)
* [**Element](https://crawlee.dev/js/api/jsdom-crawler.md#Element)
* [**enqueueLinks](https://crawlee.dev/js/api/jsdom-crawler.md#enqueueLinks)
* [**EnqueueLinksOptions](https://crawlee.dev/js/api/jsdom-crawler.md#EnqueueLinksOptions)
* [**EnqueueStrategy](https://crawlee.dev/js/api/jsdom-crawler.md#EnqueueStrategy)
* [**ErrnoException](https://crawlee.dev/js/api/jsdom-crawler.md#ErrnoException)
* [**ErrorHandler](https://crawlee.dev/js/api/jsdom-crawler.md#ErrorHandler)
* [**ErrorSnapshotter](https://crawlee.dev/js/api/jsdom-crawler.md#ErrorSnapshotter)
* [**ErrorTracker](https://crawlee.dev/js/api/jsdom-crawler.md#ErrorTracker)
* [**ErrorTrackerOptions](https://crawlee.dev/js/api/jsdom-crawler.md#ErrorTrackerOptions)
* [**EventManager](https://crawlee.dev/js/api/jsdom-crawler.md#EventManager)
* [**EventType](https://crawlee.dev/js/api/jsdom-crawler.md#EventType)
* [**EventTypeName](https://crawlee.dev/js/api/jsdom-crawler.md#EventTypeName)
* [**FileDownload](https://crawlee.dev/js/api/jsdom-crawler.md#FileDownload)
* [**FileDownloadCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler.md#FileDownloadCrawlingContext)
* [**FileDownloadErrorHandler](https://crawlee.dev/js/api/jsdom-crawler.md#FileDownloadErrorHandler)
* [**FileDownloadHook](https://crawlee.dev/js/api/jsdom-crawler.md#FileDownloadHook)
* [**FileDownloadOptions](https://crawlee.dev/js/api/jsdom-crawler.md#FileDownloadOptions)
* [**FileDownloadRequestHandler](https://crawlee.dev/js/api/jsdom-crawler.md#FileDownloadRequestHandler)
* [**filterRequestsByPatterns](https://crawlee.dev/js/api/jsdom-crawler.md#filterRequestsByPatterns)
* [**FinalStatistics](https://crawlee.dev/js/api/jsdom-crawler.md#FinalStatistics)
* [**GetUserDataFromRequest](https://crawlee.dev/js/api/jsdom-crawler.md#GetUserDataFromRequest)
* [**GlobInput](https://crawlee.dev/js/api/jsdom-crawler.md#GlobInput)
* [**GlobObject](https://crawlee.dev/js/api/jsdom-crawler.md#GlobObject)
* [**GotScrapingHttpClient](https://crawlee.dev/js/api/jsdom-crawler.md#GotScrapingHttpClient)
* [**HttpCrawler](https://crawlee.dev/js/api/jsdom-crawler.md#HttpCrawler)
* [**HttpCrawlerOptions](https://crawlee.dev/js/api/jsdom-crawler.md#HttpCrawlerOptions)
* [**HttpCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler.md#HttpCrawlingContext)
* [**HttpErrorHandler](https://crawlee.dev/js/api/jsdom-crawler.md#HttpErrorHandler)
* [**HttpHook](https://crawlee.dev/js/api/jsdom-crawler.md#HttpHook)
* [**HttpRequest](https://crawlee.dev/js/api/jsdom-crawler.md#HttpRequest)
* [**HttpRequestHandler](https://crawlee.dev/js/api/jsdom-crawler.md#HttpRequestHandler)
* [**HttpRequestOptions](https://crawlee.dev/js/api/jsdom-crawler.md#HttpRequestOptions)
* [**HttpResponse](https://crawlee.dev/js/api/jsdom-crawler.md#HttpResponse)
* [**IRequestList](https://crawlee.dev/js/api/jsdom-crawler.md#IRequestList)
* [**IRequestManager](https://crawlee.dev/js/api/jsdom-crawler.md#IRequestManager)
* [**IStorage](https://crawlee.dev/js/api/jsdom-crawler.md#IStorage)
* [**KeyConsumer](https://crawlee.dev/js/api/jsdom-crawler.md#KeyConsumer)
* [**KeyValueStore](https://crawlee.dev/js/api/jsdom-crawler.md#KeyValueStore)
* [**KeyValueStoreIteratorOptions](https://crawlee.dev/js/api/jsdom-crawler.md#KeyValueStoreIteratorOptions)
* [**KeyValueStoreOptions](https://crawlee.dev/js/api/jsdom-crawler.md#KeyValueStoreOptions)
* [**LoadedRequest](https://crawlee.dev/js/api/jsdom-crawler.md#LoadedRequest)
* [**LocalEventManager](https://crawlee.dev/js/api/jsdom-crawler.md#LocalEventManager)
* [**log](https://crawlee.dev/js/api/jsdom-crawler.md#log)
* [**Log](https://crawlee.dev/js/api/jsdom-crawler.md#Log)
* [**Logger](https://crawlee.dev/js/api/jsdom-crawler.md#Logger)
* [**LoggerJson](https://crawlee.dev/js/api/jsdom-crawler.md#LoggerJson)
* [**LoggerOptions](https://crawlee.dev/js/api/jsdom-crawler.md#LoggerOptions)
* [**LoggerText](https://crawlee.dev/js/api/jsdom-crawler.md#LoggerText)
* [**LogLevel](https://crawlee.dev/js/api/jsdom-crawler.md#LogLevel)
* [**MAX\_POOL\_SIZE](https://crawlee.dev/js/api/jsdom-crawler.md#MAX_POOL_SIZE)
* [**MinimumSpeedStream](https://crawlee.dev/js/api/jsdom-crawler.md#MinimumSpeedStream)
* [**NonRetryableError](https://crawlee.dev/js/api/jsdom-crawler.md#NonRetryableError)
* [**PERSIST\_STATE\_KEY](https://crawlee.dev/js/api/jsdom-crawler.md#PERSIST_STATE_KEY)
* [**PersistenceOptions](https://crawlee.dev/js/api/jsdom-crawler.md#PersistenceOptions)
* [**processHttpRequestOptions](https://crawlee.dev/js/api/jsdom-crawler.md#processHttpRequestOptions)
* [**ProxyConfiguration](https://crawlee.dev/js/api/jsdom-crawler.md#ProxyConfiguration)
* [**ProxyConfigurationFunction](https://crawlee.dev/js/api/jsdom-crawler.md#ProxyConfigurationFunction)
* [**ProxyConfigurationOptions](https://crawlee.dev/js/api/jsdom-crawler.md#ProxyConfigurationOptions)
* [**ProxyInfo](https://crawlee.dev/js/api/jsdom-crawler.md#ProxyInfo)
* [**PseudoUrl](https://crawlee.dev/js/api/jsdom-crawler.md#PseudoUrl)
* [**PseudoUrlInput](https://crawlee.dev/js/api/jsdom-crawler.md#PseudoUrlInput)
* [**PseudoUrlObject](https://crawlee.dev/js/api/jsdom-crawler.md#PseudoUrlObject)
* [**purgeDefaultStorages](https://crawlee.dev/js/api/jsdom-crawler.md#purgeDefaultStorages)
* [**PushErrorMessageOptions](https://crawlee.dev/js/api/jsdom-crawler.md#PushErrorMessageOptions)
* [**QueueOperationInfo](https://crawlee.dev/js/api/jsdom-crawler.md#QueueOperationInfo)
* [**RecordOptions](https://crawlee.dev/js/api/jsdom-crawler.md#RecordOptions)
* [**RecoverableState](https://crawlee.dev/js/api/jsdom-crawler.md#RecoverableState)
* [**RecoverableStateOptions](https://crawlee.dev/js/api/jsdom-crawler.md#RecoverableStateOptions)
* [**RecoverableStatePersistenceOptions](https://crawlee.dev/js/api/jsdom-crawler.md#RecoverableStatePersistenceOptions)
* [**RedirectHandler](https://crawlee.dev/js/api/jsdom-crawler.md#RedirectHandler)
* [**RegExpInput](https://crawlee.dev/js/api/jsdom-crawler.md#RegExpInput)
* [**RegExpObject](https://crawlee.dev/js/api/jsdom-crawler.md#RegExpObject)
* [**Request](https://crawlee.dev/js/api/jsdom-crawler.md#Request)
* [**RequestHandler](https://crawlee.dev/js/api/jsdom-crawler.md#RequestHandler)
* [**RequestHandlerResult](https://crawlee.dev/js/api/jsdom-crawler.md#RequestHandlerResult)
* [**RequestList](https://crawlee.dev/js/api/jsdom-crawler.md#RequestList)
* [**RequestListOptions](https://crawlee.dev/js/api/jsdom-crawler.md#RequestListOptions)
* [**RequestListSourcesFunction](https://crawlee.dev/js/api/jsdom-crawler.md#RequestListSourcesFunction)
* [**RequestListState](https://crawlee.dev/js/api/jsdom-crawler.md#RequestListState)
* [**RequestManagerTandem](https://crawlee.dev/js/api/jsdom-crawler.md#RequestManagerTandem)
* [**RequestOptions](https://crawlee.dev/js/api/jsdom-crawler.md#RequestOptions)
* [**RequestProvider](https://crawlee.dev/js/api/jsdom-crawler.md#RequestProvider)
* [**RequestProviderOptions](https://crawlee.dev/js/api/jsdom-crawler.md#RequestProviderOptions)
* [**RequestQueue](https://crawlee.dev/js/api/jsdom-crawler.md#RequestQueue)
* [**RequestQueueOperationOptions](https://crawlee.dev/js/api/jsdom-crawler.md#RequestQueueOperationOptions)
* [**RequestQueueOptions](https://crawlee.dev/js/api/jsdom-crawler.md#RequestQueueOptions)
* [**RequestQueueV1](https://crawlee.dev/js/api/jsdom-crawler.md#RequestQueueV1)
* [**RequestQueueV2](https://crawlee.dev/js/api/jsdom-crawler.md#RequestQueueV2)
* [**RequestsLike](https://crawlee.dev/js/api/jsdom-crawler.md#RequestsLike)
* [**RequestState](https://crawlee.dev/js/api/jsdom-crawler.md#RequestState)
* [**RequestTransform](https://crawlee.dev/js/api/jsdom-crawler.md#RequestTransform)
* [**ResponseLike](https://crawlee.dev/js/api/jsdom-crawler.md#ResponseLike)
* [**ResponseTypes](https://crawlee.dev/js/api/jsdom-crawler.md#ResponseTypes)
* [**RestrictedCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler.md#RestrictedCrawlingContext)
* [**RetryRequestError](https://crawlee.dev/js/api/jsdom-crawler.md#RetryRequestError)
* [**Router](https://crawlee.dev/js/api/jsdom-crawler.md#Router)
* [**RouterHandler](https://crawlee.dev/js/api/jsdom-crawler.md#RouterHandler)
* [**RouterRoutes](https://crawlee.dev/js/api/jsdom-crawler.md#RouterRoutes)
* [**Session](https://crawlee.dev/js/api/jsdom-crawler.md#Session)
* [**SessionError](https://crawlee.dev/js/api/jsdom-crawler.md#SessionError)
* [**SessionOptions](https://crawlee.dev/js/api/jsdom-crawler.md#SessionOptions)
* [**SessionPool](https://crawlee.dev/js/api/jsdom-crawler.md#SessionPool)
* [**SessionPoolOptions](https://crawlee.dev/js/api/jsdom-crawler.md#SessionPoolOptions)
* [**SessionState](https://crawlee.dev/js/api/jsdom-crawler.md#SessionState)
* [**SitemapRequestList](https://crawlee.dev/js/api/jsdom-crawler.md#SitemapRequestList)
* [**SitemapRequestListOptions](https://crawlee.dev/js/api/jsdom-crawler.md#SitemapRequestListOptions)
* [**SkippedRequestCallback](https://crawlee.dev/js/api/jsdom-crawler.md#SkippedRequestCallback)
* [**SkippedRequestReason](https://crawlee.dev/js/api/jsdom-crawler.md#SkippedRequestReason)
* [**SnapshotResult](https://crawlee.dev/js/api/jsdom-crawler.md#SnapshotResult)
* [**Snapshotter](https://crawlee.dev/js/api/jsdom-crawler.md#Snapshotter)
* [**SnapshotterOptions](https://crawlee.dev/js/api/jsdom-crawler.md#SnapshotterOptions)
* [**Source](https://crawlee.dev/js/api/jsdom-crawler.md#Source)
* [**StatisticPersistedState](https://crawlee.dev/js/api/jsdom-crawler.md#StatisticPersistedState)
* [**Statistics](https://crawlee.dev/js/api/jsdom-crawler.md#Statistics)
* [**StatisticsOptions](https://crawlee.dev/js/api/jsdom-crawler.md#StatisticsOptions)
* [**StatisticState](https://crawlee.dev/js/api/jsdom-crawler.md#StatisticState)
* [**StatusMessageCallback](https://crawlee.dev/js/api/jsdom-crawler.md#StatusMessageCallback)
* [**StatusMessageCallbackParams](https://crawlee.dev/js/api/jsdom-crawler.md#StatusMessageCallbackParams)
* [**StorageClient](https://crawlee.dev/js/api/jsdom-crawler.md#StorageClient)
* [**StorageManagerOptions](https://crawlee.dev/js/api/jsdom-crawler.md#StorageManagerOptions)
* [**StreamHandlerContext](https://crawlee.dev/js/api/jsdom-crawler.md#StreamHandlerContext)
* [**StreamingHttpResponse](https://crawlee.dev/js/api/jsdom-crawler.md#StreamingHttpResponse)
* [**SystemInfo](https://crawlee.dev/js/api/jsdom-crawler.md#SystemInfo)
* [**SystemStatus](https://crawlee.dev/js/api/jsdom-crawler.md#SystemStatus)
* [**SystemStatusOptions](https://crawlee.dev/js/api/jsdom-crawler.md#SystemStatusOptions)
* [**TieredProxy](https://crawlee.dev/js/api/jsdom-crawler.md#TieredProxy)
* [**tryAbsoluteURL](https://crawlee.dev/js/api/jsdom-crawler.md#tryAbsoluteURL)
* [**UrlPatternObject](https://crawlee.dev/js/api/jsdom-crawler.md#UrlPatternObject)
* [**useState](https://crawlee.dev/js/api/jsdom-crawler.md#useState)
* [**UseStateOptions](https://crawlee.dev/js/api/jsdom-crawler.md#UseStateOptions)
* [**withCheckedStorageAccess](https://crawlee.dev/js/api/jsdom-crawler.md#withCheckedStorageAccess)
* [**JSDOMCrawlerOptions](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlerOptions.md)
* [**JSDOMCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlingContext.md)
* [**JSDOMErrorHandler](https://crawlee.dev/js/api/jsdom-crawler.md#JSDOMErrorHandler)
* [**JSDOMHook](https://crawlee.dev/js/api/jsdom-crawler.md#JSDOMHook)
* [**JSDOMRequestHandler](https://crawlee.dev/js/api/jsdom-crawler.md#JSDOMRequestHandler)
* [**createJSDOMRouter](https://crawlee.dev/js/api/jsdom-crawler/function/createJSDOMRouter.md)

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

### [**](#ByteCounterStream)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/file-download.ts#L116)ByteCounterStream

Re-exports

<!-- -->

[ByteCounterStream](https://crawlee.dev/js/api/http-crawler/function/ByteCounterStream.md)

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

### [**](#createFileRouter)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/file-download.ts#L307)createFileRouter

Re-exports

<!-- -->

[createFileRouter](https://crawlee.dev/js/api/http-crawler/function/createFileRouter.md)

### [**](#createHttpRouter)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L1069)createHttpRouter

Re-exports

<!-- -->

[createHttpRouter](https://crawlee.dev/js/api/http-crawler/function/createHttpRouter.md)

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

### [**](#FileDownload)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/file-download.ts#L187)FileDownload

Re-exports

<!-- -->

[FileDownload](https://crawlee.dev/js/api/http-crawler/class/FileDownload.md)

### [**](#FileDownloadCrawlingContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/file-download.ts#L52)FileDownloadCrawlingContext

Re-exports

<!-- -->

[FileDownloadCrawlingContext](https://crawlee.dev/js/api/http-crawler/interface/FileDownloadCrawlingContext.md)

### [**](#FileDownloadErrorHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/file-download.ts#L20)FileDownloadErrorHandler

Re-exports

<!-- -->

[FileDownloadErrorHandler](https://crawlee.dev/js/api/http-crawler.md#FileDownloadErrorHandler)

### [**](#FileDownloadHook)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/file-download.ts#L47)FileDownloadHook

Re-exports

<!-- -->

[FileDownloadHook](https://crawlee.dev/js/api/http-crawler.md#FileDownloadHook)

### [**](#FileDownloadOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/file-download.ts#L34)FileDownloadOptions

Re-exports

<!-- -->

[FileDownloadOptions](https://crawlee.dev/js/api/http-crawler.md#FileDownloadOptions)

### [**](#FileDownloadRequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/file-download.ts#L57)FileDownloadRequestHandler

Re-exports

<!-- -->

[FileDownloadRequestHandler](https://crawlee.dev/js/api/http-crawler.md#FileDownloadRequestHandler)

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

### [**](#HttpCrawler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L331)HttpCrawler

Re-exports

<!-- -->

[HttpCrawler](https://crawlee.dev/js/api/http-crawler/class/HttpCrawler.md)

### [**](#HttpCrawlerOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L80)HttpCrawlerOptions

Re-exports

<!-- -->

[HttpCrawlerOptions](https://crawlee.dev/js/api/http-crawler/interface/HttpCrawlerOptions.md)

### [**](#HttpCrawlingContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L256)HttpCrawlingContext

Re-exports

<!-- -->

[HttpCrawlingContext](https://crawlee.dev/js/api/http-crawler/interface/HttpCrawlingContext.md)

### [**](#HttpErrorHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L75)HttpErrorHandler

Re-exports

<!-- -->

[HttpErrorHandler](https://crawlee.dev/js/api/http-crawler.md#HttpErrorHandler)

### [**](#HttpHook)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L195)HttpHook

Re-exports

<!-- -->

[HttpHook](https://crawlee.dev/js/api/http-crawler.md#HttpHook)

### [**](#HttpRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/http_clients/base-http-client.ts#L78)HttpRequest

Re-exports

<!-- -->

[HttpRequest](https://crawlee.dev/js/api/core/interface/HttpRequest.md)

### [**](#HttpRequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L259)HttpRequestHandler

Re-exports

<!-- -->

[HttpRequestHandler](https://crawlee.dev/js/api/http-crawler.md#HttpRequestHandler)

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

### [**](#MinimumSpeedStream)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/file-download.ts#L71)MinimumSpeedStream

Re-exports

<!-- -->

[MinimumSpeedStream](https://crawlee.dev/js/api/http-crawler/function/MinimumSpeedStream.md)

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

### [**](#StreamHandlerContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/file-download.ts#L25)StreamHandlerContext

Re-exports

<!-- -->

[StreamHandlerContext](https://crawlee.dev/js/api/http-crawler.md#StreamHandlerContext)

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

### [**](#JSDOMErrorHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/jsdom-crawler/src/internals/jsdom-crawler.ts#L34)JSDOMErrorHandler

**JSDOMErrorHandler\<UserData, JSONData>: [ErrorHandler](https://crawlee.dev/js/api/basic-crawler.md#ErrorHandler)<[JSDOMCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlingContext.md)\<UserData, JSONData>>

#### Type parameters

* **UserData**: Dictionary = any
* **JSONData**: Dictionary = any

### [**](#JSDOMHook)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/jsdom-crawler/src/internals/jsdom-crawler.ts#L53)JSDOMHook

**JSDOMHook\<UserData, JSONData>: InternalHttpHook<[JSDOMCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlingContext.md)\<UserData, JSONData>>

#### Type parameters

* **UserData**: Dictionary = any
* **JSONData**: Dictionary = any

### [**](#JSDOMRequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/jsdom-crawler/src/internals/jsdom-crawler.ts#L95)JSDOMRequestHandler

**JSDOMRequestHandler\<UserData, JSONData>: [RequestHandler](https://crawlee.dev/js/api/basic-crawler.md#RequestHandler)<[JSDOMCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlingContext.md)\<UserData, JSONData>>

#### Type parameters

* **UserData**: Dictionary = any
* **JSONData**: Dictionary = any
