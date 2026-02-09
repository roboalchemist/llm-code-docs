# Source: https://docs.apify.com/api/client/python/reference/class/BatchAddRequestsResult.md

# BatchAddRequestsResult<!-- -->

Result of the batch add requests operation.

## Index[**](#Index)

### Properties

* [**processedRequests](https://docs.apify.com/api/client/python/api/client/python/reference/class/BatchAddRequestsResult.md#processedRequests)
* [**unprocessedRequests](https://docs.apify.com/api/client/python/api/client/python/reference/class/BatchAddRequestsResult.md#unprocessedRequests)

## Properties<!-- -->[**](#Properties)

### [**](#processedRequests)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/request_queue.py#L44)processedRequests

**processedRequests: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict]

List of successfully added requests.

### [**](#unprocessedRequests)[**](https://undefined/apify/apify-client-python/blob/25ff4e51e07fe25d1d338b042eacba1ec0c63e84//src/apify_client/clients/resource_clients/request_queue.py#L45)unprocessedRequests

**unprocessedRequests: [list](https://docs.apify.com/api/client/python/api/client/python/reference/class/RequestQueueCollectionClient.md#list)\[dict]

List of requests that failed to be added.
