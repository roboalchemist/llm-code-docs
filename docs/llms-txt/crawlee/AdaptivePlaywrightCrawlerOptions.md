# Source: https://crawlee.dev/js/api/playwright-crawler/interface/AdaptivePlaywrightCrawlerOptions.md

# AdaptivePlaywrightCrawlerOptions<!-- -->

### Hierarchy

* Omit<[PlaywrightCrawlerOptions](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlerOptions.md), requestHandler | handlePageFunction | preNavigationHooks | postNavigationHooks>
  * *AdaptivePlaywrightCrawlerOptions*

## Index[**](#Index)

### Properties

* [**autoscaledPoolOptions](#autoscaledPoolOptions)
* [**browserPoolOptions](#browserPoolOptions)
* [**errorHandler](#errorHandler)
* [**experiments](#experiments)
* [**failedRequestHandler](#failedRequestHandler)
* [**headless](#headless)
* [**httpClient](#httpClient)
* [**ignoreIframes](#ignoreIframes)
* [**ignoreShadowRoots](#ignoreShadowRoots)
* [**keepAlive](#keepAlive)
* [**launchContext](#launchContext)
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
* [**preventDirectStorageAccess](#preventDirectStorageAccess)
* [**proxyConfiguration](#proxyConfiguration)
* [**renderingTypeDetectionRatio](#renderingTypeDetectionRatio)
* [**renderingTypePredictor](#renderingTypePredictor)
* [**requestHandler](#requestHandler)
* [**requestHandlerTimeoutSecs](#requestHandlerTimeoutSecs)
* [**requestList](#requestList)
* [**requestManager](#requestManager)
* [**requestQueue](#requestQueue)
* [**respectRobotsTxtFile](#respectRobotsTxtFile)
* [**resultChecker](#resultChecker)
* [**resultComparator](#resultComparator)
* [**retryOnBlocked](#retryOnBlocked)
* [**sameDomainDelaySecs](#sameDomainDelaySecs)
* [**sessionPoolOptions](#sessionPoolOptions)
* [**statisticsOptions](#statisticsOptions)
* [**statusMessageCallback](#statusMessageCallback)
* [**statusMessageLoggingInterval](#statusMessageLoggingInterval)
* [**useSessionPool](#useSessionPool)

## Properties<!-- -->[**](#Properties)

### [**](#autoscaledPoolOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L296)optionalinheritedautoscaledPoolOptions

**autoscaledPoolOptions?

<!-- -->

: [AutoscaledPoolOptions](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md)

Inherited from Omit.autoscaledPoolOptions

Custom options passed to the underlying [AutoscaledPool](https://crawlee.dev/js/api/core/class/AutoscaledPool.md) constructor.

> *NOTE:* The [`runTaskFunction`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#runTaskFunction) option is provided by the crawler and cannot be overridden. However, we can provide custom implementations of [`isFinishedFunction`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#isFinishedFunction) and [`isTaskReadyFunction`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#isTaskReadyFunction).

### [**](#browserPoolOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L194)optionalinheritedbrowserPoolOptions

**browserPoolOptions?

<!-- -->

: Partial<[BrowserPoolOptions](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolOptions.md)<[BrowserPlugin](https://crawlee.dev/js/api/browser-pool/class/BrowserPlugin.md)<[CommonLibrary](https://crawlee.dev/js/api/browser-pool/interface/CommonLibrary.md), undefined | Dictionary, CommonBrowser, unknown, CommonPage>>> & Partial<[BrowserPoolHooks](https://crawlee.dev/js/api/browser-pool/interface/BrowserPoolHooks.md)<[BrowserController](https://crawlee.dev/js/api/browser-pool/class/BrowserController.md)\<BrowserType<{}>, undefined | LaunchOptions, Browser, undefined | { acceptDownloads?

<!-- -->

: boolean; baseURL?

<!-- -->

: string; bypassCSP?

<!-- -->

: boolean; clientCertificates?

<!-- -->

: { cert?

<!-- -->

: ... | ...; certPath?

<!-- -->

: ... | ...; key?

<!-- -->

: ... | ...; keyPath?

<!-- -->

: ... | ...; origin: string; passphrase?

<!-- -->

: ... | ...; pfx?

<!-- -->

: ... | ...; pfxPath?

<!-- -->

: ... | ... }\[]; colorScheme?

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

: { height: ...; width: ... } }; reducedMotion?

<!-- -->

: null | reduce | no-preference; screen?

<!-- -->

: { height: number; width: number }; serviceWorkers?

<!-- -->

: allow | block; storageState?

<!-- -->

: string | { cookies: { domain: ...; expires: ...; httpOnly: ...; name: ...; path: ...; sameSite: ...; secure: ...; value: ... }\[]; origins: { localStorage: ...; origin: ... }\[] }; strictSelectors?

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

: ... | ...; certPath?

<!-- -->

: ... | ...; key?

<!-- -->

: ... | ...; keyPath?

<!-- -->

: ... | ...; origin: string; passphrase?

<!-- -->

: ... | ...; pfx?

<!-- -->

: ... | ...; pfxPath?

<!-- -->

: ... | ... }\[]; colorScheme?

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

: { height: ...; width: ... } }; reducedMotion?

<!-- -->

: null | reduce | no-preference; screen?

<!-- -->

: { height: number; width: number }; serviceWorkers?

<!-- -->

: allow | block; storageState?

<!-- -->

: string | { cookies: { domain: ...; expires: ...; httpOnly: ...; name: ...; path: ...; sameSite: ...; secure: ...; value: ... }\[]; origins: { localStorage: ...; origin: ... }\[] }; strictSelectors?

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

: null | { height: number; width: number } }, Page>, Page>>

Inherited from Omit.browserPoolOptions

Custom options passed to the underlying [BrowserPool](https://crawlee.dev/js/api/browser-pool/class/BrowserPool.md) constructor. We can tweak those to fine-tune browser management.

### [**](#errorHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L163)optionalinheritederrorHandler

**errorHandler?

<!-- -->

: [BrowserErrorHandler](https://crawlee.dev/js/api/browser-crawler.md#BrowserErrorHandler)<[PlaywrightCrawlingContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlingContext.md)\<Dictionary>>

Inherited from Omit.errorHandler

User-provided function that allows modifying the request object before it gets retried by the crawler. It's executed before each retry for the requests that failed less than [`maxRequestRetries`](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlerOptions.md#maxRequestRetries) times.

The function receives the [BrowserCrawlingContext](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlingContext.md) (actual context will be enhanced with the crawler specific properties) as the first argument, where the [`request`](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlingContext.md#request) corresponds to the request to be retried. Second argument is the `Error` instance that represents the last error thrown during processing of the request.

### [**](#experiments)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L395)optionalinheritedexperiments

**experiments?

<!-- -->

: [CrawlerExperiments](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerExperiments.md)

Inherited from Omit.experiments

Enables experimental features of Crawlee, which can alter the behavior of the crawler. WARNING: these options are not guaranteed to be stable and may change or be removed at any time.

### [**](#failedRequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L174)optionalinheritedfailedRequestHandler

**failedRequestHandler?

<!-- -->

: [BrowserErrorHandler](https://crawlee.dev/js/api/browser-crawler.md#BrowserErrorHandler)<[PlaywrightCrawlingContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlingContext.md)\<Dictionary>>

Inherited from Omit.failedRequestHandler

A function to handle requests that failed more than `option.maxRequestRetries` times.

The function receives the [BrowserCrawlingContext](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlingContext.md) (actual context will be enhanced with the crawler specific properties) as the first argument, where the [`request`](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlingContext.md#request) corresponds to the failed request. Second argument is the `Error` instance that represents the last error thrown during processing of the request.

### [**](#headless)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L260)optionalinheritedheadless

**headless?

<!-- -->

: boolean | new | old

Inherited from Omit.headless

Whether to run browser in headless mode. Defaults to `true`. Can be also set via [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md).

### [**](#httpClient)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L407)optionalinheritedhttpClient

**httpClient?

<!-- -->

: [BaseHttpClient](https://crawlee.dev/js/api/core/interface/BaseHttpClient.md)

Inherited from Omit.httpClient

HTTP client implementation for the `sendRequest` context helper and for plain HTTP crawling. Defaults to a new instance of [GotScrapingHttpClient](https://crawlee.dev/js/api/core/class/GotScrapingHttpClient.md)

### [**](#ignoreIframes)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L272)optionalinheritedignoreIframes

**ignoreIframes?

<!-- -->

: boolean

Inherited from Omit.ignoreIframes

Whether to ignore `iframes` when processing the page content via `parseWithCheerio` helper. By default, `iframes` are expanded automatically. Use this option to disable this behavior.

### [**](#ignoreShadowRoots)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L266)optionalinheritedignoreShadowRoots

**ignoreShadowRoots?

<!-- -->

: boolean

Inherited from Omit.ignoreShadowRoots

Whether to ignore custom elements (and their #shadow-roots) when processing the page content via `parseWithCheerio` helper. By default, they are expanded automatically. Use this option to disable this behavior.

### [**](#keepAlive)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L324)optionalinheritedkeepAlive

**keepAlive?

<!-- -->

: boolean

Inherited from Omit.keepAlive

Allows to keep the crawler alive even if the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) gets empty. By default, the `crawler.run()` will resolve once the queue is empty. With `keepAlive: true` it will keep running, waiting for more requests to come. Use `crawler.stop()` to exit the crawler gracefully, or `crawler.teardown()` to stop it immediately.

### [**](#launchContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/playwright-crawler.ts#L33)optionalinheritedlaunchContext

**launchContext?

<!-- -->

: [PlaywrightLaunchContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightLaunchContext.md)

Inherited from Omit.launchContext

The same options as used by [launchPlaywright](https://crawlee.dev/js/api/playwright-crawler/function/launchPlaywright.md).

### [**](#maxConcurrency)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L310)optionalinheritedmaxConcurrency

**maxConcurrency?

<!-- -->

: number

Inherited from Omit.maxConcurrency

Sets the maximum concurrency (parallelism) for the crawl. Shortcut for the AutoscaledPool [`maxConcurrency`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#maxConcurrency) option.

### [**](#maxCrawlDepth)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L287)optionalinheritedmaxCrawlDepth

**maxCrawlDepth?

<!-- -->

: number

Inherited from Omit.maxCrawlDepth

Maximum depth of the crawl. If not set, the crawl will continue until all requests are processed. Setting this to `0` will only process the initial requests, skipping all links enqueued by `crawlingContext.enqueueLinks` and `crawlingContext.addRequests`. Passing `1` will process the initial requests and all links enqueued by `crawlingContext.enqueueLinks` and `crawlingContext.addRequests` in the handler for initial requests.

### [**](#maxRequestRetries)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L258)optionalinheritedmaxRequestRetries

**maxRequestRetries?

<!-- -->

: number = 3

Inherited from Omit.maxRequestRetries

Specifies the maximum number of retries allowed for a request if its processing fails. This includes retries due to navigation errors or errors thrown from user-supplied functions (`requestHandler`, `preNavigationHooks`, `postNavigationHooks`).

This limit does not apply to retries triggered by session rotation (see [`maxSessionRotations`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxSessionRotations)).

### [**](#maxRequestsPerCrawl)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L280)optionalinheritedmaxRequestsPerCrawl

**maxRequestsPerCrawl?

<!-- -->

: number

Inherited from Omit.maxRequestsPerCrawl

Maximum number of pages that the crawler will open. The crawl will stop when this limit is reached. This value should always be set in order to prevent infinite loops in misconfigured crawlers.

> *NOTE:* In cases of parallel crawling, the actual number of pages visited might be slightly higher than this value.

### [**](#maxRequestsPerMinute)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L317)optionalinheritedmaxRequestsPerMinute

**maxRequestsPerMinute?

<!-- -->

: number

Inherited from Omit.maxRequestsPerMinute

The maximum number of requests per minute the crawler should run. By default, this is set to `Infinity`, but we can pass any positive, non-zero integer. Shortcut for the AutoscaledPool [`maxTasksPerMinute`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#maxTasksPerMinute) option.

### [**](#maxSessionRotations)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L273)optionalinheritedmaxSessionRotations

**maxSessionRotations?

<!-- -->

: number = 10

Inherited from Omit.maxSessionRotations

Maximum number of session rotations per request. The crawler will automatically rotate the session in case of a proxy error or if it gets blocked by the website.

The session rotations are not counted towards the [`maxRequestRetries`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxRequestRetries) limit.

### [**](#minConcurrency)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L304)optionalinheritedminConcurrency

**minConcurrency?

<!-- -->

: number

Inherited from Omit.minConcurrency

Sets the minimum concurrency (parallelism) for the crawl. Shortcut for the AutoscaledPool [`minConcurrency`](https://crawlee.dev/js/api/core/interface/AutoscaledPoolOptions.md#minConcurrency) option.

> *WARNING:* If we set this value too high with respect to the available system memory and CPU, our crawler will run extremely slow or crash. If not sure, it's better to keep the default value and the concurrency will scale up automatically.

### [**](#navigationTimeoutSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L248)optionalinheritednavigationTimeoutSecs

**navigationTimeoutSecs?

<!-- -->

: number

Inherited from Omit.navigationTimeoutSecs

Timeout in which page navigation needs to finish, in seconds.

### [**](#onSkippedRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L386)optionalinheritedonSkippedRequest

**onSkippedRequest?

<!-- -->

: [SkippedRequestCallback](https://crawlee.dev/js/api/core.md#SkippedRequestCallback)

Inherited from Omit.onSkippedRequest

When a request is skipped for some reason, you can use this callback to act on it. This is currently fired for requests skipped

1. based on robots.txt file,
2. because they don't match enqueueLinks filters,
3. because they are redirected to a URL that doesn't match the enqueueLinks strategy,
4. or because the [`maxRequestsPerCrawl`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#maxRequestsPerCrawl) limit has been reached

### [**](#persistCookiesPerSession)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L254)optionalinheritedpersistCookiesPerSession

**persistCookiesPerSession?

<!-- -->

: boolean

Inherited from Omit.persistCookiesPerSession

Defines whether the cookies should be persisted for sessions. This can only be used when `useSessionPool` is set to `true`.

### [**](#postNavigationHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L183)optionalpostNavigationHooks

**postNavigationHooks?

<!-- -->

: AdaptiveHook\[]

Async functions that are sequentially evaluated after the navigation. Good for checking if the navigation was successful. The function accepts a subset of the crawling context. If you attempt to access the `page` property during HTTP-only crawling, an exception will be thrown. If it's not caught, the request will be transparently retried in a browser.

### [**](#preNavigationHooks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L176)optionalpreNavigationHooks

**preNavigationHooks?

<!-- -->

: AdaptiveHook\[]

Async functions that are sequentially evaluated before the navigation. Good for setting additional cookies. The function accepts a subset of the crawling context. If you attempt to access the `page` property during HTTP-only crawling, an exception will be thrown. If it's not caught, the request will be transparently retried in a browser.

### [**](#preventDirectStorageAccess)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L221)optionalpreventDirectStorageAccess

**preventDirectStorageAccess?

<!-- -->

: boolean

Prevent direct access to storage in request handlers (only allow using context helpers). Defaults to `true`

### [**](#proxyConfiguration)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L201)optionalinheritedproxyConfiguration

**proxyConfiguration?

<!-- -->

: [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md)

Inherited from Omit.proxyConfiguration

If set, the crawler will be configured for all connections to use the Proxy URLs provided and rotated according to the configuration.

### [**](#renderingTypeDetectionRatio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L189)optionalrenderingTypeDetectionRatio

**renderingTypeDetectionRatio?

<!-- -->

: number

Specifies the frequency of rendering type detection checks - 0.1 means roughly 10% of requests. Defaults to 0.1 (so 10%).

### [**](#renderingTypePredictor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L215)optionalrenderingTypePredictor

**renderingTypePredictor?

<!-- -->

: Pick<[RenderingTypePredictor](https://crawlee.dev/js/api/playwright-crawler/class/RenderingTypePredictor.md), predict | storeResult | initialize>

A custom rendering type predictor

### [**](#requestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L169)optionalrequestHandler

**requestHandler?

<!-- -->

: (crawlingContext) => Awaitable\<void>

Function that is called to process each request.

The function receives the AdaptivePlaywrightCrawlingContext as an argument, and it must refrain from calling code with side effects, other than the methods of the crawling context. Any other side effects may be invoked repeatedly by the crawler, which can lead to inconsistent results.

The function must return a promise, which is then awaited by the crawler.

If the function throws an exception, the crawler will try to re-crawl the request later, up to `option.maxRequestRetries` times.

***

#### Type declaration

* * **(crawlingContext): Awaitable\<void>

  - #### Parameters

    * ##### crawlingContext: { request: [LoadedRequest](https://crawlee.dev/js/api/core.md#LoadedRequest)<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>> } & Omit<[AdaptivePlaywrightCrawlerContext](https://crawlee.dev/js/api/playwright-crawler/interface/AdaptivePlaywrightCrawlerContext.md)\<Dictionary>, request>

    #### Returns Awaitable\<void>

### [**](#requestHandlerTimeoutSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L205)optionalinheritedrequestHandlerTimeoutSecs

**requestHandlerTimeoutSecs?

<!-- -->

: number = 60

Inherited from Omit.requestHandlerTimeoutSecs

Timeout in which the function passed as [`requestHandler`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestHandler) needs to finish, in seconds.

### [**](#requestList)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L183)optionalinheritedrequestList

**requestList?

<!-- -->

: [IRequestList](https://crawlee.dev/js/api/core/interface/IRequestList.md)

Inherited from Omit.requestList

Static list of URLs to be processed. If not provided, the crawler will open the default request queue when the [`crawler.addRequests()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#addRequests) function is called.

> Alternatively, `requests` parameter of [`crawler.run()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#run) could be used to enqueue the initial requests - it is a shortcut for running `crawler.addRequests()` before the `crawler.run()`.

### [**](#requestManager)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L199)optionalinheritedrequestManager

**requestManager?

<!-- -->

: [IRequestManager](https://crawlee.dev/js/api/core/interface/IRequestManager.md)

Inherited from Omit.requestManager

Allows explicitly configuring a request manager. Mutually exclusive with the `requestQueue` and `requestList` options.

This enables explicitly configuring the crawler to use `RequestManagerTandem`, for instance. If using this, the type of `BasicCrawler.requestQueue` may not be fully compatible with the `RequestProvider` class.

### [**](#requestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L191)optionalinheritedrequestQueue

**requestQueue?

<!-- -->

: [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)

Inherited from Omit.requestQueue

Dynamic queue of URLs to be processed. This is useful for recursive crawling of websites. If not provided, the crawler will open the default request queue when the [`crawler.addRequests()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#addRequests) function is called.

> Alternatively, `requests` parameter of [`crawler.run()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#run) could be used to enqueue the initial requests - it is a shortcut for running `crawler.addRequests()` before the `crawler.run()`.

### [**](#respectRobotsTxtFile)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L376)optionalinheritedrespectRobotsTxtFile

**respectRobotsTxtFile?

<!-- -->

: boolean | { userAgent?

<!-- -->

: string }

Inherited from Omit.respectRobotsTxtFile

If set to `true`, the crawler will automatically try to fetch the robots.txt file for each domain, and skip those that are not allowed. This also prevents disallowed URLs to be added via `enqueueLinks`.

If an object is provided, it may contain a `userAgent` property to specify which user-agent should be used when checking the robots.txt file. If not provided, the default user-agent `*` will be used.

### [**](#resultChecker)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L196)optionalresultChecker

**resultChecker?

<!-- -->

: (result) => boolean

An optional callback that is called on dataset items found by the request handler in plain HTTP mode. If it returns false, the request is retried in a browser. If no callback is specified, every dataset item is considered valid.

***

#### Type declaration

* * **(result): boolean

  - #### Parameters

    * ##### result: [RequestHandlerResult](https://crawlee.dev/js/api/core/class/RequestHandlerResult.md)

    #### Returns boolean

### [**](#resultComparator)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L207)optionalresultComparator

**resultComparator?

<!-- -->

: (resultA, resultB) => boolean | equal | different | inconclusive

An optional callback used in rendering type detection. On each detection, the result of the plain HTTP run is compared to that of the browser one. If a callback is provided, the contract is as follows: It the callback returns true or 'equal', the results are considered equal and the target site is considered static. If it returns false or 'different', the target site is considered client-rendered. If it returns 'inconclusive', the detection result won't be used. If no result comparator is specified, but there is a `resultChecker`, any site where the `resultChecker` returns true is considered static. If neither `resultComparator` nor `resultChecker` are specified, a deep comparison of returned dataset items is used as a default.

***

#### Type declaration

* * **(resultA, resultB): boolean | equal | different | inconclusive

  - #### Parameters

    * ##### resultA: [RequestHandlerResult](https://crawlee.dev/js/api/core/class/RequestHandlerResult.md)
    * ##### resultB: [RequestHandlerResult](https://crawlee.dev/js/api/core/class/RequestHandlerResult.md)

    #### Returns boolean | equal | different | inconclusive

### [**](#retryOnBlocked)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L367)optionalinheritedretryOnBlocked

**retryOnBlocked?

<!-- -->

: boolean

Inherited from Omit.retryOnBlocked

If set to `true`, the crawler will automatically try to bypass any detected bot protection.

Currently supports:

* [**Cloudflare** Bot Management](https://www.cloudflare.com/products/bot-management/)
* [**Google Search** Rate Limiting](https://www.google.com/sorry/)

### [**](#sameDomainDelaySecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L264)optionalinheritedsameDomainDelaySecs

**sameDomainDelaySecs?

<!-- -->

: number = 0

Inherited from Omit.sameDomainDelaySecs

Indicates how much time (in seconds) to wait before crawling another same domain request.

### [**](#sessionPoolOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L335)optionalinheritedsessionPoolOptions

**sessionPoolOptions?

<!-- -->

: [SessionPoolOptions](https://crawlee.dev/js/api/core/interface/SessionPoolOptions.md)

Inherited from Omit.sessionPoolOptions

The configuration options for [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) to use.

### [**](#statisticsOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L401)optionalinheritedstatisticsOptions

**statisticsOptions?

<!-- -->

: [StatisticsOptions](https://crawlee.dev/js/api/core/interface/StatisticsOptions.md)

Inherited from Omit.statisticsOptions

Customize the way statistics collecting works, such as logging interval or whether to output them to the Key-Value store.

### [**](#statusMessageCallback)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L358)optionalinheritedstatusMessageCallback

**statusMessageCallback?

<!-- -->

: [StatusMessageCallback](https://crawlee.dev/js/api/basic-crawler.md#StatusMessageCallback)<[BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md)\<Dictionary>, [BasicCrawler](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md)<[BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md)\<Dictionary>>>

Inherited from Omit.statusMessageCallback

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

Inherited from Omit.statusMessageLoggingInterval

Defines the length of the interval for calling the `setStatusMessage` in seconds.

### [**](#useSessionPool)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L330)optionalinheriteduseSessionPool

**useSessionPool?

<!-- -->

: boolean

Inherited from Omit.useSessionPool

Basic crawler will initialize the [SessionPool](https://crawlee.dev/js/api/core/class/SessionPool.md) with the corresponding [`sessionPoolOptions`](https://crawlee.dev/js/api/core/interface/SessionPoolOptions.md). The session instance will be than available in the [`requestHandler`](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlerOptions.md#requestHandler).
