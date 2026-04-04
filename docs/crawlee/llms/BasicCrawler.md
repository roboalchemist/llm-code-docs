# Source: https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md

# BasicCrawler<!-- --> \<Context>

Provides a simple framework for parallel crawling of web pages. The URLs to crawl are fed either from a static list of URLs or from a dynamic queue of URLs enabling recursive crawling of websites.

`BasicCrawler` is a low-level tool that requires the user to implement the page download and data extraction functionality themselves. If we want a crawler that already facilitates this functionality, we should consider using [CheerioCrawler](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md), [PuppeteerCrawler](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md) or [PlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md).

`BasicCrawler` invokes the user-provided [`requestHandler`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestHandler) for each [Request](https://crawlee.dev/js/api/core/class/Request.md) object, which represents a single URL to crawl. The [Request](https://crawlee.dev/js/api/core/class/Request.md) objects are fed from the [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) or [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) instances provided by the [`requestList`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestList) or [`requestQueue`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestQueue) constructor options, respectively. If neither `requestList` nor `requestQueue` options are provided, the crawler will open the default request queue either when the [`crawler.addRequests()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#addRequests) function is called, or if `requests` parameter (representing the initial requests) of the [`crawler.run()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#run) function is provided.

If both [`requestList`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestList) and [`requestQueue`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestQueue) options are used, the instance first processes URLs from the [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) and automatically enqueues all of them to the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) before it starts their processing. This ensures that a single URL is not crawled multiple times.

