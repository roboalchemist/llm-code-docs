# Source: https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md

# BasicCrawlingContext<!-- --> \<UserData>

### Hierarchy

* [CrawlingContext](https://crawlee.dev/js/api/core/interface/CrawlingContext.md)<[BasicCrawler](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md), UserData>
  * *BasicCrawlingContext*

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

Inherited from CrawlingContext.addRequests

Add requests directly to the request queue.

***

#### Type declaration

* * **(requestsLike, options): Promise\<void>

  - #### Parameters

    * ##### requestsLike: readonly<!-- --> (string | ReadonlyObjectDeep\<Partial<[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)\<Dictionary>> & { regex?<!-- -->: RegExp; requestsFromUrl?<!-- -->: string }> | ReadonlyObjectDeep<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>)\[]

    * ##### optionaloptions: ReadonlyObjectDeep<[RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)>

      Options for the request queue

    #### Returns Promise\<void>

### [**](#crawler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L114)inheritedcrawler

**crawler: [BasicCrawler](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md)<[BasicCrawlingContext](https://crawlee.dev/js/api/basic-crawler/interface/BasicCrawlingContext.md)\<Dictionary>>

Inherited from CrawlingContext.crawler

### [**](#getKeyValueStore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L148)inheritedgetKeyValueStore

**getKeyValueStore: (idOrName) => Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

Inherited from CrawlingContext.getKeyValueStore

Get a key-value store with given name or id, or the default one for the crawler.

***

#### Type declaration

* * **(idOrName): Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

  - #### Parameters

    * ##### optionalidOrName: string

    #### Returns Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L34)inheritedid

**id: string

Inherited from CrawlingContext.id

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L109)inheritedlog

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

Inherited from CrawlingContext.log

A preconfigured logger for the request handler.

### [**](#proxyInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L41)optionalinheritedproxyInfo

**proxyInfo?

<!-- -->

: [ProxyInfo](https://crawlee.dev/js/api/core/interface/ProxyInfo.md)

Inherited from CrawlingContext.proxyInfo

An object with information about currently used proxy by the crawler and configured by the [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md) class.

### [**](#request)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L46)inheritedrequest

**request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<UserData>

Inherited from CrawlingContext.request

The original [Request](https://crawlee.dev/js/api/core/class/Request.md) object.

### [**](#session)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L35)optionalinheritedsession

**session?

<!-- -->

: [Session](https://crawlee.dev/js/api/core/class/Session.md)

Inherited from CrawlingContext.session

### [**](#useState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L97)inheriteduseState

**useState: \<State>(defaultValue) => Promise\<State>

Inherited from CrawlingContext.useState

Returns the state - a piece of mutable persistent data shared across all the request handler runs.

***

#### Type declaration

* * **\<State>(defaultValue): Promise\<State>

  - #### Parameters

    * ##### optionaldefaultValue: State

    #### Returns Promise\<State>

## Methods<!-- -->[**](#Methods)

### [**](#enqueueLinks)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L98)enqueueLinks

* ****enqueueLinks**(options): Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

- Overrides CrawlingContext.enqueueLinks

  This function automatically finds and enqueues links from the current page, adding them to the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) currently used by the crawler.

  Optionally, the function allows you to filter the target links' URLs using an array of globs or regular expressions and override settings of the enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

  Check out the [Crawl a website with relative links](https://crawlee.dev/js/docs/examples/crawl-relative-links.md) example for more details regarding its usage.

  **Example usage**

  ```
  async requestHandler({ enqueueLinks }) {
      await enqueueLinks({
        urls: [...],
      });
  },
  ```

  ***

  #### Parameters

  * ##### optionaloptions: { baseUrl?<!-- -->: string; exclude?<!-- -->: readonly<!-- --> ([GlobInput](https://crawlee.dev/js/api/core.md#GlobInput) | [RegExpInput](https://crawlee.dev/js/api/core.md#RegExpInput))\[]; forefront?<!-- -->: boolean; globs?<!-- -->: readonly<!-- --> [GlobInput](https://crawlee.dev/js/api/core.md#GlobInput)\[]; label?<!-- -->: string; limit?<!-- -->: number; onSkippedRequest?<!-- -->: [SkippedRequestCallback](https://crawlee.dev/js/api/core.md#SkippedRequestCallback); pseudoUrls?<!-- -->: readonly<!-- --> [PseudoUrlInput](https://crawlee.dev/js/api/core.md#PseudoUrlInput)\[]; regexps?<!-- -->: readonly<!-- --> [RegExpInput](https://crawlee.dev/js/api/core.md#RegExpInput)\[]; requestQueue?<!-- -->: [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md); robotsTxtFile?<!-- -->: Pick<[RobotsTxtFile](https://crawlee.dev/js/api/utils/class/RobotsTxtFile.md), isAllowed>; selector?<!-- -->: string; skipNavigation?<!-- -->: boolean; strategy?<!-- -->: [EnqueueStrategy](https://crawlee.dev/js/api/core/enum/EnqueueStrategy.md) | all | same-domain | same-hostname | same-origin; transformRequestFunction?<!-- -->: [RequestTransform](https://crawlee.dev/js/api/core/interface/RequestTransform.md); urls: readonly<!-- --> string\[]; userData?<!-- -->: Dictionary; waitForAllRequestsToBeAdded?<!-- -->: boolean }

    All `enqueueLinks()` parameters are passed via an options object.

    * ##### optionalbaseUrl: string

      A base URL that will be used to resolve relative URLs when using Cheerio. Ignored when using Puppeteer, since the relative URL resolution is done inside the browser automatically.

    * ##### optionalexclude: readonly<!-- --> ([GlobInput](https://crawlee.dev/js/api/core.md#GlobInput) | [RegExpInput](https://crawlee.dev/js/api/core.md#RegExpInput))\[]

      An array of glob pattern strings, regexp patterns or plain objects containing patterns matching URLs that will **never** be enqueued.

      The plain objects must include either the `glob` property or the `regexp` property.

      Glob matching is always case-insensitive. If you need case-sensitive matching, provide a regexp.

    * ##### optionalforefront: boolean = false

      If set to `true`:

      * while adding the request to the queue: the request will be added to the foremost position in the queue.
      * while reclaiming the request: the request will be placed to the beginning of the queue, so that it's returned in the next call to [RequestQueue.fetchNextRequest](https://crawlee.dev/js/api/core/class/RequestQueue.md#fetchNextRequest). By default, it's put to the end of the queue.

      In case the request is already present in the queue, this option has no effect.

      If more requests are added with this option at once, their order in the following `fetchNextRequest` call is arbitrary.

    * ##### optionalglobs: readonly<!-- --> [GlobInput](https://crawlee.dev/js/api/core.md#GlobInput)\[]

      An array of glob pattern strings or plain objects containing glob pattern strings matching the URLs to be enqueued.

      The plain objects must include at least the `glob` property, which holds the glob pattern string. All remaining keys will be used as request options for the corresponding enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

      The matching is always case-insensitive. If you need case-sensitive matching, use `regexps` property directly.

      If `globs` is an empty array or `undefined`, and `regexps` are also not defined, then the function enqueues the links with the same subdomain.

    * ##### optionallabel: string

      Sets [Request.label](https://crawlee.dev/js/api/core/class/Request.md#label) for newly enqueued requests.

      Note that the request options specified in `globs`, `regexps`, or `pseudoUrls` objects have priority over this option.

    * ##### optionallimit: number

      Limit the amount of actually enqueued URLs to this number. Useful for testing across the entire crawling scope.

    * ##### optionalonSkippedRequest: [SkippedRequestCallback](https://crawlee.dev/js/api/core.md#SkippedRequestCallback)

      When a request is skipped for some reason, you can use this callback to act on it. This is currently fired for requests skipped

      1. based on robots.txt file,
      2. because they don't match enqueueLinks filters,
      3. or because the maxRequestsPerCrawl limit has been reached

    * ##### optionalpseudoUrls: readonly<!-- --> [PseudoUrlInput](https://crawlee.dev/js/api/core.md#PseudoUrlInput)\[]

      *NOTE:* In future versions of SDK the options will be removed. Please use `globs` or `regexps` instead.

      An array of [PseudoUrl](https://crawlee.dev/js/api/core/class/PseudoUrl.md) strings or plain objects containing [PseudoUrl](https://crawlee.dev/js/api/core/class/PseudoUrl.md) strings matching the URLs to be enqueued.

      The plain objects must include at least the `purl` property, which holds the pseudo-URL string. All remaining keys will be used as request options for the corresponding enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

      With a pseudo-URL string, the matching is always case-insensitive. If you need case-sensitive matching, use `regexps` property directly.

      If `pseudoUrls` is an empty array or `undefined`, then the function enqueues the links with the same subdomain.

      * **@deprecated**

        prefer using `globs` or `regexps` instead

    * ##### optionalregexps: readonly<!-- --> [RegExpInput](https://crawlee.dev/js/api/core.md#RegExpInput)\[]

      An array of regular expressions or plain objects containing regular expressions matching the URLs to be enqueued.

      The plain objects must include at least the `regexp` property, which holds the regular expression. All remaining keys will be used as request options for the corresponding enqueued [Request](https://crawlee.dev/js/api/core/class/Request.md) objects.

      If `regexps` is an empty array or `undefined`, and `globs` are also not defined, then the function enqueues the links with the same subdomain.

    * ##### optionalrequestQueue: [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)

      A request queue to which the URLs will be enqueued.

    * ##### optionalrobotsTxtFile: Pick<[RobotsTxtFile](https://crawlee.dev/js/api/utils/class/RobotsTxtFile.md), isAllowed>

      RobotsTxtFile instance for the current request that triggered the `enqueueLinks`. If provided, disallowed URLs will be ignored.

    * ##### optionalselector: string

      A CSS selector matching links to be enqueued.

    * ##### optionalskipNavigation: boolean = false

      If set to `true`, tells the crawler to skip navigation and process the request directly.

    * ##### optionalstrategy: [EnqueueStrategy](https://crawlee.dev/js/api/core/enum/EnqueueStrategy.md) | all | same-domain | same-hostname | same-origin = [EnqueueStrategy](https://crawlee.dev/js/api/core/enum/EnqueueStrategy.md) | all | same-domain | same-hostname | same-origin

      The strategy to use when enqueueing the urls.

      Depending on the strategy you select, we will only check certain parts of the URLs found. Here is a diagram of each URL part and their name:

      ```
      Protocol          Domain
      ┌────┐          ┌─────────┐
      https://example.crawlee.dev/...
      │       └─────────────────┤
      │             Hostname    │
      │                         │
      └─────────────────────────┘
               Origin
      ```

    * ##### optionaltransformRequestFunction: [RequestTransform](https://crawlee.dev/js/api/core/interface/RequestTransform.md)

      Just before a new [Request](https://crawlee.dev/js/api/core/class/Request.md) is constructed and enqueued to the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md), this function can be used to remove it or modify its contents such as `userData`, `payload` or, most importantly `uniqueKey`. This is useful when you need to enqueue multiple `Requests` to the queue that share the same URL, but differ in methods or payloads, or to dynamically update or create `userData`.

      For example: by adding `keepUrlFragment: true` to the `request` object, URL fragments will not be removed when `uniqueKey` is computed.

      **Example:**

      ```
      {
          transformRequestFunction: (request) => {
              request.userData.foo = 'bar';
              request.keepUrlFragment = true;
              return request;
          }
      }
      ```

      Note that the request options specified in `globs`, `regexps`, or `pseudoUrls` objects have priority over this function. Some request options returned by `transformRequestFunction` may be overwritten by pattern-based options from `globs`, `regexps`, or `pseudoUrls`.

    * ##### urls: readonly<!-- --> string\[]

      An array of URLs to enqueue.

    * ##### optionaluserData: Dictionary

      Sets [Request.userData](https://crawlee.dev/js/api/core/class/Request.md#userData) for newly enqueued requests.

    * ##### optionalwaitForAllRequestsToBeAdded: boolean

      By default, only the first batch (1000) of found requests will be added to the queue before resolving the call. You can use this option to wait for adding all of them.

  #### Returns Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

  Promise that resolves to [BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md) object.

### [**](#pushData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L55)inheritedpushData

* ****pushData**(data, datasetIdOrName): Promise\<void>

- Inherited from CrawlingContext.pushData

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

- Inherited from CrawlingContext.sendRequest

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
