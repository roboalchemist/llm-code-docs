# Source: https://crawlee.dev/js/api/types/interface/ListAndLockHeadResult.md

# ListAndLockHeadResult<!-- -->

### Hierarchy

* [QueueHead](https://crawlee.dev/js/api/types/interface/QueueHead.md)
  * *ListAndLockHeadResult*

## Index[**](#Index)

### Properties

* [**hadMultipleClients](#hadMultipleClients)
* [**items](#items)
* [**limit](#limit)
* [**lockSecs](#lockSecs)
* [**queueHasLockedRequests](#queueHasLockedRequests)
* [**queueModifiedAt](#queueModifiedAt)

## Properties<!-- -->[**](#Properties)

### [**](#hadMultipleClients)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L228)optionalinheritedhadMultipleClients

**hadMultipleClients?

<!-- -->

: boolean

Inherited from QueueHead.hadMultipleClients

### [**](#items)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L229)inheriteditems

**items: [RequestQueueHeadItem](https://crawlee.dev/js/api/types/interface/RequestQueueHeadItem.md)\[]

Inherited from QueueHead.items

### [**](#limit)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L226)inheritedlimit

**limit: number

Inherited from QueueHead.limit

### [**](#lockSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L244)lockSecs

**lockSecs: number

### [**](#queueHasLockedRequests)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L245)optionalqueueHasLockedRequests

**queueHasLockedRequests?

<!-- -->

: boolean

### [**](#queueModifiedAt)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L227)inheritedqueueModifiedAt

**queueModifiedAt: Date

Inherited from QueueHead.queueModifiedAt
