# Source: https://docs.apify.com/api/client/python/reference/class/WebhookClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/WebhookClient.md

# WebhookClient<!-- -->

Client for managing a specific webhook.

Webhooks allow you to receive notifications when specific events occur in your Actors or tasks. This client provides methods to get, update, delete, and test webhooks, as well as retrieve webhook dispatches.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const webhookClient = client.webhook('my-webhook-id');

  // Get webhook details
  const webhook = await webhookClient.get();

  // Update webhook
  await webhookClient.update({
    isEnabled: true,
    eventTypes: ['ACTOR.RUN.SUCCEEDED'],
    requestUrl: 'https://example.com/webhook'
  });

  // Test webhook
  await webhookClient.test();
  ```

* **@see**

  <https://docs.apify.com/platform/integrations/webhooks>

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

### [**](#delete)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L80)delete

* ****delete**(): Promise\<void>

- Deletes the webhook.

  * **@see**

    <https://docs.apify.com/api/v2/webhook-delete>

  ***

  #### Returns Promise\<void>

### [**](#dispatches)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L113)dispatches

* ****dispatches**(): [WebhookDispatchCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookDispatchCollectionClient.md)

- Returns a client for the dispatches of this webhook.

  * **@see**

    <https://docs.apify.com/api/v2/webhook-webhook-dispatches-get>

  ***

  #### Returns [WebhookDispatchCollectionClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/WebhookDispatchCollectionClient.md)

  A client for the webhook's dispatches.

### [**](#get)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L58)get

* ****get**(): Promise\<undefined | [Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md)>

- Retrieves the webhook.

  * **@see**

    <https://docs.apify.com/api/v2/webhook-get>

  ***

  #### Returns Promise\<undefined | [Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md)>

  The webhook object, or `undefined` if it does not exist.

### [**](#test)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L90)test

* ****test**(): Promise\<undefined | [WebhookDispatch](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatch.md)>

- Tests the webhook by dispatching a test event.

  * **@see**

    <https://docs.apify.com/api/v2/webhook-test-post>

  ***

  #### Returns Promise\<undefined | [WebhookDispatch](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatch.md)>

  The webhook dispatch object, or `undefined` if the test fails.

### [**](#update)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook.ts#L69)update

* ****update**(newFields): Promise<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md)>

- Updates the webhook with the specified fields.

  * **@see**

    <https://docs.apify.com/api/v2/webhook-put>

  ***

  #### Parameters

  * ##### newFields: [WebhookUpdateData](https://docs.apify.com/api/client/js/api/client/js/reference.md#WebhookUpdateData)

    Fields to update.

  #### Returns Promise<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md)>

  The updated webhook object.
