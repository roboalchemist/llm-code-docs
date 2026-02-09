# Source: https://docs.apify.com/api/client/python/reference/class/BuildCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/BuildCollectionClient.md

# BuildCollectionClient<!-- -->

Client for managing the collection of Actor builds.

Provides methods to list Actor builds across all Actors or for a specific Actor. To access an individual build, use the `build()` method on the main ApifyClient.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });

  // List all builds
  const buildsClient = client.builds();
  const { items } = await buildsClient.list();

  // List builds for a specific Actor
  const actorBuildsClient = client.actor('my-actor-id').builds();
  const { items: actorBuilds } = await actorBuildsClient.list();
  ```

* **@see**

  <https://docs.apify.com/platform/actors/running/runs-and-builds#builds>

### Hierarchy

* ResourceCollectionClient
  * *BuildCollectionClient*

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

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/build_collection.ts#L60)list

* ****list**(options): PaginatedIterator<[BuildCollectionClientListItem](https://docs.apify.com/api/client/js/api/client/js/reference.md#BuildCollectionClientListItem)>

- Lists all Actor builds.

  Awaiting the return value (as you would with a Promise) will result in a single API call. The amount of fetched items in a single API call is limited.

  ```
  const paginatedList = await client.list(options);
  ```

  Asynchronous iteration is also supported. This will fetch additional pages if needed until all items are retrieved.

  ```
  for await (const singleItem of client.list(options)) {...}
  ```

  * **@see**

    <https://docs.apify.com/api/v2/actor-builds-get>

  ***

  #### Parameters

  * ##### options: [BuildCollectionClientListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildCollectionClientListOptions.md) = <!-- -->{}

    Pagination and sorting options.

  #### Returns PaginatedIterator<[BuildCollectionClientListItem](https://docs.apify.com/api/client/js/api/client/js/reference.md#BuildCollectionClientListItem)>

  A paginated iterator of Actor builds.
