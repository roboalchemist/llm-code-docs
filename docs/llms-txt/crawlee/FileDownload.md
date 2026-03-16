# Source: https://crawlee.dev/js/api/http-crawler/class/FileDownload.md

# FileDownload<!-- -->

Provides a framework for downloading files in parallel using plain HTTP requests. The URLs to download are fed either from a static list of URLs or they can be added on the fly from another crawler.

Since `FileDownload` uses raw HTTP requests to download the files, it is very fast and bandwidth-efficient. However, it doesn't parse the content - if you need to e.g. extract data from the downloaded files, you might need to use [CheerioCrawler](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md), [PuppeteerCrawler](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md) or [PlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md) instead.

`FileCrawler` downloads each URL using a plain HTTP request and then invokes the user-provided FileDownloadOptions.requestHandler where the user can specify what to do with the downloaded data.

The source URLs are represented using [Request](https://crawlee.dev/js/api/core/class/Request.md) objects that are fed from [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) or [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) instances provided by the FileDownloadOptions.requestList or FileDownloadOptions.requestQueue constructor options, respectively.

If both FileDownloadOptions.requestList and FileDownloadOptions.requestQueue are used, the instance first processes URLs from the [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) and automatically enqueues all of them to [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) before it starts their processing. This ensures that a single URL is not crawled multiple times.

The crawler finishes when there are no more [Request](https://crawlee.dev/js/api/core/class/Request.md) objects to crawl.

We can use the `preNavigationHooks` to adjust `gotOptions`:

```
preNavigationHooks: [
    (crawlingContext, gotOptions) => {
        // ...
    },
]
```

New requests are only dispatched when there is enough free CPU and memory available, using the functionality provided by the [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) class. All [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) configuration options can be passed to the `autoscaledPoolOptions` parameter of the `FileCrawler` constructor. For user convenience, the `minConcurrency` and `maxConcurrency` [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) options are available directly in the `FileCrawler` constructor.

## Example usage

```
const crawler = new FileDownloader({
    requestHandler({ body, request }) {
        writeFileSync(request.url.replace(/[^a-z0-9\.]/gi, '_'), body);
    },
});

await crawler.run([
    'http://www.example.com/document.pdf',
    'http://www.example.com/sound.mp3',
    'http://www.example.com/video.mkv',
]);
```

### Hierarchy

* [HttpCrawler](https://crawlee.dev/js/api/http-crawler/class/HttpCrawler.md)<[FileDownloadCrawlingContext](https://crawlee.dev/js/api/http-crawler/interface/FileDownloadCrawlingContext.md)>
  * *FileDownload*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**autoscaledPool](#autoscaledPool)
* [**config](#config)
* [**hasFinishedBefore](#hasFinishedBefore)
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
* [**teardown](#teardown)
* [**use](#use)
* [**useState](#useState)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/file-download.ts#L190)constructor

* ****new FileDownload**(options): [FileDownload](https://crawlee.dev/js/api/http-crawler/class/FileDownload.md)

- Overrides HttpCrawler.constructor

  #### Parameters

  * ##### options: [FileDownloadOptions](https://crawlee.dev/js/api/http-crawler.md#FileDownloadOptions)\<any, any> = <!-- -->{}

  #### Returns [FileDownload](https://crawlee.dev/js/api/http-crawler/class/FileDownload.md)

## Properties<!-- -->[**](#Properties)

### [**](#autoscaledPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L529)optionalinheritedautoscaledPool

**autoscaledPool?

<!-- -->

: [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md)

Inherited from HttpCrawler.autoscaledPool

A reference to the underlying [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) class that manages the concurrency of the crawler.

> *NOTE:* This property is only initialized after calling the [`crawler.run()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#run) function. We can use it to change the concurrency settings on the fly, to pause the crawler by calling [`autoscaledPool.pause()`](https://crawlee.dev/js/api/core/class/AutoscaledPool.md#pause) or to abort it by calling [`autoscaledPool.abort()`](https://crawlee.dev/js/api/core/class/AutoscaledPool.md#abort).

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L376)readonlyinheritedconfig

**config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) =

<!-- -->

...

Inherited from HttpCrawler.config

### [**](#hasFinishedBefore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L538)inheritedhasFinishedBefore

**hasFinishedBefore: boolean =

<!-- -->

false

Inherited from HttpCrawler.hasFinishedBefore

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L541)readonlyinheritedlog

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

Inherited from HttpCrawler.log

### [**](#proxyConfiguration)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L338)optionalinheritedproxyConfiguration

**proxyConfiguration?

<!-- -->

: [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md)

Inherited from HttpCrawler.proxyConfiguration

A reference to the underlying [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md) class that manages the crawler's proxies. Only available if used by the crawler.

### [**](#requestList)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L502)optionalinheritedrequestList

**requestList?

<!-- -->

: [IRequestList](https://crawlee.dev/js/api/core/interface/IRequestList.md)

Inherited from HttpCrawler.requestList

A reference to the underlying [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) class that manages the crawler's [requests](https://crawlee.dev/js/api/core/class/Request.md). Only available if used by the crawler.

### [**](#requestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L509)optionalinheritedrequestQueue

**requestQueue?

<!-- -->

: [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)

Inherited from HttpCrawler.requestQueue

Dynamic queue of URLs to be processed. This is useful for recursive crawling of websites. A reference to the underlying [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) class that manages the crawler's [requests](https://crawlee.dev/js/api/core/class/Request.md). Only available if used by the crawler.

### [**](#router)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L535)readonlyinheritedrouter

**router: [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)<{ request: [LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<any>> } & Omit<[FileDownloadCrawlingContext](https://crawlee.dev/js/api/http-crawler/interface/FileDownloadCrawlingContext.md)\<any, any>, request>> =

<!-- -->

...

Inherited from HttpCrawler.router

Default [Router](https://crawlee.dev/js/api/core/class/Router.md) instance that will be used if we don't specify any [`requestHandler`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestHandler). See [`router.addHandler()`](https://crawlee.dev/js/api/core/class/Router.md#addHandler) and [`router.addDefaultHandler()`](https://crawlee.dev/js/api/core/class/Router.md#addDefaultHandler).

### [**](#running)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L537)inheritedrunning

**running: boolean =

<!-- -->

false

Inherited from HttpCrawler.running

### [**](#sessionPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L520)optionalinheritedsessionPool

**sessionPool?

<!-- -->

: [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md)

Inherited from HttpCrawler.sessionPool

A reference to the underlying [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) class that manages the crawler's [sessions](https://crawlee.dev/js/api/core/class/Session.md). Only available if used by the crawler.

### [**](#stats)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L496)readonlyinheritedstats

**stats: [Statistics](https://crawlee.dev/js/api/core/class/Statistics.md)

Inherited from HttpCrawler.stats

A reference to the underlying [Statistics](https://crawlee.dev/js/api/core/class/Statistics.md) class that collects and logs run statistics for requests.

## Methods<!-- -->[**](#Methods)

### [**](#addRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1185)inheritedaddRequests

* ****addRequests**(requests, options): Promise<[CrawlerAddRequestsResult](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerAddRequestsResult.md)>

- Inherited from HttpCrawler.addRequests

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

- Inherited from HttpCrawler.exportData

  Retrieves all the data from the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) and exports them to the specified format. Supported formats are currently 'json' and 'csv', and will be inferred from the `path` automatically.

  ***

  #### Parameters

  * ##### path: string
  * ##### optionalformat: json | csv
  * ##### optionaloptions: [DatasetExportOptions](https://crawlee.dev/js/api/core/interface/DatasetExportOptions.md)

  #### Returns Promise\<Data\[]>

### [**](#getData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1282)inheritedgetData

* ****getData**(...args): Promise<[DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)\<Dictionary>>

- Inherited from HttpCrawler.getData

  Retrieves data from the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) by calling [Dataset.getData](https://crawlee.dev/js/api/core/class/Dataset.md#getData).

  ***

  #### Parameters

  * ##### rest...args: \[options: [DatasetDataOptions](https://crawlee.dev/js/api/core/interface/DatasetDataOptions.md)]

  #### Returns Promise<[DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)\<Dictionary>>

### [**](#getDataset)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1275)inheritedgetDataset

* ****getDataset**(idOrName): Promise<[Dataset](https://crawlee.dev/js/api/core/class/Dataset.md)\<Dictionary>>

- Inherited from HttpCrawler.getDataset

  Retrieves the specified [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md), or the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md).

  ***

  #### Parameters

  * ##### optionalidOrName: string

  #### Returns Promise<[Dataset](https://crawlee.dev/js/api/core/class/Dataset.md)\<Dictionary>>

### [**](#getRequestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1104)inheritedgetRequestQueue

* ****getRequestQueue**(): Promise<[RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)>

- Inherited from HttpCrawler.getRequestQueue

  #### Returns Promise<[RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)>

### [**](#pushData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1267)inheritedpushData

* ****pushData**(data, datasetIdOrName): Promise\<void>

- Inherited from HttpCrawler.pushData

  Pushes data to the specified [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md), or the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) by calling [Dataset.pushData](https://crawlee.dev/js/api/core/class/Dataset.md#pushData).

  ***

  #### Parameters

  * ##### data: Dictionary | Dictionary\[]
  * ##### optionaldatasetIdOrName: string

  #### Returns Promise\<void>

### [**](#run)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L967)inheritedrun

* ****run**(requests, options): Promise<[FinalStatistics](https://crawlee.dev/js/api/core/interface/FinalStatistics.md)>

- Inherited from HttpCrawler.run

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

- Inherited from HttpCrawler.setStatusMessage

  This method is periodically called by the crawler, every `statusMessageLoggingInterval` seconds.

  ***

  #### Parameters

  * ##### message: string
  * ##### options: [SetStatusMessageOptions](https://crawlee.dev/js/api/types/interface/SetStatusMessageOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#stop)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1096)inheritedstop

* ****stop**(reason): void

- Inherited from HttpCrawler.stop

  Gracefully stops the current run of the crawler.

  All the tasks active at the time of calling this method will be allowed to finish.

  To stop the crawler immediately, use [`crawler.teardown()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#teardown) instead.

  ***

  #### Parameters

  * ##### reason: string = <!-- -->'The crawler has been gracefully stopped.'

  #### Returns void

### [**](#teardown)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1982)inheritedteardown

* ****teardown**(): Promise\<void>

- Inherited from HttpCrawler.teardown

  Stops the crawler immediately.

  This method doesn't wait for currently active requests to finish.

  To stop the crawler gracefully (waiting for all running requests to finish), use [`crawler.stop()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#stop) instead.

  ***

  #### Returns Promise\<void>

### [**](#use)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L471)inheriteduse

* ****use**(extension): void

- Inherited from HttpCrawler.use

  **EXPERIMENTAL** Function for attaching CrawlerExtensions such as the Unblockers.

  ***

  #### Parameters

  * ##### extension: CrawlerExtension

    Crawler extension that overrides the crawler configuration.

  #### Returns void

### [**](#useState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1126)inheriteduseState

* ****useState**\<State>(defaultValue): Promise\<State>

- Inherited from HttpCrawler.useState

  #### Parameters

  * ##### defaultValue: State = <!-- -->...

  #### Returns Promise\<State>
