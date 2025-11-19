# Source: https://docs.apify.com/api/client/python/reference/class/WebhookCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/WebhookCollectionClient.md

# WebhookCollectionClient<!-- -->

### Hierarchy

* ResourceCollectionClient
  * *WebhookCollectionClient*

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

### [**](#create)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook_collection.ts#L40)create

* ****create**(webhook): Promise<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md)>

- <https://docs.apify.com/api/v2#/reference/webhooks/webhook-collection/create-webhook>

  ***

  #### Parameters

  * ##### optionalwebhook: [WebhookUpdateData](https://docs.apify.com/api/client/js/api/client/js/reference.md#WebhookUpdateData)

  #### Returns Promise<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md)>

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook_collection.ts#L22)list

* ****list**(options): Promise<[PaginatedList](https://docs.apify.com/api/client/js/api/client/js/reference/interface/PaginatedList.md)\<Omit<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md), payloadTemplate | headersTemplate>>>

- <https://docs.apify.com/api/v2#/reference/webhooks/webhook-collection/get-list-of-webhooks>

  ***

  #### Parameters

  * ##### options: [WebhookCollectionListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookCollectionListOptions.md) = <!-- -->{}

  #### Returns Promise<[PaginatedList](https://docs.apify.com/api/client/js/api/client/js/reference/interface/PaginatedList.md)\<Omit<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md), payloadTemplate | headersTemplate>>>
