# Source: https://crawlee.dev/js/api/puppeteer-crawler/interface/PuppeteerCrawlingContext.md

# PuppeteerCrawlingContext<!-- --> \<UserData>

### Hierarchy

* [BrowserCrawlingContext](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlingContext.md)<[PuppeteerCrawler](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md), Page, HTTPResponse, [PuppeteerController](https://crawlee.dev/js/api/browser-pool/class/PuppeteerController.md), UserData>
* PuppeteerContextUtils
  * *PuppeteerCrawlingContext*

## Index[**](#Index)

### Properties

* [**addRequests](#addRequests)
* [**browserController](#browserController)
* [**crawler](#crawler)
* [**getKeyValueStore](#getKeyValueStore)
* [**id](#id)
* [**log](#log)
* [**page](#page)
* [**proxyInfo](#proxyInfo)
* [**request](#request)
* [**response](#response)
* [**session](#session)
* [**useState](#useState)

### Methods

* [**addInterceptRequestHandler](#addInterceptRequestHandler)
* [**blockRequests](#blockRequests)
* [**blockResources](#blockResources)
* [**cacheResponses](#cacheResponses)
* [**closeCookieModals](#closeCookieModals)
* [**compileScript](#compileScript)
* [**enqueueLinks](#enqueueLinks)
* [**enqueueLinksByClickingElements](#enqueueLinksByClickingElements)
* [**infiniteScroll](#infiniteScroll)
* [**injectFile](#injectFile)
* [**injectJQuery](#injectJQuery)
* [**parseWithCheerio](#parseWithCheerio)
* [**pushData](#pushData)
* [**removeInterceptRequestHandler](#removeInterceptRequestHandler)
* [**saveSnapshot](#saveSnapshot)
* [**sendRequest](#sendRequest)
* [**waitForSelector](#waitForSelector)

## Properties<!-- -->[**](#Properties)

### [**](#addRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L89)inheritedaddRequests

**addRequests: (requestsLike, options) => Promise\<void>

Inherited from BrowserCrawlingContext.addRequests

Add requests directly to the request queue.

***

#### Type declaration

* * **(requestsLike, options): Promise\<void>

  - #### Parameters

    * ##### requestsLike: readonly<!-- --> (string | ReadonlyObjectDeep\<Partial<[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)\<Dictionary>> & { regex?<!-- -->: RegExp; requestsFromUrl?<!-- -->: string }> | ReadonlyObjectDeep<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>)\[]

    * ##### optionaloptions: ReadonlyObjectDeep<[RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)>

      Options for the request queue

    #### Returns Promise\<void>

### [**](#browserController)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L59)inheritedbrowserController

**browserController: [PuppeteerController](https://crawlee.dev/js/api/browser-pool/class/PuppeteerController.md)

Inherited from BrowserCrawlingContext.browserController

### [**](#crawler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L114)inheritedcrawler

**crawler: [PuppeteerCrawler](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md)

Inherited from BrowserCrawlingContext.crawler

### [**](#getKeyValueStore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L148)inheritedgetKeyValueStore

**getKeyValueStore: (idOrName) => Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

Inherited from BrowserCrawlingContext.getKeyValueStore

Get a key-value store with given name or id, or the default one for the crawler.

***

#### Type declaration

* * **(idOrName): Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

  - #### Parameters

    * ##### optionalidOrName: string

    #### Returns Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L34)inheritedid

**id: string

Inherited from BrowserCrawlingContext.id

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L109)inheritedlog

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

Inherited from BrowserCrawlingContext.log

A preconfigured logger for the request handler.

### [**](#page)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L60)inheritedpage

**page: Page

Inherited from BrowserCrawlingContext.page

### [**](#proxyInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L41)optionalinheritedproxyInfo

**proxyInfo?

<!-- -->

: [ProxyInfo](https://crawlee.dev/js/api/core/interface/ProxyInfo.md)

Inherited from BrowserCrawlingContext.proxyInfo

An object with information about currently used proxy by the crawler and configured by the [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md) class.

### [**](#request)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L46)inheritedrequest

**request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<UserData>

Inherited from BrowserCrawlingContext.request

The original [Request](https://crawlee.dev/js/api/core/class/Request.md) object.

### [**](#response)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/browser-crawler/src/internals/browser-crawler.ts#L61)optionalinheritedresponse

**response?

<!-- -->

: HTTPResponse

Inherited from BrowserCrawlingContext.response

### [**](#session)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L35)optionalinheritedsession

**session?

<!-- -->

: [Session](https://crawlee.dev/js/api/core/class/Session.md)

Inherited from BrowserCrawlingContext.session

### [**](#useState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L97)inheriteduseState

**useState: \<State>(defaultValue) => Promise\<State>

Inherited from BrowserCrawlingContext.useState

Returns the state - a piece of mutable persistent data shared across all the request handler runs.

***

#### Type declaration

* * **\<State>(defaultValue): Promise\<State>

  - #### Parameters

    * ##### optionaldefaultValue: State

    #### Returns Promise\<State>

## Methods<!-- -->[**](#Methods)

### [**](#addInterceptRequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L1064)inheritedaddInterceptRequestHandler

* ****addInterceptRequestHandler**(handler): Promise\<void>

- Inherited from PuppeteerContextUtils.addInterceptRequestHandler

  Adds request interception handler in similar to `page.on('request', handler);` but in addition to that supports multiple parallel handlers.

  All the handlers are executed sequentially in the order as they were added. Each of the handlers must call one of `request.continue()`, `request.abort()` and `request.respond()`. In addition to that any of the handlers may modify the request object (method, postData, headers) by passing its overrides to `request.continue()`. If multiple handlers modify same property then the last one wins. Headers are merged separately so you can override only a value of specific header.

  If one the handlers calls `request.abort()` or `request.respond()` then request is not propagated further to any of the remaining handlers.

  **Example usage:**

  ```
  preNavigationHooks: [
      async ({ addInterceptRequestHandler }) => {
          // Replace images with placeholder.
          await addInterceptRequestHandler((request) => {
              if (request.resourceType() === 'image') {
                  return request.respond({
                      statusCode: 200,
                      contentType: 'image/jpeg',
                      body: placeholderImageBuffer,
                  });
              }
              return request.continue();
          });

          // Abort all the scripts.
          await addInterceptRequestHandler((request) => {
              if (request.resourceType() === 'script') return request.abort();
              return request.continue();
          });

          // Change requests to post.
          await addInterceptRequestHandler((request) => {
              return request.continue({
                   method: 'POST',
              });
          });
      }),
  ],
  ```

  ***

  #### Parameters

  * ##### handler: [InterceptHandler](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerRequestInterception.md#InterceptHandler)

    Request interception handler.

  #### Returns Promise\<void>

### [**](#blockRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L959)inheritedblockRequests

* ****blockRequests**(options): Promise\<void>

- Inherited from PuppeteerContextUtils.blockRequests

  Forces the Puppeteer browser tab to block loading URLs that match a provided pattern. This is useful to speed up crawling of websites, since it reduces the amount of data that needs to be downloaded from the web, but it may break some websites or unexpectedly prevent loading of resources.

  By default, the function will block all URLs including the following patterns:

  ```
  [".css", ".jpg", ".jpeg", ".png", ".svg", ".gif", ".woff", ".pdf", ".zip"]
  ```

  If you want to extend this list further, use the `extraUrlPatterns` option, which will keep blocking the default patterns, as well as add your custom ones. If you would like to block only specific patterns, use the `urlPatterns` option, which will override the defaults and block only URLs with your custom patterns.

  This function does not use Puppeteer's request interception and therefore does not interfere with browser cache. It's also faster than blocking requests using interception, because the blocking happens directly in the browser without the round-trip to Node.js, but it does not provide the extra benefits of request interception.

  The function will never block main document loads and their respective redirects.

  **Example usage**

  ```
  preNavigationHooks: [
      async ({ blockRequests }) => {
          // Block all requests to URLs that include `adsbygoogle.js` and also all defaults.
          await blockRequests({
              extraUrlPatterns: ['adsbygoogle.js'],
          }),
      }),
  ],
  ```

  ***

  #### Parameters

  * ##### optionaloptions: [BlockRequestsOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#BlockRequestsOptions)

  #### Returns Promise\<void>

### [**](#blockResources)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L966)inheritedblockResources

* ****blockResources**(resourceTypes): Promise\<void>

- Inherited from PuppeteerContextUtils.blockResources

  `blockResources()` has a high impact on performance in recent versions of Puppeteer. Until this resolves, please use `utils.puppeteer.blockRequests()`.

  * **@deprecated**

  ***

  #### Parameters

  * ##### optionalresourceTypes: string\[]

  #### Returns Promise\<void>

### [**](#cacheResponses)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L982)inheritedcacheResponses

* ****cacheResponses**(cache, responseUrlRules): Promise\<void>

- Inherited from PuppeteerContextUtils.cacheResponses

  *NOTE:* In recent versions of Puppeteer using this function entirely disables browser cache which resolves in sub-optimal performance. Until this resolves, we suggest just relying on the in-browser cache unless absolutely necessary.

  Enables caching of intercepted responses into a provided object. Automatically enables request interception in Puppeteer. *IMPORTANT*: Caching responses stores them to memory, so too loose rules could cause memory leaks for longer running crawlers. This issue should be resolved or atleast mitigated in future iterations of this feature.

  * **@deprecated**

  ***

  #### Parameters

  * ##### cache: Dictionary\<Partial\<ResponseForRequest>>

    Object in which responses are stored

  * ##### responseUrlRules: (string | RegExp)\[]

    List of rules that are used to check if the response should be cached. String rules are compared as page.url().includes(rule) while RegExp rules are evaluated as rule.test(page.url()).

  #### Returns Promise\<void>

### [**](#closeCookieModals)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L1096)inheritedcloseCookieModals

* ****closeCookieModals**(): Promise\<void>

- Inherited from PuppeteerContextUtils.closeCookieModals

  Tries to close cookie consent modals on the page. Based on the I Don't Care About Cookies browser extension.

  Note that this method requires the idcac-playwright package to be installed. Crawlee does not include it by default due to licensing issues.

  To use this method, please install the package manually by running:

  ```
  npm install idcac-playwright
  ```

  ***

  #### Returns Promise\<void>

### [**](#compileScript)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L1013)inheritedcompileScript

* ****compileScript**(scriptString, ctx): [CompiledScriptFunction](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#CompiledScriptFunction)

- Inherited from PuppeteerContextUtils.compileScript

  Compiles a Puppeteer script into an async function that may be executed at any time by providing it with the following object:

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
  * ##### optionalctx: Dictionary

  #### Returns [CompiledScriptFunction](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#CompiledScriptFunction)

### [**](#enqueueLinks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L141)inheritedenqueueLinks

* ****enqueueLinks**(options): Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

- Inherited from BrowserCrawlingContext.enqueueLinks

  This function automatically finds and enqueues links from the current page, adding them to the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) currently used by the crawler.

  Optionally, the function allows you to filter the target links' URLs using an array of globs or regular expressions and override settings of the enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

  Check out the [Crawl a website with relative links](https://crawlee.dev/js/docs/examples/crawl-relative-links.md) example for more details regarding its usage.

  **Example usage**

  ```
  async requestHandler({ enqueueLinks }) {
      await enqueueLinks({
        globs: [
            'https://www.example.com/handbags/*',
        ],
      });
  },
  ```

  ***

  #### Parameters

  * ##### optionaloptions: ReadonlyObjectDeep\<Omit<[EnqueueLinksOptions](https://crawlee.dev/js/api/core/interface/EnqueueLinksOptions.md), requestQueue>> & Pick<[EnqueueLinksOptions](https://crawlee.dev/js/api/core/interface/EnqueueLinksOptions.md), requestQueue>

    All `enqueueLinks()` parameters are passed via an options object.

  #### Returns Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

  Promise that resolves to [BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md) object.

### [**](#enqueueLinksByClickingElements)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L919)inheritedenqueueLinksByClickingElements

* ****enqueueLinksByClickingElements**(options): Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

- Inherited from PuppeteerContextUtils.enqueueLinksByClickingElements

  The function finds elements matching a specific CSS selector in a Puppeteer page, clicks all those elements using a mouse move and a left mouse button click and intercepts all the navigation requests that are subsequently produced by the page. The intercepted requests, including their methods, headers and payloads are then enqueued to a provided [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md). This is useful to crawl JavaScript heavy pages where links are not available in `href` elements, but rather navigations are triggered in click handlers. If you're looking to find URLs in `href` attributes of the page, see enqueueLinks.

  Optionally, the function allows you to filter the target links' URLs using an array of [PseudoUrl](https://crawlee.dev/js/api/core/class/PseudoUrl.md) objects and override settings of the enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

  **IMPORTANT**: To be able to do this, this function uses various mutations on the page, such as changing the Z-index of elements being clicked and their visibility. Therefore, it is recommended to only use this function as the last operation in the page.

  **USING HEADFUL BROWSER**: When using a headful browser, this function will only be able to click elements in the focused tab, effectively limiting concurrency to 1. In headless mode, full concurrency can be achieved.

  **PERFORMANCE**: Clicking elements with a mouse and intercepting requests is not a low level operation that takes nanoseconds. It's not very CPU intensive, but it takes time. We strongly recommend limiting the scope of the clicking as much as possible by using a specific selector that targets only the elements that you assume or know will produce a navigation. You can certainly click everything by using the `*` selector, but be prepared to wait minutes to get results on a large and complex page.

  **Example usage**

  ```
  async requestHandler({ enqueueLinksByClickingElements }) {
      await enqueueLinksByClickingElements({
          selector: 'a.product-detail',
          globs: [
              'https://www.example.com/handbags/**'
              'https://www.example.com/purses/**'
          ],
      });
  });
  ```

  ***

  #### Parameters

  * ##### options: Omit<[EnqueueLinksByClickingElementsOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerClickElements.md#EnqueueLinksByClickingElementsOptions), requestQueue | page>

  #### Returns Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

  Promise that resolves to [BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md) object.

### [**](#infiniteScroll)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L1077)inheritedinfiniteScroll

* ****infiniteScroll**(options): Promise\<void>

- Inherited from PuppeteerContextUtils.infiniteScroll

  Scrolls to the bottom of a page, or until it times out. Loads dynamic content when it hits the bottom of a page, and then continues scrolling.

  ***

  #### Parameters

  * ##### optionaloptions: [InfiniteScrollOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#InfiniteScrollOptions)

  #### Returns Promise\<void>

### [**](#injectFile)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L820)inheritedinjectFile

* ****injectFile**(filePath, options): Promise\<unknown>

- Inherited from PuppeteerContextUtils.injectFile

  Injects a JavaScript file into current `page`. Unlike Puppeteer's `addScriptTag` function, this function works on pages with arbitrary Cross-Origin Resource Sharing (CORS) policies.

  File contents are cached for up to 10 files to limit file system access.

  ***

  #### Parameters

  * ##### filePath: string
  * ##### optionaloptions: [InjectFileOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#InjectFileOptions)

  #### Returns Promise\<unknown>

### [**](#injectJQuery)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L847)inheritedinjectJQuery

* ****injectJQuery**(): Promise\<unknown>

- Inherited from PuppeteerContextUtils.injectJQuery

  Injects the [jQuery](https://jquery.com/) library into current `page`. jQuery is often useful for various web scraping and crawling tasks. For example, it can help extract text from HTML elements using CSS selectors.

  Beware that the injected jQuery object will be set to the `window.$` variable and thus it might cause conflicts with other libraries included by the page that use the same variable name (e.g. another version of jQuery). This can affect functionality of page's scripts.

  The injected jQuery will survive page navigations and reloads.

  **Example usage:**

  ```
  async requestHandler({ page, injectJQuery }) {
      await injectJQuery();
      const title = await page.evaluate(() => {
          return $('head title').text();
      });
  });
  ```

  Note that `injectJQuery()` does not affect the Puppeteer's [`page.$()`](https://pptr.dev/api/puppeteer.page._/) function in any way.

  ***

  #### Returns Promise\<unknown>

### [**](#parseWithCheerio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L876)inheritedparseWithCheerio

* ****parseWithCheerio**(selector, timeoutMs): Promise<[CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)>

- Inherited from PuppeteerContextUtils.parseWithCheerio

  Returns Cheerio handle for `page.content()`, allowing to work with the data same way as with [CheerioCrawler](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md). When provided with the `selector` argument, it waits for it to be available first.

  **Example usage:**

  ```
  async requestHandler({ parseWithCheerio }) {
      const $ = await parseWithCheerio();
      const title = $('title').text();
  });
  ```

  ***

  #### Parameters

  * ##### optionalselector: string
  * ##### optionaltimeoutMs: number

  #### Returns Promise<[CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)>

### [**](#pushData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L55)inheritedpushData

* ****pushData**(data, datasetIdOrName): Promise\<void>

- Inherited from BrowserCrawlingContext.pushData

  This function allows you to push data to a [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) specified by name, or the one currently used by the crawler.

  Shortcut for `crawler.pushData()`.

  ***

  #### Parameters

  * ##### optionaldata: ReadonlyDeep\<Dictionary | Dictionary\[]>

    Data to be pushed to the default dataset.

  * ##### optionaldatasetIdOrName: string

  #### Returns Promise\<void>

### [**](#removeInterceptRequestHandler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L1071)inheritedremoveInterceptRequestHandler

* ****removeInterceptRequestHandler**(handler): Promise\<void>

- Inherited from PuppeteerContextUtils.removeInterceptRequestHandler

  Removes request interception handler for given page.

  ***

  #### Parameters

  * ##### handler: [InterceptHandler](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerRequestInterception.md#InterceptHandler)

    Request interception handler.

  #### Returns Promise\<void>

### [**](#saveSnapshot)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L1082)inheritedsaveSnapshot

* ****saveSnapshot**(options): Promise\<void>

- Inherited from PuppeteerContextUtils.saveSnapshot

  Saves a full screenshot and HTML of the current page into a Key-Value store.

  ***

  #### Parameters

  * ##### optionaloptions: [SaveSnapshotOptions](https://crawlee.dev/js/api/puppeteer-crawler/namespace/puppeteerUtils.md#SaveSnapshotOptions)

  #### Returns Promise\<void>

### [**](#sendRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L167)inheritedsendRequest

* ****sendRequest**\<Response>(overrideOptions): Promise\<Response\<Response>>

- Inherited from BrowserCrawlingContext.sendRequest

  Fires HTTP request via [`got-scraping`](https://crawlee.dev/js/docs/guides/got-scraping.md), allowing to override the request options on the fly.

  This is handy when you work with a browser crawler but want to execute some requests outside it (e.g. API requests). Check the [Skipping navigations for certain requests](https://crawlee.dev/js/docs/examples/skip-navigation.md) example for more detailed explanation of how to do that.

  ```
  async requestHandler({ sendRequest }) {
      const { body } = await sendRequest({
          // override headers only
          headers: { ... },
      });
  },
  ```

  ***

  #### Parameters

  * ##### optionaloverrideOptions: Partial\<OptionsInit>

  #### Returns Promise\<Response\<Response>>

### [**](#waitForSelector)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/puppeteer-crawler/src/internals/utils/puppeteer_utils.ts#L862)inheritedwaitForSelector

* ****waitForSelector**(selector, timeoutMs): Promise\<void>

- Inherited from PuppeteerContextUtils.waitForSelector

  Wait for an element matching the selector to appear. Timeout defaults to 5s.

  **Example usage:**

  ```
  async requestHandler({ waitForSelector, parseWithCheerio }) {
      await waitForSelector('article h1');
      const $ = await parseWithCheerio();
      const title = $('title').text();
  });
  ```

  ***

  #### Parameters

  * ##### selector: string
  * ##### optionaltimeoutMs: number

  #### Returns Promise\<void>
