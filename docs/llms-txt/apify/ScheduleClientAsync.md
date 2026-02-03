# Source: https://docs.apify.com/api/client/python/reference/class/ScheduleClientAsync.md

# ScheduleClientAsync<!-- -->

Async sub-client for manipulating a single schedule.

### Hierarchy

* [ResourceClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md)
  * *ScheduleClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleClientAsync.md#__init__)
* [**delete](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleClientAsync.md#delete)
* [**get](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleClientAsync.md#get)
* [**get\_log](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleClientAsync.md#get_log)
* [**update](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleClientAsync.md#update)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/ScheduleClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/schedule.py#L125)\_\_init\_\_

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

### [**](#delete)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/schedule.py#L183)delete

* **async **delete**(): None

- Delete the schedule.

  <https://docs.apify.com/api/v2#/reference/schedules/schedule-object/delete-schedule>

  ***

  #### Returns None

### [**](#get)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/schedule.py#L129)get

* **async **get**(): dict | None

- Return information about the schedule.

  <https://docs.apify.com/api/v2#/reference/schedules/schedule-object/get-schedule>

  ***

  #### Returns dict | None

### [**](#get_log)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/schedule.py#L190)get\_log

* **async **get\_log**(): [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list) | None

- Return log for the given schedule.

  <https://docs.apify.com/api/v2#/reference/schedules/schedule-log/get-schedule-log>

  ***

  #### Returns [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list) | None

### [**](#update)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/schedule.py#L139)update

* **async **update**(\*, cron\_expression, is\_enabled, is\_exclusive, name, actions, description, timezone, title): dict

- Update the schedule with specified fields.

  <https://docs.apify.com/api/v2#/reference/schedules/schedule-object/update-schedule>

  ***

  #### Parameters

  * ##### optionalkeyword-onlycron\_expression: str | None = <!-- -->None

    The cron expression used by this schedule.

  * ##### optionalkeyword-onlyis\_enabled: bool | None = <!-- -->None

    True if the schedule should be enabled.

  * ##### optionalkeyword-onlyis\_exclusive: bool | None = <!-- -->None

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

    A human-friendly equivalent of the name.

  #### Returns dict

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
