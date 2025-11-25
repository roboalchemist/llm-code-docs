# Source: https://docs.apify.com/sdk/js/reference/class/ApifyClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/ApifyClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ApifyClient.md

# Source: https://docs.apify.com/sdk/js/reference/class/ApifyClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/ApifyClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ApifyClient.md

# ApifyClient<!-- -->

ApifyClient is the official library to access [Apify API](https://docs.apify.com/api/v2) from your JavaScript applications. It runs both in Node.js and browser.

## Index[**](#Index)

### Constructors

* [**constructor](#constructor)

### Properties

* [**baseUrl](#baseUrl)
* [**httpClient](#httpClient)
* [**logger](#logger)
* [**publicBaseUrl](#publicBaseUrl)
* [**stats](#stats)
* [**token](#token)

### Methods

* [**actor](#actor)
* [**actors](#actors)
* [**build](#build)
* [**builds](#builds)
* [**dataset](#dataset)
* [**datasets](#datasets)
* [**keyValueStore](#keyValueStore)
* [**keyValueStores](#keyValueStores)
* [**log](#log)
* [**requestQueue](#requestQueue)
* [**requestQueues](#requestQueues)
* [**run](#run)
* [**runs](#runs)
* [**schedule](#schedule)
* [**schedules](#schedules)
* [**setStatusMessage](#setStatusMessage)
* [**store](#store)
* [**task](#task)
* [**tasks](#tasks)
* [**user](#user)
* [**webhook](#webhook)
* [**webhookDispatch](#webhookDispatch)
* [**webhookDispatches](#webhookDispatches)
* [**webhooks](#webhooks)

## Constructors<!-- -->[**](#Constructors)

### [**](#constructor)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L55)constructor

* ****new ApifyClient**(options): [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

- #### Parameters

  * ##### options: [ApifyClientOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ApifyClientOptions.md) = <!-- -->{}

  #### Returns [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

## Properties<!-- -->[**](#Properties)

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L43)baseUrl

**baseUrl: string

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L53)httpClient

**httpClient: HttpClient

### [**](#logger)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L51)logger

**logger: Log

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L45)publicBaseUrl

**publicBaseUrl: string

### [**](#stats)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L49)stats

**stats: Statistics

### [**](#token)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L47)optionaltoken

**token?

<!-- -->

: string

## Methods<!-- -->[**](#Methods)

### [**](#actor)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L120)actor

* ****actor**(id): [ActorClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorClient.md)

- <https://docs.apify.com/api/v2#/reference/actors/actor-object>

  ***

  #### Parameters

  * ##### id: string

  #### Returns [ActorClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorClient.md)

### [**](#actors)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L113)actors

* ****actors**(): [ActorCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/actors/actor-collection>

  ***

  #### Returns [ActorCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorCollectionClient.md)

### [**](#build)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L139)build

* ****build**(id): [BuildClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildClient.md)

- <https://docs.apify.com/api/v2#/reference/actor-builds/build-object>

  ***

  #### Parameters

  * ##### id: string

  #### Returns [BuildClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildClient.md)

### [**](#builds)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L132)builds

* ****builds**(): [BuildCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/actor-builds/build-collection>

  ***

  #### Returns [BuildCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildCollectionClient.md)

### [**](#dataset)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L158)dataset

* ****dataset**\<Data>(id): [DatasetClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/DatasetClient.md)\<Data>

- <https://docs.apify.com/api/v2#/reference/datasets/dataset>

  ***

  #### Parameters

  * ##### id: string

  #### Returns [DatasetClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/DatasetClient.md)\<Data>

### [**](#datasets)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L151)datasets

* ****datasets**(): [DatasetCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/DatasetCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/datasets/dataset-collection>

  ***

  #### Returns [DatasetCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/DatasetCollectionClient.md)

### [**](#keyValueStore)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L179)keyValueStore

* ****keyValueStore**(id): [KeyValueStoreClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/KeyValueStoreClient.md)

- <https://docs.apify.com/api/v2#/reference/key-value-stores/store-object>

  ***

  #### Parameters

  * ##### id: string

  #### Returns [KeyValueStoreClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/KeyValueStoreClient.md)

### [**](#keyValueStores)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L172)keyValueStores

* ****keyValueStores**(): [KeyValueStoreCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/KeyValueStoreCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/key-value-stores/store-collection>

  ***

  #### Returns [KeyValueStoreCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/KeyValueStoreCollectionClient.md)

### [**](#log)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L191)log

* ****log**(buildOrRunId): [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

- <https://docs.apify.com/api/v2#/reference/logs>

  ***

  #### Parameters

  * ##### buildOrRunId: string

  #### Returns [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

### [**](#requestQueue)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L210)requestQueue

* ****requestQueue**(id, options): [RequestQueueClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RequestQueueClient.md)

- <https://docs.apify.com/api/v2#/reference/request-queues/queue>

  ***

  #### Parameters

  * ##### id: string
  * ##### options: [RequestQueueUserOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueUserOptions.md) = <!-- -->{}

  #### Returns [RequestQueueClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RequestQueueClient.md)

### [**](#requestQueues)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L203)requestQueues

* ****requestQueues**(): [RequestQueueCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RequestQueueCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/request-queues/queue-collection>

  ***

  #### Returns [RequestQueueCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RequestQueueCollectionClient.md)

### [**](#run)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L240)run

* ****run**(id): [RunClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunClient.md)

- <https://docs.apify.com/api/v2#/reference/actor-runs/run-object-and-its-storages>

  ***

  #### Parameters

  * ##### id: string

  #### Returns [RunClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunClient.md)

### [**](#runs)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L230)runs

* ****runs**(): [RunCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/actor-runs/run-collection>

  ***

  #### Returns [RunCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunCollectionClient.md)

### [**](#schedule)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L278)schedule

* ****schedule**(id): [ScheduleClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ScheduleClient.md)

- <https://docs.apify.com/api/v2#/reference/schedules/schedule-object>

  ***

  #### Parameters

  * ##### id: string

  #### Returns [ScheduleClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ScheduleClient.md)

### [**](#schedules)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L271)schedules

* ****schedules**(): [ScheduleCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ScheduleCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/schedules/schedules-collection>

  ***

  #### Returns [ScheduleCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ScheduleCollectionClient.md)

### [**](#setStatusMessage)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L344)setStatusMessage

* ****setStatusMessage**(message, options): Promise\<void>

- #### Parameters

  * ##### message: string
  * ##### optionaloptions: SetStatusMessageOptions

  #### Returns Promise\<void>

### [**](#store)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L340)store

* ****store**(): [StoreCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/StoreCollectionClient.md)

- <https://docs.apify.com/api/v2/#/reference/store>

  ***

  #### Returns [StoreCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/StoreCollectionClient.md)

### [**](#task)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L259)task

* ****task**(id): [TaskClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/TaskClient.md)

- <https://docs.apify.com/api/v2#/reference/actor-tasks/task-object>

  ***

  #### Parameters

  * ##### id: string

  #### Returns [TaskClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/TaskClient.md)

### [**](#tasks)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L252)tasks

* ****tasks**(): [TaskCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/TaskCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/actor-tasks/task-collection>

  ***

  #### Returns [TaskCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/TaskCollectionClient.md)

### [**](#user)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L290)user

* ****user**(id): [UserClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/UserClient.md)

- <https://docs.apify.com/api/v2#/reference/users>

  ***

  #### Parameters

  * ##### id: string = <!-- -->ME\_USER\_NAME\_PLACEHOLDER

  #### Returns [UserClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/UserClient.md)

### [**](#webhook)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L309)webhook

* ****webhook**(id): [WebhookClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookClient.md)

- <https://docs.apify.com/api/v2#/reference/webhooks/webhook-object>

  ***

  #### Parameters

  * ##### id: string

  #### Returns [WebhookClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookClient.md)

### [**](#webhookDispatch)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L328)webhookDispatch

* ****webhookDispatch**(id): [WebhookDispatchClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookDispatchClient.md)

- <https://docs.apify.com/api/v2#/reference/webhook-dispatches/webhook-dispatch-object>

  ***

  #### Parameters

  * ##### id: string

  #### Returns [WebhookDispatchClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookDispatchClient.md)

### [**](#webhookDispatches)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L321)webhookDispatches

* ****webhookDispatches**(): [WebhookDispatchCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookDispatchCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/webhook-dispatches>

  ***

  #### Returns [WebhookDispatchCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookDispatchCollectionClient.md)

### [**](#webhooks)[**](https://github.com/apify/apify-client-js/blob/master/src/apify_client.ts#L302)webhooks

* ****webhooks**(): [WebhookCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/webhooks/webhook-collection>

  ***

  #### Returns [WebhookCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookCollectionClient.md)
