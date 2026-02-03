# Source: https://docs.apify.com/api/client/python/reference/class/TaskClientAsync.md

# TaskClientAsync<!-- -->

Async sub-client for manipulating a single task.

### Hierarchy

* [ResourceClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md)
  * *TaskClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#__init__)
* [**call](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#call)
* [**delete](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#delete)
* [**get](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#get)
* [**get\_input](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#get_input)
* [**last\_run](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#last_run)
* [**runs](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#runs)
* [**start](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#start)
* [**update](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#update)
* [**update\_input](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#update_input)
* [**webhooks](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#webhooks)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/task.py#L337)\_\_init\_\_

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

### [**](#call)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/task.py#L484)call

* **async **call**(\*, task\_input, build, max\_items, memory\_mbytes, timeout\_secs, restart\_on\_error, webhooks, wait\_secs): dict | None

- Start a task and wait for it to finish before returning the Run object.

  It waits indefinitely, unless the wait\_secs argument is provided.

  <https://docs.apify.com/api/v2#/reference/actor-tasks/run-collection/run-task>

  ***

  #### Parameters

  * ##### optionalkeyword-onlytask\_input: dict | None = <!-- -->None

    Task input dictionary.

  * ##### optionalkeyword-onlybuild: str | None = <!-- -->None

    Specifies the Actor build to run. It can be either a build tag or build number. By default, the run uses the build specified in the task settings (typically latest).

  * ##### optionalkeyword-onlymax\_items: int | None = <!-- -->None

    Maximum number of results that will be returned by this run. If the Actor is charged per result, you will not be charged for more results than the given limit.

  * ##### optionalkeyword-onlymemory\_mbytes: int | None = <!-- -->None

    Memory limit for the run, in megabytes. By default, the run uses a memory limit specified in the task settings.

  * ##### optionalkeyword-onlytimeout\_secs: int | None = <!-- -->None

    Optional timeout for the run, in seconds. By default, the run uses timeout specified in the task settings.

  * ##### optionalkeyword-onlyrestart\_on\_error: bool | None = <!-- -->None

    If true, the Task run process will be restarted whenever it exits with a non-zero status code.

  * ##### optionalkeyword-onlywebhooks: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict] | None = <!-- -->None

    Specifies optional webhooks associated with the Actor run, which can be used to receive a notification e.g. when the Actor finished or failed. Note: if you already have a webhook set up for the Actor or task, you do not have to add it again here.

  * ##### optionalkeyword-onlywait\_secs: int | None = <!-- -->None

    The maximum number of seconds the server waits for the task run to finish. If not provided, waits indefinitely.

  #### Returns dict | None

### [**](#delete)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/task.py#L416)delete

* **async **delete**(): None

- Delete the task.

  <https://docs.apify.com/api/v2#/reference/actor-tasks/task-object/delete-task>

  ***

  #### Returns None

### [**](#get)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/task.py#L341)get

* **async **get**(): dict | None

- Retrieve the task.

  <https://docs.apify.com/api/v2#/reference/actor-tasks/task-object/get-task>

  ***

  #### Returns dict | None

### [**](#get_input)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/task.py#L535)get\_input

* **async **get\_input**(): dict | None

- Retrieve the default input for this task.

  <https://docs.apify.com/api/v2#/reference/actor-tasks/task-input-object/get-task-input>

  ***

  #### Returns dict | None

### [**](#last_run)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/task.py#L574)last\_run

* ****last\_run**(\*, status, origin): [RunClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md)

- Retrieve the client for the last run of this task.

  Last run is retrieved based on the start time of the runs.

  ***

  #### Parameters

  * ##### optionalkeyword-onlystatus: ActorJobStatus | None = <!-- -->None

    Consider only runs with this status.

  * ##### optionalkeyword-onlyorigin: MetaOrigin | None = <!-- -->None

    Consider only runs started with this origin.

  #### Returns [RunClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md)

### [**](#runs)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/task.py#L570)runs

* ****runs**(): [RunCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunCollectionClientAsync.md)

- Retrieve a client for the runs of this task.

  ***

  #### Returns [RunCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunCollectionClientAsync.md)

### [**](#start)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/task.py#L423)start

* **async **start**(\*, task\_input, build, max\_items, memory\_mbytes, timeout\_secs, restart\_on\_error, wait\_for\_finish, webhooks): dict

- Start the task and immediately return the Run object.

  <https://docs.apify.com/api/v2#/reference/actor-tasks/run-collection/run-task>

  ***

  #### Parameters

  * ##### optionalkeyword-onlytask\_input: dict | None = <!-- -->None

    Task input dictionary.

  * ##### optionalkeyword-onlybuild: str | None = <!-- -->None

    Specifies the Actor build to run. It can be either a build tag or build number. By default, the run uses the build specified in the task settings (typically latest).

  * ##### optionalkeyword-onlymax\_items: int | None = <!-- -->None

    Maximum number of results that will be returned by this run. If the Actor is charged per result, you will not be charged for more results than the given limit.

  * ##### optionalkeyword-onlymemory\_mbytes: int | None = <!-- -->None

    Memory limit for the run, in megabytes. By default, the run uses a memory limit specified in the task settings.

  * ##### optionalkeyword-onlytimeout\_secs: int | None = <!-- -->None

    Optional timeout for the run, in seconds. By default, the run uses timeout specified in the task settings.

  * ##### optionalkeyword-onlyrestart\_on\_error: bool | None = <!-- -->None

    If true, the Task run process will be restarted whenever it exits with a non-zero status code.

  * ##### optionalkeyword-onlywait\_for\_finish: int | None = <!-- -->None

    The maximum number of seconds the server waits for the run to finish. By default, it is 0, the maximum value is 60.

  * ##### optionalkeyword-onlywebhooks: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict] | None = <!-- -->None

    Optional ad-hoc webhooks (<https://docs.apify.com/webhooks/ad-hoc-webhooks>) associated with the Actor run which can be used to receive a notification, e.g. when the Actor finished or failed. If you already have a webhook set up for the Actor or task, you do not have to add it again here. Each webhook is represented by a dictionary containing these items:

    * `event_types`: List of `` `WebhookEventType` `` values which trigger the webhook.
    * `request_url`: URL to which to send the webhook HTTP request.
    * `payload_template`: Optional template for the request payload.

  #### Returns dict

### [**](#update)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/task.py#L351)update

* **async **update**(\*, name, task\_input, build, max\_items, memory\_mbytes, timeout\_secs, restart\_on\_error, title, actor\_standby\_desired\_requests\_per\_actor\_run, actor\_standby\_max\_requests\_per\_actor\_run, actor\_standby\_idle\_timeout\_secs, actor\_standby\_build, actor\_standby\_memory\_mbytes): dict

- Update the task with specified fields.

  <https://docs.apify.com/api/v2#/reference/actor-tasks/task-object/update-task>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyname: str | None = <!-- -->None

    Name of the task.

  * ##### optionalkeyword-onlytask\_input: dict | None = <!-- -->None

    Task input dictionary.

  * ##### optionalkeyword-onlybuild: str | None = <!-- -->None

    Actor build to run. It can be either a build tag or build number. By default, the run uses the build specified in the task settings (typically latest).

  * ##### optionalkeyword-onlymax\_items: int | None = <!-- -->None

    Maximum number of results that will be returned by this run. If the Actor is charged per result, you will not be charged for more results than the given limit.

  * ##### optionalkeyword-onlymemory\_mbytes: int | None = <!-- -->None

    Memory limit for the run, in megabytes. By default, the run uses a memory limit specified in the task settings.

  * ##### optionalkeyword-onlytimeout\_secs: int | None = <!-- -->None

    Optional timeout for the run, in seconds. By default, the run uses timeout specified in the task settings.

  * ##### optionalkeyword-onlyrestart\_on\_error: bool | None = <!-- -->None

    If true, the Task run process will be restarted whenever it exits with a non-zero status code.

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

### [**](#update_input)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/task.py#L554)update\_input

* **async **update\_input**(\*, task\_input): dict

- Update the default input for this task.

  <https://docs.apify.com/api/v2#/reference/actor-tasks/task-input-object/update-task-input>

  ***

  #### Parameters

  * ##### keyword-onlytask\_input: dict

  #### Returns dict

### [**](#webhooks)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/task.py#L597)webhooks

* ****webhooks**(): [WebhookCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md)

- Retrieve a client for webhooks associated with this task.

  ***

  #### Returns [WebhookCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md)

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