The crawler finishes if there are no more [Request](https://crawlee.dev/js/api/core/class/Request.md) objects to crawl.

New requests are only dispatched when there is enough free CPU and memory available, using the functionality provided by the [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) class. All [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) configuration options can be passed to the [`autoscaledPoolOptions`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#autoscaledPoolOptions) parameter of the `BasicCrawler` constructor. For user convenience, the [`minConcurrency`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#minConcurrency) and [`maxConcurrency`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#maxConcurrency) options of the underlying [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) constructor are available directly in the `BasicCrawler` constructor.

**Example usage:**

```
import { BasicCrawler, Dataset } from 'crawlee';

// Create a crawler instance
const crawler = new BasicCrawler({
    async requestHandler({ request, sendRequest }) {
        // 'request' contains an instance of the Request class
        // Here we simply fetch the HTML of the page and store it to a dataset
        const { body } = await sendRequest({
            url: request.url,
            method: request.method,
            body: request.payload,
            headers: request.headers,
        });

        await Dataset.pushData({
            url: request.url,
            html: body,
        })
    },
});

// Enqueue the initial requests and run the crawler
await crawler.run([
    'http://www.example.com/page-1',
    'http://www.example.com/page-2',
]);
```

### Hierarchy

* *BasicCrawler*

  * [BrowserCrawler](https://crawlee.dev/js/api/browser-crawler/class/BrowserCrawler.md)
  * [HttpCrawler](https://crawlee.dev/js/api/http-crawler/class/HttpCrawler.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**autoscaledPool](#autoscaledPool)
* [**config](#config)
* [**hasFinishedBefore](#hasFinishedBefore)
* [**log](#log)
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
* [**useState](#useState)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L620)constructor

* ****new BasicCrawler**\<Context>(options, config): [BasicCrawler](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md)\<Context>

- All `BasicCrawler` parameters are passed via an options object.

  ***

  #### Parameters

  * ##### options: [BasicCrawlerOptions](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md)\<Context> = <!-- -->{}
  * ##### config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) = <!-- -->...

  #### Returns [BasicCrawler](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md)\<Context>

## Properties<!-- -->[**](#Properties)

### [**](#autoscaledPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L529)optionalautoscaledPool

**autoscaledPool?

<!-- -->

: [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md)

A reference to the underlying [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) class that manages the concurrency of the crawler.

> *NOTE:* This property is only initialized after calling the [`crawler.run()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#run) function. We can use it to change the concurrency settings on the fly, to pause the crawler by calling [`autoscaledPool.pause()`](https://crawlee.dev/js/api/core/class/AutoscaledPool.md#pause) or to abort it by calling [`autoscaledPool.abort()`](https://crawlee.dev/js/api/core/class/AutoscaledPool.md#abort).

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L622)readonlyconfig

**config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) =

<!-- -->

...

### [**](#hasFinishedBefore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L538)hasFinishedBefore

**hasFinishedBefore: boolean =

<!-- -->

false

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L541)readonlylog

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

### [**](#requestList)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L502)optionalrequestList

**requestList?

<!-- -->

: [IRequestList](https://crawlee.dev/js/api/core/interface/IRequestList.md)

A reference to the underlying [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) class that manages the crawler's [requests](https://crawlee.dev/js/api/core/class/Request.md). Only available if used by the crawler.

### [**](#requestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L509)optionalrequestQueue

**requestQueue?

<!-- -->

: [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)

Dynamic queue of URLs to be processed. This is useful for recursive crawling of websites. A reference to the underlying [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) class that manages the crawler's [requests](https://crawlee.dev/js/api/core/class/Request.md). Only available if used by the crawler.

### [**](#router)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L535)readonlyrouter

**router: [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)\<LoadedContext\<Context>> =

<!-- -->

...

Default [Router](https://crawlee.dev/js/api/core/class/Router.md) instance that will be used if we don't specify any [`requestHandler`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestHandler). See [`router.addHandler()`](https://crawlee.dev/js/api/core/class/Router.md#addHandler) and [`router.addDefaultHandler()`](https://crawlee.dev/js/api/core/class/Router.md#addDefaultHandler).

### [**](#running)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L537)running

**running: boolean =

<!-- -->

false

### [**](#sessionPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L520)optionalsessionPool

**sessionPool?

<!-- -->

: [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md)

A reference to the underlying [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) class that manages the crawler's [sessions](https://crawlee.dev/js/api/core/class/Session.md). Only available if used by the crawler.

### [**](#stats)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L496)readonlystats

**stats: [Statistics](https://crawlee.dev/js/api/core/class/Statistics.md)

A reference to the underlying [Statistics](https://crawlee.dev/js/api/core/class/Statistics.md) class that collects and logs run statistics for requests.

## Methods<!-- -->[**](#Methods)

### [**](#addRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1185)addRequests

* ****addRequests**(requests, options): Promise<[CrawlerAddRequestsResult](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerAddRequestsResult.md)>

- Adds requests to the queue in batches. By default, it will resolve after the initial batch is added, and continue adding the rest in background. You can configure the batch size via `batchSize` option and the sleep time in between the batches via `waitBetweenBatchesMillis`. If you want to wait for all batches to be added to the queue, you can use the `waitForAllRequestsToBeAdded` promise you get in the response object.

  This is an alias for calling `addRequestsBatched()` on the implicit `RequestQueue` for this crawler instance.

  ***

  #### Parameters

  * ##### requests: [RequestsLike](https://crawlee.dev/js/api/core.md#RequestsLike)

    The requests to add

  * ##### options: [CrawlerAddRequestsOptions](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerAddRequestsOptions.md) = <!-- -->{}

    Options for the request queue

  #### Returns Promise<[CrawlerAddRequestsResult](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerAddRequestsResult.md)>

### [**](#exportData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1291)exportData

* ****exportData**\<Data>(path, format, options): Promise\<Data\[]>

- Retrieves all the data from the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) and exports them to the specified format. Supported formats are currently 'json' and 'csv', and will be inferred from the `path` automatically.

  ***

  #### Parameters

  * ##### path: string
  * ##### optionalformat: json | csv
  * ##### optionaloptions: [DatasetExportOptions](https://crawlee.dev/js/api/core/interface/DatasetExportOptions.md)

  #### Returns Promise\<Data\[]>

### [**](#getData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1282)getData

* ****getData**(...args): Promise<[DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)\<Dictionary>>

- Retrieves data from the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) by calling [Dataset.getData](https://crawlee.dev/js/api/core/class/Dataset.md#getData).

  ***

  #### Parameters

  * ##### rest...args: \[options: [DatasetDataOptions](https://crawlee.dev/js/api/core/interface/DatasetDataOptions.md)]

  #### Returns Promise<[DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)\<Dictionary>>

### [**](#getDataset)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1275)getDataset

* ****getDataset**(idOrName): Promise<[Dataset](https://crawlee.dev/js/api/core/class/Dataset.md)\<Dictionary>>

- Retrieves the specified [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md), or the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md).

  ***

  #### Parameters

  * ##### optionalidOrName: string

  #### Returns Promise<[Dataset](https://crawlee.dev/js/api/core/class/Dataset.md)\<Dictionary>>

### [**](#getRequestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1104)getRequestQueue

* ****getRequestQueue**(): Promise<[RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)>

- #### Returns Promise<[RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)>

### [**](#pushData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1267)pushData

* ****pushData**(data, datasetIdOrName): Promise\<void>

- Pushes data to the specified [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md), or the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) by calling [Dataset.pushData](https://crawlee.dev/js/api/core/class/Dataset.md#pushData).

  ***

  #### Parameters

  * ##### data: Dictionary | Dictionary\[]
  * ##### optionaldatasetIdOrName: string

  #### Returns Promise\<void>

### [**](#run)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L967)run

* ****run**(requests, options): Promise<[FinalStatistics](https://crawlee.dev/js/api/core/interface/FinalStatistics.md)>

- Runs the crawler. Returns a promise that resolves once all the requests are processed and `autoscaledPool.isFinished` returns `true`.

  We can use the `requests` parameter to enqueue the initial requests — it is a shortcut for running [`crawler.addRequests()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#addRequests) before [`crawler.run()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#run).

  ***

  #### Parameters

  * ##### optionalrequests: [RequestsLike](https://crawlee.dev/js/api/core.md#RequestsLike)

    The requests to add.

  * ##### optionaloptions: [CrawlerRunOptions](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerRunOptions.md)

    Options for the request queue.

  #### Returns Promise<[FinalStatistics](https://crawlee.dev/js/api/core/interface/FinalStatistics.md)>

### [**](#setStatusMessage)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L890)setStatusMessage

* ****setStatusMessage**(message, options): Promise\<void>

- This method is periodically called by the crawler, every `statusMessageLoggingInterval` seconds.

  ***

  #### Parameters

  * ##### message: string
  * ##### options: [SetStatusMessageOptions](https://crawlee.dev/js/api/types/interface/SetStatusMessageOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#stop)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1096)stop

* ****stop**(reason): void

- Gracefully stops the current run of the crawler.

  All the tasks active at the time of calling this method will be allowed to finish.

  To stop the crawler immediately, use [`crawler.teardown()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#teardown) instead.

  ***

  #### Parameters

  * ##### reason: string = <!-- -->'The crawler has been gracefully stopped.'

  #### Returns void

### [**](#teardown)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1982)teardown

* ****teardown**(): Promise\<void>

- Stops the crawler immediately.

  This method doesn't wait for currently active requests to finish.

  To stop the crawler gracefully (waiting for all running requests to finish), use [`crawler.stop()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#stop) instead.

  ***

  #### Returns Promise\<void>

### [**](#useState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1126)useState

* ****useState**\<State>(defaultValue): Promise\<State>

- #### Parameters

  * ##### defaultValue: State = <!-- -->...

  #### Returns Promise\<State>
