# Source: https://docs.apify.com/sdk/python/reference/class/RequestQueueHead.md

# RequestQueueHead<!-- -->

Model for request queue head.

Represents a collection of requests retrieved from the beginning of a queue, including metadata about the queue's state and lock information for the requests.

## Index[**](#Index)

### Properties

* [**had\_multiple\_clients](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueHead.md#had_multiple_clients)
* [**items](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueHead.md#items)
* [**limit](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueHead.md#limit)
* [**lock\_time](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueHead.md#lock_time)
* [**model\_config](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueHead.md#model_config)
* [**queue\_has\_locked\_requests](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueHead.md#queue_has_locked_requests)
* [**queue\_modified\_at](https://docs.apify.com/sdk/python/sdk/python/reference/class/RequestQueueHead.md#queue_modified_at)

## Properties<!-- -->[**](#Properties)

### [**](#had_multiple_clients)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_models.py#L47)had\_multiple\_clients

**had\_multiple\_clients: bool

Indicates whether the queue has been accessed by multiple clients (consumers).

### [**](#items)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_models.py#L59)items

**items: list\[Request]

The list of request objects retrieved from the beginning of the queue.

### [**](#limit)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_models.py#L44)limit

**limit: int | None

The maximum number of requests that were requested from the queue.

### [**](#lock_time)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_models.py#L53)lock\_time

**lock\_time: timedelta | None

The duration for which the returned requests are locked and cannot be processed by other clients.

### [**](#model_config)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_models.py#L42)model\_config

**model\_config: Undefined

### [**](#queue_has_locked_requests)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_models.py#L56)queue\_has\_locked\_requests

**queue\_has\_locked\_requests: bool | None

Indicates whether the queue contains any locked requests.

### [**](#queue_modified_at)[**](https://github.com/apify/apify-sdk-python/blob/a01870a180ed391b8b6cad8d1894f12bcc879136//src/apify/storage_clients/_apify/_models.py#L50)queue\_modified\_at

**queue\_modified\_at: datetime

The timestamp when the queue was last modified.
