# Source: https://docs.apify.com/api/client/python/reference/class/ActorCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorCollectionClient.md

# ActorCollectionClient<!-- -->

Client for managing the collection of Actors in your account.

Provides methods to list and create Actors. To access an individual Actor, use the `actor()` method on the main ApifyClient.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const actorsClient = client.actors();

  // List all Actors
  const { items } = await actorsClient.list();

  // Create a new Actor
  const newActor = await actorsClient.create({
    name: 'my-actor',
    title: 'My Actor'
  });
  ```

* **@see**

  <https://docs.apify.com/platform/actors>

### Hierarchy

* ResourceCollectionClient
  * *ActorCollectionClient*

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

### [**](#create)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_collection.ts#L85)create

* ****create**(actor): Promise<[Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md)>

- Creates a new Actor.

  * **@see**

    <https://docs.apify.com/api/v2/acts-post>

  ***

  #### Parameters

  * ##### actor: [ActorCollectionCreateOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorCollectionCreateOptions.md)

    The Actor data.

  #### Returns Promise<[Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md)>

  The created Actor object.

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_collection.ts#L63)list

* ****list**(options): PaginatedIterator<[ActorCollectionListItem](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorCollectionListItem.md)>

- Lists all Actors.

  Awaiting the return value (as you would with a Promise) will result in a single API call. The amount of fetched items in a single API call is limited.

  ```
  const paginatedList = await client.list(options);
  ```

  Asynchronous iteration is also supported. This will fetch additional pages if needed until all items are retrieved.

  ```
  for await (const singleItem of client.list(options)) {...}
  ```

  * **@see**

    <https://docs.apify.com/api/v2/acts-get>

  ***

  #### Parameters

  * ##### options: [ActorCollectionListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorCollectionListOptions.md) = <!-- -->{}

    Pagination options.

  #### Returns PaginatedIterator<[ActorCollectionListItem](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorCollectionListItem.md)>

  A paginated iterator of Actors.
