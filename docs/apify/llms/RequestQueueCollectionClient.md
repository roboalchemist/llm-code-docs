# Source: https://docs.apify.com/api/client/python/reference/class/RequestQueueCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RequestQueueCollectionClient.md

# RequestQueueCollectionClient<!-- -->

Client for managing the collection of Request queues in your account.

Request queues store URLs to be crawled and their metadata. This client provides methods to list, create, or get request queues by name.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const queuesClient = client.requestQueues();

  // List all request queues
  const { items } = await queuesClient.list();

  // Get or create a request queue by name
  const queue = await queuesClient.getOrCreate('my-queue');
  ```

* **@see**

  <https://docs.apify.com/platform/storage/request-queue>

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

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L36)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceCollectionClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L28)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceCollectionClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L38)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceCollectionClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L24)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceCollectionClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L40)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceCollectionClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L30)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceCollectionClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L32)inheritedresourcePath

**resourcePath: string

Inherited from ResourceCollectionClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L26)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceCollectionClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L34)inheritedurl

**url: string

Inherited from ResourceCollectionClient.url

## Methods<!-- -->[**](#Methods)

### [**](#getOrCreate)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue_collection.ts#L82)getOrCreate

* ****getOrCreate**(name): Promise<[RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md)>

- Gets or creates a Request queue with the specified name.

  * **@see**

    <https://docs.apify.com/api/v2/request-queues-post>

  ***

  #### Parameters

  * ##### optionalname: string

    Name of the Request queue. If not provided, a default queue is used.

  #### Returns Promise<[RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md)>

  The Request queue object.

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue_collection.ts#L59)list

* ****list**(options): Promise<[RequestQueueCollectionListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueCollectionListResult)> & AsyncIterable<[RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md), any, any>

- Lists all Request queues.

  Awaiting the return value (as you would with a Promise) will result in a single API call. The amount of fetched items in a single API call is limited.

  ```
  const paginatedList = await client.list(options);
  ```

  Asynchronous iteration is also supported. This will fetch additional pages if needed until all items are retrieved.

  ```
  for await (const singleItem of client.list(options)) {...}
  ```

  * **@see**

    <https://docs.apify.com/api/v2/request-queues-get>

  ***

  #### Parameters

  * ##### options: [RequestQueueCollectionListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueCollectionListOptions.md) = <!-- -->{}

    Pagination options.

  #### Returns Promise<[RequestQueueCollectionListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#RequestQueueCollectionListResult)> & AsyncIterable<[RequestQueue](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueue.md), any, any>

  A paginated iterator of Request queues.
