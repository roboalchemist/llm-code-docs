# Source: https://docs.apify.com/api/client/js/reference/interface/RequestQueueClientListAndLockHeadResult.md

# RequestQueueClientListAndLockHeadResult<!-- -->

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

### [**](#clientKey)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L625)clientKey

**clientKey: string

### [**](#hadMultipleClients)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L596)inheritedhadMultipleClients

**hadMultipleClients: boolean

Inherited from RequestQueueClientListHeadResult.hadMultipleClients

### [**](#items)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L597)inheriteditems

**items: [RequestQueueClientListItem](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListItem.md)\[]

Inherited from RequestQueueClientListHeadResult.items

### [**](#limit)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L594)inheritedlimit

**limit: number

Inherited from RequestQueueClientListHeadResult.limit

### [**](#lockSecs)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L623)lockSecs

**lockSecs: number

### [**](#queueHasLockedRequests)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L624)queueHasLockedRequests

**queueHasLockedRequests: boolean

### [**](#queueModifiedAt)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/request_queue.ts#L595)inheritedqueueModifiedAt

**queueModifiedAt: Date

Inherited from RequestQueueClientListHeadResult.queueModifiedAt
