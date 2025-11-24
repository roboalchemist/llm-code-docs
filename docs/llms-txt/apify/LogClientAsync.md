# Source: https://docs.apify.com/api/client/python/reference/class/LogClientAsync.md

# LogClientAsync<!-- -->

Async sub-client for manipulating logs.

### Hierarchy

* [ResourceClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md)
  * *LogClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md#__init__)
* [**get](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md#get)
* [**get\_as\_bytes](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md#get_as_bytes)
* [**stream](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md#stream)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/LogClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L118)\_\_init\_\_

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

### [**](#get)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L122)get

* **async **get**(\*, raw): str | None

- Retrieve the log as text.

  <https://docs.apify.com/api/v2#/reference/logs/log/get-log>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyraw: bool = <!-- -->False

    If true, the log will include formatting. For example, coloring character sequences.

  #### Returns str | None

### [**](#get_as_bytes)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L147)get\_as\_bytes

* **async **get\_as\_bytes**(\*, raw): bytes | None

- Retrieve the log as raw bytes.

  <https://docs.apify.com/api/v2#/reference/logs/log/get-log>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyraw: bool = <!-- -->False

    If true, the log will include formatting. For example, coloring character sequences.

  #### Returns bytes | None

### [**](#stream)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/log.py#L173)stream

* **async **stream**(\*, raw): AsyncIterator\[impit.Response | None]

- Retrieve the log as a stream.

  <https://docs.apify.com/api/v2#/reference/logs/log/get-log>

  ***

  #### Parameters

  * ##### optionalkeyword-onlyraw: bool = <!-- -->False

    If true, the log will include formatting. For example, coloring character sequences.

  #### Returns AsyncIterator\[impit.Response | None]

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
