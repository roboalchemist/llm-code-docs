# Source: https://crawlee.dev/js/api/core/interface/RestrictedCrawlingContext.md

# RestrictedCrawlingContext<!-- --> \<UserData>

### Hierarchy

* Record\<string & {}, unknown>

  * *RestrictedCrawlingContext*

    * [CrawlingContext](https://crawlee.dev/js/api/core/interface/CrawlingContext.md)
    * [AdaptivePlaywrightCrawlerContext](https://crawlee.dev/js/api/playwright-crawler/interface/AdaptivePlaywrightCrawlerContext.md)

## Index[**](#Index)

### Properties

* [**addRequests](#addRequests)
* [**enqueueLinks](#enqueueLinks)
* [**getKeyValueStore](#getKeyValueStore)
* [**id](#id)
* [**log](#log)
* [**proxyInfo](#proxyInfo)
* [**request](#request)
* [**session](#session)
* [**useState](#useState)

### Methods

* [**pushData](#pushData)

## Properties<!-- -->[**](#Properties)

### [**](#addRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L89)addRequests

**addRequests: (requestsLike, options) => Promise\<void>

Add requests directly to the request queue.

***

#### Type declaration

* * **(requestsLike, options): Promise\<void>

  - #### Parameters

    * ##### requestsLike: readonly<!-- --> (string | ReadonlyObjectDeep\<Partial<[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)\<Dictionary>> & { regex?<!-- -->: RegExp; requestsFromUrl?<!-- -->: string }> | ReadonlyObjectDeep<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>)\[]

    * ##### optionaloptions: ReadonlyObjectDeep<[RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)>

      Options for the request queue

    #### Returns Promise\<void>

### [**](#enqueueLinks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L81)enqueueLinks

**enqueueLinks: (options) => Promise\<unknown>

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

### [**](#getKeyValueStore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L102)getKeyValueStore

**getKeyValueStore: (idOrName) => Promise\<Pick<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md), id | name | getValue | getAutoSavedValue | setValue | getPublicUrl>>

Get a key-value store with given name or id, or the default one for the crawler.

***

#### Type declaration

* * **(idOrName): Promise\<Pick<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md), id | name | getValue | getAutoSavedValue | setValue | getPublicUrl>>

  - #### Parameters

    * ##### optionalidOrName: string

    #### Returns Promise\<Pick<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md), id | name | getValue | getAutoSavedValue | setValue | getPublicUrl>>

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L34)id

**id: string

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L109)log

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

A preconfigured logger for the request handler.

### [**](#proxyInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L41)optionalproxyInfo

**proxyInfo?

<!-- -->

: [ProxyInfo](https://crawlee.dev/js/api/core/interface/ProxyInfo.md)

An object with information about currently used proxy by the crawler and configured by the [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md) class.

### [**](#request)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L46)request

**request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<UserData>

The original [Request](https://crawlee.dev/js/api/core/class/Request.md) object.

### [**](#session)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L35)optionalsession

**session?

<!-- -->

: [Session](https://crawlee.dev/js/api/core/class/Session.md)

### [**](#useState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L97)useState

**useState: \<State>(defaultValue) => Promise\<State>

Returns the state - a piece of mutable persistent data shared across all the request handler runs.

***

#### Type declaration

* * **\<State>(defaultValue): Promise\<State>

  - #### Parameters

    * ##### optionaldefaultValue: State

    #### Returns Promise\<State>

## Methods<!-- -->[**](#Methods)

### [**](#pushData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L55)pushData

* ****pushData**(data, datasetIdOrName): Promise\<void>

- This function allows you to push data to a [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) specified by name, or the one currently used by the crawler.

  Shortcut for `crawler.pushData()`.

  ***

  #### Parameters

  * ##### optionaldata: ReadonlyDeep\<Dictionary | Dictionary\[]>

    Data to be pushed to the default dataset.

  * ##### optionaldatasetIdOrName: string

  #### Returns Promise\<void>
