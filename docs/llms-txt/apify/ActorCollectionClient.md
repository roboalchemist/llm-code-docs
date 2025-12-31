# Source: https://docs.apify.com/api/client/python/reference/class/ActorCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorCollectionClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/ActorCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorCollectionClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/ActorCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorCollectionClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/ActorCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/ActorCollectionClient.md

# ActorCollectionClient<!-- -->

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

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L35)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceCollectionClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L27)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceCollectionClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L37)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceCollectionClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L23)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceCollectionClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L39)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceCollectionClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L29)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceCollectionClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L31)inheritedresourcePath

**resourcePath: string

Inherited from ResourceCollectionClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L25)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceCollectionClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/master/src/base/api_client.ts#L33)inheritedurl

**url: string

Inherited from ResourceCollectionClient.url

## Methods<!-- -->[**](#Methods)

### [**](#create)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor_collection.ts#L41)create

* ****create**(actor): Promise<[Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md)>

- <https://docs.apify.com/api/v2#/reference/actors/actor-collection/create-actor>

  ***

  #### Parameters

  * ##### actor: [ActorCollectionCreateOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorCollectionCreateOptions.md)

  #### Returns Promise<[Actor](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Actor.md)>

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/actor_collection.ts#L23)list

* ****list**(options): Promise<[ActorCollectionListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorCollectionListResult)>

- <https://docs.apify.com/api/v2#/reference/actors/actor-collection/get-list-of-actors>

  ***

  #### Parameters

  * ##### options: [ActorCollectionListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/ActorCollectionListOptions.md) = <!-- -->{}

  #### Returns Promise<[ActorCollectionListResult](https://docs.apify.com/api/client/js/api/client/js/reference.md#ActorCollectionListResult)>
