# Source: https://docs.apify.com/api/client/python/reference/class/WebhookClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/WebhookClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/WebhookClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/WebhookClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/WebhookClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/WebhookClient.md

# Source: https://docs.apify.com/api/client/python/reference/class/WebhookClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/WebhookClient.md

# WebhookClient<!-- -->

### Hierarchy

* ResourceClient
  * *WebhookClient*

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
* [**dispatches](#dispatches)
* [**get](#get)
* [**test](#test)
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

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook.ts#L43)delete

* ****delete**(): Promise\<void>

- <https://docs.apify.com/api/v2#/reference/webhooks/webhook-object/delete-webhook>

  ***

  #### Returns Promise\<void>

### [**](#dispatches)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook.ts#L70)dispatches

* ****dispatches**(): [WebhookDispatchCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookDispatchCollectionClient.md)

- <https://docs.apify.com/api/v2#/reference/webhooks/dispatches-collection>

  ***

  #### Returns [WebhookDispatchCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookDispatchCollectionClient.md)

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook.ts#L27)get

* ****get**(): Promise\<undefined | [Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md)>

- <https://docs.apify.com/api/v2#/reference/webhooks/webhook-object/get-webhook>

  ***

  #### Returns Promise\<undefined | [Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md)>

### [**](#test)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook.ts#L50)test

* ****test**(): Promise\<undefined | [WebhookDispatch](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatch.md)>

- <https://docs.apify.com/api/v2#/reference/webhooks/webhook-test/test-webhook>

  ***

  #### Returns Promise\<undefined | [WebhookDispatch](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatch.md)>

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/webhook.ts#L34)update

* ****update**(newFields): Promise<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md)>

- <https://docs.apify.com/api/v2#/reference/webhooks/webhook-object/update-webhook>

  ***

  #### Parameters

  * ##### newFields: [WebhookUpdateData](https://docs.apify.com/api/client/js/api/client/js/reference.md#WebhookUpdateData)

  #### Returns Promise<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md)>
