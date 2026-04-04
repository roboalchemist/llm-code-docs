# Source: https://docs.apify.com/api/client/js/reference/interface/RequestQueueClientListAndLockHeadResult.md

# RequestQueueClientListAndLockHeadResult<!-- -->

Result of listing and locking requests from the queue head.

Extends [RequestQueueClientListHeadResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListHeadResult.md) with lock information.

### Hierarchy

* [RequestQueueClientListHeadResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListHeadResult.md)
  * *RequestQueueClientListAndLockHeadResult*

## Index[**](#Index)

### Properties

* [**clientKey](#clientKey)
* [**hadMultipleClients](#hadMultipleClients)
* [**items](#items)
* [**limit](#limit)
* [**lockSecs](#lockSecs)
* [**queueHasLockedRequests](#queueHasLockedRequests)
* [**queueModifiedAt](#queueModifiedAt)

## Properties<!-- -->[**](#Properties)

### [**](#clientKey)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L906)clientKey

**clientKey: string

### [**](#hadMultipleClients)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L859)inheritedhadMultipleClients

**hadMultipleClients: boolean

Inherited from RequestQueueClientListHeadResult.hadMultipleClients

### [**](#items)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L860)inheriteditems

**items: [RequestQueueClientListItem](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListItem.md)\[]

Inherited from RequestQueueClientListHeadResult.items

### [**](#limit)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L857)inheritedlimit

**limit: number

Inherited from RequestQueueClientListHeadResult.limit

### [**](#lockSecs)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L904)lockSecs

**lockSecs: number

### [**](#queueHasLockedRequests)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L905)queueHasLockedRequests

**queueHasLockedRequests: boolean

### [**](#queueModifiedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L858)inheritedqueueModifiedAt

**queueModifiedAt: Date

Inherited from RequestQueueClientListHeadResult.queueModifiedAt
