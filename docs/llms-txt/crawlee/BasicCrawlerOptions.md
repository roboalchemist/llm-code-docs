# Source: https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md

# BasicCrawlerOptions<!-- --> \<Context>

### Hierarchy

* *BasicCrawlerOptions*
  * [HttpCrawlerOptions](https://crawlee.dev/js/api/http-crawler/interface/HttpCrawlerOptions.md)

## Index[**](#Index)

### Properties

* [**autoscaledPoolOptions](#autoscaledPoolOptions)
* [**errorHandler](#errorHandler)
* [**experiments](#experiments)
* [**failedRequestHandler](#failedRequestHandler)
* [**httpClient](#httpClient)
* [**keepAlive](#keepAlive)
* [**maxConcurrency](#maxConcurrency)
* [**maxCrawlDepth](#maxCrawlDepth)
* [**maxRequestRetries](#maxRequestRetries)
* [**maxRequestsPerCrawl](#maxRequestsPerCrawl)
* [**maxRequestsPerMinute](#maxRequestsPerMinute)
* [**maxSessionRotations](#maxSessionRotations)
* [**minConcurrency](#minConcurrency)
* [**onSkippedRequest](#onSkippedRequest)
* [**requestHandler](#requestHandler)
* [**requestHandlerTimeoutSecs](#requestHandlerTimeoutSecs)
* [**requestList](#requestList)
* [**requestManager](#requestManager)
* [**requestQueue](#requestQueue)
* [**respectRobotsTxtFile](#respectRobotsTxtFile)
* [**retryOnBlocked](#retryOnBlocked)
* [**sameDomainDelaySecs](#sameDomainDelaySecs)
* [**sessionPoolOptions](#sessionPoolOptions)
* [**statisticsOptions](#statisticsOptions)
* [**statusMessageCallback](#statusMessageCallback)
* [**statusMessageLoggingInterval](#statusMessageLoggingInterval)
* [**useSessionPool](#useSessionPool)

## Properties<!-- -->[**](#Properties)

### [**](#autoscaledPoolOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L296)optionalautoscaledPoolOptions

**autoscaledPoolOptions?

<!-- -->

: [AutoscaledPoolOptions](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md)

Custom options passed to the underlying [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) constructor.

> *NOTE:* The [`runTaskFunction`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#runTaskFunction) option is provided by the crawler and cannot be overridden. However, we can provide custom implementations of [`isFinishedFunction`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#isFinishedFunction) and [`isTaskReadyFunction`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#isTaskReadyFunction).

### [**](#errorHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L224)optionalerrorHandler

**errorHandler?

<!-- -->

: [ErrorHandler](https://crawlee.dev/js/api/basic-crawler.md#ErrorHandler)\<Context>

User-provided function that allows modifying the request object before it gets retried by the crawler. It's executed before each retry for the requests that failed less than [`maxRequestRetries`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxRequestRetries) times.

The function receives the [BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md) as the first argument, where the [`request`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md#request) corresponds to the request to be retried. Second argument is the `Error` instance that represents the last error thrown during processing of the request.

### [**](#experiments)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L395)optionalexperiments

**experiments?

<!-- -->

: [CrawlerExperiments](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerExperiments.md)

Enables experimental features of Crawlee, which can alter the behavior of the crawler. WARNING: these options are not guaranteed to be stable and may change or be removed at any time.

### [**](#failedRequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L234)optionalfailedRequestHandler

**failedRequestHandler?

<!-- -->

: [ErrorHandler](https://crawlee.dev/js/api/basic-crawler.md#ErrorHandler)\<Context>

A function to handle requests that failed more than [`maxRequestRetries`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxRequestRetries) times.

The function receives the [BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md) as the first argument, where the [`request`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md#request) corresponds to the failed request. Second argument is the `Error` instance that represents the last error thrown during processing of the request.

### [**](#httpClient)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L407)optionalhttpClient

**httpClient?

<!-- -->

: [BaseHttpClient](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md)

HTTP client implementation for the `sendRequest` context helper and for plain HTTP crawling. Defaults to a new instance of [GotScrapingHttpClient](https://crawlee.dev/js/api/core/class/GotScrapingHttpClient.md)

### [**](#keepAlive)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L324)optionalkeepAlive

**keepAlive?

<!-- -->

: boolean

Allows to keep the crawler alive even if the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) gets empty. By default, the `crawler.run()` will resolve once the queue is empty. With `keepAlive: true` it will keep running, waiting for more requests to come. Use `crawler.stop()` to exit the crawler gracefully, or `crawler.teardown()` to stop it immediately.

### [**](#maxConcurrency)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L310)optionalmaxConcurrency

**maxConcurrency?

<!-- -->

: number

Sets the maximum concurrency (parallelism) for the crawl. Shortcut for the AutoscaledPool [`maxConcurrency`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#maxConcurrency) option.

### [**](#maxCrawlDepth)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L287)optionalmaxCrawlDepth

**maxCrawlDepth?

<!-- -->

: number

Maximum depth of the crawl. If not set, the crawl will continue until all requests are processed. Setting this to `0` will only process the initial requests, skipping all links enqueued by `crawlingContext.enqueueLinks` and `crawlingContext.addRequests`. Passing `1` will process the initial requests and all links enqueued by `crawlingContext.enqueueLinks` and `crawlingContext.addRequests` in the handler for initial requests.

### [**](#maxRequestRetries)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L258)optionalmaxRequestRetries

**maxRequestRetries?

<!-- -->

: number = 3

Specifies the maximum number of retries allowed for a request if its processing fails. This includes retries due to navigation errors or errors thrown from user-supplied functions (`requestHandler`, `preNavigationHooks`, `postNavigationHooks`).

This limit does not apply to retries triggered by session rotation (see [`maxSessionRotations`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxSessionRotations)).

### [**](#maxRequestsPerCrawl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L280)optionalmaxRequestsPerCrawl

**maxRequestsPerCrawl?

<!-- -->

: number

Maximum number of pages that the crawler will open. The crawl will stop when this limit is reached. This value should always be set in order to prevent infinite loops in misconfigured crawlers.

> *NOTE:* In cases of parallel crawling, the actual number of pages visited might be slightly higher than this value.

### [**](#maxRequestsPerMinute)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L317)optionalmaxRequestsPerMinute

**maxRequestsPerMinute?

<!-- -->

: number

The maximum number of requests per minute the crawler should run. By default, this is set to `Infinity`, but we can pass any positive, non-zero integer. Shortcut for the AutoscaledPool [`maxTasksPerMinute`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#maxTasksPerMinute) option.

### [**](#maxSessionRotations)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L273)optionalmaxSessionRotations

**maxSessionRotations?

<!-- -->

: number = 10

Maximum number of session rotations per request. The crawler will automatically rotate the session in case of a proxy error or if it gets blocked by the website.

The session rotations are not counted towards the [`maxRequestRetries`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxRequestRetries) limit.

### [**](#minConcurrency)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L304)optionalminConcurrency

**minConcurrency?

<!-- -->

: number

Sets the minimum concurrency (parallelism) for the crawl. Shortcut for the AutoscaledPool [`minConcurrency`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#minConcurrency) option.

> *WARNING:* If we set this value too high with respect to the available system memory and CPU, our crawler will run extremely slow or crash. If not sure, it's better to keep the default value and the concurrency will scale up automatically.

### [**](#onSkippedRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L386)optionalonSkippedRequest

**onSkippedRequest?

<!-- -->

: [SkippedRequestCallback](https://crawlee.dev/js/api/core.md#SkippedRequestCallback)

When a request is skipped for some reason, you can use this callback to act on it. This is currently fired for requests skipped

1. based on robots.txt file,
2. because they don't match enqueueLinks filters,
3. because they are redirected to a URL that doesn't match the enqueueLinks strategy,
4. or because the [`maxRequestsPerCrawl`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxRequestsPerCrawl) limit has been reached

### [**](#requestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L153)optionalrequestHandler

**requestHandler?

<!-- -->

: [RequestHandler](https://crawlee.dev/js/api/basic-crawler.md#RequestHandler)\<LoadedContext\<Context>>

User-provided function that performs the logic of the crawler. It is called for each URL to crawl.

The function receives the [BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md) as an argument, where the [`request`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md#request) represents the URL to crawl.

The function must return a promise, which is then awaited by the crawler.

If the function throws an exception, the crawler will try to re-crawl the request later, up to the [`maxRequestRetries`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxRequestRetries) times. If all the retries fail, the crawler calls the function provided to the [`failedRequestHandler`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#failedRequestHandler) parameter. To make this work, we should **always** let our function throw exceptions rather than catch them. The exceptions are logged to the request using the [`Request.pushErrorMessage()`](https://crawlee.dev/js/api/core/class/Request.md#pushErrorMessage) function.

### [**](#requestHandlerTimeoutSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L205)optionalrequestHandlerTimeoutSecs

**requestHandlerTimeoutSecs?

<!-- -->

: number = 60

Timeout in which the function passed as [`requestHandler`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestHandler) needs to finish, in seconds.

### [**](#requestList)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L183)optionalrequestList

**requestList?

<!-- -->

: [IRequestList](https://crawlee.dev/js/api/core/interface/IRequestList.md)

Static list of URLs to be processed. If not provided, the crawler will open the default request queue when the [`crawler.addRequests()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#addRequests) function is called.

> Alternatively, `requests` parameter of [`crawler.run()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#run) could be used to enqueue the initial requests - it is a shortcut for running `crawler.addRequests()` before the `crawler.run()`.

### [**](#requestManager)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L199)optionalrequestManager

**requestManager?

<!-- -->

: [IRequestManager](https://crawlee.dev/js/api/core/interface/IRequestManager.md)

Allows explicitly configuring a request manager. Mutually exclusive with the `requestQueue` and `requestList` options.

This enables explicitly configuring the crawler to use `RequestManagerTandem`, for instance. If using this, the type of `BasicCrawler.requestQueue` may not be fully compatible with the `RequestProvider` class.

### [**](#requestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L191)optionalrequestQueue

**requestQueue?

<!-- -->

: [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)

Dynamic queue of URLs to be processed. This is useful for recursive crawling of websites. If not provided, the crawler will open the default request queue when the [`crawler.addRequests()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#addRequests) function is called.

> Alternatively, `requests` parameter of [`crawler.run()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#run) could be used to enqueue the initial requests - it is a shortcut for running `crawler.addRequests()` before the `crawler.run()`.

### [**](#respectRobotsTxtFile)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L376)optionalrespectRobotsTxtFile

**respectRobotsTxtFile?

<!-- -->

: boolean | { userAgent?

<!-- -->

: string }

If set to `true`, the crawler will automatically try to fetch the robots.txt file for each domain, and skip those that are not allowed. This also prevents disallowed URLs to be added via `enqueueLinks`.

If an object is provided, it may contain a `userAgent` property to specify which user-agent should be used when checking the robots.txt file. If not provided, the default user-agent `*` will be used.

### [**](#retryOnBlocked)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L367)optionalretryOnBlocked

**retryOnBlocked?

<!-- -->

: boolean

If set to `true`, the crawler will automatically try to bypass any detected bot protection.

Currently supports:

* [**Cloudflare** Bot Management](https://www.cloudflare.com/products/bot-management/)
* [**Google Search** Rate Limiting](https://www.google.com/sorry/)

### [**](#sameDomainDelaySecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L264)optionalsameDomainDelaySecs

**sameDomainDelaySecs?

<!-- -->

: number = 0

Indicates how much time (in seconds) to wait before crawling another same domain request.

### [**](#sessionPoolOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L335)optionalsessionPoolOptions

**sessionPoolOptions?

<!-- -->

: [SessionPoolOptions](https://crawlee.dev/js/api/core/interface/SessionPoolOptions.md)

The configuration options for [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) to use.

### [**](#statisticsOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L401)optionalstatisticsOptions

**statisticsOptions?

<!-- -->

: [StatisticsOptions](https://crawlee.dev/js/api/core/interface/StatisticsOptions.md)

Customize the way statistics collecting works, such as logging interval or whether to output them to the Key-Value store.

### [**](#statusMessageCallback)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L358)optionalstatusMessageCallback

**statusMessageCallback?

<!-- -->

: [StatusMessageCallback](https://crawlee.dev/js/api/basic-crawler.md#StatusMessageCallback)<[BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md)\<Dictionary>, [BasicCrawler](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md)<[BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md)\<Dictionary>>>

Allows overriding the default status message. The callback needs to call `crawler.setStatusMessage()` explicitly. The default status message is provided in the parameters.

```
const crawler = new CheerioCrawler({
    statusMessageCallback: async (ctx) => {
        return ctx.crawler.setStatusMessage(`this is status message from ${new Date().toISOString()}`, { level: 'INFO' }); // log level defaults to 'DEBUG'
    },
    statusMessageLoggingInterval: 1, // defaults to 10s
    async requestHandler({ $, enqueueLinks, request, log }) {
        // ...
    },
});
```

### [**](#statusMessageLoggingInterval)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L340)optionalstatusMessageLoggingInterval

**statusMessageLoggingInterval?

<!-- -->

: number

Defines the length of the interval for calling the `setStatusMessage` in seconds.

### [**](#useSessionPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L330)optionaluseSessionPool

**useSessionPool?

<!-- -->

: boolean

Basic crawler will initialize the [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) with the corresponding [`sessionPoolOptions`](https://crawlee.dev/js/api/core/interface/SessionPoolOptions.md). The session instance will be than available in the [`requestHandler`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestHandler).
