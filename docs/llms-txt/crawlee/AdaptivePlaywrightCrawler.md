# Source: https://crawlee.dev/js/api/playwright-crawler/class/AdaptivePlaywrightCrawler.md

# AdaptivePlaywrightCrawler<!-- -->

experimental

An extension of [PlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md) that uses a more limited request handler interface so that it is able to switch to HTTP-only crawling when it detects it may be possible.

**Example usage:**

```
const crawler = new AdaptivePlaywrightCrawler({
    renderingTypeDetectionRatio: 0.1,
    async requestHandler({ querySelector, pushData, enqueueLinks, request, log }) {
        // This function is called to extract data from a single web page
        const $prices = await querySelector('span.price')

        await pushData({
            url: request.url,
            price: $prices.filter(':contains("$")').first().text(),
        })

        await enqueueLinks({ selector: '.pagination a' })
    },
});

await crawler.run([
    'http://www.example.com/page-1',
    'http://www.example.com/page-2',
]);
```

### Hierarchy

* [PlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md)
  * *AdaptivePlaywrightCrawler*

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

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

### Accessors

* [**inFlightRenderingTypeDetectionCount](#inFlightRenderingTypeDetectionCount)

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

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L283)constructor

* ****new AdaptivePlaywrightCrawler**(options, config): [AdaptivePlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/AdaptivePlaywrightCrawler.md)

- Overrides PlaywrightCrawler.constructor

  experimental

  #### Parameters

  * ##### options: [AdaptivePlaywrightCrawlerOptions](https://crawlee.dev/js/api/playwright-crawler/interface/AdaptivePlaywrightCrawlerOptions.md) = <!-- -->{}
  * ##### config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) = <!-- -->...

  #### Returns [AdaptivePlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/AdaptivePlaywrightCrawler.md)

## Properties<!-- -->[**](#Properties)

### [**](#autoscaledPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L529)optionalinheritedautoscaledPoolexperimental

**autoscaledPool?

<!-- -->

: [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md)

Inherited from PlaywrightCrawler.autoscaledPool

A reference to the underlying [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) class that manages the concurrency of the crawler.

