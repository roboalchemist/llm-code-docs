# Source: https://crawlee.dev/js/api/playwright-crawler/interface/AdaptivePlaywrightCrawlerContext.md

# AdaptivePlaywrightCrawlerContext<!-- --> \<UserData>

### Hierarchy

* [RestrictedCrawlingContext](https://crawlee.dev/js/api/core/interface/RestrictedCrawlingContext.md)\<UserData>
  * *AdaptivePlaywrightCrawlerContext*

## Index[**](#Index)

### Properties

* [**addRequests](#addRequests)
* [**enqueueLinks](#enqueueLinks)
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

* [**parseWithCheerio](#parseWithCheerio)
* [**pushData](#pushData)
* [**querySelector](#querySelector)
* [**waitForSelector](#waitForSelector)

## Properties<!-- -->[**](#Properties)

### [**](#addRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L89)inheritedaddRequests

**addRequests: (requestsLike, options) => Promise\<void>

Inherited from RestrictedCrawlingContext.addRequests

Add requests directly to the request queue.

***

#### Type declaration

* * **(requestsLike, options): Promise\<void>

  - #### Parameters

    * ##### requestsLike: readonly<!-- --> (string | ReadonlyObjectDeep\<Partial<[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)\<Dictionary>> & { regex?<!-- -->: RegExp; requestsFromUrl?<!-- -->: string }> | ReadonlyObjectDeep<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>)\[]

    * ##### optionaloptions: ReadonlyObjectDeep<[RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)>

      Options for the request queue

    #### Returns Promise\<void>

### [**](#enqueueLinks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L81)inheritedenqueueLinks

**enqueueLinks: (options) => Promise\<unknown>

Inherited from RestrictedCrawlingContext.enqueueLinks

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

#### Type declaration

* * **(options): Promise\<unknown>

  - #### Parameters

    * ##### optionaloptions: ReadonlyObjectDeep\<Omit<[EnqueueLinksOptions](https://crawlee.dev/js/api/core/interface/EnqueueLinksOptions.md), requestQueue>>

      All `enqueueLinks()` parameters are passed via an options object.

    #### Returns Promise\<unknown>

### [**](#getKeyValueStore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L102)inheritedgetKeyValueStore

**getKeyValueStore: (idOrName) => Promise\<Pick<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md), id | name | getValue | getAutoSavedValue | setValue | getPublicUrl>>

Inherited from RestrictedCrawlingContext.getKeyValueStore

Get a key-value store with given name or id, or the default one for the crawler.

***

#### Type declaration

* * **(idOrName): Promise\<Pick<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md), id | name | getValue | getAutoSavedValue | setValue | getPublicUrl>>

  - #### Parameters

    * ##### optionalidOrName: string

    #### Returns Promise\<Pick<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md), id | name | getValue | getAutoSavedValue | setValue | getPublicUrl>>

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L34)inheritedid

**id: string

Inherited from RestrictedCrawlingContext.id

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L109)inheritedlog

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

Inherited from RestrictedCrawlingContext.log

A preconfigured logger for the request handler.

### [**](#page)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L109)page

**page: Page

Playwright Page object. If accessed in HTTP-only rendering, this will throw an error and make the AdaptivePlaywrightCrawlerContext retry the request in a browser.

### [**](#proxyInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L41)optionalinheritedproxyInfo

**proxyInfo?

<!-- -->

: [ProxyInfo](https://crawlee.dev/js/api/core/interface/ProxyInfo.md)

Inherited from RestrictedCrawlingContext.proxyInfo

An object with information about currently used proxy by the crawler and configured by the [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md) class.

### [**](#request)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L46)inheritedrequest

**request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<UserData>

Inherited from RestrictedCrawlingContext.request

The original [Request](https://crawlee.dev/js/api/core/class/Request.md) object.

### [**](#response)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L104)response

**response: [BaseHttpResponseData](https://crawlee.dev/js/api/core/interface/BaseHttpResponseData.md)

The HTTP response, either from the HTTP client or from the initial request from playwright's navigation.

### [**](#session)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L35)optionalinheritedsession

**session?

<!-- -->

: [Session](https://crawlee.dev/js/api/core/class/Session.md)

Inherited from RestrictedCrawlingContext.session

### [**](#useState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L97)inheriteduseState

**useState: \<State>(defaultValue) => Promise\<State>

Inherited from RestrictedCrawlingContext.useState

Returns the state - a piece of mutable persistent data shared across all the request handler runs.

***

#### Type declaration

* * **\<State>(defaultValue): Promise\<State>

  - #### Parameters

    * ##### optionaldefaultValue: State

    #### Returns Promise\<State>

## Methods<!-- -->[**](#Methods)

### [**](#parseWithCheerio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L144)parseWithCheerio

* ****parseWithCheerio**(selector, timeoutMs): Promise<[CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)>

- Returns Cheerio handle for `page.content()`, allowing to work with the data same way as with [CheerioCrawler](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md). When provided with the `selector` argument, it will first look for the selector with a 5s timeout.

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

- Inherited from RestrictedCrawlingContext.pushData

  This function allows you to push data to a [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) specified by name, or the one currently used by the crawler.

  Shortcut for `crawler.pushData()`.

  ***

  #### Parameters

  * ##### optionaldata: ReadonlyDeep\<Dictionary | Dictionary\[]>

    Data to be pushed to the default dataset.

  * ##### optionaldatasetIdOrName: string

  #### Returns Promise\<void>

### [**](#querySelector)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L115)querySelector

* ****querySelector**(selector, timeoutMs): Promise<[Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>>

- Wait for an element matching the selector to appear and return a Cheerio object of matched elements. Timeout defaults to 5s.

  ***

  #### Parameters

  * ##### selector: string
  * ##### optionaltimeoutMs: number

  #### Returns Promise<[Cheerio](https://crawlee.dev/js/api/basic-crawler/class/Cheerio.md)<[Element](https://crawlee.dev/js/api/basic-crawler/class/Element.md)>>

### [**](#waitForSelector)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/playwright-crawler/src/internals/adaptive-playwright-crawler.ts#L130)waitForSelector

* ****waitForSelector**(selector, timeoutMs): Promise\<void>

- Wait for an element matching the selector to appear. Timeout defaults to 5s.

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
