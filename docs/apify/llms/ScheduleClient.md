# Source: https://docs.apify.com/api/client/python/reference/class/ScheduleClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ScheduleClient.md

# ScheduleClient<!-- -->

Client for managing a specific Schedule.

Schedules are used to automatically start Actors or tasks at specified times. This client provides methods to get, update, and delete schedules, as well as retrieve schedule logs.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const scheduleClient = client.schedule('my-schedule-id');

  // Get schedule details
  const schedule = await scheduleClient.get();

  // Update schedule
  await scheduleClient.update({
    cronExpression: '0 12 * * *',
    isEnabled: true
  });
  ```

* **@see**

  <https://docs.apify.com/platform/schedules>

### Hierarchy

* ResourceClient
  * *ScheduleClient*

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

* [**delete](#delete)
* [**get](#get)
* [**getLog](#getLog)
* [**update](#update)

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

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/schedule.ts#L72)delete

* ****delete**(): Promise\<void>

- Deletes the schedule.

  * **@see**

    <https://docs.apify.com/api/v2/schedule-delete>

  ***

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/schedule.ts#L51)get

* ****get**(): Promise\<undefined | [Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md)>

- Retrieves the schedule.

  * **@see**

    <https://docs.apify.com/api/v2/schedule-get>

  ***

  #### Returns Promise\<undefined | [Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md)>

  The schedule object, or `undefined` if it does not exist.

### [**](#getLog)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/schedule.ts#L82)getLog

* ****getLog**(): Promise\<undefined | string>

- Retrieves the schedule's log.

  * **@see**

    <https://docs.apify.com/api/v2/schedule-log-get>

  ***

  #### Returns Promise\<undefined | string>

  The schedule log as a string, or `undefined` if it does not exist.

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/schedule.ts#L62)update

* ****update**(newFields): Promise<[Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md)>

- Updates the schedule with the specified fields.

  * **@see**

    <https://docs.apify.com/api/v2/schedule-put>

  ***

  #### Parameters

  * ##### newFields: Partial\<Pick<[Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md), name | description | title | cronExpression | timezone | isEnabled | isExclusive | notifications> & { actions: DistributiveOptional<[ScheduleAction](https://docs.apify.com/api/client/js/api/client/js/reference.md#ScheduleAction), id>\[] }>

    Fields to update.

  #### Returns Promise<[Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md)>

  The updated schedule object.
