# Source: https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md

# playwrightUtils<!-- -->

A namespace that contains various utilities for [Playwright](https://github.com/microsoft/playwright) - the headless Chrome Node API.

**Example usage:**

```
import { launchPlaywright, playwrightUtils } from 'crawlee';

// Navigate to https://www.example.com in Playwright with a POST request
const browser = await launchPlaywright();
const page = await browser.newPage();
await playwrightUtils.gotoExtended(page, {
    url: 'https://example.com,
    method: 'POST',
});
```

## Index[**](#Index)

### Interfaces

* [**BlockRequestsOptions](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#BlockRequestsOptions)
* [**CompiledScriptParams](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#CompiledScriptParams)
* [**DirectNavigationOptions](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#DirectNavigationOptions)
* [**InfiniteScrollOptions](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#InfiniteScrollOptions)
* [**InjectFileOptions](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#InjectFileOptions)
* [**SaveSnapshotOptions](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#SaveSnapshotOptions)

### Type Aliases

* [**CompiledScriptFunction](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#CompiledScriptFunction)

### Functions

* [**blockRequests](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#blockRequests)
* [**closeCookieModals](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#closeCookieModals)
* [**compileScript](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#compileScript)
* [**enqueueLinksByClickingElements](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#enqueueLinksByClickingElements)
* [**gotoExtended](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#gotoExtended)
* [**infiniteScroll](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#infiniteScroll)
* [**injectFile](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#injectFile)
* [**injectJQuery](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#injectJQuery)
* [**parseWithCheerio](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#parseWithCheerio)
* [**registerUtilsToContext](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#registerUtilsToContext)
* [**saveSnapshot](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#saveSnapshot)

## Interfaces<!-- -->[**](#Interfaces)

### [**](#BlockRequestsOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L63)BlockRequestsOptions

**BlockRequestsOptions:

### [**](#extraUrlPatterns)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L75)optionalextraUrlPatterns

**extraUrlPatterns?

<!-- -->

: string\[]

If you just want to append to the default blocked patterns, use this property.

### [**](#urlPatterns)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L70)optionalurlPatterns

**urlPatterns?

<!-- -->

: string\[]

The patterns of URLs to block from being loaded by the browser. Only `*` can be used as a wildcard. It is also automatically added to the beginning and end of the pattern. This limitation is enforced by the DevTools protocol. `.png` is the same as `*.png*`.

### [**](#CompiledScriptParams)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L314)CompiledScriptParams

**CompiledScriptParams:

### [**](#page)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L315)page

**page: Page

### [**](#request)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L316)request

**request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

### [**](#DirectNavigationOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L153)DirectNavigationOptions

**DirectNavigationOptions:

### [**](#referer)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L173)optionalreferer

**referer?

<!-- -->

: string

Referer header value. If provided it will take preference over the referer header value set by page.setExtraHTTPHeaders(headers).

### [**](#timeout)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L160)optionaltimeout

**timeout?

<!-- -->

: number

Maximum operation time in milliseconds, defaults to 30 seconds, pass `0` to disable timeout. The default value can be changed by using the browserContext.setDefaultNavigationTimeout(timeout), browserContext.setDefaultTimeout(timeout), page.setDefaultNavigationTimeout(timeout) or page.setDefaultTimeout(timeout) methods.

### [**](#waitUntil)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L168)optionalwaitUntil

**waitUntil?

<!-- -->

: domcontentloaded | load | networkidle

When to consider operation succeeded, defaults to `load`. Events can be either:

* `'domcontentloaded'` - consider operation to be finished when the `DOMContentLoaded` event is fired.
* `'load'` - consider operation to be finished when the `load` event is fired.
* `'networkidle'` - consider operation to be finished when there are no network connections for at least `500` ms.

### [**](#InfiniteScrollOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L363)InfiniteScrollOptions

**InfiniteScrollOptions:

### [**](#buttonSelector)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L391)optionalbuttonSelector

**buttonSelector?

<!-- -->

: string

Optionally checks and clicks a button if it appears while scrolling. This is required on some websites for the scroll to work.

### [**](#maxScrollHeight)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L374)optionalmaxScrollHeight

**maxScrollHeight?

<!-- -->

: number = 0

How many pixels to scroll down. If 0, will scroll until bottom of page.

### [**](#scrollDownAndUp)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L386)optionalscrollDownAndUp

**scrollDownAndUp?

<!-- -->

: boolean = false

If true, it will scroll up a bit after each scroll down. This is required on some websites for the scroll to work.

### [**](#stopScrollCallback)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L396)optionalstopScrollCallback

**stopScrollCallback?

<!-- -->

: () => unknown

This function is called after every scroll and stops the scrolling process if it returns `true`. The function can be `async`.

***

#### Type declaration

* * **(): unknown

  - #### Returns unknown

### [**](#timeoutSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L368)optionaltimeoutSecs

**timeoutSecs?

<!-- -->

: number = 0

How many seconds to scroll for. If 0, will scroll until bottom of page.

### [**](#waitForSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L380)optionalwaitForSecs

**waitForSecs?

<!-- -->

: number = 4

How many seconds to wait for no new content to load before exit.

### [**](#InjectFileOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L54)InjectFileOptions

**InjectFileOptions:

### [**](#surviveNavigations)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L60)optionalsurviveNavigations

**surviveNavigations?

<!-- -->

: boolean

Enables the injected script to survive page navigations and reloads without need to be re-injected manually. This does not mean, however, that internal state will be preserved. Just that it will be automatically re-injected on each navigation before any other scripts get the chance to execute.

### [**](#SaveSnapshotOptions)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L505)SaveSnapshotOptions

**SaveSnapshotOptions:

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L540)optionalconfig

**config?

<!-- -->

: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) = [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)

Configuration of the crawler that will be used to save the snapshot.

### [**](#key)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L510)optionalkey

**key?

<!-- -->

: string = ‘SNAPSHOT’

Key under which the screenshot and HTML will be saved. `.jpg` will be appended for screenshot and `.html` for HTML.

### [**](#keyValueStoreName)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L534)optionalkeyValueStoreName

**keyValueStoreName?

<!-- -->

: null | string = null | string

Name or id of the Key-Value store where snapshot is saved. By default it is saved to default Key-Value store.

### [**](#saveHtml)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L528)optionalsaveHtml

**saveHtml?

<!-- -->

: boolean = true

If true, it will save a full HTML of the current page as a record with `key` appended by `.html`.

### [**](#saveScreenshot)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L522)optionalsaveScreenshot

**saveScreenshot?

<!-- -->

: boolean = true

If true, it will save a full screenshot of the current page as a record with `key` appended by `.jpg`.

### [**](#screenshotQuality)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L516)optionalscreenshotQuality

**screenshotQuality?

<!-- -->

: number = 50

The quality of the image, between 0-100. Higher quality images have bigger size and require more storage.

## Type Aliases<!-- -->[**](<#Type Aliases>)

### [**](#CompiledScriptFunction)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L319)CompiledScriptFunction

**CompiledScriptFunction: (params) => Promise\<unknown>

#### Type declaration

* * **(params): Promise\<unknown>

  - #### Parameters

    * ##### params: [CompiledScriptParams](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#CompiledScriptParams)

    #### Returns Promise\<unknown>

## Functions<!-- -->[**](#Functions)

### [**](#blockRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L290)blockRequests

* ****blockRequests**(page, options): Promise\<void>

- > This is a **Chromium-only feature.**
  >
  > Using this option with Firefox and WebKit browsers doesn't have any effect. To set up request blocking for these browsers, use `page.route()` instead.

  Forces the Playwright browser tab to block loading URLs that match a provided pattern. This is useful to speed up crawling of websites, since it reduces the amount of data that needs to be downloaded from the web, but it may break some websites or unexpectedly prevent loading of resources.

  By default, the function will block all URLs including the following patterns:

  ```
  [".css", ".jpg", ".jpeg", ".png", ".svg", ".gif", ".woff", ".pdf", ".zip"]
  ```

  If you want to extend this list further, use the `extraUrlPatterns` option, which will keep blocking the default patterns, as well as add your custom ones. If you would like to block only specific patterns, use the `urlPatterns` option, which will override the defaults and block only URLs with your custom patterns.

  This function does not use Playwright's request interception and therefore does not interfere with browser cache. It's also faster than blocking requests using interception, because the blocking happens directly in the browser without the round-trip to Node.js, but it does not provide the extra benefits of request interception.

  The function will never block main document loads and their respective redirects.

  **Example usage**

  ```
  import { launchPlaywright, playwrightUtils } from 'crawlee';

  const browser = await launchPlaywright();
  const page = await browser.newPage();

  // Block all requests to URLs that include `adsbygoogle.js` and also all defaults.
  await playwrightUtils.blockRequests(page, {
      extraUrlPatterns: ['adsbygoogle.js'],
  });

  await page.goto('https://cnn.com');
  ```

  ***

  #### Parameters

  * ##### page: Page

    Playwright [`Page`](https://playwright.dev/docs/api/class-page) object.

  * ##### optionaloptions: [BlockRequestsOptions](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#BlockRequestsOptions) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#closeCookieModals)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L680)closeCookieModals

* ****closeCookieModals**(page): Promise\<void>

- #### Parameters

  * ##### page: Page

  #### Returns Promise\<void>

### [**](#compileScript)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L347)compileScript

* ****compileScript**(scriptString, context): [CompiledScriptFunction](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#CompiledScriptFunction)

- Compiles a Playwright script into an async function that may be executed at any time by providing it with the following object:

  ```
  {
     page: Page,
     request: Request,
  }
  ```

  Where `page` is a Playwright [`Page`](https://playwright.dev/docs/api/class-page) and `request` is a [Request](https://crawlee.dev/js/api/core/class/Request.md).

  The function is compiled by using the `scriptString` parameter as the function's body, so any limitations to function bodies apply. Return value of the compiled function is the return value of the function body = the `scriptString` parameter.

  As a security measure, no globals such as `process` or `require` are accessible from within the function body. Note that the function does not provide a safe sandbox and even though globals are not easily accessible, malicious code may still execute in the main process via prototype manipulation. Therefore you should only use this function to execute sanitized or safe code.

  Custom context may also be provided using the `context` parameter. To improve security, make sure to only pass the really necessary objects to the context. Preferably making secured copies beforehand.

  ***

  #### Parameters

  * ##### scriptString: string
  * ##### context: Dictionary = <!-- -->...

  #### Returns [CompiledScriptFunction](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#CompiledScriptFunction)

### [**](#enqueueLinksByClickingElements)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/enqueue-links/click-elements.ts#L225)enqueueLinksByClickingElements

* ****enqueueLinksByClickingElements**(options): Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

- The function finds elements matching a specific CSS selector in a Playwright page, clicks all those elements using a mouse move and a left mouse button click and intercepts all the navigation requests that are subsequently produced by the page. The intercepted requests, including their methods, headers and payloads are then enqueued to a provided [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md). This is useful to crawl JavaScript heavy pages where links are not available in `href` elements, but rather navigations are triggered in click handlers. If you're looking to find URLs in `href` attributes of the page, see enqueueLinks.

  Optionally, the function allows you to filter the target links' URLs using an array of [PseudoUrl](https://crawlee.dev/js/api/core/class/PseudoUrl.md) objects and override settings of the enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

  **IMPORTANT**: To be able to do this, this function uses various mutations on the page, such as changing the Z-index of elements being clicked and their visibility. Therefore, it is recommended to only use this function as the last operation in the page.

  **USING HEADFUL BROWSER**: When using a headful browser, this function will only be able to click elements in the focused tab, effectively limiting concurrency to 1. In headless mode, full concurrency can be achieved.

  **PERFORMANCE**: Clicking elements with a mouse and intercepting requests is not a low level operation that takes nanoseconds. It's not very CPU intensive, but it takes time. We strongly recommend limiting the scope of the clicking as much as possible by using a specific selector that targets only the elements that you assume or know will produce a navigation. You can certainly click everything by using the `*` selector, but be prepared to wait minutes to get results on a large and complex page.

  **Example usage**

  ```
  await playwrightUtils.enqueueLinksByClickingElements({
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

  * ##### options: [EnqueueLinksByClickingElementsOptions](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightClickElements.md#EnqueueLinksByClickingElementsOptions)

  #### Returns Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

  Promise that resolves to [BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md) object.

### [**](#gotoExtended)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L188)gotoExtended

* ****gotoExtended**(page, request, gotoOptions): Promise\<Response | null>

- Extended version of Playwright's `page.goto()` allowing to perform requests with HTTP method other than GET, with custom headers and POST payload. URL, method, headers and payload are taken from request parameter that must be an instance of Request class.

  *NOTE:* In recent versions of Playwright using requests other than GET, overriding headers and adding payloads disables browser cache which degrades performance.

  ***

  #### Parameters

  * ##### page: Page

    Playwright [`Page`](https://playwright.dev/docs/api/class-page) object.

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

  * ##### optionalgotoOptions: [DirectNavigationOptions](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#DirectNavigationOptions) = <!-- -->{}

    Custom options for `page.goto()`.

  #### Returns Promise\<Response | null>

### [**](#infiniteScroll)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L405)infiniteScroll

* ****infiniteScroll**(page, options): Promise\<void>

- Scrolls to the bottom of a page, or until it times out. Loads dynamic content when it hits the bottom of a page, and then continues scrolling.

  ***

  #### Parameters

  * ##### page: Page

    Playwright [`Page`](https://playwright.dev/docs/api/class-page) object.

  * ##### optionaloptions: [InfiniteScrollOptions](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#InfiniteScrollOptions) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#injectFile)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L94)injectFile

* ****injectFile**(page, filePath, options): Promise\<unknown>

- Injects a JavaScript file into a Playwright page. Unlike Playwright's `addScriptTag` function, this function works on pages with arbitrary Cross-Origin Resource Sharing (CORS) policies.

  File contents are cached for up to 10 files to limit file system access.

  ***

  #### Parameters

  * ##### page: Page

    Playwright [`Page`](https://playwright.dev/docs/api/class-page) object.

  * ##### filePath: string

    File path

  * ##### optionaloptions: [InjectFileOptions](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#InjectFileOptions) = <!-- -->{}

  #### Returns Promise\<unknown>

### [**](#injectJQuery)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L148)injectJQuery

* ****injectJQuery**(page, options): Promise\<unknown>

- Injects the [jQuery](https://jquery.com/) library into a Playwright page. jQuery is often useful for various web scraping and crawling tasks. For example, it can help extract text from HTML elements using CSS selectors.

  Beware that the injected jQuery object will be set to the `window.$` variable and thus it might cause conflicts with other libraries included by the page that use the same variable name (e.g. another version of jQuery). This can affect functionality of page's scripts.

  The injected jQuery will survive page navigations and reloads by default.

  **Example usage:**

  ```
  await playwrightUtils.injectJQuery(page);
  const title = await page.evaluate(() => {
    return $('head title').text();
  });
  ```

  Note that `injectJQuery()` does not affect the Playwright [`page.$()`](https://playwright.dev/docs/api/class-page#page-query-selector) function in any way.

  ***

  #### Parameters

  * ##### page: Page

    Playwright [`Page`](https://playwright.dev/docs/api/class-page) object.

  * ##### optionaloptions: { surviveNavigations?<!-- -->: boolean }
    * ##### optionalsurviveNavigations: boolean

      Opt-out option to disable the JQuery reinjection after navigation.

  #### Returns Promise\<unknown>

### [**](#parseWithCheerio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L609)parseWithCheerio

* ****parseWithCheerio**(page, ignoreShadowRoots, ignoreIframes): Promise<[CheerioRoot](https://crawlee.dev/js/api/basic-crawler.md#CheerioRoot)>

- Returns Cheerio handle for `page.content()`, allowing to work with the data same way as with [CheerioCrawler](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md).

  **Example usage:**

  ```
  const $ = await playwrightUtils.parseWithCheerio(page);
  const title = $('title').text();
  ```

  ***

  #### Parameters

  * ##### page: Page

    Playwright [`Page`](https://playwright.dev/docs/api/class-page) object.

  * ##### ignoreShadowRoots: boolean = <!-- -->false

  * ##### ignoreIframes: boolean = <!-- -->false

  #### Returns Promise<[CheerioRoot](https://crawlee.dev/js/api/basic-crawler.md#CheerioRoot)>

### [**](#registerUtilsToContext)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L1067)registerUtilsToContext

* ****registerUtilsToContext**(context, crawlerOptions): void

- #### Parameters

  * ##### context: [PlaywrightCrawlingContext](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlingContext.md)\<Dictionary>
  * ##### crawlerOptions: [PlaywrightCrawlerOptions](https://crawlee.dev/js/api/playwright-crawler/interface/PlaywrightCrawlerOptions.md)

  #### Returns void

### [**](#saveSnapshot)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/utils/playwright-utils.ts#L548)saveSnapshot

* ****saveSnapshot**(page, options): Promise\<void>

- Saves a full screenshot and HTML of the current page into a Key-Value store.

  ***

  #### Parameters

  * ##### page: Page

    Playwright [`Page`](https://playwright.dev/docs/api/class-page) object.

  * ##### optionaloptions: [SaveSnapshotOptions](https://crawlee.dev/js/api/playwright-crawler/namespace/playwrightUtils.md#SaveSnapshotOptions) = <!-- -->{}

  #### Returns Promise\<void>
