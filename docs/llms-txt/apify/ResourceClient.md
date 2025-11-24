# Source: https://docs.apify.com/api/client/python/reference/class/ResourceClient.md

# ResourceClient<!-- -->

Base class for sub-clients manipulating a single resource.

### Hierarchy

* [BaseClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClient.md)

  * *ResourceClient*

    * [RequestQueueClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClient.md)
    * [DatasetClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClient.md)
    * [UserClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/UserClient.md)
    * [ScheduleClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleClient.md)
    * [WebhookDispatchClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchClient.md)
    * [ActorEnvVarClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarClient.md)
    * [TaskClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClient.md)
    * [ActorClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClient.md)
    * [ActorVersionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClient.md)
    * [WebhookClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClient.md)
    * [KeyValueStoreClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClient.md)
    * [LogClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClient.md)
    * [ActorJobBaseClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorJobBaseClient.md)

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClient.md#__init__)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClient.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClient.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClient.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClient.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClient.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L56)\_\_init\_\_

* ****\_\_init\_\_**(\*, base\_url, root\_client, http\_client, resource\_id, resource\_path, params): None

- Overrides [ResourceClient.\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClient.md#__init__)

  Initialize a new instance.

  ***

  #### Parameters

  * ##### keyword-onlybase\_url: str

    Base URL of the API server.

  * ##### keyword-onlyroot\_client: [ApifyClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClient.md)

    The ApifyClient instance under which this resource client exists.

  * ##### keyword-onlyhttp\_client: [HTTPClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClient.md)

    The HTTPClient instance to be used in this client.

  * ##### optionalkeyword-onlyresource\_id: str | None = <!-- -->None

    ID of the manipulated resource, in case of a single-resource client.

  * ##### keyword-onlyresource\_path: str

    Path to the resource's endpoint on the API server.

  * ##### optionalkeyword-onlyparams: dict | None = <!-- -->None

    Parameters to include in all requests from this client.

  #### Returns None

## Properties<!-- -->[**](#Properties)

### [**](#http_client)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L53)http\_client

**http\_client: [HTTPClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClient.md) | [HTTPClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md)

Inherited from [BaseClient.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClient.md#http_client)

Overrides [\_BaseBaseClient.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#http_client)

### [**](#params)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L17)params

**params: dict

Inherited from [\_BaseBaseClient.params](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#params)

### [**](#resource_id)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L15)resource\_id

**resource\_id: str | None

Inherited from [\_BaseBaseClient.resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#resource_id)

### [**](#root_client)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L54)root\_client

**root\_client: [ApifyClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClient.md) | [ApifyClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md)

Inherited from [BaseClient.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClient.md#root_client)

Overrides [\_BaseBaseClient.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#root_client)

### [**](#url)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/base/base_client.py#L16)url

**url: str

Inherited from [\_BaseBaseClient.url](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#url)
