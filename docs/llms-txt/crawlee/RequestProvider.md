# Source: https://crawlee.dev/js/api/core/class/RequestProvider.md

# abstractRequestProvider<!-- -->

Represents a provider of requests/URLs to crawl.

### Hierarchy

* *RequestProvider*

  * [RequestQueueV1](https://crawlee.dev/js/api/core/class/RequestQueueV1.md)
  * [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md)

### Implements

* [IStorage](https://crawlee.dev/js/api/core/interface/IStorage.md)
* [IRequestManager](https://crawlee.dev/js/api/core/interface/IRequestManager.md)

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

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

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L135)constructor

* ****new RequestProvider**(options, config): [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)

- #### Parameters

  * ##### options: InternalRequestProviderOptions
  * ##### config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) = <!-- -->...

  #### Returns [RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)

## Properties<!-- -->[**](#Properties)

### [**](#assumedHandledCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L117)assumedHandledCount

**assumedHandledCount: number =

<!-- -->

0

### [**](#assumedTotalCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L116)assumedTotalCount

**assumedTotalCount: number =

<!-- -->

0

### [**](#client)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L107)client

**client: [RequestQueueClient](https://crawlee.dev/js/api/types/interface/RequestQueueClient.md)

### [**](#clientKey)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L106)clientKey

**clientKey: string =

<!-- -->

...

### [**](#config)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L137)readonlyconfig

**config: [Configuration](https://crawlee.dev/js/api/core/class/Configuration.md) =

<!-- -->

...

### [**](#id)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L103)id

**id: string

Implementation of IStorage.id

### [**](#internalTimeoutMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L111)internalTimeoutMillis

**internalTimeoutMillis: number =

<!-- -->

...

### [**](#log)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L110)log

**log: [Log](https://crawlee.dev/js/api/core/class/Log.md)

### [**](#name)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L104)optionalname

**name?

<!-- -->

: string

Implementation of IStorage.name

### [**](#requestLockSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L112)requestLockSecs

**requestLockSecs: number =

<!-- -->

...

### [**](#timeoutSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L105)timeoutSecs

**timeoutSecs: number =

<!-- -->

30

## Methods<!-- -->[**](#Methods)

### [**](#\[asyncIterator])[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L728)\[asyncIterator]

* ****\[asyncIterator]**(): AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, void, unknown>

- Implementation of IRequestManager.\[asyncIterator]

  Can be used to iterate over the `RequestManager` instance in a `for await .. of` loop. Provides an alternative for the repeated use of `fetchNextRequest`.

  ***

  #### Returns AsyncGenerator<[Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>, void, unknown>

### [**](#addRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L191)addRequest

* ****addRequest**(requestLike, options): Promise\<RequestQueueOperationInfo>

- Implementation of IRequestManager.addRequest

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

### [**](#addRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L275)addRequests

* ****addRequests**(requestsLike, options): Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

- Adds requests to the queue in batches of 25. This method will wait till all the requests are added to the queue before resolving. You should prefer using `queue.addRequestsBatched()` or `crawler.addRequests()` if you don't want to block the processing, as those methods will only wait for the initial 1000 requests, start processing right after that happens, and continue adding more in the background.

  If a request passed in is already present due to its `uniqueKey` property being the same, it will not be updated. You can find out whether this happened by finding the request in the resulting [BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md) object.

  ***

  #### Parameters

  * ##### requestsLike: [RequestsLike](https://crawlee.dev/js/api/core.md#RequestsLike)

    [Request](https://crawlee.dev/js/api/core/class/Request.md) objects or vanilla objects with request data. Note that the function sets the `uniqueKey` and `id` fields to the passed requests if missing.

  * ##### optionaloptions: [RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md) = <!-- -->{}

    Request queue operation options.

  #### Returns Promise<[BatchAddRequestsResult](https://crawlee.dev/js/api/types/interface/BatchAddRequestsResult.md)>

### [**](#addRequestsBatched)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L395)addRequestsBatched

* ****addRequestsBatched**(requests, options): Promise<[AddRequestsBatchedResult](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedResult.md)>

- Implementation of IRequestManager.addRequestsBatched

  Adds requests to the queue in batches. By default, it will resolve after the initial batch is added, and continue adding the rest in the background. You can configure the batch size via `batchSize` option and the sleep time in between the batches via `waitBetweenBatchesMillis`. If you want to wait for all batches to be added to the queue, you can use the `waitForAllRequestsToBeAdded` promise you get in the response object.

  ***

  #### Parameters

  * ##### requests: [RequestsLike](https://crawlee.dev/js/api/core.md#RequestsLike)

    The requests to add

  * ##### options: [AddRequestsBatchedOptions](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedOptions.md) = <!-- -->{}

    Options for the request queue

  #### Returns Promise<[AddRequestsBatchedResult](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedResult.md)>

### [**](#drop)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L717)drop

* ****drop**(): Promise\<void>

- Removes the queue either from the Apify Cloud storage or from the local database, depending on the mode of operation.

  ***

  #### Returns Promise\<void>

### [**](#fetchNextRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L563)abstractfetchNextRequest

* ****fetchNextRequest**\<T>(): Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<T>>

- Implementation of IRequestManager.fetchNextRequest

  Returns a next request in the queue to be processed, or `null` if there are no more pending requests.

  Once you successfully finish processing of the request, you need to call [RequestQueue.markRequestHandled](https://crawlee.dev/js/api/core/class/RequestQueue.md#markRequestHandled) to mark the request as handled in the queue. If there was some error in processing the request, call [RequestQueue.reclaimRequest](https://crawlee.dev/js/api/core/class/RequestQueue.md#reclaimRequest) instead, so that the queue will give the request to some other consumer in another call to the `fetchNextRequest` function.

  Note that the `null` return value doesn't mean the queue processing finished, it means there are currently no pending requests. To check whether all requests in queue were finished, use [RequestQueue.isFinished](https://crawlee.dev/js/api/core/class/RequestQueue.md#isFinished) instead.

  ***

  #### Returns Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<T>>

  Returns the request object or `null` if there are no more pending requests.

### [**](#getInfo)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L776)getInfo

* ****getInfo**(): Promise\<undefined | [RequestQueueInfo](https://crawlee.dev/js/api/types/interface/RequestQueueInfo.md)>

- Returns an object containing general information about the request queue.

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

### [**](#getPendingCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L173)getPendingCount

* ****getPendingCount**(): number

- Implementation of IRequestManager.getPendingCount

  Returns an offline approximation of the total number of pending requests in the queue.

  Survives restarts and Actor migrations.

  ***

  #### Returns number

### [**](#getRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L535)getRequest

* ****getRequest**\<T>(id): Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<T>>

- Gets the request from the queue specified by ID.

  ***

  #### Parameters

  * ##### id: string

    ID of the request.

  #### Returns Promise\<null | [Request](https://crawlee.dev/js/api/core/class/Request.md)\<T>>

  Returns the request object, or `null` if it was not found.

### [**](#getTotalCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L164)getTotalCount

* ****getTotalCount**(): number

- Implementation of IRequestManager.getTotalCount

  Returns an offline approximation of the total number of requests in the queue (i.e. pending + handled).

  Survives restarts and actor migrations.

  ***

  #### Returns number

### [**](#handledCount)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L746)handledCount

* ****handledCount**(): Promise\<number>

- Implementation of IRequestManager.handledCount

  Returns number of handled requests.

  ***

  #### Returns Promise\<number>

### [**](#isEmpty)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L663)isEmpty

* ****isEmpty**(): Promise\<boolean>

- Implementation of IRequestManager.isEmpty

  Resolves to `true` if the next call to [RequestQueue.fetchNextRequest](https://crawlee.dev/js/api/core/class/RequestQueue.md#fetchNextRequest) would return `null`, otherwise it resolves to `false`. Note that even if the queue is empty, there might be some pending requests currently being processed. If you need to ensure that there is no activity in the queue, use [RequestQueue.isFinished](https://crawlee.dev/js/api/core/class/RequestQueue.md#isFinished).

  ***

  #### Returns Promise\<boolean>

### [**](#isFinished)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L674)abstractisFinished

* ****isFinished**(): Promise\<boolean>

- Implementation of IRequestManager.isFinished

  Resolves to `true` if all requests were already handled and there are no more left. Due to the nature of distributed storage used by the queue, the function may occasionally return a false negative, but it shall never return a false positive.

  ***

  #### Returns Promise\<boolean>

### [**](#markRequestHandled)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L571)markRequestHandled

* ****markRequestHandled**(request): Promise\<null | RequestQueueOperationInfo>

- Implementation of IRequestManager.markRequestHandled

  Marks a request that was previously returned by the [RequestQueue.fetchNextRequest](https://crawlee.dev/js/api/core/class/RequestQueue.md#fetchNextRequest) function as handled after successful processing. Handled requests will never again be returned by the `fetchNextRequest` function.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>

  #### Returns Promise\<null | RequestQueueOperationInfo>

### [**](#reclaimRequest)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L617)reclaimRequest

* ****reclaimRequest**(request, options): Promise\<null | RequestQueueOperationInfo>

- Implementation of IRequestManager.reclaimRequest

  Reclaims a failed request back to the queue, so that it can be returned for processing later again by another call to [RequestQueue.fetchNextRequest](https://crawlee.dev/js/api/core/class/RequestQueue.md#fetchNextRequest). The request record in the queue is updated using the provided `request` parameter. For example, this lets you store the number of retries or error messages for the request.

  ***

  #### Parameters

  * ##### request: [Request](https://crawlee.dev/js/api/core/class/Request.md)\<Dictionary>
  * ##### options: [RequestQueueOperationOptions](https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md) = <!-- -->{}

  #### Returns Promise\<null | RequestQueueOperationInfo>

### [**](#open)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L859)staticopen

* ****open**(queueIdOrName, options): Promise<[RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)>

- Opens a request queue and returns a promise resolving to an instance of the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) class.

  [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) represents a queue of URLs to crawl, which is stored either on local filesystem or in the cloud. The queue is used for deep crawling of websites, where you start with several URLs and then recursively follow links to other pages. The data structure supports both breadth-first and depth-first crawling orders.

  For more details and code examples, see the [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) class.

  ***

  #### Parameters

  * ##### optionalqueueIdOrName: null | string

    ID or name of the request queue to be opened. If `null` or `undefined`, the function returns the default request queue associated with the crawler run.

  * ##### optionaloptions: [StorageManagerOptions](https://crawlee.dev/js/api/core/interface/StorageManagerOptions.md) = <!-- -->{}

    Open Request Queue options.

  #### Returns Promise<[RequestProvider](https://crawlee.dev/js/api/core/class/RequestProvider.md)>
