# Source: https://docs.apify.com/api/client/python/reference/class/RequestQueueClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RequestQueueClient.md

# RequestQueueClient<!-- -->

Client for managing a specific Request queue.

Request queues store URLs to be crawled and their metadata. Each request in the queue has a unique ID and can be in various states (pending, handled). This client provides methods to add, get, update, and delete requests, as well as manage the queue itself.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const queueClient = client.requestQueue('my-queue-id');

  // Add a request to the queue
  await queueClient.addRequest({
    url: 'https://example.com',
    uniqueKey: 'example-com'
  });

  // Get the next request from the queue
  const request = await queueClient.listHead();

  // Mark request as handled
  await queueClient.updateRequest({
    id: request.id,
    handledAt: new Date().toISOString()
  });
  ```

* **@see**

  <https://docs.apify.com/platform/storage/request-queue>

### Hierarchy

* ResourceClient
  * *RequestQueueClient*

## Index[**](#Index)

### Properties

* [**apifyClient](#apifyClient)
* [**baseUrl](#baseUrl)
* [**httpClient](#httpClient)
* [**id](#id)
* [**params](#params)
* [**publicBaseUrl](#publicBaseUrl)
* [**resourcePath](#resourcePath)
* [**safeId](#safeId)
* [**url](#url)

### Methods

* [**addRequest](#addRequest)
* [**batchAddRequests](#batchAddRequests)
* [**batchDeleteRequests](#batchDeleteRequests)
* [**delete](#delete)
* [**deleteRequest](#deleteRequest)
* [**deleteRequestLock](#deleteRequestLock)
* [**get](#get)
* [**getRequest](#getRequest)
* [**listAndLockHead](#listAndLockHead)
* [**listHead](#listHead)
* [**listRequests](#listRequests)
* [**paginateRequests](#paginateRequests)
* [**prolongRequestLock](#prolongRequestLock)
* [**unlockRequests](#unlockRequests)
* [**update](#update)
* [**updateRequest](#updateRequest)

## Properties<!-- -->[**](#Properties)

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L36)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L28)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L38)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L24)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L40)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L30)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L32)inheritedresourcePath

**resourcePath: string

Inherited from ResourceClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L26)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L34)inheritedurl

**url: string

Inherited from ResourceClient.url

## Methods<!-- -->[**](#Methods)

### [**](#addRequest)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L233)addRequest

* ****addRequest**(request, options): Promise<[RequestQueueClientAddRequestResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientAddRequestResult.md)>

- Adds a single request to the queue.

  If a request with the same `uniqueKey` already exists, the method will return information about the existing request without adding a duplicate. The `uniqueKey` is used for deduplication - typically it's the URL, but you can use any string to identify the request.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-requests-post>

  * **@example**

    ```
    const result = await client.requestQueue('my-queue').addRequest({
      url: 'https://example.com',
      uniqueKey: 'example-page',
      method: 'GET',
      userData: { label: 'START', depth: 0 }
    });
    console.log(`Request ID: ${result.requestId}`);
    console.log(`Already present: ${result.wasAlreadyPresent}`);
    console.log(`Already handled: ${result.wasAlreadyHandled}`);

    // Add urgent request to the front of the queue
    await client.requestQueue('my-queue').addRequest(
      { url: 'https://priority.com', uniqueKey: 'priority-page' },
      { forefront: true }
    );
    ```

  ***

  #### Parameters

  * ##### request: Omit<[RequestQueueClientRequestSchema](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientRequestSchema.md), id>

    The request object to add (excluding `id`, which is assigned by the API)

  * ##### options: [RequestQueueClientAddRequestOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientAddRequestOptions.md) = <!-- -->{}

    Additional options

  #### Returns Promise<[RequestQueueClientAddRequestResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientAddRequestResult.md)>

  Object with `requestId`, `wasAlreadyPresent`, and `wasAlreadyHandled` flags

### [**](#batchAddRequests)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L410)batchAddRequests

* ****batchAddRequests**(requests, options): Promise<[RequestQueueClientBatchRequestsOperationResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientBatchRequestsOperationResult.md)>

- Adds multiple requests to the queue in a single operation.

  This is significantly more efficient than calling addRequest multiple times, especially for large batches. The method automatically handles batching (max 25 requests per API call), retries on rate limiting, and parallel processing. Requests are sent in chunks respecting the API payload size limit, and any unprocessed requests due to rate limits are automatically retried with exponential backoff.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-requests-batch-post>

  * **@example**

    ```
    // Add a batch of URLs to crawl
    const requests = [
      { url: 'https://example.com', uniqueKey: 'page1', userData: { depth: 1 } },
      { url: 'https://example.com/2', uniqueKey: 'page2', userData: { depth: 1 } },
      { url: 'https://example.com/3', uniqueKey: 'page3', userData: { depth: 1 } }
    ];
    const result = await client.requestQueue('my-queue').batchAddRequests(requests);
    console.log(`Successfully added: ${result.processedRequests.length}`);
    console.log(`Failed: ${result.unprocessedRequests.length}`);

    // Batch add with custom retry settings
    const result = await client.requestQueue('my-queue').batchAddRequests(
      requests,
      { maxUnprocessedRequestsRetries: 5, maxParallel: 10 }
    );
    ```

  ***

  #### Parameters

  * ##### requests: Omit<[RequestQueueClientRequestSchema](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientRequestSchema.md), id>\[]

    Array of request objects to add (excluding `id` fields)

  * ##### options: [RequestQueueClientBatchAddRequestWithRetriesOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientBatchAddRequestWithRetriesOptions.md) = <!-- -->{}

    Batch operation configuration

  #### Returns Promise<[RequestQueueClientBatchRequestsOperationResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientBatchRequestsOperationResult.md)>

  Object with `processedRequests` (successfully added) and `unprocessedRequests` (failed after all retries)

### [**](#batchDeleteRequests)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L480)batchDeleteRequests

* ****batchDeleteRequests**(requests): Promise<[RequestQueueClientBatchRequestsOperationResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientBatchRequestsOperationResult.md)>

- Deletes multiple requests from the queue in a single operation.

  Requests can be identified by either their ID or unique key.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-requests-batch-delete>

  ***

  #### Parameters

  * ##### requests: [RequestQueueClientRequestToDelete](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueClientRequestToDelete)\[]

    Array of requests to delete (by id or uniqueKey)

  #### Returns Promise<[RequestQueueClientBatchRequestsOperationResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientBatchRequestsOperationResult.md)>

  Result containing processed and unprocessed requests

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L103)delete

* ****delete**(): Promise\<void>

- Deletes the Request queue.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-delete>

  ***

  #### Returns Promise\<void>

### [**](#deleteRequest)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L576)deleteRequest

* ****deleteRequest**(id): Promise\<void>

- Deletes a specific request from the queue.

  ***

  #### Parameters

  * ##### id: string

    Request ID

  #### Returns Promise\<void>

### [**](#deleteRequestLock)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L650)deleteRequestLock

* ****deleteRequestLock**(id, options): Promise\<void>

- Releases the lock on a request, allowing other clients to process it.

  This should be called after successfully processing a request or when you decide not to process it.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-request-lock-delete>

  ***

  #### Parameters

  * ##### id: string

    Request ID

  * ##### options: [RequestQueueClientDeleteRequestLockOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientDeleteRequestLockOptions.md) = <!-- -->{}

    Options such as whether to move to front

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L81)get

* ****get**(): Promise\<undefined | [RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md)>

- Gets the Request queue object from the Apify API.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-get>

  ***

  #### Returns Promise\<undefined | [RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md)>

  The RequestQueue object, or `undefined` if it does not exist

### [**](#getRequest)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L513)getRequest

* ****getRequest**(id): Promise\<undefined | [RequestQueueClientGetRequestResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueClientGetRequestResult)>

- Gets a specific request from the queue by its ID.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-request-get>

  ***

  #### Parameters

  * ##### id: string

    Request ID

  #### Returns Promise\<undefined | [RequestQueueClientGetRequestResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueClientGetRequestResult)>

  The request object, or `undefined` if not found

### [**](#listAndLockHead)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L170)listAndLockHead

* ****listAndLockHead**(options): Promise<[RequestQueueClientListAndLockHeadResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListAndLockHeadResult.md)>

- Gets and locks the next requests from the queue head for processing.

  This method retrieves requests from the beginning of the queue and locks them for the specified duration to prevent other clients from processing them simultaneously. This is the primary method used by distributed web crawlers to coordinate work across multiple workers. Locked requests won't be returned to other clients until the lock expires or is explicitly released using deleteRequestLock.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-head-lock-post>

  * **@example**

    ```
    // Get and lock up to 10 requests for 60 seconds
    const { items, lockSecs } = await client.requestQueue('my-queue').listAndLockHead({
      lockSecs: 60,
      limit: 10
    });

    // Process each locked request
    for (const request of items) {
      console.log(`Processing: ${request.url}`);
      // ... process request ...
      // Delete lock after successful processing
      await client.requestQueue('my-queue').deleteRequestLock(request.id);
    }
    ```

  ***

  #### Parameters

  * ##### options: [RequestQueueClientListAndLockHeadOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListAndLockHeadOptions.md)

    Lock configuration

  #### Returns Promise<[RequestQueueClientListAndLockHeadResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListAndLockHeadResult.md)>

  Object containing `items` (locked requests), `queueModifiedAt`, `hadMultipleClients`, and lock information

### [**](#listHead)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L117)listHead

* ****listHead**(options): Promise<[RequestQueueClientListHeadResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListHeadResult.md)>

- Lists requests from the beginning of the queue (head).

  Returns the first N requests from the queue without locking them. This is useful for inspecting what requests are waiting to be processed.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-head-get>

  ***

  #### Parameters

  * ##### options: [RequestQueueClientListHeadOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListHeadOptions.md) = <!-- -->{}

    Options for listing (e.g., limit)

  #### Returns Promise<[RequestQueueClientListHeadResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListHeadResult.md)>

  List of requests from the queue head

### [**](#listRequests)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L680)listRequests

* ****listRequests**(options): Promise<[RequestQueueClientListRequestsResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListRequestsResult.md)> & AsyncIterable<[RequestQueueClientRequestSchema](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientRequestSchema.md), any, any>

- Lists all requests in the queue.

  Returns a paginated list of all requests, allowing you to iterate through the entire queue contents.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-requests-get>

  ***

  #### Parameters

  * ##### options: [RequestQueueClientListRequestsOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListRequestsOptions.md) = <!-- -->{}

    Pagination options

  #### Returns Promise<[RequestQueueClientListRequestsResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListRequestsResult.md)> & AsyncIterable<[RequestQueueClientRequestSchema](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientRequestSchema.md), any, any>

  List of requests with pagination information

### [**](#paginateRequests)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L771)paginateRequests

* ****paginateRequests**(options): [RequestQueueRequestsAsyncIterable](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueRequestsAsyncIterable)<[RequestQueueClientListRequestsResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListRequestsResult.md)>

- Returns an async iterable for paginating through all requests in the queue.

  This allows you to efficiently process all requests using a for-await-of loop, automatically handling pagination behind the scenes.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-requests-get>

  * **@example**

    ```
    for await (const { items } of client.requestQueue('my-queue').paginateRequests({ limit: 100 })) {
      items.forEach((request) => console.log(request.url));
    }
    ```

  ***

  #### Parameters

  * ##### options: [RequestQueueClientPaginateRequestsOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientPaginateRequestsOptions.md) = <!-- -->{}

    Pagination options

  #### Returns [RequestQueueRequestsAsyncIterable](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueRequestsAsyncIterable)<[RequestQueueClientListRequestsResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListRequestsResult.md)>

  An async iterable of request pages

### [**](#prolongRequestLock)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L613)prolongRequestLock

* ****prolongRequestLock**(id, options): Promise<[RequestQueueClientProlongRequestLockResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientProlongRequestLockResult.md)>

- Prolongs the lock on a request to prevent it from being returned to other clients.

  This is useful when processing a request takes longer than expected and you need to extend the lock duration to prevent other workers from picking it up. The lock expiration time is reset to the current time plus the specified duration.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-request-lock-put>

  * **@example**

    ```
    // Lock request for initial processing
    const { items } = await client.requestQueue('my-queue').listAndLockHead({ lockSecs: 60, limit: 1 });
    const request = items[0];

    // Processing takes longer than expected, extend the lock
    await client.requestQueue('my-queue').prolongRequestLock(request.id, { lockSecs: 120 });
    ```

  ***

  #### Parameters

  * ##### id: string

    Request ID (obtained from listAndLockHead or getRequest)

  * ##### options: [RequestQueueClientProlongRequestLockOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientProlongRequestLockOptions.md)

    Lock extension options

  #### Returns Promise<[RequestQueueClientProlongRequestLockResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientProlongRequestLockResult.md)>

  Object with new `lockExpiresAt` timestamp

### [**](#unlockRequests)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L741)unlockRequests

* ****unlockRequests**(): Promise<[RequestQueueClientUnlockRequestsResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientUnlockRequestsResult.md)>

- Unlocks all requests locked by this client.

  This is useful for releasing all locks at once, for example when shutting down a crawler gracefully.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-requests-unlock-post>

  ***

  #### Returns Promise<[RequestQueueClientUnlockRequestsResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientUnlockRequestsResult.md)>

  Number of requests that were unlocked

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L92)update

* ****update**(newFields): Promise<[RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md)>

- Updates the Request queue with specified fields.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-put>

  ***

  #### Parameters

  * ##### newFields: [RequestQueueClientUpdateOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientUpdateOptions.md)

    Fields to update in the Request queue

  #### Returns Promise<[RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md)>

  The updated RequestQueue object

### [**](#updateRequest)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L539)updateRequest

* ****updateRequest**(request, options): Promise<[RequestQueueClientAddRequestResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientAddRequestResult.md)>

- Updates a request in the queue.

  * **@see**

    <https://docs.apify.com/api/v2/request-queue-request-put>

  ***

  #### Parameters

  * ##### request: [RequestQueueClientRequestSchema](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientRequestSchema.md)

    The updated request object (must include id)

  * ##### options: [RequestQueueClientAddRequestOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientAddRequestOptions.md) = <!-- -->{}

    Update options such as whether to move to front

  #### Returns Promise<[RequestQueueClientAddRequestResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientAddRequestResult.md)>

  Information about the updated request
