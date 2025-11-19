# Source: https://docs.apify.com/api/client/python/reference/class/UserClientAsync.md

# UserClientAsync<!-- -->

Async sub-client for querying user data.

### Hierarchy

* [ResourceClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ResourceClientAsync.md)
  * *UserClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/UserClientAsync.md#__init__)
* [**get](https://docs.apify.com/api/client/python/api/client/python/reference/class/UserClientAsync.md#get)
* [**limits](https://docs.apify.com/api/client/python/api/client/python/reference/class/UserClientAsync.md#limits)
* [**monthly\_usage](https://docs.apify.com/api/client/python/api/client/python/reference/class/UserClientAsync.md#monthly_usage)
* [**update\_limits](https://docs.apify.com/api/client/python/api/client/python/reference/class/UserClientAsync.md#update_limits)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/UserClientAsync.md#http_client)
* [**params](https://docs.apify.com/api/client/python/api/client/python/reference/class/UserClientAsync.md#params)
* [**resource\_id](https://docs.apify.com/api/client/python/api/client/python/reference/class/UserClientAsync.md#resource_id)
* [**root\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/UserClientAsync.md#root_client)
* [**url](https://docs.apify.com/api/client/python/api/client/python/reference/class/UserClientAsync.md#url)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/user.py#L109)\_\_init\_\_

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

### [**](#get)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/user.py#L116)get

* **async **get**(): dict | None

- Return information about user account.

  You receive all or only public info based on your token permissions.

  <https://docs.apify.com/api/v2#/reference/users>

  ***

  #### Returns dict | None

### [**](#limits)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/user.py#L153)limits

* **async **limits**(): dict | None

- Return a complete summary of the user account's limits.

  It is the same information which is available on the account's Limits page. The returned data includes the current usage cycle, a summary of the account's limits, and the current usage.

  <https://docs.apify.com/api/v2#/reference/request-queues/request/get-request>

  ***

  #### Returns dict | None

### [**](#monthly_usage)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/user.py#L128)monthly\_usage

* **async **monthly\_usage**(): dict | None

- Return monthly usage of the user account.

  This includes a complete usage summary for the current usage cycle, an overall sum, as well as a daily breakdown of usage. It is the same information which is available on the account's Billing page. The information includes use of storage, data transfer, and request queue usage.

  <https://docs.apify.com/api/v2/#/reference/users/monthly-usage>

  ***

  #### Returns dict | None

### [**](#update_limits)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/clients/resource_clients/user.py#L177)update\_limits

* **async **update\_limits**(\*, max\_monthly\_usage\_usd, data\_retention\_days): None

- Update the account's limits manageable on your account's Limits page.

  ***

  #### Parameters

  * ##### optionalkeyword-onlymax\_monthly\_usage\_usd: int | None = <!-- -->None
  * ##### optionalkeyword-onlydata\_retention\_days: int | None = <!-- -->None

  #### Returns None

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
