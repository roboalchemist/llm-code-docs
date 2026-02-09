# Source: https://docs.apify.com/api/client/python/reference/class/WebhookDispatchCollectionClient.md

# Source: https://docs.apify.com/api/client/js/reference/class/WebhookDispatchCollectionClient.md

# WebhookDispatchCollectionClient<!-- -->

Client for managing the collection of webhook dispatches.

Webhook dispatches represent individual notifications sent by a webhook. This client provides methods to list all dispatches for a specific webhook.

* **@example**

  ```
  const client = new ApifyClient({ token: 'my-token' });
  const webhookClient = client.webhook('my-webhook-id');

  // List all dispatches for this webhook
  const dispatchesClient = webhookClient.dispatches();
  const { items } = await dispatchesClient.list();
  ```

* **@see**

  <https://docs.apify.com/platform/integrations/webhooks>

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

### [**](#list)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_dispatch_collection.ts#L57)list

* ****list**(options): PaginatedIterator<[WebhookDispatch](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatch.md)>

- Lists all webhook dispatches.

  Awaiting the return value (as you would with a Promise) will result in a single API call. The amount of fetched items in a single API call is limited.

  ```
  const paginatedList = await client.list(options);
  ```

  Asynchronous iteration is also supported. This will fetch additional pages if needed until all items are retrieved.

  ```
  for await (const singleItem of client.list(options)) {...}
  ```

  * **@see**

    <https://docs.apify.com/api/v2/webhook-dispatches-get>

  ***

  #### Parameters

  * ##### options: [WebhookDispatchCollectionListOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatchCollectionListOptions.md) = <!-- -->{}

    Pagination and sorting options.

  #### Returns PaginatedIterator<[WebhookDispatch](https://docs.apify.com/api/client/js/api/client/js/reference/interface/WebhookDispatch.md)>

  A paginated iterator of webhook dispatches.
