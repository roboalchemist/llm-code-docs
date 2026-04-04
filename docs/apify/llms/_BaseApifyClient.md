# Source: https://docs.apify.com/api/client/python/reference/class/_BaseApifyClient.md

# \_BaseApifyClient<!-- -->

### Hierarchy

* *\_BaseApifyClient*

  * [ApifyClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClient.md)
  * [ApifyClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/ApifyClientAsync.md)

## Index[**](#Index)

### Methods

* [**\_\_init\_\_](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseApifyClient.md#__init__)

### Properties

* [**http\_client](https://docs.apify.com/api/client/python/api/client/python/reference/class/_BaseApifyClient.md#http_client)

## Methods<!-- -->[**](#Methods)

### [**](#__init__)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/client.py#L62)\_\_init\_\_

* ****\_\_init\_\_**(token, \*, api\_url, api\_public\_url, max\_retries, min\_delay\_between\_retries\_millis, timeout\_secs): None

- Initialize a new instance.

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

## Properties<!-- -->[**](#Properties)

### [**](#http_client)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/client.py#L60)http\_client

**http\_client: [HTTPClient](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClient.md) | [HTTPClientAsync](https://docs.apify.com/api/client/python/api/client/python/reference/class/HTTPClientAsync.md)
