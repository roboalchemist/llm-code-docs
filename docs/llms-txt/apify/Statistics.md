# Source: https://docs.apify.com/api/client/python/reference/class/Statistics.md

# Statistics<!-- -->

Statistics about API client usage and rate limit errors.

## Index[**](#Index)

### Methods

* [**add\_rate\_limit\_error](https://docs.apify.com/api/client/python/api/client/python/reference/class/Statistics.md#add_rate_limit_error)

### Properties

* [**calls](https://docs.apify.com/api/client/python/api/client/python/reference/class/Statistics.md#calls)
* [**rate\_limit\_errors](https://docs.apify.com/api/client/python/api/client/python/reference/class/Statistics.md#rate_limit_errors)
* [**requests](https://docs.apify.com/api/client/python/api/client/python/reference/class/Statistics.md#requests)

## Methods<!-- -->[**](#Methods)

### [**](#add_rate_limit_error)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/_statistics.py#L18)add\_rate\_limit\_error

* ****add\_rate\_limit\_error**(attempt): None

- Add rate limit error for specific attempt.

  ***

  #### Parameters

  * ##### attempt: int

    The attempt number (1-based indexing).

  #### Returns None

## Properties<!-- -->[**](#Properties)

### [**](#calls)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/_statistics.py#L9)calls

**calls: int

Total number of API method calls made by the client.

### [**](#rate_limit_errors)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/_statistics.py#L15)rate\_limit\_errors

**rate\_limit\_errors: defaultdict\[int, int]

List tracking which retry attempts encountered rate limit (429) errors.

### [**](#requests)[**](https://undefined/apify/apify-client-python/blob/master//src/apify_client/_statistics.py#L12)requests

**requests: int

Total number of HTTP requests sent, including retries.
