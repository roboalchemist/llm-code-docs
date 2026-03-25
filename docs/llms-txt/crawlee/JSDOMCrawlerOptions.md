# Source: https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlerOptions.md

# JSDOMCrawlerOptions<!-- --> \<UserData, JSONData>

### Hierarchy

* [HttpCrawlerOptions](https://crawlee.dev/js/api/http-crawler/interface/HttpCrawlerOptions.md)<[JSDOMCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlingContext.md)\<UserData, JSONData>>
  * *JSDOMCrawlerOptions*

## Index[**](#Index)

### Properties

* [**additionalHttpErrorStatusCodes](#additionalHttpErrorStatusCodes)
* [**additionalMimeTypes](#additionalMimeTypes)
* [**autoscaledPoolOptions](#autoscaledPoolOptions)
* [**errorHandler](#errorHandler)
* [**experiments](#experiments)
* [**failedRequestHandler](#failedRequestHandler)
* [**forceResponseEncoding](#forceResponseEncoding)
* [**handlePageFunction](#handlePageFunction)
* [**hideInternalConsole](#hideInternalConsole)
* [**httpClient](#httpClient)
* [**ignoreHttpErrorStatusCodes](#ignoreHttpErrorStatusCodes)
* [**ignoreSslErrors](#ignoreSslErrors)
* [**keepAlive](#keepAlive)
* [**maxConcurrency](#maxConcurrency)
* [**maxCrawlDepth](#maxCrawlDepth)
* [**maxRequestRetries](#maxRequestRetries)
* [**maxRequestsPerCrawl](#maxRequestsPerCrawl)
* [**maxRequestsPerMinute](#maxRequestsPerMinute)
* [**maxSessionRotations](#maxSessionRotations)
* [**minConcurrency](#minConcurrency)
* [**navigationTimeoutSecs](#navigationTimeoutSecs)
* [**onSkippedRequest](#onSkippedRequest)
* [**persistCookiesPerSession](#persistCookiesPerSession)
* [**postNavigationHooks](#postNavigationHooks)
* [**preNavigationHooks](#preNavigationHooks)
* [**proxyConfiguration](#proxyConfiguration)
* [**requestHandler](#requestHandler)
* [**requestHandlerTimeoutSecs](#requestHandlerTimeoutSecs)
* [**requestList](#requestList)
* [**requestManager](#requestManager)
* [**requestQueue](#requestQueue)
* [**respectRobotsTxtFile](#respectRobotsTxtFile)
* [**retryOnBlocked](#retryOnBlocked)
* [**runScripts](#runScripts)
* [**sameDomainDelaySecs](#sameDomainDelaySecs)
* [**sessionPoolOptions](#sessionPoolOptions)
* [**statisticsOptions](#statisticsOptions)
* [**statusMessageCallback](#statusMessageCallback)
* [**statusMessageLoggingInterval](#statusMessageLoggingInterval)
* [**suggestResponseEncoding](#suggestResponseEncoding)
* [**useSessionPool](#useSessionPool)

## Properties<!-- -->[**](#Properties)

### [**](#additionalHttpErrorStatusCodes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L187)optionalinheritedadditionalHttpErrorStatusCodes

**additionalHttpErrorStatusCodes?

<!-- -->

: number\[]

Inherited from HttpCrawlerOptions.additionalHttpErrorStatusCodes

An array of additional HTTP response [Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) to be treated as errors. By default, status codes >= 500 trigger errors.

### [**](#additionalMimeTypes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L143)optionalinheritedadditionalMimeTypes

**additionalMimeTypes?

<!-- -->

: string\[]

Inherited from HttpCrawlerOptions.additionalMimeTypes

An array of [MIME types](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types/Complete_list_of_MIME_types) you want the crawler to load and process. By default, only `text/html`, `application/xhtml+xml`, `text/xml`, `application/xml`, and `application/json` MIME types are supported.

### [**](#autoscaledPoolOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L296)optionalinheritedautoscaledPoolOptions

**autoscaledPoolOptions?

<!-- -->

: [AutoscaledPoolOptions](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md)

Inherited from HttpCrawlerOptions.autoscaledPoolOptions

Custom options passed to the underlying [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) constructor.

> *NOTE:* The [`runTaskFunction`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#runTaskFunction) option is provided by the crawler and cannot be overridden. However, we can provide custom implementations of [`isFinishedFunction`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#isFinishedFunction) and [`isTaskReadyFunction`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#isTaskReadyFunction).

### [**](#errorHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L224)optionalinheritederrorHandler

**errorHandler?

<!-- -->

: [ErrorHandler](https://crawlee.dev/js/api/basic-crawler.md#ErrorHandler)<[JSDOMCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlingContext.md)\<UserData, JSONData>>

Inherited from HttpCrawlerOptions.errorHandler

User-provided function that allows modifying the request object before it gets retried by the crawler. It's executed before each retry for the requests that failed less than [`maxRequestRetries`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxRequestRetries) times.

The function receives the [BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md) as the first argument, where the [`request`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md#request) corresponds to the request to be retried. Second argument is the `Error` instance that represents the last error thrown during processing of the request.

### [**](#experiments)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L395)optionalinheritedexperiments

**experiments?

<!-- -->

: [CrawlerExperiments](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerExperiments.md)

Inherited from HttpCrawlerOptions.experiments

Enables experimental features of Crawlee, which can alter the behavior of the crawler. WARNING: these options are not guaranteed to be stable and may change or be removed at any time.

### [**](#failedRequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L234)optionalinheritedfailedRequestHandler

**failedRequestHandler?

<!-- -->

: [ErrorHandler](https://crawlee.dev/js/api/basic-crawler.md#ErrorHandler)<[JSDOMCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlingContext.md)\<UserData, JSONData>>

Inherited from HttpCrawlerOptions.failedRequestHandler

A function to handle requests that failed more than [`maxRequestRetries`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxRequestRetries) times.

The function receives the [BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md) as the first argument, where the [`request`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md#request) corresponds to the failed request. Second argument is the `Error` instance that represents the last error thrown during processing of the request.

### [**](#forceResponseEncoding)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L167)optionalinheritedforceResponseEncoding

**forceResponseEncoding?

<!-- -->

: string

Inherited from HttpCrawlerOptions.forceResponseEncoding

By default this crawler will extract correct encoding from the HTTP response headers. Use `forceResponseEncoding` to force a certain encoding, disregarding the response headers. To only provide a default for missing encodings, use [HttpCrawlerOptions.suggestResponseEncoding](https://crawlee.dev/js/api/http-crawler/interface/HttpCrawlerOptions.md#suggestResponseEncoding)

```
// Will force windows-1250 encoding even if headers say otherwise
forceResponseEncoding: 'windows-1250'
```

### [**](#handlePageFunction)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L87)optionalinheritedhandlePageFunction

**handlePageFunction?

<!-- -->

: [RequestHandler](https://crawlee.dev/js/api/basic-crawler.md#RequestHandler)<{ request: [LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<UserData>> } & Omit<[JSDOMCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlingContext.md)\<UserData, JSONData>, request>>

Inherited from HttpCrawlerOptions.handlePageFunction

An alias for [HttpCrawlerOptions.requestHandler](https://crawlee.dev/js/api/http-crawler/interface/HttpCrawlerOptions.md#requestHandler) Soon to be removed, use `requestHandler` instead.

* **@deprecated**

### [**](#hideInternalConsole)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/jsdom-crawler/src/internals/jsdom-crawler.ts#L50)optionalhideInternalConsole

**hideInternalConsole?

<!-- -->

: boolean

Suppress the logs from JSDOM internal console.

### [**](#httpClient)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L407)optionalinheritedhttpClient

**httpClient?

<!-- -->

: [BaseHttpClient](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md)

Inherited from HttpCrawlerOptions.httpClient

HTTP client implementation for the `sendRequest` context helper and for plain HTTP crawling. Defaults to a new instance of [GotScrapingHttpClient](https://crawlee.dev/js/api/core/class/GotScrapingHttpClient.md)

### [**](#ignoreHttpErrorStatusCodes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L181)optionalinheritedignoreHttpErrorStatusCodes

**ignoreHttpErrorStatusCodes?

<!-- -->

: number\[]

Inherited from HttpCrawlerOptions.ignoreHttpErrorStatusCodes

An array of HTTP response [Status Codes](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status) to be excluded from error consideration. By default, status codes >= 500 trigger errors.

### [**](#ignoreSslErrors)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L97)optionalinheritedignoreSslErrors

**ignoreSslErrors?

<!-- -->

: boolean

Inherited from HttpCrawlerOptions.ignoreSslErrors

If set to true, SSL certificate errors will be ignored.

### [**](#keepAlive)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L324)optionalinheritedkeepAlive

**keepAlive?

<!-- -->

: boolean

Inherited from HttpCrawlerOptions.keepAlive

Allows to keep the crawler alive even if the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) gets empty. By default, the `crawler.run()` will resolve once the queue is empty. With `keepAlive: true` it will keep running, waiting for more requests to come. Use `crawler.stop()` to exit the crawler gracefully, or `crawler.teardown()` to stop it immediately.

### [**](#maxConcurrency)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L310)optionalinheritedmaxConcurrency

**maxConcurrency?

<!-- -->

: number

Inherited from HttpCrawlerOptions.maxConcurrency

Sets the maximum concurrency (parallelism) for the crawl. Shortcut for the AutoscaledPool [`maxConcurrency`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#maxConcurrency) option.

### [**](#maxCrawlDepth)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L287)optionalinheritedmaxCrawlDepth

**maxCrawlDepth?

<!-- -->

: number

Inherited from HttpCrawlerOptions.maxCrawlDepth

Maximum depth of the crawl. If not set, the crawl will continue until all requests are processed. Setting this to `0` will only process the initial requests, skipping all links enqueued by `crawlingContext.enqueueLinks` and `crawlingContext.addRequests`. Passing `1` will process the initial requests and all links enqueued by `crawlingContext.enqueueLinks` and `crawlingContext.addRequests` in the handler for initial requests.

### [**](#maxRequestRetries)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L258)optionalinheritedmaxRequestRetries

**maxRequestRetries?

<!-- -->

: number = 3

Inherited from HttpCrawlerOptions.maxRequestRetries

Specifies the maximum number of retries allowed for a request if its processing fails. This includes retries due to navigation errors or errors thrown from user-supplied functions (`requestHandler`, `preNavigationHooks`, `postNavigationHooks`).

This limit does not apply to retries triggered by session rotation (see [`maxSessionRotations`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxSessionRotations)).

### [**](#maxRequestsPerCrawl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L280)optionalinheritedmaxRequestsPerCrawl

**maxRequestsPerCrawl?

<!-- -->

: number

Inherited from HttpCrawlerOptions.maxRequestsPerCrawl

Maximum number of pages that the crawler will open. The crawl will stop when this limit is reached. This value should always be set in order to prevent infinite loops in misconfigured crawlers.

> *NOTE:* In cases of parallel crawling, the actual number of pages visited might be slightly higher than this value.

### [**](#maxRequestsPerMinute)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L317)optionalinheritedmaxRequestsPerMinute

**maxRequestsPerMinute?

<!-- -->

: number

Inherited from HttpCrawlerOptions.maxRequestsPerMinute

The maximum number of requests per minute the crawler should run. By default, this is set to `Infinity`, but we can pass any positive, non-zero integer. Shortcut for the AutoscaledPool [`maxTasksPerMinute`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#maxTasksPerMinute) option.

### [**](#maxSessionRotations)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L273)optionalinheritedmaxSessionRotations

**maxSessionRotations?

<!-- -->

: number = 10

Inherited from HttpCrawlerOptions.maxSessionRotations

Maximum number of session rotations per request. The crawler will automatically rotate the session in case of a proxy error or if it gets blocked by the website.

The session rotations are not counted towards the [`maxRequestRetries`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxRequestRetries) limit.

### [**](#minConcurrency)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L304)optionalinheritedminConcurrency

**minConcurrency?

<!-- -->

: number

Inherited from HttpCrawlerOptions.minConcurrency

Sets the minimum concurrency (parallelism) for the crawl. Shortcut for the AutoscaledPool [`minConcurrency`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#minConcurrency) option.

> *WARNING:* If we set this value too high with respect to the available system memory and CPU, our crawler will run extremely slow or crash. If not sure, it's better to keep the default value and the concurrency will scale up automatically.

### [**](#navigationTimeoutSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L92)optionalinheritednavigationTimeoutSecs

**navigationTimeoutSecs?

<!-- -->

: number

Inherited from HttpCrawlerOptions.navigationTimeoutSecs

Timeout in which the HTTP request to the resource needs to finish, given in seconds.

### [**](#onSkippedRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L386)optionalinheritedonSkippedRequest

**onSkippedRequest?

<!-- -->

: [SkippedRequestCallback](https://crawlee.dev/js/api/core.md#SkippedRequestCallback)

Inherited from HttpCrawlerOptions.onSkippedRequest

When a request is skipped for some reason, you can use this callback to act on it. This is currently fired for requests skipped

1. based on robots.txt file,
2. because they don't match enqueueLinks filters,
3. because they are redirected to a URL that doesn't match the enqueueLinks strategy,
4. or because the [`maxRequestsPerCrawl`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxRequestsPerCrawl) limit has been reached

### [**](#persistCookiesPerSession)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L175)optionalinheritedpersistCookiesPerSession

**persistCookiesPerSession?

<!-- -->

: boolean

Inherited from HttpCrawlerOptions.persistCookiesPerSession

Automatically saves cookies to Session. Works only if Session Pool is used.

It parses cookie from response "set-cookie" header saves or updates cookies for session and once the session is used for next request. It passes the "Cookie" header to the request with the session cookies.

### [**](#postNavigationHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L136)optionalinheritedpostNavigationHooks

**postNavigationHooks?

<!-- -->

: InternalHttpHook<[JSDOMCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlingContext.md)\<UserData, JSONData>>\[]

Inherited from HttpCrawlerOptions.postNavigationHooks

Async functions that are sequentially evaluated after the navigation. Good for checking if the navigation was successful. The function accepts `crawlingContext` as the only parameter. Example:

```
postNavigationHooks: [
    async (crawlingContext) => {
        // ...
    },
]
```

### [**](#preNavigationHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L122)optionalinheritedpreNavigationHooks

**preNavigationHooks?

<!-- -->

: InternalHttpHook<[JSDOMCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlingContext.md)\<UserData, JSONData>>\[]

Inherited from HttpCrawlerOptions.preNavigationHooks

Async functions that are sequentially evaluated before the navigation. Good for setting additional cookies or browser properties before navigation. The function accepts two parameters, `crawlingContext` and `gotOptions`, which are passed to the `requestAsBrowser()` function the crawler calls to navigate. Example:

```
preNavigationHooks: [
    async (crawlingContext, gotOptions) => {
        // ...
    },
]
```

Modyfing `pageOptions` is supported only in Playwright incognito. See [PrePageCreateHook](https://crawlee.dev/js/api/browser-pool.md#PrePageCreateHook)

### [**](#proxyConfiguration)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L104)optionalinheritedproxyConfiguration

**proxyConfiguration?

<!-- -->

: [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md)

Inherited from HttpCrawlerOptions.proxyConfiguration

If set, this crawler will be configured for all connections to use [Apify Proxy](https://console.apify.com/proxy) or your own Proxy URLs provided and rotated according to the configuration. For more information, see the [documentation](https://docs.apify.com/proxy).

### [**](#requestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L153)optionalinheritedrequestHandler

**requestHandler?

<!-- -->

: [RequestHandler](https://crawlee.dev/js/api/basic-crawler.md#RequestHandler)<{ request: [LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<UserData>> } & Omit<[JSDOMCrawlingContext](https://crawlee.dev/js/api/jsdom-crawler/interface/JSDOMCrawlingContext.md)\<UserData, JSONData>, request>>

Inherited from HttpCrawlerOptions.requestHandler

User-provided function that performs the logic of the crawler. It is called for each URL to crawl.

The function receives the [BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md) as an argument, where the [`request`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md#request) represents the URL to crawl.

The function must return a promise, which is then awaited by the crawler.

If the function throws an exception, the crawler will try to re-crawl the request later, up to the [`maxRequestRetries`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxRequestRetries) times. If all the retries fail, the crawler calls the function provided to the [`failedRequestHandler`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#failedRequestHandler) parameter. To make this work, we should **always** let our function throw exceptions rather than catch them. The exceptions are logged to the request using the [`Request.pushErrorMessage()`](https://crawlee.dev/js/api/core/class/Request.md#pushErrorMessage) function.

### [**](#requestHandlerTimeoutSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L205)optionalinheritedrequestHandlerTimeoutSecs

**requestHandlerTimeoutSecs?

<!-- -->

: number = 60

Inherited from HttpCrawlerOptions.requestHandlerTimeoutSecs

Timeout in which the function passed as [`requestHandler`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestHandler) needs to finish, in seconds.

### [**](#requestList)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L183)optionalinheritedrequestList

**requestList?

<!-- -->

: [IRequestList](https://crawlee.dev/js/api/core/interface/IRequestList.md)

Inherited from HttpCrawlerOptions.requestList

Static list of URLs to be processed. If not provided, the crawler will open the default request queue when the [`crawler.addRequests()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#addRequests) function is called.

> Alternatively, `requests` parameter of [`crawler.run()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#run) could be used to enqueue the initial requests - it is a shortcut for running `crawler.addRequests()` before the `crawler.run()`.

### [**](#requestManager)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L199)optionalinheritedrequestManager

**requestManager?

<!-- -->

: [IRequestManager](https://crawlee.dev/js/api/core/interface/IRequestManager.md)

Inherited from HttpCrawlerOptions.requestManager

Allows explicitly configuring a request manager. Mutually exclusive with the `requestQueue` and `requestList` options.

This enables explicitly configuring the crawler to use `RequestManagerTandem`, for instance. If using this, the type of `BasicCrawler.requestQueue` may not be fully compatible with the `RequestProvider` class.

### [**](#requestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L191)optionalinheritedrequestQueue

**requestQueue?

<!-- -->

: [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)

Inherited from HttpCrawlerOptions.requestQueue

Dynamic queue of URLs to be processed. This is useful for recursive crawling of websites. If not provided, the crawler will open the default request queue when the [`crawler.addRequests()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#addRequests) function is called.

> Alternatively, `requests` parameter of [`crawler.run()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#run) could be used to enqueue the initial requests - it is a shortcut for running `crawler.addRequests()` before the `crawler.run()`.

### [**](#respectRobotsTxtFile)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L376)optionalinheritedrespectRobotsTxtFile

**respectRobotsTxtFile?

<!-- -->

: boolean | { userAgent?

<!-- -->

: string }

Inherited from HttpCrawlerOptions.respectRobotsTxtFile

If set to `true`, the crawler will automatically try to fetch the robots.txt file for each domain, and skip those that are not allowed. This also prevents disallowed URLs to be added via `enqueueLinks`.

If an object is provided, it may contain a `userAgent` property to specify which user-agent should be used when checking the robots.txt file. If not provided, the default user-agent `*` will be used.

### [**](#retryOnBlocked)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L367)optionalinheritedretryOnBlocked

**retryOnBlocked?

<!-- -->

: boolean

Inherited from HttpCrawlerOptions.retryOnBlocked

If set to `true`, the crawler will automatically try to bypass any detected bot protection.

Currently supports:

* [**Cloudflare** Bot Management](https://www.cloudflare.com/products/bot-management/)
* [**Google Search** Rate Limiting](https://www.google.com/sorry/)

### [**](#runScripts)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/jsdom-crawler/src/internals/jsdom-crawler.ts#L46)optionalrunScripts

**runScripts?

<!-- -->

: boolean

Download and run scripts.

### [**](#sameDomainDelaySecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L264)optionalinheritedsameDomainDelaySecs

**sameDomainDelaySecs?

<!-- -->

: number = 0

Inherited from HttpCrawlerOptions.sameDomainDelaySecs

Indicates how much time (in seconds) to wait before crawling another same domain request.

### [**](#sessionPoolOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L335)optionalinheritedsessionPoolOptions

**sessionPoolOptions?

<!-- -->

: [SessionPoolOptions](https://crawlee.dev/js/api/core/interface/SessionPoolOptions.md)

Inherited from HttpCrawlerOptions.sessionPoolOptions

The configuration options for [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) to use.

### [**](#statisticsOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L401)optionalinheritedstatisticsOptions

**statisticsOptions?

<!-- -->

: [StatisticsOptions](https://crawlee.dev/js/api/core/interface/StatisticsOptions.md)

Inherited from HttpCrawlerOptions.statisticsOptions

Customize the way statistics collecting works, such as logging interval or whether to output them to the Key-Value store.

### [**](#statusMessageCallback)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L358)optionalinheritedstatusMessageCallback

**statusMessageCallback?

<!-- -->

: [StatusMessageCallback](https://crawlee.dev/js/api/basic-crawler.md#StatusMessageCallback)<[BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md)\<Dictionary>, [BasicCrawler](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md)<[BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md)\<Dictionary>>>

Inherited from HttpCrawlerOptions.statusMessageCallback

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

### [**](#statusMessageLoggingInterval)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L340)optionalinheritedstatusMessageLoggingInterval

**statusMessageLoggingInterval?

<!-- -->

: number

Inherited from HttpCrawlerOptions.statusMessageLoggingInterval

Defines the length of the interval for calling the `setStatusMessage` in seconds.

### [**](#suggestResponseEncoding)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L156)optionalinheritedsuggestResponseEncoding

**suggestResponseEncoding?

<!-- -->

: string

Inherited from HttpCrawlerOptions.suggestResponseEncoding

By default this crawler will extract correct encoding from the HTTP response headers. Sadly, there are some websites which use invalid headers. Those are encoded using the UTF-8 encoding. If those sites actually use a different encoding, the response will be corrupted. You can use `suggestResponseEncoding` to fall back to a certain encoding, if you know that your target website uses it. To force a certain encoding, disregarding the response headers, use [HttpCrawlerOptions.forceResponseEncoding](https://crawlee.dev/js/api/http-crawler/interface/HttpCrawlerOptions.md#forceResponseEncoding)

```
// Will fall back to windows-1250 encoding if none found
suggestResponseEncoding: 'windows-1250'
```

### [**](#useSessionPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L330)optionalinheriteduseSessionPool

**useSessionPool?

<!-- -->

: boolean

Inherited from HttpCrawlerOptions.useSessionPool

Basic crawler will initialize the [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) with the corresponding [`sessionPoolOptions`](https://crawlee.dev/js/api/core/interface/SessionPoolOptions.md). The session instance will be than available in the [`requestHandler`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestHandler).
