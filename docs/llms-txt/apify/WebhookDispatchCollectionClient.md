# Source: https://docs.apify.com/api/client/python/reference/class/WebhookDispatchCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/WebhookDispatchCollectionClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/WebhookDispatchCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/WebhookDispatchCollectionClient.md

# WebhookDispatchCollectionClient<!-- -->

### Hierarchy

* ResourceCollectionClient
  * *WebhookDispatchCollectionClient*

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

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook_dispatch_collection.ts#L22)list

* ****list**(options): Promise<[PaginatedList](https://docs.apify.com/api/client/js/api/client/js/reference/interface/PaginatedList.md)<[WebhookDispatch](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatch.md)>>

- <https://docs.apify.com/api/v2#/reference/webhook-dispatches/webhook-dispatches-collection/get-list-of-webhook-dispatches>

  ***

  #### Parameters

  * ##### options: [WebhookDispatchCollectionListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatchCollectionListOptions.md) = <!-- -->{}

  #### Returns Promise<[PaginatedList](https://docs.apify.com/api/client/js/api/client/js/reference/interface/PaginatedList.md)<[WebhookDispatch](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatch.md)>>
