# Source: https://docs.apify.com/api/client/python/reference/class/RequestQueueClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RequestQueueClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/RequestQueueClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RequestQueueClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/RequestQueueClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RequestQueueClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/RequestQueueClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RequestQueueClient.md

# RequestQueueClient<!-- -->

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

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L35)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L27)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L37)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L23)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L39)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L29)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L31)inheritedresourcePath

**resourcePath: string

Inherited from ResourceClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L25)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L33)inheritedurl

**url: string

Inherited from ResourceClient.url

## Methods<!-- -->[**](#Methods)

### [**](#addRequest)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L123)addRequest

* ****addRequest**(request, options): Promise<[RequestQueueClientAddRequestResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientAddRequestResult.md)>

- <https://docs.apify.com/api/v2#/reference/request-queues/request-collection/add-request>

  ***

  #### Parameters

  * ##### request: Omit<[RequestQueueClientRequestSchema](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientRequestSchema.md), id>
  * ##### options: [RequestQueueClientAddRequestOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientAddRequestOptions.md) = <!-- -->{}

  #### Returns Promise<[RequestQueueClientAddRequestResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientAddRequestResult.md)>

### [**](#batchAddRequests)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L266)batchAddRequests

* ****batchAddRequests**(requests, options): Promise<[RequestQueueClientBatchRequestsOperationResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientBatchRequestsOperationResult.md)>

- <https://docs.apify.com/api/v2#/reference/request-queues/batch-request-operations/add-requests>

  ***

  #### Parameters

  * ##### requests: Omit<[RequestQueueClientRequestSchema](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientRequestSchema.md), id>\[]
  * ##### options: [RequestQueueClientBatchAddRequestWithRetriesOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientBatchAddRequestWithRetriesOptions.md) = <!-- -->{}

  #### Returns Promise<[RequestQueueClientBatchRequestsOperationResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientBatchRequestsOperationResult.md)>

### [**](#batchDeleteRequests)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L330)batchDeleteRequests

* ****batchDeleteRequests**(requests): Promise<[RequestQueueClientBatchRequestsOperationResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientBatchRequestsOperationResult.md)>

- <https://docs.apify.com/api/v2#/reference/request-queues/batch-request-operations/delete-requests>

  ***

  #### Parameters

  * ##### requests: [RequestQueueClientRequestToDelete](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueClientRequestToDelete)\[]

  #### Returns Promise<[RequestQueueClientBatchRequestsOperationResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientBatchRequestsOperationResult.md)>

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L64)delete

* ****delete**(): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/request-queues/queue/delete-request-queue>

  ***

  #### Returns Promise\<void>

### [**](#deleteRequest)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L412)deleteRequest

* ****deleteRequest**(id): Promise\<void>

- #### Parameters

  * ##### id: string

  #### Returns Promise\<void>

### [**](#deleteRequestLock)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L458)deleteRequestLock

* ****deleteRequestLock**(id, options): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/request-queues/request-lock/delete-request-lock>

  ***

  #### Parameters

  * ##### id: string
  * ##### options: [RequestQueueClientDeleteRequestLockOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientDeleteRequestLockOptions.md) = <!-- -->{}

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L48)get

* ****get**(): Promise\<undefined | [RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md)>

- <https://docs.apify.com/api/v2#/reference/request-queues/queue/get-request-queue>

  ***

  #### Returns Promise\<undefined | [RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md)>

### [**](#getRequest)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L359)getRequest

* ****getRequest**(id): Promise\<undefined | [RequestQueueClientGetRequestResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueClientGetRequestResult)>

- <https://docs.apify.com/api/v2#/reference/request-queues/request/get-request>

  ***

  #### Parameters

  * ##### id: string

  #### Returns Promise\<undefined | [RequestQueueClientGetRequestResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueClientGetRequestResult)>

### [**](#listAndLockHead)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L95)listAndLockHead

* ****listAndLockHead**(options): Promise<[RequestQueueClientListAndLockHeadResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListAndLockHeadResult.md)>

