# Source: https://docs.apify.com/api/client/python/reference/class/WebhookDispatchCollectionClientAsync.md

# WebhookDispatchCollectionClientAsync<!-- -->

Async sub-client for listing webhook dispatches.

### Hierarchy

* [ResourceCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClientAsync.md)
  * *WebhookDispatchCollectionClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchCollectionClientAsync.md#__init__)
* [**list](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchCollectionClientAsync.md#list)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchCollectionClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchCollectionClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchCollectionClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchCollectionClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchCollectionClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/webhook_dispatch_collection.py#L43)\_\_init\_\_

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

### [**](#list)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/webhook_dispatch_collection.py#L47)list

* **async **list**(\*, limit, offset, desc): [ListPage](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md)\[dict]

- List all webhook dispatches of a user.

  <https://docs.apify.com/api/v2#/reference/webhook-dispatches/webhook-dispatches-collection/get-list-of-webhook-dispatches>

  ***

  #### Parameters

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

    How many webhook dispatches to retrieve.

  * ##### optionalkeyword-onlyoffset: int | None = <!-- -->None

    What webhook dispatch to include as first when retrieving the list.

  * ##### optionalkeyword-onlydesc: bool | None = <!-- -->None

    Whether to sort the webhook dispatches in descending order based on the date of their creation.

  #### Returns [ListPage](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md)\[dict]

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
