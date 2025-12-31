# Source: https://docs.apify.com/api/client/python/reference/class/RunClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RunClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/RunClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RunClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/RunClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RunClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/RunClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/RunClient.md

# RunClient<!-- -->

### Hierarchy

* ResourceClient
  * *RunClient*

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

* [**abort](#abort)
* [**charge](#charge)
* [**dataset](#dataset)
* [**delete](#delete)
* [**get](#get)
* [**keyValueStore](#keyValueStore)
* [**log](#log)
* [**metamorph](#metamorph)
* [**reboot](#reboot)
* [**requestQueue](#requestQueue)
* [**resurrect](#resurrect)
* [**update](#update)
* [**waitForFinish](#waitForFinish)

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

### [**](#abort)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L46)abort

* ****abort**(options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- <https://docs.apify.com/api/v2#/reference/actor-runs/abort-run/abort-run>

  ***

  #### Parameters

  * ##### options: [RunAbortOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunAbortOptions.md) = <!-- -->{}

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

### [**](#charge)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L160)charge

* ****charge**(options): Promise\<ApifyResponse\<Record\<string, never>>>

- <https://docs.apify.com/api/v2#/reference/actor-runs/charge-events-in-run>

  ***

  #### Parameters

  * ##### options: [RunChargeOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunChargeOptions.md)

  #### Returns Promise\<ApifyResponse\<Record\<string, never>>>

### [**](#dataset)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L220)dataset

* ****dataset**(): [DatasetClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/DatasetClient.md)\<Record\<string | number, unknown>>

- <https://docs.apify.com/api/v2#/reference/actor-runs/run-object-and-its-storages>

  This also works through `actorClient.lastRun().dataset()`. <https://docs.apify.com/api/v2#/reference/actors/last-run-object-and-its-storages>

  ***

  #### Returns [DatasetClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/DatasetClient.md)\<Record\<string | number, unknown>>

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L66)delete

* ****delete**(): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/actor-runs/delete-run/delete-run>

  ***

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L32)get

* ****get**(options): Promise\<undefined | [ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- <https://docs.apify.com/api/v2#/reference/actor-runs/run-object/get-run>

  ***

  #### Parameters

  * ##### options: [RunGetOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunGetOptions.md) = <!-- -->{}

  #### Returns Promise\<undefined | [ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

### [**](#keyValueStore)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L234)keyValueStore

* ****keyValueStore**(): [KeyValueStoreClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/KeyValueStoreClient.md)

- <https://docs.apify.com/api/v2#/reference/actor-runs/run-object-and-its-storages>

  This also works through `actorClient.lastRun().keyValueStore()`. <https://docs.apify.com/api/v2#/reference/actors/last-run-object-and-its-storages>

  ***

  #### Returns [KeyValueStoreClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/KeyValueStoreClient.md)

### [**](#log)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L262)log

* ****log**(): [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

- <https://docs.apify.com/api/v2#/reference/actor-runs/run-object-and-its-storages>

  This also works through `actorClient.lastRun().log()`. <https://docs.apify.com/api/v2#/reference/actors/last-run-object-and-its-storages>

  ***

  #### Returns [LogClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/LogClient.md)

### [**](#metamorph)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L73)metamorph

* ****metamorph**(targetActorId, input, options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- <https://docs.apify.com/api/v2#/reference/actor-runs/metamorph-run/metamorph-run>

  ***

  #### Parameters

  * ##### targetActorId: string
  * ##### input: unknown
  * ##### options: [RunMetamorphOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunMetamorphOptions.md) = <!-- -->{}

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

### [**](#reboot)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L116)reboot

* ****reboot**(): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- <https://docs.apify.com/api/v2#/reference/actor-runs/reboot-run/reboot-run>

  ***

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

### [**](#requestQueue)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L248)requestQueue

* ****requestQueue**(): [RequestQueueClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RequestQueueClient.md)

- <https://docs.apify.com/api/v2#/reference/actor-runs/run-object-and-its-storages>

  This also works through `actorClient.lastRun().requestQueue()`. <https://docs.apify.com/api/v2#/reference/actors/last-run-object-and-its-storages>

  ***

  #### Returns [RequestQueueClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RequestQueueClient.md)

### [**](#resurrect)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L135)resurrect

* ****resurrect**(options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- <https://docs.apify.com/api/v2#/reference/actor-runs/resurrect-run/resurrect-run>

  ***

  #### Parameters

  * ##### options: [RunResurrectOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunResurrectOptions.md) = <!-- -->{}

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L126)update

* ****update**(newFields): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- #### Parameters

  * ##### newFields: [RunUpdateOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunUpdateOptions.md)

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

### [**](#waitForFinish)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L203)waitForFinish

* ****waitForFinish**(options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Returns a promise that resolves with the finished Run object when the provided actor run finishes or with the unfinished Run object when the `waitSecs` timeout lapses. The promise is NOT rejected based on run status. You can inspect the `status` property of the Run object to find out its status.

  The difference between this function and the `waitForFinish` parameter of the `get` method is the fact that this function can wait indefinitely. Its use is preferable to the `waitForFinish` parameter alone, which it uses internally.

  This is useful when you need to chain actor executions. Similar effect can be achieved by using webhooks, so be sure to review which technique fits your use-case better.

  ***

  #### Parameters

  * ##### options: [RunWaitForFinishOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RunWaitForFinishOptions.md) = <!-- -->{}

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>
