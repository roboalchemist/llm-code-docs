# Source: https://docs.apify.com/api/client/python/reference/class/ScheduleCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ScheduleCollectionClient.md

# ScheduleCollectionClient<!-- -->

Client for managing the collection of Schedules in your account.

Schedules are used to automatically start Actors or tasks at specified times. This client provides methods to list and create schedules.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const schedulesClient = client.schedules();

  // List all schedules
  const { items } = await schedulesClient.list();

  // Create a new schedule
  const newSchedule = await schedulesClient.create({
    actorId: 'my-actor-id',
    cronExpression: '0 9 * * *',
    isEnabled: true
  });
  ```

* **@see**

  <https://docs.apify.com/platform/schedules>

### Hierarchy

* ResourceCollectionClient
  * *ScheduleCollectionClient*

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

### [**](#create)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/schedule_collection.ts#L83)create

* ****create**(schedule): Promise<[Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md)>

- Creates a new schedule.

  * **@see**

    <https://docs.apify.com/api/v2/schedules-post>

  ***

  #### Parameters

  * ##### optionalschedule: Partial\<Pick<[Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md), name | description | title | cronExpression | timezone | isEnabled | isExclusive | notifications> & { actions: DistributiveOptional<[ScheduleAction](https://docs.apify.com/api/client/js/api/client/js/reference.md#ScheduleAction), id>\[] }>

    The schedule data.

  #### Returns Promise<[Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md)>

  The created schedule object.

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/schedule_collection.ts#L63)list

* ****list**(options): PaginatedIterator<[Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md)>

- Lists all schedules.

  Awaiting the return value (as you would with a Promise) will result in a single API call. The amount of fetched items in a single API call is limited.

  ```
  const paginatedList = await client.list(options);
  ```

  Asynchronous iteration is also supported. This will fetch additional pages if needed until all items are retrieved.

  ```
  for await (const singleItem of client.list(options)) {...}
  ```

  * **@see**

    <https://docs.apify.com/api/v2/schedules-get>

  ***

  #### Parameters

  * ##### options: [ScheduleCollectionListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ScheduleCollectionListOptions.md) = <!-- -->{}

    Pagination and sorting options.

  #### Returns PaginatedIterator<[Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md)>

  A paginated iterator of schedules.
