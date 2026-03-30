# Source: https://crawlee.dev/js/api/core/interface/CrawlingContext.md

# CrawlingContext<!-- --> \<Crawler, UserData>

### Hierarchy

* [RestrictedCrawlingContext](https://crawlee.dev/js/api/core/interface/RestrictedCrawlingContext.md)\<UserData>

  * *CrawlingContext*

    * [BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md)
    * [BrowserCrawlingContext](https://crawlee.dev/js/api/browser-crawler/interface/BrowserCrawlingContext.md)

## Index[**](#Index)

### Properties

* [**addRequests](#addRequests)
* [**crawler](#crawler)
* [**getKeyValueStore](#getKeyValueStore)
* [**id](#id)
* [**log](#log)
* [**proxyInfo](#proxyInfo)
* [**request](#request)
* [**session](#session)
* [**useState](#useState)

### Methods

* [**enqueueLinks](#enqueueLinks)
* [**pushData](#pushData)
* [**sendRequest](#sendRequest)

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

### [**](#crawler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L114)crawler

**crawler: Crawler

### [**](#getKeyValueStore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L148)getKeyValueStore

**getKeyValueStore: (idOrName) => Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

Overrides RestrictedCrawlingContext.getKeyValueStore

Get a key-value store with given name or id, or the default one for the crawler.

***

#### Type declaration

* * **(idOrName): Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

  - #### Parameters

    * ##### optionalidOrName: string

    #### Returns Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L34)inheritedid

**id: string

Inherited from RestrictedCrawlingContext.id

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L109)inheritedlog

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

Inherited from RestrictedCrawlingContext.log

A preconfigured logger for the request handler.

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

### [**](#enqueueLinks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L141)enqueueLinks

* ****enqueueLinks**(options): Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

- Overrides RestrictedCrawlingContext.enqueueLinks

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

- Inherited from RestrictedCrawlingContext.pushData

  This function allows you to push data to a [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) specified by name, or the one currently used by the crawler.

  Shortcut for `crawler.pushData()`.

  ***

  #### Parameters

  * ##### optionaldata: ReadonlyDeep\<Dictionary | Dictionary\[]>

    Data to be pushed to the default dataset.

  * ##### optionaldatasetIdOrName: string

  #### Returns Promise\<void>

### [**](#sendRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L167)sendRequest

* ****sendRequest**\<Response>(overrideOptions): Promise\<Response\<Response>>

- Fires HTTP request via [`got-scraping`](https://crawlee.dev/js/docs/guides/got-scraping.md), allowing to override the request options on the fly.

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
