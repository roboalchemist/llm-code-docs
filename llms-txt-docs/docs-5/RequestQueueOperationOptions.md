# Source: https://docs.apify.com/sdk/js/reference/interface/RequestQueueOperationOptions.md

# externalRequestQueueOperationOptions<!-- -->

## Index[**](#Index)

### Properties

* [**forefront](#forefront)

## Properties<!-- -->[**](#Properties)

### [**](#forefront)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/request_provider.d.ts#L256)externaloptionalforefront

**forefront?

<!-- -->

: boolean = false

If set to `true`:

* while adding the request to the queue: the request will be added to the foremost position in the queue.
* while reclaiming the request: the request will be placed to the beginning of the queue, so that it's returned in the next call to [RequestQueue.fetchNextRequest](https://docs.apify.com/sdk/js/sdk/js/reference/class/RequestQueue.md#fetchNextRequest). By default, it's put to the end of the queue.

In case the request is already present in the queue, this option has no effect.

If more requests are added with this option at once, their order in the following `fetchNextRequest` call is arbitrary.
