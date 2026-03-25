# Source: https://crawlee.dev/js/api/core/class/RequestQueueV1.md

# RequestQueueV1<!-- -->

Represents a queue of URLs to crawl, which is used for deep crawling of websites where you start with several URLs and then recursively follow links to other pages. The data structure supports both breadth-first and depth-first crawling orders.

Each URL is represented using an instance of the [Request](https://crawlee.dev/js/api/core/class/Request.md) class. The queue can only contain unique URLs. More precisely, it can only contain [Request](https://crawlee.dev/js/api/core/class/Request.md) instances with distinct `uniqueKey` properties. By default, `uniqueKey` is generated from the URL, but it can also be overridden. To add a single URL multiple times to the queue, corresponding [Request](https://crawlee.dev/js/api/core/class/Request.md) objects will need to have different `uniqueKey` properties.

Do not instantiate this class directly, use the [RequestQueue.open](https://crawlee.dev/js/api/core/class/RequestQueue.md#open) function instead.

`RequestQueue` is used by [BasicCrawler](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md), [CheerioCrawler](https://crawlee.dev/js/api/cheerio-crawler/class/CheerioCrawler.md), [PuppeteerCrawler](https://crawlee.dev/js/api/puppeteer-crawler/class/PuppeteerCrawler.md) and [PlaywrightCrawler](https://crawlee.dev/js/api/playwright-crawler/class/PlaywrightCrawler.md) as a source of URLs to crawl. Unlike [RequestList](https://crawlee.dev/js/api/core/class/RequestList.md), `RequestQueue` supports dynamic adding and removing of requests. On the other hand, the queue is not optimized for operations that add or remove a large number of URLs in a batch.

`RequestQueue` stores its data either on local disk or in the Apify Cloud, depending on whether the `APIFY_LOCAL_STORAGE_DIR` or `APIFY_TOKEN` environment variable is set.

If the `APIFY_LOCAL_STORAGE_DIR` environment variable is set, the queue data is stored in that directory in an SQLite database file.

If the `APIFY_TOKEN` environment variable is set but `APIFY_LOCAL_STORAGE_DIR` is not, the data is stored in the [Apify Request Queue](https://docs.apify.com/storage/request-queue) cloud storage. Note that you can force usage of the cloud storage also by passing the `forceCloud` option to [RequestQueue.open](https://crawlee.dev/js/api/core/class/RequestQueue.md#open) function, even if the `APIFY_LOCAL_STORAGE_DIR` variable is set.

**Example usage:**

```
// Open the default request queue associated with the crawler run
const queue = await RequestQueue.open();

// Open a named request queue
const queueWithName = await RequestQueue.open('some-name');

// Enqueue few requests
await queue.addRequest({ url: 'http://example.com/aaa' });
await queue.addRequest({ url: 'http://example.com/bbb' });
await queue.addRequest({ url: 'http://example.com/foo/bar' }, { forefront: true });
```

### Hierarchy

* [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)
  * *RequestQueueV1*

## Index[**](#Index)

### Properties

* [**assumedHandledCount](#assumedHandledCount)
* [**assumedTotalCount](#assumedTotalCount)
* [**client](#client)
* [**clientKey](#clientKey)
* [**config](#config)
* [**id](#id)
* [**internalTimeoutMillis](#internalTimeoutMillis)
* [**log](#log)
* [**name](#name)
* [**requestLockSecs](#requestLockSecs)
* [**timeoutSecs](#timeoutSecs)

### Methods

* [**\[asyncIterator\]](#\[asyncIterator])
* [**addRequest](#addRequest)
* [**addRequests](#addRequests)
* [**addRequestsBatched](#addRequestsBatched)
* [**drop](#drop)
* [**fetchNextRequest](#fetchNextRequest)
* [**getInfo](#getInfo)
* [**getPendingCount](#getPendingCount)
* [**getRequest](#getRequest)
* [**getTotalCount](#getTotalCount)
* [**handledCount](#handledCount)
* [**isEmpty](#isEmpty)
* [**isFinished](#isFinished)
* [**markRequestHandled](#markRequestHandled)
* [**reclaimRequest](#reclaimRequest)
* [**open](#open)

## Properties<!-- -->[**](#Properties)

### [**](#assumedHandledCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L117)inheritedassumedHandledCount

**assumedHandledCount: number =

<!-- -->

0

Inherited from RequestProvider.assumedHandledCount

### [**](#assumedTotalCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L116)inheritedassumedTotalCount

**assumedTotalCount: number =

<!-- -->

0

Inherited from RequestProvider.assumedTotalCount

### [**](#client)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L107)inheritedclient

**client: [RequestQueueClient](https://crawlee.dev/js/api/types/interface/RequestQueueClient.md)

Inherited from RequestProvider.client

### [**](#clientKey)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L106)inheritedclientKey

**clientKey: string =

<!-- -->

...

Inherited from RequestProvider.clientKey

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L137)readonlyinheritedconfig

**config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) =

<!-- -->

...

Inherited from RequestProvider.config

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L103)inheritedid

**id: string

Inherited from RequestProvider.id

### [**](#internalTimeoutMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L111)inheritedinternalTimeoutMillis

**internalTimeoutMillis: number =

<!-- -->

...

Inherited from RequestProvider.internalTimeoutMillis

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L110)inheritedlog

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

Inherited from RequestProvider.log

### [**](#name)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L104)optionalinheritedname

**name?

<!-- -->

: string

Inherited from RequestProvider.name

### [**](#requestLockSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L112)inheritedrequestLockSecs

**requestLockSecs: number =

<!-- -->

...

Inherited from RequestProvider.requestLockSecs

### [**](#timeoutSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L105)inheritedtimeoutSecs

**timeoutSecs: number =

<!-- -->

30

Inherited from RequestProvider.timeoutSecs

## Methods<!-- -->[**](#Methods)

### [**](#\[asyncIterator])[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L728)inherited\[asyncIterator]

* ****\[asyncIterator]**(): AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, void, unknown>

- Inherited from RequestProvider.\[asyncIterator]

  Can be used to iterate over the `RequestManager` instance in a `for await .. of` loop. Provides an alternative for the repeated use of `fetchNextRequest`.

  ***

  #### Returns AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, void, unknown>

### [**](#addRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L191)inheritedaddRequest

* ****addRequest**(requestLike, options): Promise\<RequestQueueOperationInfo>

- Inherited from RequestProvider.addRequest

  Adds a request to the queue.

  If a request with the same `uniqueKey` property is already present in the queue, it will not be updated. You can find out whether this happened from the resulting [QueueOperationInfo](https://crawlee.dev/js/api/core/interface/QueueOperationInfo.md) object.

  To add multiple requests to the queue by extracting links from a webpage, see the enqueueLinks helper function.

  ***

  #### Parameters

  * ##### requestLike: [Source](https://crawlee.dev/js/api/core.md#Source)

    [Request](https://crawlee.dev/js/api/core/class/Request.md) object or vanilla object with request data. Note that the function sets the `uniqueKey` and `id` fields to the passed Request.

  * ##### optionaloptions: [RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md) = <!-- -->{}

    Request queue operation options.

  #### Returns Promise\<RequestQueueOperationInfo>

### [**](#addRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L275)inheritedaddRequests

* ****addRequests**(requestsLike, options): Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

- Inherited from RequestProvider.addRequests

  Adds requests to the queue in batches of 25. This method will wait till all the requests are added to the queue before resolving. You should prefer using `queue.addRequestsBatched()` or `crawler.addRequests()` if you don't want to block the processing, as those methods will only wait for the initial 1000 requests, start processing right after that happens, and continue adding more in the background.

  If a request passed in is already present due to its `uniqueKey` property being the same, it will not be updated. You can find out whether this happened by finding the request in the resulting [BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md) object.

  ***

  #### Parameters

  * ##### requestsLike: [RequestsLike](https://crawlee.dev/js/api/core.md#RequestsLike)

    [Request](https://crawlee.dev/js/api/core/class/Request.md) objects or vanilla objects with request data. Note that the function sets the `uniqueKey` and `id` fields to the passed requests if missing.

  * ##### optionaloptions: [RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md) = <!-- -->{}

    Request queue operation options.

  #### Returns Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

### [**](#addRequestsBatched)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L395)inheritedaddRequestsBatched

* ****addRequestsBatched**(requests, options): Promise<[AddRequestsBatchedResult](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedResult.md)>

- Inherited from RequestProvider.addRequestsBatched

  Adds requests to the queue in batches. By default, it will resolve after the initial batch is added, and continue adding the rest in the background. You can configure the batch size via `batchSize` option and the sleep time in between the batches via `waitBetweenBatchesMillis`. If you want to wait for all batches to be added to the queue, you can use the `waitForAllRequestsToBeAdded` promise you get in the response object.

  ***

  #### Parameters

  * ##### requests: [RequestsLike](https://crawlee.dev/js/api/core.md#RequestsLike)

    The requests to add

  * ##### options: [AddRequestsBatchedOptions](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedOptions.md) = <!-- -->{}

    Options for the request queue

  #### Returns Promise<[AddRequestsBatchedResult](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedResult.md)>

### [**](#drop)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L717)inheriteddrop

* ****drop**(): Promise\<void>

- Inherited from RequestProvider.drop

  Removes the queue either from the Apify Cloud storage or from the local database, depending on the mode of operation.

  ***

  #### Returns Promise\<void>

### [**](#fetchNextRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_queue.ts#L126)fetchNextRequest

* ****fetchNextRequest**\<T>(): Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<T>>

- Overrides RequestProvider.fetchNextRequest

  Returns a next request in the queue to be processed, or `null` if there are no more pending requests.

  Once you successfully finish processing of the request, you need to call [RequestQueue.markRequestHandled](https://crawlee.dev/js/api/core/class/RequestQueue.md#markRequestHandled) to mark the request as handled in the queue. If there was some error in processing the request, call [RequestQueue.reclaimRequest](https://crawlee.dev/js/api/core/class/RequestQueue.md#reclaimRequest) instead, so that the queue will give the request to some other consumer in another call to the `fetchNextRequest` function.

  Note that the `null` return value doesn't mean the queue processing finished, it means there are currently no pending requests. To check whether all requests in queue were finished, use [RequestQueue.isFinished](https://crawlee.dev/js/api/core/class/RequestQueue.md#isFinished) instead.

  ***

  #### Returns Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<T>>

  Returns the request object or `null` if there are no more pending requests.

### [**](#getInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L776)inheritedgetInfo

* ****getInfo**(): Promise\<undefined | [RequestQueueInfo](https://crawlee.dev/js/api/types/interface/RequestQueueInfo.md)>

- Inherited from RequestProvider.getInfo

  Returns an object containing general information about the request queue.

  The function returns the same object as the Apify API Client's [getQueue](https://docs.apify.com/api/apify-client-js/latest#ApifyClient-requestQueues) function, which in turn calls the [Get request queue](https://apify.com/docs/api/v2#/reference/request-queues/queue/get-request-queue) API endpoint.

  **Example:**

  ```
  {
    id: "WkzbQMuFYuamGv3YF",
    name: "my-queue",
    userId: "wRsJZtadYvn4mBZmm",
    createdAt: new Date("2015-12-12T07:34:14.202Z"),
    modifiedAt: new Date("2015-12-13T08:36:13.202Z"),
    accessedAt: new Date("2015-12-14T08:36:13.202Z"),
    totalRequestCount: 25,
    handledRequestCount: 5,
    pendingRequestCount: 20,
  }
  ```

  ***

  #### Returns Promise\<undefined | [RequestQueueInfo](https://crawlee.dev/js/api/types/interface/RequestQueueInfo.md)>

### [**](#getPendingCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L173)inheritedgetPendingCount

* ****getPendingCount**(): number

- Inherited from RequestProvider.getPendingCount

  Returns an offline approximation of the total number of pending requests in the queue.

  Survives restarts and Actor migrations.

  ***

  #### Returns number

### [**](#getRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L535)inheritedgetRequest

* ****getRequest**\<T>(id): Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<T>>

- Inherited from RequestProvider.getRequest

  Gets the request from the queue specified by ID.

  ***

  #### Parameters

  * ##### id: string

    ID of the request.

  #### Returns Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<T>>

  Returns the request object, or `null` if it was not found.

### [**](#getTotalCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L164)inheritedgetTotalCount

* ****getTotalCount**(): number

- Inherited from RequestProvider.getTotalCount

  Returns an offline approximation of the total number of requests in the queue (i.e. pending + handled).

  Survives restarts and actor migrations.

  ***

  #### Returns number

### [**](#handledCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L746)inheritedhandledCount

* ****handledCount**(): Promise\<number>

- Inherited from RequestProvider.handledCount

  Returns number of handled requests.

  ***

  #### Returns Promise\<number>

### [**](#isEmpty)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L663)inheritedisEmpty

* ****isEmpty**(): Promise\<boolean>

- Inherited from RequestProvider.isEmpty

  Resolves to `true` if the next call to [RequestQueue.fetchNextRequest](https://crawlee.dev/js/api/core/class/RequestQueue.md#fetchNextRequest) would return `null`, otherwise it resolves to `false`. Note that even if the queue is empty, there might be some pending requests currently being processed. If you need to ensure that there is no activity in the queue, use [RequestQueue.isFinished](https://crawlee.dev/js/api/core/class/RequestQueue.md#isFinished).

  ***

  #### Returns Promise\<boolean>

### [**](#isFinished)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_queue.ts#L309)isFinished

* ****isFinished**(): Promise\<boolean>

- Overrides RequestProvider.isFinished

  Resolves to `true` if all requests were already handled and there are no more left. Due to the nature of distributed storage used by the queue, the function may occasionally return a false negative, but it shall never return a false positive.

  ***

  #### Returns Promise\<boolean>

### [**](#markRequestHandled)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_queue.ts#L366)markRequestHandled

* ****markRequestHandled**(request): Promise\<null | RequestQueueOperationInfo>

- Overrides RequestProvider.markRequestHandled

  Marks a request that was previously returned by the [RequestQueue.fetchNextRequest](https://crawlee.dev/js/api/core/class/RequestQueue.md#fetchNextRequest) function as handled after successful processing. Handled requests will never again be returned by the `fetchNextRequest` function.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

  #### Returns Promise\<null | RequestQueueOperationInfo>

### [**](#reclaimRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_queue.ts#L336)reclaimRequest

* ****reclaimRequest**(...args): Promise\<null | RequestQueueOperationInfo>

- Overrides RequestProvider.reclaimRequest

  Reclaims a failed request back to the queue, so that it can be returned for processing later again by another call to [RequestQueue.fetchNextRequest](https://crawlee.dev/js/api/core/class/RequestQueue.md#fetchNextRequest). The request record in the queue is updated using the provided `request` parameter. For example, this lets you store the number of retries or error messages for the request.

  ***

  #### Parameters

  * ##### rest...args: \[request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, options: [RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md)]

  #### Returns Promise\<null | RequestQueueOperationInfo>

### [**](#open)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_queue.ts#L396)staticopen

* ****open**(...args): Promise<[RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueueV1.md)>

- Overrides RequestProvider.open

  Opens a request queue and returns a promise resolving to an instance of the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) class.

  [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) represents a queue of URLs to crawl, which is stored either on local filesystem or in the cloud. The queue is used for deep crawling of websites, where you start with several URLs and then recursively follow links to other pages. The data structure supports both breadth-first and depth-first crawling orders.

  For more details and code examples, see the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) class.

  ***

  #### Parameters

  * ##### rest...args: \[queueIdOrName?: null | string, options: [StorageManagerOptions](https://crawlee.dev/js/api/core/interface/StorageManagerOptions.md)]

  #### Returns Promise<[RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueueV1.md)>
