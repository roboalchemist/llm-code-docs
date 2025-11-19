# Source: https://docs.apify.com/api/client/python/reference/class/RunClientAsync.md

# RunClientAsync<!-- -->

Async sub-client for manipulating a single Actor run.

### Hierarchy

* [ActorJobBaseClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorJobBaseClientAsync.md)
  * *RunClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#__init__)
* [**abort](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#abort)
* [**charge](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#charge)
* [**dataset](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#dataset)
* [**delete](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#delete)
* [**get](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#get)
* [**get\_status\_message\_watcher](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#get_status_message_watcher)
* [**get\_streamed\_log](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#get_streamed_log)
* [**key\_value\_store](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#key_value_store)
* [**log](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#log)
* [**metamorph](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#metamorph)
* [**reboot](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#reboot)
* [**request\_queue](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#request_queue)
* [**resurrect](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#resurrect)
* [**update](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#update)
* [**wait\_for\_finish](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#wait_for_finish)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L364)\_\_init\_\_

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

### [**](#abort)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L405)abort

* **async **abort**(\*, gracefully): dict

- Abort the Actor run which is starting or currently running and return its details.

  <https://docs.apify.com/api/v2#/reference/actor-runs/abort-run/abort-run>

  ***

  #### Parameters

  * ##### optionalkeyword-onlygracefully: bool | None = <!-- -->None

    If True, the Actor run will abort gracefully. It will send `aborting` and `persistStates` events into the run and force-stop the run after 30 seconds. It is helpful in cases where you plan to resurrect the run later.

  #### Returns dict

### [**](#charge)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L623)charge

* **async **charge**(event\_name, count, idempotency\_key): None

- Charge for an event of a Pay-Per-Event Actor run.

  <https://docs.apify.com/api/v2#/reference/actor-runs/charge-events-in-run>

  ***

  #### Parameters

  * ##### event\_name: str
  * ##### optionalcount: int | None = <!-- -->None
  * ##### optionalidempotency\_key: str | None = <!-- -->None

  #### Returns None

### [**](#dataset)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L546)dataset

* ****dataset**(): [DatasetClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md)

- Get the client for the default dataset of the Actor run.

  <https://docs.apify.com/api/v2#/reference/actors/last-run-object-and-its-storages>

  ***

  #### Returns [DatasetClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md)

### [**](#delete)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L432)delete

* **async **delete**(): None

- Delete the run.

  <https://docs.apify.com/api/v2#/reference/actor-runs/delete-run/delete-run>

  ***

  #### Returns None

### [**](#get)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L368)get

* **async **get**(): dict | None

- Return information about the Actor run.

  <https://docs.apify.com/api/v2#/reference/actor-runs/run-object/get-run>

  ***

  #### Returns dict | None

### [**](#get_status_message_watcher)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L658)get\_status\_message\_watcher

* **async **get\_status\_message\_watcher**(to\_logger, check\_period): [StatusMessageWatcherAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherAsync.md)

- Get `StatusMessageWatcher` instance that can be used to redirect status and status messages to logs.

  `StatusMessageWatcher` can be explicitly started and stopped or used as a context manager.

  ***

  #### Parameters

  * ##### optionalto\_logger: logging.Logger | None = <!-- -->None

    `Logger` used for logging the status and status messages. If not provided, a new logger is created.

  * ##### optionalcheck\_period: timedelta = <!-- -->timedelta(seconds=1)

    The period with which the status message will be polled.

  #### Returns [StatusMessageWatcherAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/StatusMessageWatcherAsync.md)

### [**](#get_streamed_log)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L594)get\_streamed\_log

* **async **get\_streamed\_log**(to\_logger, \*, from\_start): [StreamedLogAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogAsync.md)

- Get `StreamedLog` instance that can be used to redirect logs.

  `StreamedLog` can be explicitly started and stopped or used as a context manager.

  ***

  #### Parameters

  * ##### optionalto\_logger: logging.Logger | None = <!-- -->None

    `Logger` used for logging the redirected messages. If not provided, a new logger is created

  * ##### optionalkeyword-onlyfrom\_start: bool = <!-- -->True

    If `True`, all logs from the start of the actor run will be redirected. If `False`, only newly arrived logs will be redirected. This can be useful for redirecting only a small portion of relevant logs for long-running actors in stand-by.

  #### Returns [StreamedLogAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/StreamedLogAsync.md)

### [**](#key_value_store)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L558)key\_value\_store

* ****key\_value\_store**(): [KeyValueStoreClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md)

- Get the client for the default key-value store of the Actor run.

  <https://docs.apify.com/api/v2#/reference/actors/last-run-object-and-its-storages>

  ***

  #### Returns [KeyValueStoreClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md)

### [**](#log)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L582)log

* ****log**(): [LogClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md)

- Get the client for the log of the Actor run.

  <https://docs.apify.com/api/v2#/reference/actors/last-run-object-and-its-storages>

  ***

  #### Returns [LogClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md)

### [**](#metamorph)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L439)metamorph

* **async **metamorph**(\*, target\_actor\_id, target\_actor\_build, run\_input, content\_type): dict

- Transform an Actor run into a run of another Actor with a new input.

  <https://docs.apify.com/api/v2#/reference/actor-runs/metamorph-run/metamorph-run>

  ***

  #### Parameters

  * ##### keyword-onlytarget\_actor\_id: str

    ID of the target Actor that the run should be transformed into.

  * ##### optionalkeyword-onlytarget\_actor\_build: str | None = <!-- -->None

    The build of the target Actor. It can be either a build tag or build number. By default, the run uses the build specified in the default run configuration for the target Actor (typically the latest build).

  * ##### optionalkeyword-onlyrun\_input: Any = <!-- -->None

    The input to pass to the new run.

  * ##### optionalkeyword-onlycontent\_type: str | None = <!-- -->None

    The content type of the input.

  #### Returns dict

### [**](#reboot)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L532)reboot

* **async **reboot**(): dict

- Reboot an Actor run. Only runs that are running, i.e. runs with status RUNNING can be rebooted.

  <https://docs.apify.com/api/v2#/reference/actor-runs/reboot-run/reboot-run>

  ***

  #### Returns dict

### [**](#request_queue)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L570)request\_queue

* ****request\_queue**(): [RequestQueueClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md)

- Get the client for the default request queue of the Actor run.

  <https://docs.apify.com/api/v2#/reference/actors/last-run-object-and-its-storages>

  ***

  #### Returns [RequestQueueClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md)

### [**](#resurrect)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L481)resurrect

* **async **resurrect**(\*, build, memory\_mbytes, timeout\_secs, max\_items, max\_total\_charge\_usd, restart\_on\_error): dict

- Resurrect a finished Actor run.

  Only finished runs, i.e. runs with status FINISHED, FAILED, ABORTED and TIMED-OUT can be resurrected. Run status will be updated to RUNNING and its container will be restarted with the same default storages.

  <https://docs.apify.com/api/v2#/reference/actor-runs/resurrect-run/resurrect-run>

  ***

  #### Parameters

  * ##### optionalkeyword-onlybuild: str | None = <!-- -->None

    Which Actor build the resurrected run should use. It can be either a build tag or build number. By default, the resurrected run uses the same build as before.

  * ##### optionalkeyword-onlymemory\_mbytes: int | None = <!-- -->None

    New memory limit for the resurrected run, in megabytes. By default, the resurrected run uses the same memory limit as before.

  * ##### optionalkeyword-onlytimeout\_secs: int | None = <!-- -->None

    New timeout for the resurrected run, in seconds. By default, the resurrected run uses the same timeout as before.

  * ##### optionalkeyword-onlymax\_items: int | None = <!-- -->None

    Maximum number of items that the resurrected pay-per-result run will return. By default, the resurrected run uses the same limit as before. Limit can be only increased.

  * ##### optionalkeyword-onlymax\_total\_charge\_usd: Decimal | None = <!-- -->None

    Maximum cost for the resurrected pay-per-event run in USD. By default, the resurrected run uses the same limit as before. Limit can be only increased.

  * ##### optionalkeyword-onlyrestart\_on\_error: bool | None = <!-- -->None

    Determines whether the resurrected run will be restarted if it fails. By default, the resurrected run uses the same setting as before.

  #### Returns dict

### [**](#update)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L378)update

* **async **update**(\*, status\_message, is\_status\_message\_terminal, general\_access): dict

- Update the run with the specified fields.

  <https://docs.apify.com/api/v2#/reference/actor-runs/run-object/update-run>

  ***

  #### Parameters

  * ##### optionalkeyword-onlystatus\_message: str | None = <!-- -->None

    The new status message for the run.

  * ##### optionalkeyword-onlyis\_status\_message\_terminal: bool | None = <!-- -->None

    Set this flag to True if this is the final status message of the Actor run.

  * ##### optionalkeyword-onlygeneral\_access: RunGeneralAccess | None = <!-- -->None

    Determines how others can access the run and its storages.

  #### Returns dict

### [**](#wait_for_finish)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/run.py#L420)wait\_for\_finish

* **async **wait\_for\_finish**(\*, wait\_secs): dict | None

- Wait synchronously until the run finishes or the server times out.

  ***

  #### Parameters

  * ##### optionalkeyword-onlywait\_secs: int | None = <!-- -->None

    How long does the client wait for run to finish. None for indefinite.

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
