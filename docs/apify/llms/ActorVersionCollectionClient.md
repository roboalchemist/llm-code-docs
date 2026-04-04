# Source: https://docs.apify.com/api/client/python/reference/class/ActorVersionCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorVersionCollectionClient.md

# ActorVersionCollectionClient<!-- -->

Client for managing the collection of Actor versions.

Actor versions represent specific builds or snapshots of an Actor's code. This client provides methods to list and create versions for a specific Actor.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const actorClient = client.actor('my-actor-id');

  // List all versions
  const versionsClient = actorClient.versions();
  const { items } = await versionsClient.list();

  // Create a new version
  const newVersion = await versionsClient.create({
    versionNumber: '0.2',
    buildTag: 'latest'
  });
  ```

* **@see**

  <https://docs.apify.com/platform/actors/development/actor-definition/versions>

### Hierarchy

* ResourceCollectionClient
  * *ActorVersionCollectionClient*

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

* [**create](#create)
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

### [**](#create)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_version_collection.ts#L75)create

* ****create**(actorVersion): Promise<[FinalActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#FinalActorVersion)>

- Creates a new Actor version.

  * **@see**

    <https://docs.apify.com/api/v2/act-versions-post>

  ***

  #### Parameters

  * ##### actorVersion: [ActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorVersion)

    The Actor version data.

  #### Returns Promise<[FinalActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#FinalActorVersion)>

  The created Actor version object.

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_version_collection.ts#L62)list

* ****list**(\_options): Promise<[ActorVersionListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorVersionListResult)> & AsyncIterable<[FinalActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#FinalActorVersion), any, any>

- Lists all Actor versions.

  Awaiting the return value (as you would with a Promise) will result in a single API call. The amount of fetched items in a single API call is limited.

  ```
  const paginatedList = await client.list();
  ```

  Asynchronous iteration is also supported. This will fetch additional pages if needed until all items are retrieved.

  ```
  for await (const singleItem of client.list()) {...}
  ```

  * **@see**

    <https://docs.apify.com/api/v2/act-versions-get>

  ***

  #### Parameters

  * ##### \_options: [ActorVersionCollectionListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorVersionCollectionListOptions.md) = <!-- -->{}

  #### Returns Promise<[ActorVersionListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorVersionListResult)> & AsyncIterable<[FinalActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#FinalActorVersion), any, any>

  A paginated iterator of Actor versions.
