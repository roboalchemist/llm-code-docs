# Source: https://crawlee.dev/js/api/browser-crawler/class/BrowserCrawler.md

# abstractBrowserCrawler<!-- --> \<InternalBrowserPoolOptions, LaunchOptions, Context, GoToOptions>

Provides a simple framework for parallel crawling of web pages using headless browsers with [Puppeteer](https://github.com/puppeteer/puppeteer) and [Playwright](https://github.com/microsoft/playwright). The URLs to crawl are fed either from a static list of URLs or from a dynamic queue of URLs enabling recursive crawling of websites.

Since `BrowserCrawler` uses headless (or even headful) browsers to download web pages and extract data, it is useful for crawling of websites that require to execute JavaScript. If the target website doesn't need JavaScript, we should consider using the [CheerioCrawler](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md), which downloads the pages using raw HTTP requests and is about 10x faster.

The source URLs are represented by the [Request](https://crawlee.dev/js/api/core/class/Request.md) objects that are fed from the [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) or [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) instances provided by the [`requestList`](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlerOptions.md#requestList) or [`requestQueue`](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlerOptions.md#requestQueue) constructor options, respectively. If neither `requestList` nor `requestQueue` options are provided, the crawler will open the default request queue either when the [`crawler.addRequests()`](https://crawlee.dev/js/api/browser-crawler/class/BrowserCrawler.md#addRequests) function is called, or if `requests` parameter (representing the initial requests) of the [`crawler.run()`](https://crawlee.dev/js/api/browser-crawler/class/BrowserCrawler.md#run) function is provided.

If both [`requestList`](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlerOptions.md#requestList) and [`requestQueue`](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlerOptions.md#requestQueue) options are used, the instance first processes URLs from the [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) and automatically enqueues all of them to the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) before it starts their processing. This ensures that a single URL is not crawled multiple times.

The crawler finishes when there are no more [Request](https://crawlee.dev/js/api/core/class/Request.md) objects to crawl.

`BrowserCrawler` opens a new browser page (i.e. tab or window) for each [Request](https://crawlee.dev/js/api/core/class/Request.md) object to crawl and then calls the function provided by user as the [`requestHandler`](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlerOptions.md#requestHandler) option.

New pages are only opened when there is enough free CPU and memory available, using the functionality provided by the [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) class. All [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) configuration options can be passed to the [`autoscaledPoolOptions`](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlerOptions.md#autoscaledPoolOptions) parameter of the `BrowserCrawler` constructor. For user convenience, the [`minConcurrency`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#minConcurrency) and [`maxConcurrency`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#maxConcurrency) options of the underlying [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) constructor are available directly in the `BrowserCrawler` constructor.

> *NOTE:* the pool of browser instances is internally managed by the [BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md) class.

### Hierarchy

* [BasicCrawler](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md)\<Context>

  * *BrowserCrawler*

    * [PuppeteerCrawler](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md)
    * [PlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md)
    * [StagehandCrawler](https://crawlee.dev/js/api/stagehand-crawler/class/StagehandCrawler.md)

## Index[**](#Index)

### Properties

* [**autoscaledPool](#autoscaledPool)
* [**browserPool](#browserPool)
* [**config](#config)
* [**hasFinishedBefore](#hasFinishedBefore)
* [**launchContext](#launchContext)
* [**log](#log)
* [**proxyConfiguration](#proxyConfiguration)
* [**requestList](#requestList)
* [**requestQueue](#requestQueue)
* [**router](#router)
* [**running](#running)
* [**sessionPool](#sessionPool)
* [**stats](#stats)

### Methods

* [**addRequests](#addRequests)
* [**exportData](#exportData)
* [**getData](#getData)
* [**getDataset](#getDataset)
* [**getRequestQueue](#getRequestQueue)
* [**pushData](#pushData)
* [**run](#run)
* [**setStatusMessage](#setStatusMessage)
* [**stop](#stop)
* [**useState](#useState)

## Properties<!-- -->[**](#Properties)

### [**](#autoscaledPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L529)optionalinheritedautoscaledPool

**autoscaledPool?

<!-- -->

: [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md)

Inherited from BasicCrawler.autoscaledPool

A reference to the underlying [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) class that manages the concurrency of the crawler.

> *NOTE:* This property is only initialized after calling the [`crawler.run()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#run) function. We can use it to change the concurrency settings on the fly, to pause the crawler by calling [`autoscaledPool.pause()`](https://crawlee.dev/js/api/core/class/AutoscaledPool.md#pause) or to abort it by calling [`autoscaledPool.abort()`](https://crawlee.dev/js/api/core/class/AutoscaledPool.md#abort).

### [**](#browserPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L329)browserPool

**browserPool: [BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md)\<InternalBrowserPoolOptions, [InferBrowserPluginArray](https://crawlee.dev/js/api/browser-pool.md#InferBrowserPluginArray)\<InternalBrowserPoolOptions\[browserPlugins], \[]>, ReturnType<[InferBrowserPluginArray](https://crawlee.dev/js/api/browser-pool.md#InferBrowserPluginArray)\<InternalBrowserPoolOptions\[browserPlugins], \[]>\[number]\[createController]>, ReturnType<[InferBrowserPluginArray](https://crawlee.dev/js/api/browser-pool.md#InferBrowserPluginArray)\<InternalBrowserPoolOptions\[browserPlugins], \[]>\[number]\[createLaunchContext]>, Parameters\<ReturnType<[InferBrowserPluginArray](https://crawlee.dev/js/api/browser-pool.md#InferBrowserPluginArray)\<InternalBrowserPoolOptions\[browserPlugins], \[]>\[number]\[createController]>\[newPage]>\[0], [UnwrapPromise](https://crawlee.dev/js/api/browser-pool.md#UnwrapPromise)\<ReturnType\<ReturnType<[InferBrowserPluginArray](https://crawlee.dev/js/api/browser-pool.md#InferBrowserPluginArray)\<InternalBrowserPoolOptions\[browserPlugins], \[]>\[number]\[createController]>\[newPage]>>>

A reference to the underlying [BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md) class that manages the crawler's browsers.

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L364)readonlyinheritedconfig

**config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) =

<!-- -->

...

Inherited from BasicCrawler.config

### [**](#hasFinishedBefore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L538)inheritedhasFinishedBefore

**hasFinishedBefore: boolean =

<!-- -->

false

Inherited from BasicCrawler.hasFinishedBefore

### [**](#launchContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L331)launchContext

**launchContext: [BrowserLaunchContext](https://crawlee.dev/js/api/browser-crawler/interface/BrowserLaunchContext.md)\<LaunchOptions, unknown>

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L541)readonlyinheritedlog

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

Inherited from BasicCrawler.log

### [**](#proxyConfiguration)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L324)optionalproxyConfiguration

**proxyConfiguration?

<!-- -->

: [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md)

A reference to the underlying [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md) class that manages the crawler's proxies. Only available if used by the crawler.

### [**](#requestList)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L502)optionalinheritedrequestList

**requestList?

<!-- -->

: [IRequestList](https://crawlee.dev/js/api/core/interface/IRequestList.md)

Inherited from BasicCrawler.requestList

A reference to the underlying [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) class that manages the crawler's [requests](https://crawlee.dev/js/api/core/class/Request.md). Only available if used by the crawler.

### [**](#requestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L509)optionalinheritedrequestQueue

**requestQueue?

<!-- -->

: [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)

Inherited from BasicCrawler.requestQueue

Dynamic queue of URLs to be processed. This is useful for recursive crawling of websites. A reference to the underlying [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) class that manages the crawler's [requests](https://crawlee.dev/js/api/core/class/Request.md). Only available if used by the crawler.

### [**](#router)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L535)readonlyinheritedrouter

**router: [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<LoadedContext\<Context>> =

<!-- -->

...

Inherited from BasicCrawler.router

Default [Router](https://crawlee.dev/js/api/core/class/Router.md) instance that will be used if we don't specify any [`requestHandler`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestHandler). See [`router.addHandler()`](https://crawlee.dev/js/api/core/class/Router.md#addHandler) and [`router.addDefaultHandler()`](https://crawlee.dev/js/api/core/class/Router.md#addDefaultHandler).

### [**](#running)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L537)inheritedrunning

**running: boolean =

<!-- -->

false

Inherited from BasicCrawler.running

### [**](#sessionPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L520)optionalinheritedsessionPool

**sessionPool?

<!-- -->

: [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md)

Inherited from BasicCrawler.sessionPool

A reference to the underlying [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) class that manages the crawler's [sessions](https://crawlee.dev/js/api/core/class/Session.md). Only available if used by the crawler.

### [**](#stats)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L496)readonlyinheritedstats

**stats: [Statistics](https://crawlee.dev/js/api/core/class/Statistics.md)

Inherited from BasicCrawler.stats

A reference to the underlying [Statistics](https://crawlee.dev/js/api/core/class/Statistics.md) class that collects and logs run statistics for requests.

## Methods<!-- -->[**](#Methods)

### [**](#addRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1185)inheritedaddRequests

* ****addRequests**(requests, options): Promise<[CrawlerAddRequestsResult](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerAddRequestsResult.md)>

- Inherited from BasicCrawler.addRequests

  Adds requests to the queue in batches. By default, it will resolve after the initial batch is added, and continue adding the rest in background. You can configure the batch size via `batchSize` option and the sleep time in between the batches via `waitBetweenBatchesMillis`. If you want to wait for all batches to be added to the queue, you can use the `waitForAllRequestsToBeAdded` promise you get in the response object.

  This is an alias for calling `addRequestsBatched()` on the implicit `RequestQueue` for this crawler instance.

  ***

  #### Parameters

  * ##### requests: [RequestsLike](https://crawlee.dev/js/api/core.md#RequestsLike)

    The requests to add

  * ##### options: [CrawlerAddRequestsOptions](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerAddRequestsOptions.md) = <!-- -->{}

    Options for the request queue

  #### Returns Promise<[CrawlerAddRequestsResult](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerAddRequestsResult.md)>

### [**](#exportData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1291)inheritedexportData

* ****exportData**\<Data>(path, format, options): Promise\<Data\[]>

- Inherited from BasicCrawler.exportData

  Retrieves all the data from the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) and exports them to the specified format. Supported formats are currently 'json' and 'csv', and will be inferred from the `path` automatically.

  ***

  #### Parameters

  * ##### path: string
  * ##### optionalformat: json | csv
  * ##### optionaloptions: [DatasetExportOptions](https://crawlee.dev/js/api/core/interface/DatasetExportOptions.md)

  #### Returns Promise\<Data\[]>

### [**](#getData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1282)inheritedgetData

* ****getData**(...args): Promise<[DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)\<Dictionary>>

- Inherited from BasicCrawler.getData

  Retrieves data from the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) by calling [Dataset.getData](https://crawlee.dev/js/api/core/class/Dataset.md#getData).

  ***

  #### Parameters

  * ##### rest...args: \[options: [DatasetDataOptions](https://crawlee.dev/js/api/core/interface/DatasetDataOptions.md)]

  #### Returns Promise<[DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)\<Dictionary>>

### [**](#getDataset)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1275)inheritedgetDataset

* ****getDataset**(idOrName): Promise<[Dataset](https://crawlee.dev/js/api/core/class/Dataset.md)\<Dictionary>>

- Inherited from BasicCrawler.getDataset

  Retrieves the specified [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md), or the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md).

  ***

  #### Parameters

  * ##### optionalidOrName: string

  #### Returns Promise<[Dataset](https://crawlee.dev/js/api/core/class/Dataset.md)\<Dictionary>>

### [**](#getRequestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1104)inheritedgetRequestQueue

* ****getRequestQueue**(): Promise<[RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)>

- Inherited from BasicCrawler.getRequestQueue

  #### Returns Promise<[RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)>

### [**](#pushData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1267)inheritedpushData

* ****pushData**(data, datasetIdOrName): Promise\<void>

- Inherited from BasicCrawler.pushData

  Pushes data to the specified [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md), or the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) by calling [Dataset.pushData](https://crawlee.dev/js/api/core/class/Dataset.md#pushData).

  ***

  #### Parameters

  * ##### data: Dictionary | Dictionary\[]
  * ##### optionaldatasetIdOrName: string

  #### Returns Promise\<void>

### [**](#run)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L967)inheritedrun

* ****run**(requests, options): Promise<[FinalStatistics](https://crawlee.dev/js/api/core/interface/FinalStatistics.md)>

- Inherited from BasicCrawler.run

  Runs the crawler. Returns a promise that resolves once all the requests are processed and `autoscaledPool.isFinished` returns `true`.

  We can use the `requests` parameter to enqueue the initial requests — it is a shortcut for running [`crawler.addRequests()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#addRequests) before [`crawler.run()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#run).

  ***

  #### Parameters

  * ##### optionalrequests: [RequestsLike](https://crawlee.dev/js/api/core.md#RequestsLike)

    The requests to add.

  * ##### optionaloptions: [CrawlerRunOptions](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerRunOptions.md)

    Options for the request queue.

  #### Returns Promise<[FinalStatistics](https://crawlee.dev/js/api/core/interface/FinalStatistics.md)>

### [**](#setStatusMessage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L890)inheritedsetStatusMessage

* ****setStatusMessage**(message, options): Promise\<void>

- Inherited from BasicCrawler.setStatusMessage

  This method is periodically called by the crawler, every `statusMessageLoggingInterval` seconds.

  ***

  #### Parameters

  * ##### message: string
  * ##### options: [SetStatusMessageOptions](https://crawlee.dev/js/api/types/interface/SetStatusMessageOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#stop)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1096)inheritedstop

* ****stop**(reason): void

- Inherited from BasicCrawler.stop

  Gracefully stops the current run of the crawler.

  All the tasks active at the time of calling this method will be allowed to finish.

  To stop the crawler immediately, use [`crawler.teardown()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#teardown) instead.

  ***

  #### Parameters

  * ##### reason: string = <!-- -->'The crawler has been gracefully stopped.'

  #### Returns void

### [**](#useState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1126)inheriteduseState

* ****useState**\<State>(defaultValue): Promise\<State>

- Inherited from BasicCrawler.useState

  #### Parameters

  * ##### defaultValue: State = <!-- -->...

  #### Returns Promise\<State>
