# Source: https://crawlee.dev/js/api/core/interface/RequestQueueOperationOptions.md

# RequestQueueOperationOptions<!-- -->

### Hierarchy

* *RequestQueueOperationOptions*

  * [EnqueueLinksOptions](https://crawlee.dev/js/api/core/interface/EnqueueLinksOptions.md)
  * [AddRequestsBatchedOptions](https://crawlee.dev/js/api/core/interface/AddRequestsBatchedOptions.md)

## Index[**](#Index)

### Properties

* [**forefront](#forefront)

## Properties<!-- -->[**](#Properties)

### [**](#forefront)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/request_provider.ts#L950)optionalforefront

**forefront?

<!-- -->

: boolean = false

If set to `true`:

* while adding the request to the queue: the request will be added to the foremost position in the queue.
* while reclaiming the request: the request will be placed to the beginning of the queue, so that it's returned in the next call to [RequestQueue.fetchNextRequest](https://crawlee.dev/js/api/core/class/RequestQueue.md#fetchNextRequest). By default, it's put to the end of the queue.

In case the request is already present in the queue, this option has no effect.

If more requests are added with this option at once, their order in the following `fetchNextRequest` call is arbitrary.
