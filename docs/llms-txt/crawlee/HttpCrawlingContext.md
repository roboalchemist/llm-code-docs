# Source: https://crawlee.dev/js/api/http-crawler/interface/HttpCrawlingContext.md

# HttpCrawlingContext<!-- --> \<UserData, JSONData>

### Hierarchy

* InternalHttpCrawlingContext\<UserData, JSONData, [HttpCrawler](https://crawlee.dev/js/api/http-crawler/class/HttpCrawler.md)<[HttpCrawlingContext](https://crawlee.dev/js/api/http-crawler/interface/HttpCrawlingContext.md)\<UserData, JSONData>>>
  * *HttpCrawlingContext*

## Index[**](#Index)

### Properties

* [**addRequests](#addRequests)
* [**body](#body)
* [**contentType](#contentType)
* [**crawler](#crawler)
* [**getKeyValueStore](#getKeyValueStore)
* [**id](#id)
* [**json](#json)
* [**log](#log)
* [**proxyInfo](#proxyInfo)
* [**request](#request)
* [**response](#response)
* [**session](#session)
* [**useState](#useState)

### Methods

* [**enqueueLinks](#enqueueLinks)
* [**parseWithCheerio](#parseWithCheerio)
* [**pushData](#pushData)
* [**sendRequest](#sendRequest)
* [**waitForSelector](#waitForSelector)

## Properties<!-- -->[**](#Properties)

### [**](#addRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L89)inheritedaddRequests

**addRequests: (requestsLike, options) => Promise\<void>

Inherited from InternalHttpCrawlingContext.addRequests

Add requests directly to the request queue.

***

#### Type declaration

* * **(requestsLike, options): Promise\<void>

  - #### Parameters

    * ##### requestsLike: readonly<!-- --> (string | ReadonlyObjectDeep\<Partial<[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)\<Dictionary>> & { regex?<!-- -->: RegExp; requestsFromUrl?<!-- -->: string }> | ReadonlyObjectDeep<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>)\[]

    * ##### optionaloptions: ReadonlyObjectDeep<[RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)>

      Options for the request queue

    #### Returns Promise\<void>

### [**](#body)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L214)inheritedbody

**body: string | Buffer\<ArrayBufferLike>

Inherited from InternalHttpCrawlingContext.body

The request body of the web page. The type depends on the `Content-Type` header of the web page:

* String for `text/html`, `application/xhtml+xml`, `application/xml` MIME content types
* Buffer for others MIME content types

### [**](#contentType)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L224)inheritedcontentType

**contentType: { encoding: BufferEncoding; type: string }

Inherited from InternalHttpCrawlingContext.contentType

Parsed `Content-Type header: { type, encoding }`.

***

#### Type declaration

* ##### encoding: BufferEncoding
* ##### type: string

### [**](#crawler)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L114)inheritedcrawler

**crawler: [HttpCrawler](https://crawlee.dev/js/api/http-crawler/class/HttpCrawler.md)<[HttpCrawlingContext](https://crawlee.dev/js/api/http-crawler/interface/HttpCrawlingContext.md)\<UserData, JSONData>>

Inherited from InternalHttpCrawlingContext.crawler

### [**](#getKeyValueStore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L148)inheritedgetKeyValueStore

**getKeyValueStore: (idOrName) => Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

Inherited from InternalHttpCrawlingContext.getKeyValueStore

Get a key-value store with given name or id, or the default one for the crawler.

***

#### Type declaration

* * **(idOrName): Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

  - #### Parameters

    * ##### optionalidOrName: string

    #### Returns Promise<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md)>

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L34)inheritedid

**id: string

Inherited from InternalHttpCrawlingContext.id

### [**](#json)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L219)inheritedjson

**json: JSONData

Inherited from InternalHttpCrawlingContext.json

The parsed object from JSON string if the response contains the content type application/json.

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L109)inheritedlog

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

Inherited from InternalHttpCrawlingContext.log

A preconfigured logger for the request handler.

### [**](#proxyInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L41)optionalinheritedproxyInfo

**proxyInfo?

<!-- -->

: [ProxyInfo](https://crawlee.dev/js/api/core/interface/ProxyInfo.md)

Inherited from InternalHttpCrawlingContext.proxyInfo

An object with information about currently used proxy by the crawler and configured by the [ProxyConfiguration](https://crawlee.dev/js/api/core/class/ProxyConfiguration.md) class.

### [**](#request)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L46)inheritedrequest

**request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<UserData>

Inherited from InternalHttpCrawlingContext.request

The original [Request](https://crawlee.dev/js/api/core/class/Request.md) object.

### [**](#response)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L225)inheritedresponse

**response: PlainResponse

Inherited from InternalHttpCrawlingContext.response

### [**](#session)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L35)optionalinheritedsession

**session?

<!-- -->

: [Session](https://crawlee.dev/js/api/core/class/Session.md)

Inherited from InternalHttpCrawlingContext.session

### [**](#useState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L97)inheriteduseState

**useState: \<State>(defaultValue) => Promise\<State>

Inherited from InternalHttpCrawlingContext.useState

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

- Inherited from InternalHttpCrawlingContext.enqueueLinks

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

### [**](#parseWithCheerio)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L253)inheritedparseWithCheerio

* ****parseWithCheerio**(selector, timeoutMs): Promise<[CheerioAPI](https://crawlee.dev/js/api/basic-crawler/interface/CheerioAPI.md)>

- Inherited from InternalHttpCrawlingContext.parseWithCheerio

  Returns Cheerio handle for `page.content()`, allowing to work with the data same way as with [CheerioCrawler](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md). When provided with the `selector` argument, it will throw if it's not available.

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

- Inherited from InternalHttpCrawlingContext.pushData

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

- Inherited from InternalHttpCrawlingContext.sendRequest

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

### [**](#waitForSelector)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/http-crawler/src/internals/http-crawler.ts#L239)inheritedwaitForSelector

* ****waitForSelector**(selector, timeoutMs): Promise\<void>

- Inherited from InternalHttpCrawlingContext.waitForSelector

  Wait for an element matching the selector to appear. Timeout is ignored.

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
