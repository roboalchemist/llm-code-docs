# Source: https://docs.apify.com/api/client/python/reference/class/ResourceCollectionClientAsync.md

# ResourceCollectionClientAsync<!-- -->

Base class for async sub-clients manipulating a resource collection.

### Hierarchy

* [BaseClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClientAsync.md)

  * *ResourceCollectionClientAsync*

    * [RequestQueueCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClientAsync.md)
    * [StoreCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/StoreCollectionClientAsync.md)
    * [DatasetCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetCollectionClientAsync.md)
    * [KeyValueStoreCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreCollectionClientAsync.md)
    * [ScheduleCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleCollectionClientAsync.md)
    * [ActorVersionCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionCollectionClientAsync.md)
    * [WebhookCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md)
    * [ActorCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorCollectionClientAsync.md)
    * [ActorEnvVarCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarCollectionClientAsync.md)
    * [BuildCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildCollectionClientAsync.md)
    * [TaskCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskCollectionClientAsync.md)
    * [RunCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunCollectionClientAsync.md)
    * [WebhookDispatchCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchCollectionClientAsync.md)

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClientAsync.md#__init__)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L97)\_\_init\_\_

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
