# Source: https://docs.apify.com/api/client/python/reference/class/WebhookClientAsync.md

# WebhookClientAsync<!-- -->

Async sub-client for manipulating a single webhook.

### Hierarchy

* [ResourceClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md)
  * *WebhookClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClientAsync.md#__init__)
* [**delete](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClientAsync.md#delete)
* [**dispatches](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClientAsync.md#dispatches)
* [**get](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClientAsync.md#get)
* [**test](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClientAsync.md#test)
* [**update](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClientAsync.md#update)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/webhook.py#L175)\_\_init\_\_

* ****\_\_init\_\_**(\*, base\_url, root\_client, http\_client, resource\_id, resource\_path, params): None

- Overrides [ResourceClientAsync.\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md#__init__)

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

### [**](#delete)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/webhook.py#L238)delete

* **async **delete**(): None

- Delete the webhook.

  <https://docs.apify.com/api/v2#/reference/webhooks/webhook-object/delete-webhook>

  ***

  #### Returns None

### [**](#dispatches)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/webhook.py#L269)dispatches

* ****dispatches**(): [WebhookDispatchCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchCollectionClientAsync.md)

- Get dispatches of the webhook.

  <https://docs.apify.com/api/v2#/reference/webhooks/dispatches-collection/get-collection>

  ***

  #### Returns [WebhookDispatchCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchCollectionClientAsync.md)

### [**](#get)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/webhook.py#L179)get

* **async **get**(): dict | None

- Retrieve the webhook.

  <https://docs.apify.com/api/v2#/reference/webhooks/webhook-object/get-webhook>

  ***

  #### Returns dict | None

### [**](#test)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/webhook.py#L245)test

* **async **test**(): dict | None

- Test a webhook.

  Creates a webhook dispatch with a dummy payload.

  <https://docs.apify.com/api/v2#/reference/webhooks/webhook-test/test-webhook>

  ***

  #### Returns dict | None

### [**](#update)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/webhook.py#L189)update

* **async **update**(\*, event\_types, request\_url, payload\_template, headers\_template, actor\_id, actor\_task\_id, actor\_run\_id, ignore\_ssl\_errors, do\_not\_retry, is\_ad\_hoc): dict

- Update the webhook.

  <https://docs.apify.com/api/v2#/reference/webhooks/webhook-object/update-webhook>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyevent\_types: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[WebhookEventType] | None = <!-- -->None

    List of event types that should trigger the webhook. At least one is required.

  * ##### optionalkeyword-onlyrequest\_url: str | None = <!-- -->None

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

  * ##### optionalkeyword-onlyis\_ad\_hoc: bool | None = <!-- -->None

    Set to True if you want the webhook to be triggered only the first time the condition is fulfilled. Only applicable when actor\_run\_id is filled.

  #### Returns dict

## Properties<!-- -->[**](#Properties)

### [**](#http_client)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L94)http\_client

**http\_client: [HTTPClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClient.md) | [HTTPClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md)

Inherited from [BaseClientAsync.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClientAsync.md#http_client)

Overrides [\_BaseBaseClient.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#http_client)

### [**](#params)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L17)params

**params: dict

Inherited from [\_BaseBaseClient.params](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#params)

### [**](#resource_id)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L15)resource\_id

**resource\_id: str | None

Inherited from [\_BaseBaseClient.resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#resource_id)

### [**](#root_client)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L95)root\_client

**root\_client: [ApifyClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClient.md) | [ApifyClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md)

Inherited from [BaseClientAsync.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClientAsync.md#root_client)

Overrides [\_BaseBaseClient.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#root_client)

### [**](#url)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L16)url

**url: str

Inherited from [\_BaseBaseClient.url](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#url)
