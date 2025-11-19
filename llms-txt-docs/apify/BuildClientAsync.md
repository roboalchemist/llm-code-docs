# Source: https://docs.apify.com/api/client/python/reference/class/BuildClientAsync.md

# BuildClientAsync<!-- -->

Async sub-client for manipulating a single Actor build.

### Hierarchy

* [ActorJobBaseClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorJobBaseClientAsync.md)
  * *BuildClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md#__init__)
* [**abort](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md#abort)
* [**delete](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md#delete)
* [**get](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md#get)
* [**get\_open\_api\_definition](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md#get_open_api_definition)
* [**log](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md#log)
* [**wait\_for\_finish](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md#wait_for_finish)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/build.py#L88)\_\_init\_\_

* ****\_\_init\_\_**(\*, base\_url, root\_client, http\_client, resource\_id, resource\_path, params): None

- Overrides [ActorJobBaseClientAsync.\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorJobBaseClientAsync.md#__init__)

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

### [**](#abort)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/build.py#L102)abort

* **async **abort**(): dict

- Abort the Actor build which is starting or currently running and return its details.

  <https://docs.apify.com/api/v2#/reference/actor-builds/abort-build/abort-build>

  ***

  #### Returns dict

### [**](#delete)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/build.py#L112)delete

* **async **delete**(): None

- Delete the build.

  <https://docs.apify.com/api/v2#/reference/actor-builds/delete-build/delete-build>

  ***

  #### Returns None

### [**](#get)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/build.py#L92)get

* **async **get**(): dict | None

- Return information about the Actor build.

  <https://docs.apify.com/api/v2#/reference/actor-builds/build-object/get-build>

  ***

  #### Returns dict | None

### [**](#get_open_api_definition)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/build.py#L119)get\_open\_api\_definition

* **async **get\_open\_api\_definition**(): dict | None

- Return OpenAPI definition of the Actor's build.

  <https://docs.apify.com/api/v2/actor-build-openapi-json-get>

  ***

  #### Returns dict | None

### [**](#log)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/build.py#L148)log

* ****log**(): [LogClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md)

- Get the client for the log of the Actor build.

  <https://docs.apify.com/api/v2/#/reference/actor-builds/build-log/get-log>

  ***

  #### Returns [LogClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md)

### [**](#wait_for_finish)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/build.py#L136)wait\_for\_finish

* **async **wait\_for\_finish**(\*, wait\_secs): dict | None

- Wait synchronously until the build finishes or the server times out.

  ***

  #### Parameters

  * ##### optionalkeyword-onlywait\_secs: int | None = <!-- -->None

    How long does the client wait for build to finish. None for indefinite.

  #### Returns dict | None

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
