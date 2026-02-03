# Source: https://docs.apify.com/api/client/python/reference/class/ScheduleCollectionClientAsync.md

# ScheduleCollectionClientAsync<!-- -->

Async sub-client for manipulating schedules.

### Hierarchy

* [ResourceCollectionClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceCollectionClientAsync.md)
  * *ScheduleCollectionClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleCollectionClientAsync.md#__init__)
* [**create](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleCollectionClientAsync.md#create)
* [**list](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleCollectionClientAsync.md#list)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleCollectionClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleCollectionClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleCollectionClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleCollectionClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleCollectionClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/schedule_collection.py#L92)\_\_init\_\_

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

### [**](#create)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/schedule_collection.py#L117)create

* **async **create**(\*, cron\_expression, is\_enabled, is\_exclusive, name, actions, description, timezone, title): dict

- Create a new schedule.

  <https://docs.apify.com/api/v2#/reference/schedules/schedules-collection/create-schedule>

  ***

  #### Parameters

  * ##### keyword-onlycron\_expression: str

    The cron expression used by this schedule.

  * ##### keyword-onlyis\_enabled: bool

    True if the schedule should be enabled.

  * ##### keyword-onlyis\_exclusive: bool

    When set to true, don't start Actor or Actor task if it's still running from the previous schedule.

  * ##### optionalkeyword-onlyname: str | None = <!-- -->None

    The name of the schedule to create.

  * ##### optionalkeyword-onlyactions: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict] | None = <!-- -->None

    Actors or tasks that should be run on this schedule. See the API documentation for exact structure.

  * ##### optionalkeyword-onlydescription: str | None = <!-- -->None

    Description of this schedule.

  * ##### optionalkeyword-onlytimezone: str | None = <!-- -->None

    Timezone in which your cron expression runs (TZ database name from <https://en.wikipedia.org/wiki/List_of_tz_database_time_zones>).

  * ##### optionalkeyword-onlytitle: str | None = <!-- -->None

    Title of this schedule.

  #### Returns dict

### [**](#list)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/schedule_collection.py#L96)list

* **async **list**(\*, limit, offset, desc): [ListPage](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md)\[dict]

- List the available schedules.

  <https://docs.apify.com/api/v2#/reference/schedules/schedules-collection/get-list-of-schedules>

  ***

  #### Parameters

  * ##### optionalkeyword-onlylimit: int | None = <!-- -->None

    How many schedules to retrieve.

  * ##### optionalkeyword-onlyoffset: int | None = <!-- -->None

    What schedules to include as first when retrieving the list.

  * ##### optionalkeyword-onlydesc: bool | None = <!-- -->None

    Whether to sort the schedules in descending order based on their modification date.

  #### Returns [ListPage](https://docs.apify.com/api/client/python/api/client/python/reference/class/ListPage.md)\[dict]

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
