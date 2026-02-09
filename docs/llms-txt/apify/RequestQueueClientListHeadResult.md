# Source: https://docs.apify.com/api/client/js/reference/interface/RequestQueueClientListHeadResult.md

# RequestQueueClientListHeadResult<!-- -->

Result of listing requests from the queue head.

### Hierarchy

* *RequestQueueClientListHeadResult*
  * [RequestQueueClientListAndLockHeadResult](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListAndLockHeadResult.md)

## Index[**](#Index)

### Properties

* [**hadMultipleClients](#hadMultipleClients)
* [**items](#items)
* [**limit](#limit)
* [**queueModifiedAt](#queueModifiedAt)

## Properties<!-- -->[**](#Properties)

### [**](#hadMultipleClients)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L859)hadMultipleClients

**hadMultipleClients: boolean

### [**](#items)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L860)items

**items: [RequestQueueClientListItem](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueClientListItem.md)\[]

### [**](#limit)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L857)limit

**limit: number

### [**](#queueModifiedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L858)queueModifiedAt

**queueModifiedAt: Date
