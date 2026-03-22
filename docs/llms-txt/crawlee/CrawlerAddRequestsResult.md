# Source: https://crawlee.dev/js/api/basic-crawler/interface/CrawlerAddRequestsResult.md

# CrawlerAddRequestsResult<!-- -->

### Hierarchy

* [AddRequestsBatchedResult](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedResult.md)
  * *CrawlerAddRequestsResult*

## Index[**](#Index)

### Properties

* [**addedRequests](#addedRequests)
* [**waitForAllRequestsToBeAdded](#waitForAllRequestsToBeAdded)

## Properties<!-- -->[**](#Properties)

### [**](#addedRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L986)inheritedaddedRequests

**addedRequests: [ProcessedRequest](https://crawlee.dev/js/api/types/interface/ProcessedRequest.md)\[]

Inherited from AddRequestsBatchedResult.addedRequests

### [**](#waitForAllRequestsToBeAdded)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L1003)inheritedwaitForAllRequestsToBeAdded

**waitForAllRequestsToBeAdded: Promise<[ProcessedRequest](https://crawlee.dev/js/api/types/interface/ProcessedRequest.md)\[]>

Inherited from AddRequestsBatchedResult.waitForAllRequestsToBeAdded

A promise which will resolve with the rest of the requests that were added to the queue.

Alternatively, we can set [`waitForAllRequestsToBeAdded`](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedOptions.md#waitForAllRequestsToBeAdded) to `true` in the [`crawler.addRequests()`](https://crawlee.dev/js/api/basic-crawler/class/BasicCrawler.md#addRequests) options.

**Example:**

```
// Assuming `requests` is a list of requests.
const result = await crawler.addRequests(requests);

// If we want to wait for the rest of the requests to be added to the queue:
await result.waitForAllRequestsToBeAdded;
```
