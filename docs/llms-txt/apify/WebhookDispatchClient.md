# Source: https://docs.apify.com/api/client/python/reference/class/WebhookDispatchClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/WebhookDispatchClient.md

# WebhookDispatchClient<!-- -->

Client for managing a specific webhook dispatch.

Webhook dispatches represent individual notifications sent by webhooks. This client provides methods to retrieve details about a specific dispatch.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const webhookClient = client.webhook('my-webhook-id');

  // Get a specific dispatch
  const dispatchClient = webhookClient.dispatches().get('dispatch-id');
  const dispatch = await dispatchClient.get();
  ```

* **@see**

  <https://docs.apify.com/platform/integrations/webhooks>

### Hierarchy

* ResourceClient
  * *WebhookDispatchClient*

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

* [**get](#get)

## Properties<!-- -->[**](#Properties)

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L36)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L28)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L38)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L24)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L40)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L30)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L32)inheritedresourcePath

**resourcePath: string

Inherited from ResourceClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L26)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L34)inheritedurl

**url: string

Inherited from ResourceClient.url

## Methods<!-- -->[**](#Methods)

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_dispatch.ts#L40)get

* ****get**(): Promise\<undefined | [WebhookDispatch](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatch.md)>

- Retrieves the webhook dispatch.

  * **@see**

    <https://docs.apify.com/api/v2/webhook-dispatch-get>

  ***

  #### Returns Promise\<undefined | [WebhookDispatch](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatch.md)>

  The webhook dispatch object, or `undefined` if it does not exist.
