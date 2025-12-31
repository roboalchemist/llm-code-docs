# Source: https://docs.apify.com/api/client/python/reference/class/ScheduleClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ScheduleClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/ScheduleClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ScheduleClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/ScheduleClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ScheduleClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/ScheduleClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ScheduleClient.md

# ScheduleClient<!-- -->

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

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/schedule.ts#L40)delete

* ****delete**(): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/schedules/schedule-object/delete-schedule>

  ***

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/schedule.ts#L25)get

* ****get**(): Promise\<undefined | [Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md)>

- <https://docs.apify.com/api/v2#/reference/schedules/schedule-object/get-schedule>

  ***

  #### Returns Promise\<undefined | [Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md)>

### [**](#getLog)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/schedule.ts#L47)getLog

* ****getLog**(): Promise\<undefined | string>

- <https://docs.apify.com/api/v2#/reference/schedules/schedule-log/get-schedule-log>

  ***

  #### Returns Promise\<undefined | string>

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/schedule.ts#L32)update

* ****update**(newFields): Promise<[Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md)>

- <https://docs.apify.com/api/v2#/reference/schedules/schedule-object/update-schedule>

  ***

  #### Parameters

  * ##### newFields: Partial\<Pick<[Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md), name | description | title | cronExpression | timezone | isEnabled | isExclusive | notifications> & { actions: DistributiveOptional<[ScheduleAction](https://docs.apify.com/api/client/js/api/client/js/reference.md#ScheduleAction), id>\[] }>

  #### Returns Promise<[Schedule](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Schedule.md)>
