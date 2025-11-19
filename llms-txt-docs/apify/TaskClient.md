# Source: https://docs.apify.com/api/client/python/reference/class/TaskClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/TaskClient.md

# TaskClient<!-- -->

### Hierarchy

* ResourceClient
  * *TaskClient*

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

* [**call](#call)
* [**delete](#delete)
* [**get](#get)
* [**getInput](#getInput)
* [**lastRun](#lastRun)
* [**runs](#runs)
* [**start](#start)
* [**update](#update)
* [**updateInput](#updateInput)
* [**webhooks](#webhooks)

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

### [**](#call)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/task.ts#L105)call

* ****call**(input, options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Starts a task and waits for it to finish before returning the Run object. It waits indefinitely, unless the `waitSecs` option is provided. <https://docs.apify.com/api/v2#/reference/actor-tasks/run-collection/run-task>

  ***

  #### Parameters

  * ##### optionalinput: [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)
  * ##### options: [TaskCallOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/TaskCallOptions.md) = <!-- -->{}

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/task.ts#L46)delete

* ****delete**(): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/actor-tasks/task-object/delete-task>

  ***

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/task.ts#L30)get

* ****get**(): Promise\<undefined | [Task](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Task.md)>

- <https://docs.apify.com/api/v2#/reference/actor-tasks/task-object/get-task>

  ***

  #### Returns Promise\<undefined | [Task](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Task.md)>

### [**](#getInput)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/task.ts#L134)getInput

* ****getInput**(): Promise\<undefined | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary) | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)\[]>

- <https://docs.apify.com/api/v2#/reference/actor-tasks/task-input-object/get-task-input>

  ***

  #### Returns Promise\<undefined | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary) | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)\[]>

### [**](#lastRun)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/task.ts#L167)lastRun

* ****lastRun**(options): [RunClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunClient.md)

- <https://docs.apify.com/api/v2#/reference/actor-tasks/last-run-object-and-its-storages>

  ***

  #### Parameters

  * ##### options: [TaskLastRunOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/TaskLastRunOptions.md) = <!-- -->{}

  #### Returns [RunClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunClient.md)

### [**](#runs)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/task.ts#L188)runs

* ****runs**(): [RunCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/actor-tasks/run-collection>

  ***

  #### Returns [RunCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunCollectionClient.md)

### [**](#start)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/task.ts#L54)start

* ****start**(input, options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Starts a task and immediately returns the Run object. <https://docs.apify.com/api/v2#/reference/actor-tasks/run-collection/run-task>

  ***

  #### Parameters

  * ##### optionalinput: [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)
  * ##### options: [TaskStartOptions](https://docs.apify.com/api/client/js/api/client/js/reference.md#TaskStartOptions) = <!-- -->{}

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/task.ts#L37)update

* ****update**(newFields): Promise<[Task](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Task.md)>

- <https://docs.apify.com/api/v2#/reference/actor-tasks/task-object/update-task>

  ***

  #### Parameters

  * ##### newFields: Partial\<Pick<[Task](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Task.md), name | description | title | actorStandby | input | options>>

  #### Returns Promise<[Task](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Task.md)>

### [**](#updateInput)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/task.ts#L153)updateInput

* ****updateInput**(newFields): Promise<[Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary) | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)\[]>

- <https://docs.apify.com/api/v2#/reference/actor-tasks/task-input-object/update-task-input>

  ***

  #### Parameters

  * ##### newFields: [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary) | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)\[]

  #### Returns Promise<[Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary) | [Dictionary](https://docs.apify.com/api/client/js/api/client/js/reference.md#Dictionary)\[]>

### [**](#webhooks)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/task.ts#L199)webhooks

* ****webhooks**(): [WebhookCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/actor-tasks/webhook-collection>

  ***

  #### Returns [WebhookCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookCollectionClient.md)
