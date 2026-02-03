# Source: https://docs.apify.com/api/client/python/reference/class/HTTPClientAsync.md

# HTTPClientAsync<!-- -->

### Hierarchy

* [\_BaseHTTPClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseHTTPClient.md)
  * *HTTPClientAsync*

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md#__init__)
* [**call](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md#call)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/_http_client.py#L33)\_\_init\_\_

* ****\_\_init\_\_**(\*, token, max\_retries, min\_delay\_between\_retries\_millis, timeout\_secs, stats): None

- Inherited from [\_BaseHTTPClient.\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseHTTPClient.md#__init__)

  #### Parameters

  * ##### optionalkeyword-onlytoken: str | None = <!-- -->None
  * ##### optionalkeyword-onlymax\_retries: int = <!-- -->8
  * ##### optionalkeyword-onlymin\_delay\_between\_retries\_millis: int = <!-- -->500
  * ##### optionalkeyword-onlytimeout\_secs: int = <!-- -->360
  * ##### optionalkeyword-onlystats: [Statistics](https://docs.apify.com/api/client/python/api/client/python/reference/class/Statistics.md) | None = <!-- -->None

  #### Returns None

### [**](#call)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/_http_client.py#L220)call

* **async **call**(\*, method, url, headers, params, data, json, stream, timeout\_secs): impit.Response

- #### Parameters

  * ##### keyword-onlymethod: str
  * ##### keyword-onlyurl: str
  * ##### optionalkeyword-onlyheaders: dict | None = <!-- -->None
  * ##### optionalkeyword-onlyparams: dict | None = <!-- -->None
  * ##### optionalkeyword-onlydata: Any = <!-- -->None
  * ##### optionalkeyword-onlyjson: [JSONSerializable](https://docs.apify.com/api/client/python/api/client/python/reference.md#JSONSerializable) | None = <!-- -->None
  * ##### optionalkeyword-onlystream: bool | None = <!-- -->None
  * ##### optionalkeyword-onlytimeout\_secs: int | None = <!-- -->None

  #### Returns impit.Response
