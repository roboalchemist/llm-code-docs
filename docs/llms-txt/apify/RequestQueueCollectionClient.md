# Source: https://docs.apify.com/api/client/python/reference/class/RequestQueueCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RequestQueueCollectionClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/RequestQueueCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RequestQueueCollectionClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/RequestQueueCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RequestQueueCollectionClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/RequestQueueCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RequestQueueCollectionClient.md

# RequestQueueCollectionClient<!-- -->

### Hierarchy

* ResourceCollectionClient
  * *RequestQueueCollectionClient*

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

* [**getOrCreate](#getOrCreate)
* [**list](#list)

## Properties<!-- -->[**](#Properties)

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L35)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceCollectionClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L27)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceCollectionClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L37)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceCollectionClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L23)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceCollectionClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L39)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceCollectionClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L29)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceCollectionClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L31)inheritedresourcePath

**resourcePath: string

Inherited from ResourceCollectionClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L25)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceCollectionClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L33)inheritedurl

**url: string

Inherited from ResourceCollectionClient.url

## Methods<!-- -->[**](#Methods)

### [**](#getOrCreate)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue_collection.ts#L39)getOrCreate

* ****getOrCreate**(name): Promise<[RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md)>

- <https://docs.apify.com/api/v2#/reference/request-queues/queue-collection/create-request-queue>

  ***

  #### Parameters

  * ##### optionalname: string

  #### Returns Promise<[RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md)>

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue_collection.ts#L22)list

* ****list**(options): Promise<[RequestQueueCollectionListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueCollectionListResult)>

- <https://docs.apify.com/api/v2#/reference/request-queues/queue-collection/get-list-of-request-queues>

  ***

  #### Parameters

  * ##### options: [RequestQueueCollectionListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueCollectionListOptions.md) = <!-- -->{}

  #### Returns Promise<[RequestQueueCollectionListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueCollectionListResult)>
