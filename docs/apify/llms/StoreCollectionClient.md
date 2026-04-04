# Source: https://docs.apify.com/api/client/python/reference/class/StoreCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/StoreCollectionClient.md

# StoreCollectionClient<!-- -->

Client for browsing Actors in the Apify Store.

The Apify Store contains publicly available Actors that can be used by anyone. This client provides methods to search and list Actors from the Store.

* **@example**

  ```
  const client = new ApifyClient();
  const storeClient = client.store();

  // Search for Actors in the Store
  const { items } = await storeClient.list({ search: 'web scraper' });

  // Get details about a specific Store Actor
  const actor = await storeClient.list({ username: 'apify', actorName: 'web-scraper' });
  ```

* **@see**

  <https://docs.apify.com/platform/actors/publishing>

### Hierarchy

* ResourceCollectionClient
  * *StoreCollectionClient*

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

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/store_collection.ts#L59)list

* ****list**(options): PaginatedIterator<[ActorStoreList](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorStoreList.md)>

- Lists Actors from the Apify Store.

  Awaiting the return value (as you would with a Promise) will result in a single API call. The amount of fetched items in a single API call is limited.

  ```
  const paginatedList = await client.list(options);
  ```

  Asynchronous iteration is also supported. This will fetch additional pages if needed until all items are retrieved.

  ```
  for await (const singleItem of client.list(options)) {...}
  ```

  * **@see**

    <https://docs.apify.com/api/v2/store-actors-get>

  ***

  #### Parameters

  * ##### options: [StoreCollectionListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/StoreCollectionListOptions.md) = <!-- -->{}

    Search and pagination options.

  #### Returns PaginatedIterator<[ActorStoreList](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorStoreList.md)>

  A paginated iterator of store Actors.
