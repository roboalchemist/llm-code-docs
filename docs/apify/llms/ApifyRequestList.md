# Source: https://docs.apify.com/sdk/python/reference/class/ApifyRequestList.md

# ApifyRequestList<!-- -->

Extends crawlee RequestList.

Method open is used to create RequestList from actor's requestListSources input.

## Index[**](#Index)

### Methods

* [**open](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestList.md#open)

## Methods<!-- -->[**](#Methods)

### [**](#open)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/request_loaders/_apify_request_list.py#L48)open

* **async **open**(name, request\_list\_sources\_input, http\_client): [ApifyRequestList](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestList.md)

- Initialize a new instance from request list source input.

  ***

  #### Parameters

  * ##### optionalname: str | None = <!-- -->None

    Name of the returned RequestList.

  * ##### optionalrequest\_list\_sources\_input: list\[dict\[str, Any]] | None = <!-- -->None

    List of dicts with either url key or requestsFromUrl key.

  * ##### optionalhttp\_client: HttpClient | None = <!-- -->None

    Client that will be used to send get request to urls defined by value of requestsFromUrl keys.

  #### Returns [ApifyRequestList](https://docs.apify.com/sdk/python/sdk/python/reference/class/ApifyRequestList.md)
