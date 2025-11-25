# Source: https://docs.apify.com/api/client/python/reference/class/ActorVersionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorVersionClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/ActorVersionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorVersionClient.md

# ActorVersionClient<!-- -->

### Hierarchy

* ResourceClient
  * *ActorVersionClient*

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
* [**envVar](#envVar)
* [**envVars](#envVars)
* [**get](#get)
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

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor_version.ts#L38)delete

* ****delete**(): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/actors/version-object/delete-version>

  ***

  #### Returns Promise\<void>

### [**](#envVar)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor_version.ts#L45)envVar

* ****envVar**(envVarName): [ActorEnvVarClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorEnvVarClient.md)

- TODO: <https://docs.apify.com/api/v2#/reference/actors/env-var-object>

  ***

  #### Parameters

  * ##### envVarName: string

  #### Returns [ActorEnvVarClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorEnvVarClient.md)

### [**](#envVars)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor_version.ts#L58)envVars

* ****envVars**(): [ActorEnvVarCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorEnvVarCollectionClient.md)

- TODO: <https://docs.apify.com/api/v2#/reference/actors/env-var-collection>

  ***

  #### Returns [ActorEnvVarCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ActorEnvVarCollectionClient.md)

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor_version.ts#L22)get

* ****get**(): Promise\<undefined | [FinalActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#FinalActorVersion)>

- <https://docs.apify.com/api/v2#/reference/actors/version-object/get-version>

  ***

  #### Returns Promise\<undefined | [FinalActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#FinalActorVersion)>

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor_version.ts#L29)update

* ****update**(newFields): Promise<[FinalActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#FinalActorVersion)>

- <https://docs.apify.com/api/v2#/reference/actors/version-object/update-version>

  ***

  #### Parameters

  * ##### newFields: [ActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorVersion)

  #### Returns Promise<[FinalActorVersion](https://docs.apify.com/api/client/js/api/client/js/reference.md#FinalActorVersion)>