- <https://docs.apify.com/api/v2#/reference/request-queues/queue-head-with-locks/get-head-and-lock>

  ***

  #### Parameters

  * ##### options: [RequestQueueClientListAndLockHeadOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListAndLockHeadOptions.md)

  #### Returns Promise<[RequestQueueClientListAndLockHeadResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListAndLockHeadResult.md)>

### [**](#listHead)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L71)listHead

* ****listHead**(options): Promise<[RequestQueueClientListHeadResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListHeadResult.md)>

- <https://docs.apify.com/api/v2#/reference/request-queues/queue-head/get-head>

  ***

  #### Parameters

  * ##### options: [RequestQueueClientListHeadOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListHeadOptions.md) = <!-- -->{}

  #### Returns Promise<[RequestQueueClientListHeadResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListHeadResult.md)>

### [**](#listRequests)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L481)listRequests

* ****listRequests**(options): Promise<[RequestQueueClientListRequestsResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListRequestsResult.md)>

- <https://docs.apify.com/api/v2#/reference/request-queues/request-collection/list-requests>

  ***

  #### Parameters

  * ##### options: [RequestQueueClientListRequestsOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListRequestsOptions.md) = <!-- -->{}

  #### Returns Promise<[RequestQueueClientListRequestsResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListRequestsResult.md)>

### [**](#paginateRequests)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L530)paginateRequests

* ****paginateRequests**(options): [RequestQueueRequestsAsyncIterable](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueRequestsAsyncIterable)<[RequestQueueClientListRequestsResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListRequestsResult.md)>

- <https://docs.apify.com/api/v2#/reference/request-queues/request-collection/list-requests>

  Usage: for await (const { items } of client.paginateRequests({ limit: 10 })) { items.forEach((request) => console.log(request)); }

  ***

  #### Parameters

  * ##### options: [RequestQueueClientPaginateRequestsOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientPaginateRequestsOptions.md) = <!-- -->{}

  #### Returns [RequestQueueRequestsAsyncIterable](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueRequestsAsyncIterable)<[RequestQueueClientListRequestsResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListRequestsResult.md)>

### [**](#prolongRequestLock)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L428)prolongRequestLock

* ****prolongRequestLock**(id, options): Promise<[RequestQueueClientProlongRequestLockResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientProlongRequestLockResult.md)>

- <https://docs.apify.com/api/v2#/reference/request-queues/request-lock/prolong-request-lock>

  ***

  #### Parameters

  * ##### id: string
  * ##### options: [RequestQueueClientProlongRequestLockOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientProlongRequestLockOptions.md)

  #### Returns Promise<[RequestQueueClientProlongRequestLockResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientProlongRequestLockResult.md)>

### [**](#unlockRequests)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L509)unlockRequests

* ****unlockRequests**(): Promise<[RequestQueueClientUnlockRequestsResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientUnlockRequestsResult.md)>

- <https://docs.apify.com/api/v2/request-queue-requests-unlock-post>

  ***

  #### Returns Promise<[RequestQueueClientUnlockRequestsResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientUnlockRequestsResult.md)>

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L55)update

* ****update**(newFields): Promise<[RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md)>

- <https://docs.apify.com/api/v2#/reference/request-queues/queue/update-request-queue>

  ***

  #### Parameters

  * ##### newFields: [RequestQueueClientUpdateOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientUpdateOptions.md)

  #### Returns Promise<[RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md)>

### [**](#updateRequest)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L380)updateRequest

* ****updateRequest**(request, options): Promise<[RequestQueueClientAddRequestResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientAddRequestResult.md)>

- <https://docs.apify.com/api/v2#/reference/request-queues/request/update-request>

  ***

  #### Parameters

  * ##### request: [RequestQueueClientRequestSchema](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientRequestSchema.md)
  * ##### options: [RequestQueueClientAddRequestOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientAddRequestOptions.md) = <!-- -->{}

  #### Returns Promise<[RequestQueueClientAddRequestResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientAddRequestResult.md)>
