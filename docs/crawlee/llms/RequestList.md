# Source: https://crawlee.dev/js/api/core/class/RequestList.md

# RequestList<!-- -->

Represents a static list of URLs to crawl. The URLs can be provided either in code or parsed from a text file hosted on the web. `RequestList` is used by [BasicCrawler](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md), [CheerioCrawler](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md), [PuppeteerCrawler](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md) and [PlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md) as a source of URLs to crawl.

Each URL is represented using an instance of the [Request](https://crawlee.dev/js/api/core/class/Request.md) class. The list can only contain unique URLs. More precisely, it can only contain `Request` instances with distinct `uniqueKey` properties. By default, `uniqueKey` is generated from the URL, but it can also be overridden. To add a single URL to the list multiple times, corresponding [Request](https://crawlee.dev/js/api/core/class/Request.md) objects will need to have different `uniqueKey` properties. You can use the `keepDuplicateUrls` option to do this for you when initializing the `RequestList` from sources.

`RequestList` doesn't have a public constructor, you need to create it with the asynchronous [RequestList.open](https://crawlee.dev/js/api/core/class/RequestList.md#open) function. After the request list is created, no more URLs can be added to it. Unlike [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md), `RequestList` is static but it can contain even millions of URLs.

> Note that `RequestList` can be used together with `RequestQueue` by the same crawler. In such cases, each request from `RequestList` is enqueued into `RequestQueue` first and then consumed from the latter. This is necessary to avoid the same URL being processed more than once (from the list first and then possibly from the queue). In practical terms, such a combination can be useful when there is a large number of initial URLs, but more URLs would be added dynamically by the crawler.

`RequestList` has an internal state where it stores information about which requests were already handled, which are in progress and which were reclaimed. The state may be automatically persisted to the default [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md) by setting the `persistStateKey` option so that if the Node.js process is restarted, the crawling can continue where it left off. The automated persisting is launched upon receiving the `persistState` event that is periodically emitted by [EventManager](https://crawlee.dev/js/api/core/class/EventManager.md).

The internal state is closely tied to the provided sources (URLs). If the sources change on crawler restart, the state will become corrupted and `RequestList` will raise an exception. This typically happens when the sources is a list of URLs downloaded from the web. In such case, use the `persistRequestsKey` option in conjunction with `persistStateKey`, to make the `RequestList` store the initial sources to the default key-value store and load them after restart, which will prevent any issues that a live list of URLs might cause.

**Basic usage:**

```
const requestList = await RequestList.open('my-request-list', [
    'http://www.example.com/page-1',
    { url: 'http://www.example.com/page-2', method: 'POST', userData: { foo: 'bar' }},
    { requestsFromUrl: 'http://www.example.com/my-url-list.txt', userData: { isFromUrl: true } },
]);
```

**Advanced usage:**

```
const requestList = await RequestList.open(null, [
    // Separate requests
    { url: 'http://www.example.com/page-1', method: 'GET', headers: { ... } },
    { url: 'http://www.example.com/page-2', userData: { foo: 'bar' }},

    // Bulk load of URLs from file `http://www.example.com/my-url-list.txt`
    // Note that all URLs must start with http:// or https://
    { requestsFromUrl: 'http://www.example.com/my-url-list.txt', userData: { isFromUrl: true } },
], {
    // Persist the state to avoid re-crawling which can lead to data duplications.
    // Keep in mind that the sources have to be immutable or this will throw an error.
    persistStateKey: 'my-state',
});
```

### Implements

* [IRequestList](https://crawlee.dev/js/api/core/interface/IRequestList.md)

## Index[**](#Index)

### Methods

* [**\[asyncIterator\]](#\[asyncIterator])
* [**fetchNextRequest](#fetchNextRequest)
* [**getState](#getState)
* [**handledCount](#handledCount)
* [**isEmpty](#isEmpty)
* [**isFinished](#isFinished)
* [**length](#length)
* [**markRequestHandled](#markRequestHandled)
* [**persistState](#persistState)
* [**reclaimRequest](#reclaimRequest)
* [**open](#open)

## Methods<!-- -->[**](#Methods)

### [**](#\[asyncIterator])[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L684)\[asyncIterator]

* ****\[asyncIterator]**(): AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, void, unknown>

- Implementation of IRequestList.\[asyncIterator]

  Can be used to iterate over the `RequestList` instance in a `for await .. of` loop. Provides an alternative for the repeated use of `fetchNextRequest`.

  ***

  #### Returns AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, void, unknown>

### [**](#fetchNextRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L657)fetchNextRequest

* ****fetchNextRequest**(): Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>

- Implementation of IRequestList.fetchNextRequest

  Gets the next [Request](https://crawlee.dev/js/api/core/class/Request.md) to process. First, the function gets a request previously reclaimed using the [RequestList.reclaimRequest](https://crawlee.dev/js/api/core/class/RequestList.md#reclaimRequest) function, if there is any. Otherwise it gets the next request from sources.

  The function's `Promise` resolves to `null` if there are no more requests to process.

  ***

  #### Returns Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>>

### [**](#getState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L626)getState

* ****getState**(): [RequestListState](https://crawlee.dev/js/api/core/interface/RequestListState.md)

- Returns an object representing the internal state of the `RequestList` instance. Note that the object's fields can change in future releases.

  ***

  #### Returns [RequestListState](https://crawlee.dev/js/api/core/interface/RequestListState.md)

### [**](#handledCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L870)handledCount

* ****handledCount**(): number

- Implementation of IRequestList.handledCount

  Returns number of handled requests.

  ***

  #### Returns number

### [**](#isEmpty)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L639)isEmpty

* ****isEmpty**(): Promise\<boolean>

- Implementation of IRequestList.isEmpty

  Resolves to `true` if the next call to [IRequestList.fetchNextRequest](https://crawlee.dev/js/api/core/interface/IRequestList.md#fetchNextRequest) function would return `null`, otherwise it resolves to `false`. Note that even if the list is empty, there might be some pending requests currently being processed.

  ***

  #### Returns Promise\<boolean>

### [**](#isFinished)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L648)isFinished

* ****isFinished**(): Promise\<boolean>

- Implementation of IRequestList.isFinished

  Returns `true` if all requests were already handled and there are no more left.

  ***

  #### Returns Promise\<boolean>

### [**](#length)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L861)length

* ****length**(): number

- Implementation of IRequestList.length

  Returns the total number of unique requests present in the `RequestList`.

  ***

  #### Returns number

### [**](#markRequestHandled)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L704)markRequestHandled

* ****markRequestHandled**(request): Promise\<void>

- Implementation of IRequestList.markRequestHandled

  Marks request as handled after successful processing.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

  #### Returns Promise\<void>

### [**](#persistState)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L504)persistState

* ****persistState**(): Promise\<void>

- Implementation of IRequestList.persistState

  Persists the current state of the `IRequestList` into the default [KeyValueStore](https://crawlee.dev/js/api/core/class/KeyValueStore.md). The state is persisted automatically in regular intervals, but calling this method manually is useful in cases where you want to have the most current state available after you pause or stop fetching its requests. For example after you pause or abort a crawl. Or just before a server migration.

  ***

  #### Returns Promise\<void>

### [**](#reclaimRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L718)reclaimRequest

* ****reclaimRequest**(request): Promise\<void>

- Implementation of IRequestList.reclaimRequest

  Reclaims request to the list if its processing failed. The request will become available in the next `this.fetchNextRequest()`.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

  #### Returns Promise\<void>

### [**](#open)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_list.ts#L929)staticopen

* ****open**(listNameOrOptions, sources, options): Promise<[RequestList](https://crawlee.dev/js/api/core/class/RequestList.md)>

- Opens a request list and returns a promise resolving to an instance of the [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) class that is already initialized.

  [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) represents a list of URLs to crawl, which is always stored in memory. To enable picking up where left off after a process restart, the request list sources are persisted to the key-value store at initialization of the list. Then, while crawling, a small state object is regularly persisted to keep track of the crawling status.

  For more details and code examples, see the [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) class.

  **Example usage:**

  ```
  const sources = [
      'https://www.example.com',
      'https://www.google.com',
      'https://www.bing.com'
  ];

  const requestList = await RequestList.open('my-name', sources);
  ```

  ***

  #### Parameters

  * ##### listNameOrOptions: null | string | [RequestListOptions](https://crawlee.dev/js/api/core/interface/RequestListOptions.md)

    Name of the request list to be opened, or the options object. Setting a name enables the `RequestList`'s state to be persisted in the key-value store. This is useful in case of a restart or migration. Since `RequestList` is only stored in memory, a restart or migration wipes it clean. Setting a name will enable the `RequestList`'s state to survive those situations and continue where it left off.

    The name will be used as a prefix in key-value store, producing keys such as `NAME-REQUEST_LIST_STATE` and `NAME-REQUEST_LIST_SOURCES`.

    If `null`, the list will not be persisted and will only be stored in memory. Process restart will then cause the list to be crawled again from the beginning. We suggest always using a name.

  * ##### optionalsources: RequestListSource\[]

    An array of sources of URLs for the [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md). It can be either an array of strings, plain objects that define at least the `url` property, or an array of [Request](https://crawlee.dev/js/api/core/class/Request.md) instances.

    **IMPORTANT:** The `sources` array will be consumed (left empty) after [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) initializes. This is a measure to prevent memory leaks in situations when millions of sources are added.

    Additionally, the `requestsFromUrl` property may be used instead of `url`, which will instruct [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) to download the source URLs from a given remote location. The URLs will be parsed from the received response. In this case you can limit the URLs using `regex` parameter containing regular expression pattern for URLs to be included.

    For details, see the [RequestListOptions.sources](https://crawlee.dev/js/api/core/interface/RequestListOptions.md#sources)

  * ##### optionaloptions: [RequestListOptions](https://crawlee.dev/js/api/core/interface/RequestListOptions.md) = <!-- -->{}

    The [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md) options. Note that the `listName` parameter supersedes the [RequestListOptions.persistStateKey](https://crawlee.dev/js/api/core/interface/RequestListOptions.md#persistStateKey) and [RequestListOptions.persistRequestsKey](https://crawlee.dev/js/api/core/interface/RequestListOptions.md#persistRequestsKey) options and the `sources` parameter supersedes the [RequestListOptions.sources](https://crawlee.dev/js/api/core/interface/RequestListOptions.md#sources) option.

  #### Returns Promise<[RequestList](https://crawlee.dev/js/api/core/class/RequestList.md)>
