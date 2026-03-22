# Source: https://crawlee.dev/js/api/core/class/RequestHandlerResult.md

# RequestHandlerResult<!-- -->

experimental

A partial implementation of [RestrictedCrawlingContext](https://crawlee.dev/js/api/core/interface/RestrictedCrawlingContext.md) that stores parameters of calls to context methods for later inspection.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**addRequests](#addRequests)
* [**getKeyValueStore](#getKeyValueStore)
* [**pushData](#pushData)
* [**useState](#useState)

### Accessors

* [**calls](#calls)
* [**datasetItems](#datasetItems)
* [**enqueuedUrlLists](#enqueuedUrlLists)
* [**enqueuedUrls](#enqueuedUrls)
* [**keyValueStoreChanges](#keyValueStoreChanges)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L183)constructor

* ****new RequestHandlerResult**(config, crawleeStateKey): [RequestHandlerResult](https://crawlee.dev/js/api/core/class/RequestHandlerResult.md)

- experimental

  #### Parameters

  * ##### config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md)
  * ##### crawleeStateKey: string

  #### Returns [RequestHandlerResult](https://crawlee.dev/js/api/core/class/RequestHandlerResult.md)

## Properties<!-- -->[**](#Properties)

### [**](#addRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L267)addRequests

**addRequests: (requestsLike, options) => Promise\<void> =

<!-- -->

...

#### Type declaration

* * **(requestsLike, options): Promise\<void>

  - #### Parameters

    * ##### requestsLike: readonly<!-- --> (string | ReadonlyObjectDeep\<Partial<[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)\<Dictionary>> & { regex?<!-- -->: RegExp; requestsFromUrl?<!-- -->: string }> | ReadonlyObjectDeep<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>)\[]
    * ##### optionaloptions: ReadonlyObjectDeep<[RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)>

    #### Returns Promise\<void>

### [**](#getKeyValueStore)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L276)getKeyValueStore

**getKeyValueStore: (idOrName) => Promise\<Pick<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md), id | name | getValue | getAutoSavedValue | setValue | getPublicUrl>> =

<!-- -->

...

#### Type declaration

* * **(idOrName): Promise\<Pick<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md), id | name | getValue | getAutoSavedValue | setValue | getPublicUrl>>

  - #### Parameters

    * ##### optionalidOrName: string

    #### Returns Promise\<Pick<[KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md), id | name | getValue | getAutoSavedValue | setValue | getPublicUrl>>

### [**](#pushData)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L263)pushData

**pushData: (data, datasetIdOrName) => Promise\<void> =

<!-- -->

...

#### Type declaration

* * **(data, datasetIdOrName): Promise\<void>

  - This function allows you to push data to a [Dataset](https://crawlee.dev/js/api/core/class/Dataset.md) specified by name, or the one currently used by the crawler.

    Shortcut for `crawler.pushData()`.

    ***

    #### Parameters

    * ##### optionaldata: ReadonlyDeep\<Dictionary | Dictionary\[]>

      Data to be pushed to the default dataset.

    * ##### optionaldatasetIdOrName: string

    #### Returns Promise\<void>

### [**](#useState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L271)useState

**useState: \<State>(defaultValue) => Promise\<State> =

<!-- -->

...

#### Type declaration

* * **\<State>(defaultValue): Promise\<State>

  - #### Parameters

    * ##### optionaldefaultValue: State

    #### Returns Promise\<State>

## Accessors<!-- -->[**](#Accessors)

### [**](#calls)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L191)calls

* **get calls(): ReadonlyObjectDeep<{ addRequests: \[requestsLike: readonly
  <!-- -->
  (string | ReadonlyObjectDeep\<Partial<[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)\<Dictionary>> & { regex?
  <!-- -->
  : RegExp; requestsFromUrl?
  <!-- -->
  : string }> | ReadonlyObjectDeep<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>)\[], options?: ReadonlyObjectDeep<[RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)>]\[]; pushData: \[data: ReadonlyDeep\<Dictionary | Dictionary\[]>, datasetIdOrName?: string]\[] }>

- experimental

  A record of calls to [RestrictedCrawlingContext.pushData](https://crawlee.dev/js/api/core/interface/RestrictedCrawlingContext.md#pushData), [RestrictedCrawlingContext.addRequests](https://crawlee.dev/js/api/core/interface/RestrictedCrawlingContext.md#addRequests), [RestrictedCrawlingContext.enqueueLinks](https://crawlee.dev/js/api/core/interface/RestrictedCrawlingContext.md#enqueueLinks) made by a request handler.

  ***

  #### Returns ReadonlyObjectDeep<{ addRequests: \[requestsLike: readonly<!-- --> (string | ReadonlyObjectDeep\<Partial<[RequestOptions](https://crawlee.dev/js/api/core/interface/RequestOptions.md)\<Dictionary>> & { regex?<!-- -->: RegExp; requestsFromUrl?<!-- -->: string }> | ReadonlyObjectDeep<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>)\[], options?: ReadonlyObjectDeep<[RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)>]\[]; pushData: \[data: ReadonlyDeep\<Dictionary | Dictionary\[]>, datasetIdOrName?: string]\[] }>

### [**](#datasetItems)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L213)datasetItems

* **get datasetItems(): readonly
  <!-- -->
  ReadonlyObjectDeep<{ datasetIdOrName?
  <!-- -->
  : string; item: Dictionary }>\[]

- experimental

  Items added to datasets by a request handler.

  ***

  #### Returns readonly<!-- --> ReadonlyObjectDeep<{ datasetIdOrName?<!-- -->: string; item: Dictionary }>\[]

### [**](#enqueuedUrlLists)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L245)enqueuedUrlLists

* **get enqueuedUrlLists(): readonly
  <!-- -->
  ReadonlyObjectDeep<{ label?
  <!-- -->
  : string; listUrl: string }>\[]

- experimental

  URL lists enqueued to the request queue by a request handler via [RestrictedCrawlingContext.addRequests](https://crawlee.dev/js/api/core/interface/RestrictedCrawlingContext.md#addRequests) using the `requestsFromUrl` option.

  ***

  #### Returns readonly<!-- --> ReadonlyObjectDeep<{ label?<!-- -->: string; listUrl: string }>\[]

### [**](#enqueuedUrls)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L222)enqueuedUrls

* **get enqueuedUrls(): readonly
  <!-- -->
  ReadonlyObjectDeep<{ label?
  <!-- -->
  : string; url: string }>\[]

- experimental

  URLs enqueued to the request queue by a request handler, either via [RestrictedCrawlingContext.addRequests](https://crawlee.dev/js/api/core/interface/RestrictedCrawlingContext.md#addRequests) or [RestrictedCrawlingContext.enqueueLinks](https://crawlee.dev/js/api/core/interface/RestrictedCrawlingContext.md#enqueueLinks)

  ***

  #### Returns readonly<!-- --> ReadonlyObjectDeep<{ label?<!-- -->: string; url: string }>\[]

### [**](#keyValueStoreChanges)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/crawlers/crawler_commons.ts#L204)keyValueStoreChanges

* **get keyValueStoreChanges(): ReadonlyObjectDeep\<Record\<string, Record\<string, { changedValue: unknown; options?
  <!-- -->
  : [RecordOptions](https://crawlee.dev/js/api/core/interface/RecordOptions.md) }>>>

- experimental

  A record of changes made to key-value stores by a request handler.

  ***

  #### Returns ReadonlyObjectDeep\<Record\<string, Record\<string, { changedValue: unknown; options?<!-- -->: [RecordOptions](https://crawlee.dev/js/api/core/interface/RecordOptions.md) }>>>
