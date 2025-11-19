# Source: https://docs.apify.com/api/client/python/reference/class/ActorClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorClient.md

# ActorClient<!-- -->

### Hierarchy

* ResourceClient
  * *ActorClient*

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

* [**build](#build)
* [**builds](#builds)
* [**call](#call)
* [**defaultBuild](#defaultBuild)
* [**delete](#delete)
* [**get](#get)
* [**lastRun](#lastRun)
* [**runs](#runs)
* [**start](#start)
* [**update](#update)
* [**version](#version)
* [**versions](#versions)
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

### [**](#build)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L160)build

* ****build**(versionNumber, options): Promise<[Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

- <https://docs.apify.com/api/v2#/reference/actors/build-collection/build-actor>

  ***

  #### Parameters

  * ##### versionNumber: string
  * ##### options: [ActorBuildOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorBuildOptions.md) = <!-- -->{}

  #### Returns Promise<[Build](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Build.md)>

### [**](#builds)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L229)builds

* ****builds**(): [BuildCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/actors/build-collection>

  ***

  #### Returns [BuildCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildCollectionClient.md)

### [**](#call)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L128)call

* ****call**(input, options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Starts an actor and waits for it to finish before returning the Run object. It waits indefinitely, unless the `waitSecs` option is provided. <https://docs.apify.com/api/v2#/reference/actors/run-collection/run-actor>

  ***

  #### Parameters

  * ##### optionalinput: unknown
  * ##### options: [ActorCallOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorCallOptions.md) = <!-- -->{}

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

### [**](#defaultBuild)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L187)defaultBuild

* ****defaultBuild**(options): Promise<[BuildClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildClient.md)>

- <https://docs.apify.com/api/v2/act-build-default-get>

  ***

  #### Parameters

  * ##### options: [BuildClientGetOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/BuildClientGetOptions.md) = <!-- -->{}

  #### Returns Promise<[BuildClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/BuildClient.md)>

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L51)delete

* ****delete**(): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/actors/actor-object/delete-actor>

  ***

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L35)get

* ****get**(): Promise\<undefined | [Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md)>

- <https://docs.apify.com/api/v2#/reference/actors/actor-object/get-actor>

  ***

  #### Returns Promise\<undefined | [Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md)>

### [**](#lastRun)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L208)lastRun

* ****lastRun**(options): [RunClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunClient.md)

- <https://docs.apify.com/api/v2#/reference/actors/last-run-object-and-its-storages>

  ***

  #### Parameters

  * ##### options: [ActorLastRunOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorLastRunOptions.md) = <!-- -->{}

  #### Returns [RunClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunClient.md)

### [**](#runs)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L240)runs

* ****runs**(): [RunCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/actors/run-collection>

  ***

  #### Returns [RunCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/RunCollectionClient.md)

### [**](#start)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L59)start

* ****start**(input, options): Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

- Starts an actor and immediately returns the Run object. <https://docs.apify.com/api/v2#/reference/actors/run-collection/run-actor>

  ***

  #### Parameters

  * ##### optionalinput: unknown
  * ##### options: [ActorStartOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorStartOptions.md) = <!-- -->{}

  #### Returns Promise<[ActorRun](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorRun.md)>

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L42)update

* ****update**(newFields): Promise<[Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md)>

- <https://docs.apify.com/api/v2#/reference/actors/actor-object/update-actor>

  ***

  #### Parameters

  * ##### newFields: Partial\<Pick<[Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md), name | description | isPublic | isDeprecated | seoTitle | seoDescription | title | restartOnError | versions | categories | defaultRunOptions | actorStandby>>

  #### Returns Promise<[Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md)>

### [**](#version)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L251)version

* ****version**(versionNumber): [ActorVersionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorVersionClient.md)

- <https://docs.apify.com/api/v2#/reference/actors/version-object>

  ***

  #### Parameters

  * ##### versionNumber: string

  #### Returns [ActorVersionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorVersionClient.md)

### [**](#versions)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L264)versions

* ****versions**(): [ActorVersionCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorVersionCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/actors/version-collection>

  ***

  #### Returns [ActorVersionCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorVersionCollectionClient.md)

### [**](#webhooks)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor.ts#L272)webhooks

* ****webhooks**(): [WebhookCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/actors/webhook-collection>

  ***

  #### Returns [WebhookCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookCollectionClient.md)
