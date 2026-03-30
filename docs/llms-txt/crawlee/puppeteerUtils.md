# Source: https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md

# puppeteerUtils<!-- -->

A namespace that contains various utilities for [Puppeteer](https://github.com/puppeteer/puppeteer) - the headless Chrome Node API.

**Example usage:**

```
import { launchPuppeteer, utils } from 'crawlee';

// Open https://www.example.com in Puppeteer
const browser = await launchPuppeteer();
const page = await browser.newPage();
await page.goto('https://www.example.com');

// Inject jQuery into a page
await utils.puppeteer.injectJQuery(page);
```

## Index[**](#Index)

### References

* [**addInterceptRequestHandler](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#addInterceptRequestHandler)
* [**removeInterceptRequestHandler](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#removeInterceptRequestHandler)

### Interfaces

* [**BlockRequestsOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#BlockRequestsOptions)
* [**CompiledScriptParams](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#CompiledScriptParams)
* [**DirectNavigationOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#DirectNavigationOptions)
* [**InfiniteScrollOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#InfiniteScrollOptions)
* [**InjectFileOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#InjectFileOptions)
* [**SaveSnapshotOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#SaveSnapshotOptions)

### Type Aliases

* [**CompiledScriptFunction](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#CompiledScriptFunction)

### Functions

* [**blockRequests](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#blockRequests)
* [**blockResources](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#blockResources)
* [**cacheResponses](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#cacheResponses)
* [**closeCookieModals](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#closeCookieModals)
* [**compileScript](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#compileScript)
* [**enqueueLinksByClickingElements](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#enqueueLinksByClickingElements)
* [**gotoExtended](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#gotoExtended)
* [**infiniteScroll](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#infiniteScroll)
* [**injectFile](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#injectFile)
* [**injectJQuery](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#injectJQuery)
* [**parseWithCheerio](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#parseWithCheerio)
* [**saveSnapshot](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#saveSnapshot)

## References<!-- -->[**](#References)

### [**](#addInterceptRequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L1153)addInterceptRequestHandler

Re-exports

<!-- -->

[addInterceptRequestHandler](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerRequestInterception.md#addInterceptRequestHandler)

### [**](#removeInterceptRequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L1153)removeInterceptRequestHandler

Re-exports

<!-- -->

[removeInterceptRequestHandler](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerRequestInterception.md#removeInterceptRequestHandler)

## Interfaces<!-- -->[**](#Interfaces)

### [**](#BlockRequestsOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L83)BlockRequestsOptions

**BlockRequestsOptions:

### [**](#extraUrlPatterns)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L95)optionalextraUrlPatterns

**extraUrlPatterns?

<!-- -->

: string\[]

If you just want to append to the default blocked patterns, use this property.

### [**](#urlPatterns)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L90)optionalurlPatterns

**urlPatterns?

<!-- -->

: string\[]

The patterns of URLs to block from being loaded by the browser. Only `*` can be used as a wildcard. It is also automatically added to the beginning and end of the pattern. This limitation is enforced by the DevTools protocol. `.png` is the same as `*.png*`.

### [**](#CompiledScriptParams)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L98)CompiledScriptParams

**CompiledScriptParams:

### [**](#page)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L99)page

**page: Page

### [**](#request)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L100)request

**request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

### [**](#DirectNavigationOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L49)DirectNavigationOptions

**DirectNavigationOptions:

### [**](#referer)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L71)optionalreferer

**referer?

<!-- -->

: string

Referer header value. If provided it will take preference over the referer header value set by page.setExtraHTTPHeaders(headers).

### [**](#timeout)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L56)optionaltimeout

**timeout?

<!-- -->

: number

Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the browserContext.setDefaultNavigationTimeout(timeout), browserContext.setDefaultTimeout(timeout), page.setDefaultNavigationTimeout(timeout) or page.setDefaultTimeout(timeout) methods.

### [**](#waitUntil)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L66)optionalwaitUntil

**waitUntil?

<!-- -->

: domcontentloaded | load | networkidle | networkidle0 | networkidle2

When to consider operation succeeded, defaults to `load`. Events can be either:

* `domcontentloaded` - consider operation to be finished when the `DOMContentLoaded` event is fired.
* `load` - consider operation to be finished when the `load` event is fired.
* `networkidle0` - consider operation to be finished when there are no network connections for at least `500` ms.
* `networkidle2` - consider operation to be finished when there are no more than 2 network connections for at least `500` ms.
* `networkidle` - alias for `networkidle0`

### [**](#InfiniteScrollOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L525)InfiniteScrollOptions

**InfiniteScrollOptions:

### [**](#buttonSelector)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L553)optionalbuttonSelector

**buttonSelector?

<!-- -->

: string

Optionally checks and clicks a button if it appears while scrolling. This is required on some websites for the scroll to work.

### [**](#maxScrollHeight)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L536)optionalmaxScrollHeight

**maxScrollHeight?

<!-- -->

: number = 0

How many pixels to scroll down. If 0, will scroll until bottom of page.

### [**](#scrollDownAndUp)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L548)optionalscrollDownAndUp

**scrollDownAndUp?

<!-- -->

: boolean = false

If true, it will scroll up a bit after each scroll down. This is required on some websites for the scroll to work.

### [**](#stopScrollCallback)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L558)optionalstopScrollCallback

**stopScrollCallback?

<!-- -->

: () => unknown

This function is called after every scroll and stops the scrolling process if it returns `true`. The function can be `async`.

***

#### Type declaration

* * **(): unknown

  - #### Returns unknown

### [**](#timeoutSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L530)optionaltimeoutSecs

**timeoutSecs?

<!-- -->

: number = 0

How many seconds to scroll for. If 0, will scroll until bottom of page.

### [**](#waitForSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L542)optionalwaitForSecs

**waitForSecs?

<!-- -->

: number = 4

How many seconds to wait for no new content to load before exit.

### [**](#InjectFileOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L74)InjectFileOptions

**InjectFileOptions:

### [**](#surviveNavigations)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L80)optionalsurviveNavigations

**surviveNavigations?

<!-- -->

: boolean

Enables the injected script to survive page navigations and reloads without need to be re-injected manually. This does not mean, however, that internal state will be preserved. Just that it will be automatically re-injected on each navigation before any other scripts get the chance to execute.

### [**](#SaveSnapshotOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L689)SaveSnapshotOptions

**SaveSnapshotOptions:

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L724)optionalconfig

**config?

<!-- -->

: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) = [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)

Configuration of the crawler that will be used to save the snapshot.

### [**](#key)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L694)optionalkey

**key?

<!-- -->

: string = ‘SNAPSHOT’

Key under which the screenshot and HTML will be saved. `.jpg` will be appended for screenshot and `.html` for HTML.

### [**](#keyValueStoreName)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L718)optionalkeyValueStoreName

**keyValueStoreName?

<!-- -->

: null | string = null | string

Name or id of the Key-Value store where snapshot is saved. By default it is saved to default Key-Value store.

### [**](#saveHtml)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L712)optionalsaveHtml

**saveHtml?

<!-- -->

: boolean = true

If true, it will save a full HTML of the current page as a record with `key` appended by `.html`.

### [**](#saveScreenshot)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L706)optionalsaveScreenshot

**saveScreenshot?

<!-- -->

: boolean = true

If true, it will save a full screenshot of the current page as a record with `key` appended by `.jpg`.

### [**](#screenshotQuality)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L700)optionalscreenshotQuality

**screenshotQuality?

<!-- -->

: number = 50

The quality of the image, between 0-100. Higher quality images have bigger size and require more storage.

## Type Aliases<!-- -->[**](<#Type Aliases>)

### [**](#CompiledScriptFunction)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L103)CompiledScriptFunction

**CompiledScriptFunction: (params) => Promise\<unknown>

#### Type declaration

* * **(params): Promise\<unknown>

  - #### Parameters

    * ##### params: [CompiledScriptParams](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#CompiledScriptParams)

    #### Returns Promise\<unknown>

## Functions<!-- -->[**](#Functions)

### [**](#blockRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L281)blockRequests

* ****blockRequests**(page, options): Promise\<void>

- Forces the Puppeteer browser tab to block loading URLs that match a provided pattern. This is useful to speed up crawling of websites, since it reduces the amount of data that needs to be downloaded from the web, but it may break some websites or unexpectedly prevent loading of resources.

  By default, the function will block all URLs including the following patterns:

  ```
  [".css", ".jpg", ".jpeg", ".png", ".svg", ".gif", ".woff", ".pdf", ".zip"]
  ```

  If you want to extend this list further, use the `extraUrlPatterns` option, which will keep blocking the default patterns, as well as add your custom ones. If you would like to block only specific patterns, use the `urlPatterns` option, which will override the defaults and block only URLs with your custom patterns.

  This function does not use Puppeteer's request interception and therefore does not interfere with browser cache. It's also faster than blocking requests using interception, because the blocking happens directly in the browser without the round-trip to Node.js, but it does not provide the extra benefits of request interception.

  The function will never block main document loads and their respective redirects.

  **Example usage**

  ```
  import { launchPuppeteer, utils } from 'crawlee';

  const browser = await launchPuppeteer();
  const page = await browser.newPage();

  // Block all requests to URLs that include `adsbygoogle.js` and also all defaults.
  await utils.puppeteer.blockRequests(page, {
      extraUrlPatterns: ['adsbygoogle.js'],
  });

  await page.goto('https://cnn.com');
  ```

  ***

  #### Parameters

  * ##### page: Page

    Puppeteer [`Page`](https://pptr.dev/api/puppeteer.page) object.

  * ##### optionaloptions: [BlockRequestsOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#BlockRequestsOptions) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#blockResources)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L333)blockResources

* ****blockResources**(page, resourceTypes): Promise\<void>

- #### Parameters

  * ##### page: Page
  * ##### resourceTypes: string\[] = <!-- -->...

  #### Returns Promise\<void>

### [**](#cacheResponses)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L361)cacheResponses

* ****cacheResponses**(page, cache, responseUrlRules): Promise\<void>

- *NOTE:* In recent versions of Puppeteer using this function entirely disables browser cache which resolves in sub-optimal performance. Until this resolves, we suggest just relying on the in-browser cache unless absolutely necessary.

  Enables caching of intercepted responses into a provided object. Automatically enables request interception in Puppeteer. *IMPORTANT*: Caching responses stores them to memory, so too loose rules could cause memory leaks for longer running crawlers. This issue should be resolved or atleast mitigated in future iterations of this feature.

  * **@deprecated**

  ***

  #### Parameters

  * ##### page: Page

    Puppeteer [`Page`](https://pptr.dev/api/puppeteer.page) object.

  * ##### cache: Dictionary\<Partial\<ResponseForRequest>>

    Object in which responses are stored

  * ##### responseUrlRules: (string | RegExp)\[]

    List of rules that are used to check if the response should be cached. String rules are compared as page.url().includes(rule) while RegExp rules are evaluated as rule.test(page.url()).

  #### Returns Promise\<void>

### [**](#closeCookieModals)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L802)closeCookieModals

* ****closeCookieModals**(page): Promise\<void>

- #### Parameters

  * ##### page: Page

  #### Returns Promise\<void>

### [**](#compileScript)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L439)compileScript

* ****compileScript**(scriptString, context): [CompiledScriptFunction](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#CompiledScriptFunction)

- Compiles a Puppeteer script into an async function that may be executed at any time by providing it with the following object:

  ```
  {
     page: Page,
     request: Request,
  }
  ```

  Where `page` is a Puppeteer [`Page`](https://pptr.dev/api/puppeteer.page) and `request` is a [Request](https://crawlee.dev/js/api/core/class/Request.md).

  The function is compiled by using the `scriptString` parameter as the function's body, so any limitations to function bodies apply. Return value of the compiled function is the return value of the function body = the `scriptString` parameter.

  As a security measure, no globals such as `process` or `require` are accessible from within the function body. Note that the function does not provide a safe sandbox and even though globals are not easily accessible, malicious code may still execute in the main process via prototype manipulation. Therefore you should only use this function to execute sanitized or safe code.

  Custom context may also be provided using the `context` parameter. To improve security, make sure to only pass the really necessary objects to the context. Preferably making secured copies beforehand.

  ***

  #### Parameters

  * ##### scriptString: string
  * ##### context: Dictionary = <!-- -->...

  #### Returns [CompiledScriptFunction](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#CompiledScriptFunction)

### [**](#enqueueLinksByClickingElements)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/enqueue-links/click-elements.ts#L225)enqueueLinksByClickingElements

* ****enqueueLinksByClickingElements**(options): Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

- The function finds elements matching a specific CSS selector in a Puppeteer page, clicks all those elements using a mouse move and a left mouse button click and intercepts all the navigation requests that are subsequently produced by the page. The intercepted requests, including their methods, headers and payloads are then enqueued to a provided [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md). This is useful to crawl JavaScript heavy pages where links are not available in `href` elements, but rather navigations are triggered in click handlers. If you're looking to find URLs in `href` attributes of the page, see enqueueLinks.

  Optionally, the function allows you to filter the target links' URLs using an array of [PseudoUrl](https://crawlee.dev/js/api/core/class/PseudoUrl.md) objects and override settings of the enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

  **IMPORTANT**: To be able to do this, this function uses various mutations on the page, such as changing the Z-index of elements being clicked and their visibility. Therefore, it is recommended to only use this function as the last operation in the page.

  **USING HEADFUL BROWSER**: When using a headful browser, this function will only be able to click elements in the focused tab, effectively limiting concurrency to 1. In headless mode, full concurrency can be achieved.

  **PERFORMANCE**: Clicking elements with a mouse and intercepting requests is not a low level operation that takes nanoseconds. It's not very CPU intensive, but it takes time. We strongly recommend limiting the scope of the clicking as much as possible by using a specific selector that targets only the elements that you assume or know will produce a navigation. You can certainly click everything by using the `*` selector, but be prepared to wait minutes to get results on a large and complex page.

  **Example usage**

  ```
  await utils.puppeteer.enqueueLinksByClickingElements({
    page,
    requestQueue,
    selector: 'a.product-detail',
    pseudoUrls: [
        'https://www.example.com/handbags/[.*]'
        'https://www.example.com/purses/[.*]'
    ],
  });
  ```

  ***

  #### Parameters

  * ##### options: [EnqueueLinksByClickingElementsOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerClickElements.md#EnqueueLinksByClickingElementsOptions)

  #### Returns Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

  Promise that resolves to [BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md) object.

### [**](#gotoExtended)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L467)gotoExtended

* ****gotoExtended**(page, request, gotoOptions): Promise\<HTTPResponse | null>

- Extended version of Puppeteer's `page.goto()` allowing to perform requests with HTTP method other than GET, with custom headers and POST payload. URL, method, headers and payload are taken from request parameter that must be an instance of Request class.

  *NOTE:* In recent versions of Puppeteer using requests other than GET, overriding headers and adding payloads disables browser cache which degrades performance.

  ***

  #### Parameters

  * ##### page: Page

    Puppeteer [`Page`](https://pptr.dev/api/puppeteer.page) object.

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

  * ##### optionalgotoOptions: [DirectNavigationOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#DirectNavigationOptions) = <!-- -->{}

    Custom options for `page.goto()`.

  #### Returns Promise\<HTTPResponse | null>

### [**](#infiniteScroll)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L567)infiniteScroll

* ****infiniteScroll**(page, options): Promise\<void>

- Scrolls to the bottom of a page, or until it times out. Loads dynamic content when it hits the bottom of a page, and then continues scrolling.

  ***

  #### Parameters

  * ##### page: Page

    Puppeteer [`Page`](https://pptr.dev/api/puppeteer.page) object.

  * ##### optionaloptions: [InfiniteScrollOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#InfiniteScrollOptions) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#injectFile)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L121)injectFile

* ****injectFile**(page, filePath, options): Promise\<unknown>

- Injects a JavaScript file into a Puppeteer page. Unlike Puppeteer's `addScriptTag` function, this function works on pages with arbitrary Cross-Origin Resource Sharing (CORS) policies.

  File contents are cached for up to 10 files to limit file system access.

  ***

  #### Parameters

  * ##### page: Page

    Puppeteer [`Page`](https://pptr.dev/api/puppeteer.page) object.

  * ##### filePath: string

    File path

  * ##### optionaloptions: [InjectFileOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#InjectFileOptions) = <!-- -->{}

  #### Returns Promise\<unknown>

### [**](#injectJQuery)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L174)injectJQuery

* ****injectJQuery**(page, options): Promise\<unknown>

- Injects the [jQuery](https://jquery.com/) library into a Puppeteer page. jQuery is often useful for various web scraping and crawling tasks. For example, it can help extract text from HTML elements using CSS selectors.

  Beware that the injected jQuery object will be set to the `window.$` variable and thus it might cause conflicts with other libraries included by the page that use the same variable name (e.g. another version of jQuery). This can affect functionality of page's scripts.

  The injected jQuery will survive page navigations and reloads by default.

  **Example usage:**

  ```
  await utils.puppeteer.injectJQuery(page);
  const title = await page.evaluate(() => {
    return $('head title').text();
  });
  ```

  Note that `injectJQuery()` does not affect the Puppeteer's [`page.$()`](https://pptr.dev/api/puppeteer.page._/) function in any way.

  ***

  #### Parameters

  * ##### page: Page

    Puppeteer [`Page`](https://pptr.dev/api/puppeteer.page) object.

  * ##### optionaloptions: { surviveNavigations?<!-- -->: boolean }
    * ##### optionalsurviveNavigations: boolean

      Opt-out option to disable the JQuery reinjection after navigation.

  #### Returns Promise\<unknown>

### [**](#parseWithCheerio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L191)parseWithCheerio

* ****parseWithCheerio**(page, ignoreShadowRoots, ignoreIframes): Promise<[CheerioRoot](https://crawlee.dev/js/api/basic-crawler.md#CheerioRoot)>

- Returns Cheerio handle for `page.content()`, allowing to work with the data same way as with [CheerioCrawler](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md).

  **Example usage:**

  ```
  const $ = await utils.puppeteer.parseWithCheerio(page);
  const title = $('title').text();
  ```

  ***

  #### Parameters

  * ##### page: Page

    Puppeteer [`Page`](https://pptr.dev/api/puppeteer.page) object.

  * ##### ignoreShadowRoots: boolean = <!-- -->false

  * ##### ignoreIframes: boolean = <!-- -->false

  #### Returns Promise<[CheerioRoot](https://crawlee.dev/js/api/basic-crawler.md#CheerioRoot)>

### [**](#saveSnapshot)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L732)saveSnapshot

* ****saveSnapshot**(page, options): Promise\<void>

- Saves a full screenshot and HTML of the current page into a Key-Value store.

  ***

  #### Parameters

  * ##### page: Page

    Puppeteer [`Page`](https://pptr.dev/api/puppeteer.page) object.

  * ##### optionaloptions: [SaveSnapshotOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#SaveSnapshotOptions) = <!-- -->{}

  #### Returns Promise\<void>
