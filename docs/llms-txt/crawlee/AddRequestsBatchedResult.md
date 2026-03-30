# Source: https://crawlee.dev/js/api/core/interface/AddRequestsBatchedResult.md

# AddRequestsBatchedResult<!-- -->

### Hierarchy

* *AddRequestsBatchedResult*
  * [CrawlerAddRequestsResult](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerAddRequestsResult.md)

## Index[**](#Index)

### Properties

* [**addedRequests](#addedRequests)
* [**waitForAllRequestsToBeAdded](#waitForAllRequestsToBeAdded)

## Properties<!-- -->[**](#Properties)

### [**](#addedRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L986)addedRequests

**addedRequests: [ProcessedRequest](https://crawlee.dev/js/api/types/interface/ProcessedRequest.md)\[]

### [**](#waitForAllRequestsToBeAdded)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L1003)waitForAllRequestsToBeAdded

**waitForAllRequestsToBeAdded: Promise<[ProcessedRequest](https://crawlee.dev/js/api/types/interface/ProcessedRequest.md)\[]>

A promise which will resolve with the rest of the requests that were added to the queue.

Alternatively, we can set [`waitForAllRequestsToBeAdded`](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedOptions.md#waitForAllRequestsToBeAdded) to `true` in the [`crawler.addRequests()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#addRequests) options.

**Example:**

```
// Assuming `requests` is a list of requests.
const result = await crawler.addRequests(requests);

// If we want to wait for the rest of the requests to be added to the queue:
await result.waitForAllRequestsToBeAdded;
```
