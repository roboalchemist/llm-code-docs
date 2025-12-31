# Source: https://docs.apify.com/api/client/python/reference/class/ActorVersionClientAsync.md

# ActorVersionClientAsync<!-- -->

Async sub-client for manipulating a single Actor version.

### Hierarchy

* [ResourceClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md)
  * *ActorVersionClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClientAsync.md#__init__)
* [**delete](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClientAsync.md#delete)
* [**env\_var](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClientAsync.md#env_var)
* [**env\_vars](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClientAsync.md#env_vars)
* [**get](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClientAsync.md#get)
* [**update](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClientAsync.md#update)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorVersionClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor_version.py#L133)\_\_init\_\_

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

### [**](#delete)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor_version.py#L195)delete

* **async **delete**(): None

- Delete the Actor version.

  <https://docs.apify.com/api/v2#/reference/actors/version-object/delete-version>

  ***

  #### Returns None

### [**](#env_var)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor_version.py#L206)env\_var

* ****env\_var**(env\_var\_name): [ActorEnvVarClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarClientAsync.md)

- Retrieve the client for the specified environment variable of this Actor version.

  ***

  #### Parameters

  * ##### env\_var\_name: str

    The name of the environment variable for which to retrieve the resource client.

  #### Returns [ActorEnvVarClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarClientAsync.md)

### [**](#env_vars)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor_version.py#L202)env\_vars

* ****env\_vars**(): [ActorEnvVarCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarCollectionClientAsync.md)

- Retrieve a client for the environment variables of this Actor version.

  ***

  #### Returns [ActorEnvVarCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorEnvVarCollectionClientAsync.md)

### [**](#get)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor_version.py#L137)get

* **async **get**(): dict | None

- Return information about the Actor version.

  <https://docs.apify.com/api/v2#/reference/actors/version-object/get-version>

  ***

  #### Returns dict | None

### [**](#update)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor_version.py#L147)update

* **async **update**(\*, build\_tag, env\_vars, apply\_env\_vars\_to\_build, source\_type, source\_files, git\_repo\_url, tarball\_url, github\_gist\_url): dict

- Update the Actor version with specified fields.

  <https://docs.apify.com/api/v2#/reference/actors/version-object/update-version>

  ***

  #### Parameters

  * ##### optionalkeyword-onlybuild\_tag: str | None = <!-- -->None

    Tag that is automatically set to the latest successful build of the current version.

  * ##### optionalkeyword-onlyenv\_vars: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict] | None = <!-- -->None

    Environment variables that will be available to the Actor run process, and optionally also to the build process. See the API docs for their exact structure.

  * ##### optionalkeyword-onlyapply\_env\_vars\_to\_build: bool | None = <!-- -->None

    Whether the environment variables specified for the Actor run will also be set to the Actor build process.

  * ##### optionalkeyword-onlysource\_type: ActorSourceType | None = <!-- -->None

    What source type is the Actor version using.

  * ##### optionalkeyword-onlysource\_files: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict] | None = <!-- -->None

    Source code comprised of multiple files, each an item of the array. Required when `source_type` is `ActorSourceType.SOURCE_FILES`. See the API docs for the exact structure.

  * ##### optionalkeyword-onlygit\_repo\_url: str | None = <!-- -->None

    The URL of a Git repository from which the source code will be cloned. Required when `source_type` is `ActorSourceType.GIT_REPO`.

  * ##### optionalkeyword-onlytarball\_url: str | None = <!-- -->None

    The URL of a tarball or a zip archive from which the source code will be downloaded. Required when `source_type` is `ActorSourceType.TARBALL`.

  * ##### optionalkeyword-onlygithub\_gist\_url: str | None = <!-- -->None

    The URL of a GitHub Gist from which the source will be downloaded. Required when `source_type` is `ActorSourceType.GITHUB_GIST`.

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
