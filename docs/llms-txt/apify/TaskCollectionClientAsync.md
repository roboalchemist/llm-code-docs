# Source: https://docs.apify.com/api/client/python/reference/class/TaskCollectionClientAsync.md

# TaskCollectionClientAsync<!-- -->

Async sub-client for manipulating tasks.

### Hierarchy

* [ResourceCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClientAsync.md)
  * *TaskCollectionClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskCollectionClientAsync.md#__init__)
* [**create](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskCollectionClientAsync.md#create)
* [**list](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskCollectionClientAsync.md#list)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskCollectionClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskCollectionClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskCollectionClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskCollectionClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskCollectionClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/task_collection.py#L113)\_\_init\_\_

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

### [**](#create)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/task_collection.py#L138)create

* **async **create**(\*, actor\_id, name, build, timeout\_secs, memory\_mbytes, max\_items, restart\_on\_error, task\_input, title, actor\_standby\_desired\_requests\_per\_actor\_run, actor\_standby\_max\_requests\_per\_actor\_run, actor\_standby\_idle\_timeout\_secs, actor\_standby\_build, actor\_standby\_memory\_mbytes): dict

- Create a new task.

  <https://docs.apify.com/api/v2#/reference/actor-tasks/task-collection/create-task>

  ***

  #### Parameters

  * ##### keyword-onlyactor\_id: str

    Id of the Actor that should be run.

  * ##### keyword-onlyname: str

    Name of the task.

  * ##### optionalkeyword-onlybuild: str | None = <!-- -->None

    Actor build to run. It can be either a build tag or build number. By default, the run uses the build specified in the task settings (typically latest).

  * ##### optionalkeyword-onlytimeout\_secs: int | None = <!-- -->None

    Optional timeout for the run, in seconds. By default, the run uses timeout specified in the task settings.

  * ##### optionalkeyword-onlymemory\_mbytes: int | None = <!-- -->None

    Memory limit for the run, in megabytes. By default, the run uses a memory limit specified in the task settings.

  * ##### optionalkeyword-onlymax\_items: int | None = <!-- -->None

    Maximum number of results that will be returned by runs of this task. If the Actor of this task is charged per result, you will not be charged for more results than the given limit.

  * ##### optionalkeyword-onlyrestart\_on\_error: bool | None = <!-- -->None

    If true, the Task run process will be restarted whenever it exits with a non-zero status code.

  * ##### optionalkeyword-onlytask\_input: dict | None = <!-- -->None

    Task input object.

  * ##### optionalkeyword-onlytitle: str | None = <!-- -->None

    A human-friendly equivalent of the name.

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

### [**](#list)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/task_collection.py#L117)list

* **async **list**(\*, limit, offset, desc): [ListPage](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md)\[dict]

- List the available tasks.

  <https://docs.apify.com/api/v2#/reference/actor-tasks/task-collection/get-list-of-tasks>

  ***

  #### Parameters

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

    How many tasks to list.

  * ##### optionalkeyword-onlyoffset: int | None = <!-- -->None

    What task to include as first when retrieving the list.

  * ##### optionalkeyword-onlydesc: bool | None = <!-- -->None

    Whether to sort the tasks in descending order based on their creation date.

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
