# Source: https://docs.apify.com/sdk/python/reference/class/AddRequestsResponse.md

# AddRequestsResponse<!-- -->

Model for a response to add requests to a queue.

Contains detailed information about the processing results when adding multiple requests to a queue. This includes which requests were successfully processed and which ones encountered issues during processing.

## Index[**](#Index)

### Properties

* [**model\_config](https://docs.apify.com/sdk/python/sdk/python/reference/class/AddRequestsResponse.md#model_config)
* [**processed\_requests](https://docs.apify.com/sdk/python/sdk/python/reference/class/AddRequestsResponse.md#processed_requests)
* [**unprocessed\_requests](https://docs.apify.com/sdk/python/sdk/python/reference/class/AddRequestsResponse.md#unprocessed_requests)

## Properties<!-- -->[**](#Properties)

### [**](#model_config)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L168)model\_config

**model\_config: Undefined

### [**](#processed_requests)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L170)processed\_requests

**processed\_requests: list\[[ProcessedRequest](https://crawlee.dev/python/api/class/ProcessedRequest)]

Successfully processed requests, including information about whether they were already present in the queue and whether they had been handled previously.

### [**](#unprocessed_requests)[**](https://github.com/apify/crawlee-python/blob/4b41e9719dcea4247ee874e5950c51d60de7e647//src/crawlee/storage_clients/models.py#L174)unprocessed\_requests

**unprocessed\_requests: list\[[UnprocessedRequest](https://crawlee.dev/python/api/class/UnprocessedRequest)]

Requests that could not be processed, typically due to validation errors or other issues.
