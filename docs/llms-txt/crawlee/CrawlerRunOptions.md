# Source: https://crawlee.dev/js/api/basic-crawler/interface/CrawlerRunOptions.md

# CrawlerRunOptions<!-- -->

### Hierarchy

* [CrawlerAddRequestsOptions](https://crawlee.dev/js/api/basic-crawler/interface/CrawlerAddRequestsOptions.md)
  * *CrawlerRunOptions*

## Index[**](#Index)

### Properties

* [**batchSize](#batchSize)
* [**forefront](#forefront)
* [**purgeRequestQueue](#purgeRequestQueue)
* [**waitBetweenBatchesMillis](#waitBetweenBatchesMillis)
* [**waitForAllRequestsToBeAdded](#waitForAllRequestsToBeAdded)

## Properties<!-- -->[**](#Properties)

### [**](#batchSize)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L977)optionalinheritedbatchSize

**batchSize?

<!-- -->

: number = 1000

Inherited from CrawlerAddRequestsOptions.batchSize

### [**](#forefront)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L950)optionalinheritedforefront

**forefront?

<!-- -->

: boolean = false

Inherited from CrawlerAddRequestsOptions.forefront

If set to `true`:

* while adding the request to the queue: the request will be added to the foremost position in the queue.
* while reclaiming the request: the request will be placed to the beginning of the queue, so that it's returned in the next call to [RequestQueue.fetchNextRequest](https://crawlee.dev/js/api/core/class/RequestQueue.md#fetchNextRequest). By default, it's put to the end of the queue.

In case the request is already present in the queue, this option has no effect.

If more requests are added with this option at once, their order in the following `fetchNextRequest` call is arbitrary.

### [**](#purgeRequestQueue)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/basic-crawler/src/internals/basic-crawler.ts#L2121)optionalpurgeRequestQueue

**purgeRequestQueue?

<!-- -->

: boolean = true

Whether to purge the RequestQueue before running the crawler again. Defaults to true, so it is possible to reprocess failed requests. When disabled, only new requests will be considered. Note that even a failed request is considered as handled.

### [**](#waitBetweenBatchesMillis)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L982)optionalinheritedwaitBetweenBatchesMillis

**waitBetweenBatchesMillis?

<!-- -->

: number = 1000

Inherited from CrawlerAddRequestsOptions.waitBetweenBatchesMillis

### [**](#waitForAllRequestsToBeAdded)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L972)optionalinheritedwaitForAllRequestsToBeAdded

**waitForAllRequestsToBeAdded?

<!-- -->

: boolean = false

Inherited from CrawlerAddRequestsOptions.waitForAllRequestsToBeAdded

Whether to wait for all the provided requests to be added, instead of waiting just for the initial batch of up to `batchSize`.
