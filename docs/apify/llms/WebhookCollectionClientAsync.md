# Source: https://docs.apify.com/api/client/python/reference/class/WebhookCollectionClientAsync.md

# WebhookCollectionClientAsync<!-- -->

Async sub-client for manipulating webhooks.

### Hierarchy

* [ResourceCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClientAsync.md)
  * *WebhookCollectionClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md#__init__)
* [**create](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md#create)
* [**list](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md#list)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/webhook_collection.py#L102)\_\_init\_\_

* ****\_\_init\_\_**(\*, base\_url, root\_client, http\_client, resource\_id, resource\_path, params): None

- Overrides [ResourceCollectionClientAsync.\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClientAsync.md#__init__)

  Initialize a new instance.

  ***

  #### Parameters

  * ##### keyword-onlybase\_url: str

    Base URL of the API server.

  * ##### keyword-onlyroot\_client: [ApifyClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md)

    The ApifyClientAsync instance under which this resource client exists.

  * ##### keyword-onlyhttp\_client: [HTTPClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md)

    The HTTPClientAsync instance to be used in this client.

  * ##### optionalkeyword-onlyresource\_id: str | None = <!-- -->None

    ID of the manipulated resource, in case of a single-resource client.

  * ##### keyword-onlyresource\_path: str

    Path to the resource's endpoint on the API server.

  * ##### optionalkeyword-onlyparams: dict | None = <!-- -->None

    Parameters to include in all requests from this client.

  #### Returns None

### [**](#create)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/webhook_collection.py#L127)create

* **async **create**(\*, event\_types, request\_url, payload\_template, headers\_template, actor\_id, actor\_task\_id, actor\_run\_id, ignore\_ssl\_errors, do\_not\_retry, idempotency\_key, is\_ad\_hoc): dict

- Create a new webhook.

  You have to specify exactly one out of actor\_id, actor\_task\_id or actor\_run\_id.

  <https://docs.apify.com/api/v2#/reference/webhooks/webhook-collection/create-webhook>

  ***

  #### Parameters

  * ##### keyword-onlyevent\_types: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[WebhookEventType]

    List of event types that should trigger the webhook. At least one is required.

  * ##### keyword-onlyrequest\_url: str

    URL that will be invoked once the webhook is triggered.

  * ##### optionalkeyword-onlypayload\_template: str | None = <!-- -->None

    Specification of the payload that will be sent to request\_url.

  * ##### optionalkeyword-onlyheaders\_template: str | None = <!-- -->None

    Headers that will be sent to the request\_url.

  * ##### optionalkeyword-onlyactor\_id: str | None = <!-- -->None

    Id of the Actor whose runs should trigger the webhook.

  * ##### optionalkeyword-onlyactor\_task\_id: str | None = <!-- -->None

    Id of the Actor task whose runs should trigger the webhook.

  * ##### optionalkeyword-onlyactor\_run\_id: str | None = <!-- -->None

    Id of the Actor run which should trigger the webhook.

  * ##### optionalkeyword-onlyignore\_ssl\_errors: bool | None = <!-- -->None

    Whether the webhook should ignore SSL errors returned by request\_url.

  * ##### optionalkeyword-onlydo\_not\_retry: bool | None = <!-- -->None

    Whether the webhook should retry sending the payload to request\_url upon failure.

  * ##### optionalkeyword-onlyidempotency\_key: str | None = <!-- -->None

    A unique identifier of a webhook. You can use it to ensure that you won't create the same webhook multiple times.

  * ##### optionalkeyword-onlyis\_ad\_hoc: bool | None = <!-- -->None

    Set to True if you want the webhook to be triggered only the first time the condition is fulfilled. Only applicable when actor\_run\_id is filled.

  #### Returns dict

### [**](#list)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/webhook_collection.py#L106)list

* **async **list**(\*, limit, offset, desc): [ListPage](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md)\[dict]

- List the available webhooks.

  <https://docs.apify.com/api/v2#/reference/webhooks/webhook-collection/get-list-of-webhooks>

  ***

  #### Parameters

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

    How many webhooks to retrieve.

  * ##### optionalkeyword-onlyoffset: int | None = <!-- -->None

    What webhook to include as first when retrieving the list.

  * ##### optionalkeyword-onlydesc: bool | None = <!-- -->None

    Whether to sort the webhooks in descending order based on their date of creation.

  #### Returns [ListPage](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md)\[dict]

## Properties<!-- -->[**](#Properties)

### [**](#http_client)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L94)http\_client

**http\_client: [HTTPClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClient.md) | [HTTPClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md)

Inherited from [BaseClientAsync.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClientAsync.md#http_client)

Overrides [\_BaseBaseClient.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#http_client)

### [**](#params)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L17)params

**params: dict

Inherited from [\_BaseBaseClient.params](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#params)

### [**](#resource_id)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L15)resource\_id

**resource\_id: str | None

Inherited from [\_BaseBaseClient.resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#resource_id)

### [**](#root_client)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L95)root\_client

**root\_client: [ApifyClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClient.md) | [ApifyClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md)

Inherited from [BaseClientAsync.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClientAsync.md#root_client)

Overrides [\_BaseBaseClient.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#root_client)

### [**](#url)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L16)url

**url: str

Inherited from [\_BaseBaseClient.url](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#url)
