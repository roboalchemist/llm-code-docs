# Source: https://crawlee.dev/js/api/stagehand-crawler/interface/StagehandCrawlingContext.md

# StagehandCrawlingContext<!-- --> \<UserData>

Crawling context for StagehandCrawler with enhanced page object.

### Hierarchy

* [BrowserCrawlingContext](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlingContext.md)<[StagehandCrawler](https://crawlee.dev/js/api/stagehand-crawler/class/StagehandCrawler.md), [StagehandPage](https://crawlee.dev/js/api/stagehand-crawler/interface/StagehandPage.md), Response, StagehandController, UserData>
  * *StagehandCrawlingContext*

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
* [**stagehand](#stagehand)
* [**useState](#useState)

### Methods

* [**enqueueLinks](#enqueueLinks)
* [**pushData](#pushData)
* [**sendRequest](#sendRequest)

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

**browserController: StagehandController

Inherited from BrowserCrawlingContext.browserController

### [**](#crawler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L114)inheritedcrawler

**crawler: [StagehandCrawler](https://crawlee.dev/js/api/stagehand-crawler/class/StagehandCrawler.md)

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

### [**](#page)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L213)page

**page: [StagehandPage](https://crawlee.dev/js/api/stagehand-crawler/interface/StagehandPage.md)

Overrides BrowserCrawlingContext.page

Enhanced Playwright page with Stagehand AI methods. Use page.act(), page.extract(), page.observe(), page.agent() for AI-powered operations.

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

: Response

Inherited from BrowserCrawlingContext.response

### [**](#session)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L35)optionalinheritedsession

**session?

<!-- -->

: [Session](https://crawlee.dev/js/api/core/class/Session.md)

Inherited from BrowserCrawlingContext.session

### [**](#stagehand)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/stagehand-crawler/src/internals/stagehand-crawler.ts#L219)stagehand

**stagehand: [V3](https://crawlee.dev/js/api/stagehand-crawler/class/Stagehand.md)

Stagehand instance for advanced control. Usually you don't need to access this directly - use the enhanced page methods instead.

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
