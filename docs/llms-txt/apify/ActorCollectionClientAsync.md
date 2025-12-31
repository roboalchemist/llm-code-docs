# Source: https://docs.apify.com/api/client/python/reference/class/ActorCollectionClientAsync.md

# ActorCollectionClientAsync<!-- -->

Async sub-client for manipulating Actors.

### Hierarchy

* [ResourceCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClientAsync.md)
  * *ActorCollectionClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorCollectionClientAsync.md#__init__)
* [**create](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorCollectionClientAsync.md#create)
* [**list](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorCollectionClientAsync.md#list)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorCollectionClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorCollectionClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorCollectionClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorCollectionClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorCollectionClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor_collection.py#L141)\_\_init\_\_

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

### [**](#create)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor_collection.py#L170)create

* **async **create**(\*, name, title, description, seo\_title, seo\_description, versions, restart\_on\_error, is\_public, is\_deprecated, is\_anonymously\_runnable, categories, default\_run\_build, default\_run\_max\_items, default\_run\_memory\_mbytes, default\_run\_timeout\_secs, example\_run\_input\_body, example\_run\_input\_content\_type, actor\_standby\_is\_enabled, actor\_standby\_desired\_requests\_per\_actor\_run, actor\_standby\_max\_requests\_per\_actor\_run, actor\_standby\_idle\_timeout\_secs, actor\_standby\_build, actor\_standby\_memory\_mbytes): dict

- Create a new Actor.

  <https://docs.apify.com/api/v2#/reference/actors/actor-collection/create-actor>

  ***

  #### Parameters

  * ##### keyword-onlyname: str

    The name of the Actor.

  * ##### optionalkeyword-onlytitle: str | None = <!-- -->None

    The title of the Actor (human-readable).

  * ##### optionalkeyword-onlydescription: str | None = <!-- -->None

    The description for the Actor.

  * ##### optionalkeyword-onlyseo\_title: str | None = <!-- -->None

    The title of the Actor optimized for search engines.

  * ##### optionalkeyword-onlyseo\_description: str | None = <!-- -->None

    The description of the Actor optimized for search engines.

  * ##### optionalkeyword-onlyversions: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict] | None = <!-- -->None

    The list of Actor versions.

  * ##### optionalkeyword-onlyrestart\_on\_error: bool | None = <!-- -->None

    If true, the Actor run process will be restarted whenever it exits with a non-zero status code.

  * ##### optionalkeyword-onlyis\_public: bool | None = <!-- -->None

    Whether the Actor is public.

  * ##### optionalkeyword-onlyis\_deprecated: bool | None = <!-- -->None

    Whether the Actor is deprecated.

  * ##### optionalkeyword-onlyis\_anonymously\_runnable: bool | None = <!-- -->None

    Whether the Actor is anonymously runnable.

  * ##### optionalkeyword-onlycategories: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[str] | None = <!-- -->None

    The categories to which the Actor belongs to.

  * ##### optionalkeyword-onlydefault\_run\_build: str | None = <!-- -->None

    Tag or number of the build that you want to run by default.

  * ##### optionalkeyword-onlydefault\_run\_max\_items: int | None = <!-- -->None

    Default limit of the number of results that will be returned by runs of this Actor, if the Actor is charged per result.

  * ##### optionalkeyword-onlydefault\_run\_memory\_mbytes: int | None = <!-- -->None

    Default amount of memory allocated for the runs of this Actor, in megabytes.

  * ##### optionalkeyword-onlydefault\_run\_timeout\_secs: int | None = <!-- -->None

    Default timeout for the runs of this Actor in seconds.

  * ##### optionalkeyword-onlyexample\_run\_input\_body: Any = <!-- -->None

    Input to be prefilled as default input to new users of this Actor.

  * ##### optionalkeyword-onlyexample\_run\_input\_content\_type: str | None = <!-- -->None

    The content type of the example run input.

  * ##### optionalkeyword-onlyactor\_standby\_is\_enabled: bool | None = <!-- -->None

    Whether the Actor Standby is enabled.

  * ##### optionalkeyword-onlyactor\_standby\_desired\_requests\_per\_actor\_run: int | None = <!-- -->None

    The desired number of concurrent HTTP requests for a single Actor Standby run.

  * ##### optionalkeyword-onlyactor\_standby\_max\_requests\_per\_actor\_run: int | None = <!-- -->None

    The maximum number of concurrent HTTP requests for a single Actor Standby run.

  * ##### optionalkeyword-onlyactor\_standby\_idle\_timeout\_secs: int | None = <!-- -->None

    If the Actor run does not receive any requests for this time, it will be shut down.

  * ##### optionalkeyword-onlyactor\_standby\_build: str | None = <!-- -->None

    The build tag or number to run when the Actor is in Standby mode.

  * ##### optionalkeyword-onlyactor\_standby\_memory\_mbytes: int | None = <!-- -->None

    The memory in megabytes to use when the Actor is in Standby mode.

  #### Returns dict

### [**](#list)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/actor_collection.py#L145)list

* **async **list**(\*, my, limit, offset, desc, sort\_by): [ListPage](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md)\[dict]

- List the Actors the user has created or used.

  <https://docs.apify.com/api/v2#/reference/actors/actor-collection/get-list-of-actors>

  ***

  #### Parameters

  * ##### optionalkeyword-onlymy: bool | None = <!-- -->None

    If True, will return only Actors which the user has created themselves.

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

    How many Actors to list.

  * ##### optionalkeyword-onlyoffset: int | None = <!-- -->None

    What Actor to include as first when retrieving the list.

  * ##### optionalkeyword-onlydesc: bool | None = <!-- -->None

    Whether to sort the Actors in descending order based on their creation date.

  * ##### optionalkeyword-onlysort\_by: Literal\[createdAt, stats.lastRunStartedAt] | None = <!-- -->'createdAt'

    Field to sort the results by.

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
