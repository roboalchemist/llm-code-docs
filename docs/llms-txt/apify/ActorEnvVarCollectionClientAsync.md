# Source: https://docs.apify.com/api/client/python/reference/class/ActorEnvVarCollectionClientAsync.md

# ActorEnvVarCollectionClientAsync<!-- -->

Async sub-client for manipulating actor env vars.

### Hierarchy

* [ResourceCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClientAsync.md)
  * *ActorEnvVarCollectionClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarCollectionClientAsync.md#__init__)
* [**create](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarCollectionClientAsync.md#create)
* [**list](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarCollectionClientAsync.md#list)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarCollectionClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarCollectionClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarCollectionClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarCollectionClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarCollectionClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor_env_var_collection.py#L61)\_\_init\_\_

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

### [**](#create)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor_env_var_collection.py#L75)create

* **async **create**(\*, is\_secret, name, value): dict

- Create a new actor environment variable.

  <https://docs.apify.com/api/v2#/reference/actors/environment-variable-collection/create-environment-variable>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyis\_secret: bool | None = <!-- -->None

    Whether the environment variable is secret or not.

  * ##### keyword-onlyname: str

    The name of the environment variable.

  * ##### keyword-onlyvalue: str

    The value of the environment variable.

  #### Returns dict

### [**](#list)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor_env_var_collection.py#L65)list

* **async **list**(): [ListPage](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md)\[dict]

- List the available actor environment variables.

  <https://docs.apify.com/api/v2#/reference/actors/environment-variable-collection/get-list-of-environment-variables>

  ***

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
