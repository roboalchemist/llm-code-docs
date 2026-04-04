# Source: https://docs.apify.com/api/client/python/reference/class/WebhookCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/WebhookCollectionClient.md

# WebhookCollectionClient<!-- -->

Client for managing the collection of Webhooks.

Webhooks allow you to receive notifications when specific events occur in your Actors or tasks. This client provides methods to list and create webhooks for specific Actors or tasks.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });

  // List webhooks for an Actor
  const actorWebhooksClient = client.actor('my-actor-id').webhooks();
  const { items } = await actorWebhooksClient.list();

  // Create a webhook
  const newWebhook = await actorWebhooksClient.create({
    eventTypes: ['ACTOR.RUN.SUCCEEDED'],
    requestUrl: 'https://example.com/webhook'
  });
  ```

* **@see**

  <https://docs.apify.com/platform/integrations/webhooks>

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

### [**](#apifyClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L36)inheritedapifyClient

**apifyClient: [ApifyClient](https://docs.apify.com/api/client/js/api/client/js/reference/class/ApifyClient.md)

Inherited from ResourceCollectionClient.apifyClient

### [**](#baseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L28)inheritedbaseUrl

**baseUrl: string

Inherited from ResourceCollectionClient.baseUrl

### [**](#httpClient)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L38)inheritedhttpClient

**httpClient: HttpClient

Inherited from ResourceCollectionClient.httpClient

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L24)optionalinheritedid

**id?

<!-- -->

: string

Inherited from ResourceCollectionClient.id

### [**](#params)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L40)optionalinheritedparams

**params?

<!-- -->

: Record\<string, unknown>

Inherited from ResourceCollectionClient.params

### [**](#publicBaseUrl)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L30)inheritedpublicBaseUrl

**publicBaseUrl: string

Inherited from ResourceCollectionClient.publicBaseUrl

### [**](#resourcePath)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L32)inheritedresourcePath

**resourcePath: string

Inherited from ResourceCollectionClient.resourcePath

### [**](#safeId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L26)optionalinheritedsafeId

**safeId?

<!-- -->

: string

Inherited from ResourceCollectionClient.safeId

### [**](#url)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/base/api_client.ts#L34)inheritedurl

**url: string

Inherited from ResourceCollectionClient.url

## Methods<!-- -->[**](#Methods)

### [**](#create)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_collection.ts#L85)create

* ****create**(webhook): Promise<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md)>

- Creates a new webhook.

  * **@see**

    <https://docs.apify.com/api/v2/webhooks-post>

  ***

  #### Parameters

  * ##### optionalwebhook: [WebhookUpdateData](https://docs.apify.com/api/client/js/api/client/js/reference.md#WebhookUpdateData)

    The webhook data.

  #### Returns Promise<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md)>

  The created webhook object.

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_collection.ts#L63)list

* ****list**(options): PaginatedIterator\<Omit<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md), payloadTemplate | headersTemplate>>

- Lists all Webhooks.

  Awaiting the return value (as you would with a Promise) will result in a single API call. The amount of fetched items in a single API call is limited.

  ```
  const paginatedList = await client.list(options);
  ```

  Asynchronous iteration is also supported. This will fetch additional pages if needed until all items are retrieved.

  ```
  for await (const singleItem of client.list(options)) {...}
  ```

  * **@see**

    <https://docs.apify.com/api/v2/webhooks-get>

  ***

  #### Parameters

  * ##### options: [WebhookCollectionListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookCollectionListOptions.md) = <!-- -->{}

    Pagination and sorting options.

  #### Returns PaginatedIterator\<Omit<[Webhook](https://docs.apify.com/api/client/js/api/client/js/reference/interface/Webhook.md), payloadTemplate | headersTemplate>>

  A paginated iterator of webhooks.