> *NOTE:* This property is only initialized after calling the [`crawler.run()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#run) function. We can use it to change the concurrency settings on the fly, to pause the crawler by calling [`autoscaledPool.pause()`](https://crawlee.dev/js/api/core/class/AutoscaledPool.md#pause) or to abort it by calling [`autoscaledPool.abort()`](https://crawlee.dev/js/api/core/class/AutoscaledPool.md#abort).

### [**](#browserPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L329)inheritedbrowserPoolexperimental

**browserPool: [BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md)<{ browserPlugins: \[[PlaywrightPlugin](https://crawlee.dev/js/api/browser-pool/class/PlaywrightPlugin.md)] }, \[[PlaywrightPlugin](https://crawlee.dev/js/api/browser-pool/class/PlaywrightPlugin.md)], [BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)\<BrowserType<{}>, undefined | LaunchOptions, Browser, undefined | { acceptDownloads?

<!-- -->

: boolean; baseURL?

<!-- -->

: string; bypassCSP?

<!-- -->

: boolean; clientCertificates?

<!-- -->

: { cert?

<!-- -->

: Buffer\<ArrayBufferLike>; certPath?

<!-- -->

: string; key?

<!-- -->

: Buffer\<ArrayBufferLike>; keyPath?

<!-- -->

: string; origin: string; passphrase?

<!-- -->

: string; pfx?

<!-- -->

: Buffer\<ArrayBufferLike>; pfxPath?

<!-- -->

: string }\[]; colorScheme?

<!-- -->

: null | light | dark | no-preference; contrast?

<!-- -->

: null | no-preference | more; deviceScaleFactor?

<!-- -->

: number; extraHTTPHeaders?

<!-- -->

: {}; forcedColors?

<!-- -->

: null | active | none; geolocation?

<!-- -->

: { accuracy?

<!-- -->

: number; latitude: number; longitude: number }; hasTouch?

<!-- -->

: boolean; httpCredentials?

<!-- -->

: { origin?

<!-- -->

: string; password: string; send?

<!-- -->

: unauthorized | always; username: string }; ignoreHTTPSErrors?

<!-- -->

: boolean; isMobile?

<!-- -->

: boolean; javaScriptEnabled?

<!-- -->

: boolean; locale?

<!-- -->

: string; logger?

<!-- -->

: Logger; offline?

<!-- -->

: boolean; permissions?

<!-- -->

: string\[]; proxy?

<!-- -->

: { bypass?

<!-- -->

: string; password?

<!-- -->

: string; server: string; username?

<!-- -->

: string }; recordHar?

<!-- -->

: { content?

<!-- -->

: omit | embed | attach; mode?

<!-- -->

: full | minimal; omitContent?

<!-- -->

: boolean; path: string; urlFilter?

<!-- -->

: string | RegExp }; recordVideo?

<!-- -->

: { dir: string; size?

<!-- -->

: { height: number; width: number } }; reducedMotion?

<!-- -->

: null | reduce | no-preference; screen?

<!-- -->

: { height: number; width: number }; serviceWorkers?

<!-- -->

: allow | block; storageState?

<!-- -->

: string | { cookies: { domain: string; expires: number; httpOnly: boolean; name: string; path: string; sameSite: Strict | Lax | None; secure: boolean; value: string }\[]; origins: { localStorage: { name: string; value: string }\[]; origin: string }\[] }; strictSelectors?

<!-- -->

: boolean; timezoneId?

<!-- -->

: string; userAgent?

<!-- -->

: string; videoSize?

<!-- -->

: { height: number; width: number }; videosPath?

<!-- -->

: string; viewport?

<!-- -->

: null | { height: number; width: number } }, Page>, [LaunchContext](https://crawlee.dev/js/api/browser-pool/class/LaunchContext.md)\<BrowserType<{}>, undefined | LaunchOptions, Browser, undefined | { acceptDownloads?

<!-- -->

: boolean; baseURL?

<!-- -->

: string; bypassCSP?

<!-- -->

: boolean; clientCertificates?

<!-- -->

: { cert?

<!-- -->

: Buffer\<ArrayBufferLike>; certPath?

<!-- -->

: string; key?

<!-- -->

: Buffer\<ArrayBufferLike>; keyPath?

<!-- -->

: string; origin: string; passphrase?

<!-- -->

: string; pfx?

<!-- -->

: Buffer\<ArrayBufferLike>; pfxPath?

<!-- -->

: string }\[]; colorScheme?

<!-- -->

: null | light | dark | no-preference; contrast?

<!-- -->

: null | no-preference | more; deviceScaleFactor?

<!-- -->

: number; extraHTTPHeaders?

<!-- -->

: {}; forcedColors?

<!-- -->

: null | active | none; geolocation?

<!-- -->

: { accuracy?

<!-- -->

: number; latitude: number; longitude: number }; hasTouch?

<!-- -->

: boolean; httpCredentials?

<!-- -->

: { origin?

<!-- -->

: string; password: string; send?

<!-- -->

: unauthorized | always; username: string }; ignoreHTTPSErrors?

<!-- -->

: boolean; isMobile?

<!-- -->

: boolean; javaScriptEnabled?

<!-- -->

: boolean; locale?

<!-- -->

: string; logger?

<!-- -->

: Logger; offline?

<!-- -->

: boolean; permissions?

<!-- -->

: string\[]; proxy?

<!-- -->

: { bypass?

<!-- -->

: string; password?

<!-- -->

: string; server: string; username?

<!-- -->

: string }; recordHar?

<!-- -->

: { content?

<!-- -->

: omit | embed | attach; mode?

<!-- -->

: full | minimal; omitContent?

<!-- -->

: boolean; path: string; urlFilter?

<!-- -->

: string | RegExp }; recordVideo?

<!-- -->

: { dir: string; size?

<!-- -->

: { height: number; width: number } }; reducedMotion?

<!-- -->

: null | reduce | no-preference; screen?

<!-- -->

: { height: number; width: number }; serviceWorkers?

<!-- -->

: allow | block; storageState?

<!-- -->

: string | { cookies: { domain: string; expires: number; httpOnly: boolean; name: string; path: string; sameSite: Strict | Lax | None; secure: boolean; value: string }\[]; origins: { localStorage: { name: string; value: string }\[]; origin: string }\[] }; strictSelectors?

<!-- -->

: boolean; timezoneId?

<!-- -->

: string; userAgent?

<!-- -->

: string; videoSize?

<!-- -->

: { height: number; width: number }; videosPath?

<!-- -->

: string; viewport?

<!-- -->

: null | { height: number; width: number } }, Page>, undefined | { acceptDownloads?

<!-- -->

: boolean; baseURL?

<!-- -->

: string; bypassCSP?

<!-- -->

: boolean; clientCertificates?

<!-- -->

: { cert?

<!-- -->

: Buffer\<ArrayBufferLike>; certPath?

<!-- -->

: string; key?

<!-- -->

: Buffer\<ArrayBufferLike>; keyPath?

<!-- -->

: string; origin: string; passphrase?

<!-- -->

: string; pfx?

<!-- -->

: Buffer\<ArrayBufferLike>; pfxPath?

<!-- -->

: string }\[]; colorScheme?

<!-- -->

: null | light | dark | no-preference; contrast?

<!-- -->

: null | no-preference | more; deviceScaleFactor?

<!-- -->

: number; extraHTTPHeaders?

<!-- -->

: {}; forcedColors?

<!-- -->

: null | active | none; geolocation?

<!-- -->

: { accuracy?

<!-- -->

: number; latitude: number; longitude: number }; hasTouch?

<!-- -->

: boolean; httpCredentials?

<!-- -->

: { origin?

<!-- -->

: string; password: string; send?

<!-- -->

: unauthorized | always; username: string }; ignoreHTTPSErrors?

<!-- -->

: boolean; isMobile?

<!-- -->

: boolean; javaScriptEnabled?

<!-- -->

: boolean; locale?

<!-- -->

: string; logger?

<!-- -->

: Logger; offline?

<!-- -->

: boolean; permissions?

<!-- -->

: string\[]; proxy?

<!-- -->

: { bypass?

<!-- -->

: string; password?

<!-- -->

: string; server: string; username?

<!-- -->

: string }; recordHar?

<!-- -->

: { content?

<!-- -->

: omit | embed | attach; mode?

<!-- -->

: full | minimal; omitContent?

<!-- -->

: boolean; path: string; urlFilter?

<!-- -->

: string | RegExp }; recordVideo?

<!-- -->

: { dir: string; size?

<!-- -->

: { height: number; width: number } }; reducedMotion?

<!-- -->

: null | reduce | no-preference; screen?

<!-- -->

: { height: number; width: number }; serviceWorkers?

<!-- -->

: allow | block; storageState?

<!-- -->

: string | { cookies: { domain: string; expires: number; httpOnly: boolean; name: string; path: string; sameSite: Strict | Lax | None; secure: boolean; value: string }\[]; origins: { localStorage: { name: string; value: string }\[]; origin: string }\[] }; strictSelectors?

<!-- -->

: boolean; timezoneId?

<!-- -->

: string; userAgent?

<!-- -->

: string; videoSize?

<!-- -->

: { height: number; width: number }; videosPath?

<!-- -->

: string; viewport?

<!-- -->

: null | { height: number; width: number } }, Page>

Inherited from PlaywrightCrawler.browserPool

A reference to the underlying [BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md) class that manages the crawler's browsers.

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L285)readonlyinheritedconfigexperimental

**config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) =

<!-- -->

...

Inherited from PlaywrightCrawler.config

### [**](#hasFinishedBefore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L538)inheritedhasFinishedBeforeexperimental

**hasFinishedBefore: boolean =

<!-- -->

false

Inherited from PlaywrightCrawler.hasFinishedBefore

### [**](#launchContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L331)inheritedlaunchContextexperimental

**launchContext: [BrowserLaunchContext](https://crawlee.dev/js/api/browser-crawler/interface/BrowserLaunchContext.md)\<LaunchOptions, unknown>

Inherited from PlaywrightCrawler.launchContext

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L541)readonlyinheritedlogexperimental

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

Inherited from PlaywrightCrawler.log

### [**](#proxyConfiguration)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L324)optionalinheritedproxyConfigurationexperimental

**proxyConfiguration?

<!-- -->

: [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md)

Inherited from PlaywrightCrawler.proxyConfiguration

A reference to the underlying [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md) class that manages the crawler's proxies. Only available if used by the crawler.

### [**](#requestList)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L502)optionalinheritedrequestListexperimental

**requestList?

<!-- -->

: [IRequestList](https://crawlee.dev/js/api/core/interface/IRequestList.md)

Inherited from PlaywrightCrawler.requestList

A reference to the underlying [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) class that manages the crawler's [requests](https://crawlee.dev/js/api/core/class/Request.md). Only available if used by the crawler.

### [**](#requestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L509)optionalinheritedrequestQueueexperimental

**requestQueue?

<!-- -->

: [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)

Inherited from PlaywrightCrawler.requestQueue

Dynamic queue of URLs to be processed. This is useful for recursive crawling of websites. A reference to the underlying [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) class that manages the crawler's [requests](https://crawlee.dev/js/api/core/class/Request.md). Only available if used by the crawler.

### [**](#router)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L280)readonlyrouterexperimental

**router: [RouterHandler](https://crawlee.dev/js/api/core/interface/RouterHandler.md)<[AdaptivePlaywrightCrawlerContext](https://crawlee.dev/js/api/playwright-crawler/interface/AdaptivePlaywrightCrawlerContext.md)\<Dictionary>> =

<!-- -->

...

Overrides PlaywrightCrawler.router

Default [Router](https://crawlee.dev/js/api/core/class/Router.md) instance that will be used if we don't specify any [`requestHandler`](https://crawlee.dev/js/api/playwright-crawler/interface/AdaptivePlaywrightCrawlerOptions.md#requestHandler). See [`router.addHandler()`](https://crawlee.dev/js/api/core/class/Router.md#addHandler) and [`router.addDefaultHandler()`](https://crawlee.dev/js/api/core/class/Router.md#addDefaultHandler).

### [**](#running)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L537)inheritedrunningexperimental

**running: boolean =

<!-- -->

false

Inherited from PlaywrightCrawler.running

### [**](#sessionPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L520)optionalinheritedsessionPoolexperimental

**sessionPool?

<!-- -->

: [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md)

Inherited from PlaywrightCrawler.sessionPool

A reference to the underlying [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) class that manages the crawler's [sessions](https://crawlee.dev/js/api/core/class/Session.md). Only available if used by the crawler.

### [**](#stats)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L272)readonlystatsexperimental

**stats: AdaptivePlaywrightCrawlerStatistics

Overrides PlaywrightCrawler.stats

A reference to the underlying [Statistics](https://crawlee.dev/js/api/core/class/Statistics.md) class that collects and logs run statistics for requests.

## Accessors<!-- -->[**](#Accessors)

### [**](#inFlightRenderingTypeDetectionCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L332)inFlightRenderingTypeDetectionCount

* **get inFlightRenderingTypeDetectionCount(): number

- experimental

  Returns the number of rendering type detections currently in progress.

  ***

  #### Returns number

## Methods<!-- -->[**](#Methods)

### [**](#addRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1185)inheritedaddRequests

* ****addRequests**(requests, options): Promise<[CrawlerAddRequestsResult](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerAddRequestsResult.md)>

- Inherited from PlaywrightCrawler.addRequests

  experimental

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

- Inherited from PlaywrightCrawler.exportData

  experimental

  Retrieves all the data from the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) and exports them to the specified format. Supported formats are currently 'json' and 'csv', and will be inferred from the `path` automatically.

  ***

  #### Parameters

  * ##### path: string
  * ##### optionalformat: json | csv
  * ##### optionaloptions: [DatasetExportOptions](https://crawlee.dev/js/api/core/interface/DatasetExportOptions.md)

  #### Returns Promise\<Data\[]>

### [**](#getData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1282)inheritedgetData

* ****getData**(...args): Promise<[DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)\<Dictionary>>

- Inherited from PlaywrightCrawler.getData

  experimental

  Retrieves data from the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) by calling [Dataset.getData](https://crawlee.dev/js/api/core/class/Dataset.md#getData).

  ***

  #### Parameters

  * ##### rest...args: \[options: [DatasetDataOptions](https://crawlee.dev/js/api/core/interface/DatasetDataOptions.md)]

  #### Returns Promise<[DatasetContent](https://crawlee.dev/js/api/core/interface/DatasetContent.md)\<Dictionary>>

### [**](#getDataset)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1275)inheritedgetDataset

* ****getDataset**(idOrName): Promise<[Dataset](https://crawlee.dev/js/api/core/class/Dataset.md)\<Dictionary>>

- Inherited from PlaywrightCrawler.getDataset

  experimental

  Retrieves the specified [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md), or the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md).

  ***

  #### Parameters

  * ##### optionalidOrName: string

  #### Returns Promise<[Dataset](https://crawlee.dev/js/api/core/class/Dataset.md)\<Dictionary>>

### [**](#getRequestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1104)inheritedgetRequestQueue

* ****getRequestQueue**(): Promise<[RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)>

- Inherited from PlaywrightCrawler.getRequestQueue

  experimental

  #### Returns Promise<[RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)>

### [**](#pushData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1267)inheritedpushData

* ****pushData**(data, datasetIdOrName): Promise\<void>

- Inherited from PlaywrightCrawler.pushData

  experimental

  Pushes data to the specified [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md), or the default crawler [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) by calling [Dataset.pushData](https://crawlee.dev/js/api/core/class/Dataset.md#pushData).

  ***

  #### Parameters

  * ##### data: Dictionary | Dictionary\[]
  * ##### optionaldatasetIdOrName: string

  #### Returns Promise\<void>

### [**](#run)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L967)inheritedrun

* ****run**(requests, options): Promise<[FinalStatistics](https://crawlee.dev/js/api/core/interface/FinalStatistics.md)>

- Inherited from PlaywrightCrawler.run

  experimental

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

- Inherited from PlaywrightCrawler.setStatusMessage

  experimental

  This method is periodically called by the crawler, every `statusMessageLoggingInterval` seconds.

  ***

  #### Parameters

  * ##### message: string
  * ##### options: [SetStatusMessageOptions](https://crawlee.dev/js/api/types/interface/SetStatusMessageOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#stop)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1096)inheritedstop

* ****stop**(reason): void

- Inherited from PlaywrightCrawler.stop

  experimental

  Gracefully stops the current run of the crawler.

  All the tasks active at the time of calling this method will be allowed to finish.

  To stop the crawler immediately, use [`crawler.teardown()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#teardown) instead.

  ***

  #### Parameters

  * ##### reason: string = <!-- -->'The crawler has been gracefully stopped.'

  #### Returns void

### [**](#useState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L1126)inheriteduseState

* ****useState**\<State>(defaultValue): Promise\<State>

- Inherited from PlaywrightCrawler.useState

  experimental

  #### Parameters

  * ##### defaultValue: State = <!-- -->...

  #### Returns Promise\<State>
