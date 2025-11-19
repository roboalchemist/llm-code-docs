# Source: https://docs.apify.com/api/client/python/reference/class/ApifyClientAsync.md

# ApifyClientAsync<!-- -->

The asynchronous version of the Apify API client.

### Hierarchy

* [\_BaseApifyClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseApifyClient.md)
  * *ApifyClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#__init__)
* [**actor](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#actor)
* [**actors](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#actors)
* [**build](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#build)
* [**builds](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#builds)
* [**dataset](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#dataset)
* [**datasets](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#datasets)
* [**key\_value\_store](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#key_value_store)
* [**key\_value\_stores](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#key_value_stores)
* [**log](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#log)
* [**request\_queue](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#request_queue)
* [**request\_queues](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#request_queues)
* [**run](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#run)
* [**runs](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#runs)
* [**schedule](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#schedule)
* [**schedules](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#schedules)
* [**store](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#store)
* [**task](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#task)
* [**tasks](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#tasks)
* [**user](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#user)
* [**webhook](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#webhook)
* [**webhook\_dispatch](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#webhook_dispatch)
* [**webhook\_dispatches](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#webhook_dispatches)
* [**webhooks](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#webhooks)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md#http_client)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L295)\_\_init\_\_

* ****\_\_init\_\_**(token, \*, api\_url, api\_public\_url, max\_retries, min\_delay\_between\_retries\_millis, timeout\_secs): None

- Overrides [\_BaseApifyClient.\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseApifyClient.md#__init__)

  Initialize a new instance.

  ***

  #### Parameters

  * ##### optionaltoken: str | None = <!-- -->None

    The Apify API token.

  * ##### optionalkeyword-onlyapi\_url: str | None = <!-- -->None

    The URL of the Apify API server to which to connect. Defaults to <https://api.apify.com>. It can be an internal URL that is not globally accessible, in such case `api_public_url` should be set as well.

  * ##### optionalkeyword-onlyapi\_public\_url: str | None = <!-- -->None

    The globally accessible URL of the Apify API server. It should be set only if the `api_url` is an internal URL that is not globally accessible.

  * ##### optionalkeyword-onlymax\_retries: int | None = <!-- -->8

    How many times to retry a failed request at most.

  * ##### optionalkeyword-onlymin\_delay\_between\_retries\_millis: int | None = <!-- -->500

    How long will the client wait between retrying requests (increases exponentially from this value).

  * ##### optionalkeyword-onlytimeout\_secs: int | None = <!-- -->DEFAULT\_TIMEOUT

    The socket timeout of the HTTP requests sent to the Apify API.

  #### Returns None

### [**](#actor)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L336)actor

* ****actor**(actor\_id): [ActorClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md)

- Retrieve the sub-client for manipulating a single Actor.

  ***

  #### Parameters

  * ##### actor\_id: str

    ID of the Actor to be manipulated.

  #### Returns [ActorClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorClientAsync.md)

### [**](#actors)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L344)actors

* ****actors**(): [ActorCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorCollectionClientAsync.md)

- Retrieve the sub-client for manipulating Actors.

  ***

  #### Returns [ActorCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ActorCollectionClientAsync.md)

### [**](#build)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L348)build

* ****build**(build\_id): [BuildClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md)

- Retrieve the sub-client for manipulating a single Actor build.

  ***

  #### Parameters

  * ##### build\_id: str

    ID of the Actor build to be manipulated.

  #### Returns [BuildClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildClientAsync.md)

### [**](#builds)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L356)builds

* ****builds**(): [BuildCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildCollectionClientAsync.md)

- Retrieve the sub-client for querying multiple builds of a user.

  ***

  #### Returns [BuildCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/BuildCollectionClientAsync.md)

### [**](#dataset)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L372)dataset

* ****dataset**(dataset\_id): [DatasetClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md)

- Retrieve the sub-client for manipulating a single dataset.

  ***

  #### Parameters

  * ##### dataset\_id: str

    ID of the dataset to be manipulated.

  #### Returns [DatasetClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetClientAsync.md)

### [**](#datasets)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L380)datasets

* ****datasets**(): [DatasetCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetCollectionClientAsync.md)

- Retrieve the sub-client for manipulating datasets.

  ***

  #### Returns [DatasetCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/DatasetCollectionClientAsync.md)

### [**](#key_value_store)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L384)key\_value\_store

* ****key\_value\_store**(key\_value\_store\_id): [KeyValueStoreClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md)

- Retrieve the sub-client for manipulating a single key-value store.

  ***

  #### Parameters

  * ##### key\_value\_store\_id: str

    ID of the key-value store to be manipulated.

  #### Returns [KeyValueStoreClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreClientAsync.md)

### [**](#key_value_stores)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L392)key\_value\_stores

* ****key\_value\_stores**(): [KeyValueStoreCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreCollectionClientAsync.md)

- Retrieve the sub-client for manipulating key-value stores.

  ***

  #### Returns [KeyValueStoreCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/KeyValueStoreCollectionClientAsync.md)

### [**](#log)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L445)log

* ****log**(build\_or\_run\_id): [LogClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md)

- Retrieve the sub-client for retrieving logs.

  ***

  #### Parameters

  * ##### build\_or\_run\_id: str

    ID of the Actor build or run for which to access the log.

  #### Returns [LogClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md)

### [**](#request_queue)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L396)request\_queue

* ****request\_queue**(request\_queue\_id, \*, client\_key): [RequestQueueClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md)

- Retrieve the sub-client for manipulating a single request queue.

  ***

  #### Parameters

  * ##### request\_queue\_id: str

    ID of the request queue to be manipulated.

  * ##### optionalkeyword-onlyclient\_key: str | None = <!-- -->None

    A unique identifier of the client accessing the request queue.

  #### Returns [RequestQueueClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueClientAsync.md)

### [**](#request_queues)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L405)request\_queues

* ****request\_queues**(): [RequestQueueCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClientAsync.md)

- Retrieve the sub-client for manipulating request queues.

  ***

  #### Returns [RequestQueueCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClientAsync.md)

### [**](#run)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L360)run

* ****run**(run\_id): [RunClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md)

- Retrieve the sub-client for manipulating a single Actor run.

  ***

  #### Parameters

  * ##### run\_id: str

    ID of the Actor run to be manipulated.

  #### Returns [RunClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunClientAsync.md)

### [**](#runs)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L368)runs

* ****runs**(): [RunCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunCollectionClientAsync.md)

- Retrieve the sub-client for querying multiple Actor runs of a user.

  ***

  #### Returns [RunCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/RunCollectionClientAsync.md)

### [**](#schedule)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L433)schedule

* ****schedule**(schedule\_id): [ScheduleClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleClientAsync.md)

- Retrieve the sub-client for manipulating a single schedule.

  ***

  #### Parameters

  * ##### schedule\_id: str

    ID of the schedule to be manipulated.

  #### Returns [ScheduleClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleClientAsync.md)

### [**](#schedules)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L441)schedules

* ****schedules**(): [ScheduleCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleCollectionClientAsync.md)

- Retrieve the sub-client for manipulating schedules.

  ***

  #### Returns [ScheduleCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleCollectionClientAsync.md)

### [**](#store)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L473)store

* ****store**(): [StoreCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/StoreCollectionClientAsync.md)

- Retrieve the sub-client for Apify store.

  ***

  #### Returns [StoreCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/StoreCollectionClientAsync.md)

### [**](#task)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L453)task

* ****task**(task\_id): [TaskClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md)

- Retrieve the sub-client for manipulating a single task.

  ***

  #### Parameters

  * ##### task\_id: str

    ID of the task to be manipulated.

  #### Returns [TaskClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskClientAsync.md)

### [**](#tasks)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L461)tasks

* ****tasks**(): [TaskCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskCollectionClientAsync.md)

- Retrieve the sub-client for manipulating tasks.

  ***

  #### Returns [TaskCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/TaskCollectionClientAsync.md)

### [**](#user)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L465)user

* ****user**(user\_id): [UserClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/UserClientAsync.md)

- Retrieve the sub-client for querying users.

  ***

  #### Parameters

  * ##### optionaluser\_id: str | None = <!-- -->None

    ID of user to be queried. If None, queries the user belonging to the token supplied to the client.

  #### Returns [UserClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/UserClientAsync.md)

### [**](#webhook)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L409)webhook

* ****webhook**(webhook\_id): [WebhookClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClientAsync.md)

- Retrieve the sub-client for manipulating a single webhook.

  ***

  #### Parameters

  * ##### webhook\_id: str

    ID of the webhook to be manipulated.

  #### Returns [WebhookClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookClientAsync.md)

### [**](#webhook_dispatch)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L421)webhook\_dispatch

* ****webhook\_dispatch**(webhook\_dispatch\_id): [WebhookDispatchClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchClientAsync.md)

- Retrieve the sub-client for accessing a single webhook dispatch.

  ***

  #### Parameters

  * ##### webhook\_dispatch\_id: str

    ID of the webhook dispatch to access.

  #### Returns [WebhookDispatchClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchClientAsync.md)

### [**](#webhook_dispatches)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L429)webhook\_dispatches

* ****webhook\_dispatches**(): [WebhookDispatchCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchCollectionClientAsync.md)

- Retrieve the sub-client for querying multiple webhook dispatches of a user.

  ***

  #### Returns [WebhookDispatchCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookDispatchCollectionClientAsync.md)

### [**](#webhooks)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L417)webhooks

* ****webhooks**(): [WebhookCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md)

- Retrieve the sub-client for querying multiple webhooks of a user.

  ***

  #### Returns [WebhookCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/WebhookCollectionClientAsync.md)

## Properties<!-- -->[**](#Properties)

### [**](#http_client)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/client.py#L293)http\_client

**http\_client: [HTTPClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClient.md) | [HTTPClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md)

Overrides [\_BaseApifyClient.http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseApifyClient.md#http_client)
