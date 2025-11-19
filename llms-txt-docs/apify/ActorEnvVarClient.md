# Source: https://docs.apify.com/api/client/python/reference/class/ActorEnvVarClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorEnvVarClient.md

# ActorEnvVarClient<!-- -->

### Hierarchy

* ResourceClient
  * *ActorEnvVarClient*

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

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor_env_var.ts#L36)delete

* ****delete**(): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/actors/environment-variable-object/delete-environment-variable>

  ***

  #### Returns Promise\<void>

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor_env_var.ts#L21)get

* ****get**(): Promise\<undefined | [ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md)>

- <https://docs.apify.com/api/v2#/reference/actors/environment-variable-object/get-environment-variable>

  ***

  #### Returns Promise\<undefined | [ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md)>

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor_env_var.ts#L28)update

* ****update**(actorEnvVar): Promise<[ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md)>

- <https://docs.apify.com/api/v2#/reference/actors/environment-variable-object/update-environment-variable>

  ***

  #### Parameters

  * ##### actorEnvVar: [ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md)

  #### Returns Promise<[ActorEnvironmentVariable](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorEnvironmentVariable.md)>
