# Source: https://docs.apify.com/api/client/python/reference/class/ResourceCollectionClient.md

# ResourceCollectionClient<!-- -->

Base class for sub-clients manipulating a resource collection.

### Hierarchy

* [BaseClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClient.md)

  * *ResourceCollectionClient*

    * [RequestQueueCollectionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md)
    * [StoreCollectionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/StoreCollectionClient.md)
    * [DatasetCollectionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetCollectionClient.md)
    * [KeyValueStoreCollectionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreCollectionClient.md)
    * [ScheduleCollectionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleCollectionClient.md)
    * [ActorVersionCollectionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionCollectionClient.md)
    * [WebhookCollectionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClient.md)
    * [ActorCollectionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorCollectionClient.md)
    * [ActorEnvVarCollectionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarCollectionClient.md)
    * [BuildCollectionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildCollectionClient.md)
    * [TaskCollectionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskCollectionClient.md)
    * [RunCollectionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunCollectionClient.md)
    * [WebhookDispatchCollectionClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchCollectionClient.md)

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClient.md#__init__)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClient.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClient.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClient.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClient.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClient.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L56)\_\_init\_\_

* ****\_\_init\_\_**(\*, base\_url, root\_client, http\_client, resource\_id, resource\_path, params): None

- Overrides [ResourceCollectionClient.\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClient.md#__init__)

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

### [**](#http_client)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L53)http\_client

**http\_client: [HTTPClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClient.md) | [HTTPClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md)

Inherited from [BaseClient.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClient.md#http_client)

Overrides [\_BaseBaseClient.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#http_client)

### [**](#params)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L17)params

**params: dict

Inherited from [\_BaseBaseClient.params](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#params)

### [**](#resource_id)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L15)resource\_id

**resource\_id: str | None

Inherited from [\_BaseBaseClient.resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#resource_id)

### [**](#root_client)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L54)root\_client

**root\_client: [ApifyClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClient.md) | [ApifyClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md)

Inherited from [BaseClient.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BaseClient.md#root_client)

Overrides [\_BaseBaseClient.root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#root_client)

### [**](#url)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/base/base_client.py#L16)url

**url: str

Inherited from [\_BaseBaseClient.url](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseBaseClient.md#url)
