# Source: https://docs.apify.com/sdk/python/reference/class/RequestQueue.md

# Source: https://docs.apify.com/sdk/js/reference/class/RequestQueue.md

# Source: https://docs.apify.com/api/client/js/reference/interface/RequestQueue.md

# RequestQueue<!-- -->

Represents a Request Queue storage on the Apify platform.

Request queues store URLs (requests) to be processed by web crawlers. They provide automatic deduplication, request locking for parallel processing, and persistence.

## Index[**](#Index)

### Properties

* [**accessedAt](#accessedAt)
* [**actId](#actId)
* [**actRunId](#actRunId)
* [**createdAt](#createdAt)
* [**expireAt](#expireAt)
* [**generalAccess](#generalAccess)
* [**hadMultipleClients](#hadMultipleClients)
* [**handledRequestCount](#handledRequestCount)
* [**id](#id)
* [**modifiedAt](#modifiedAt)
* [**name](#name)
* [**pendingRequestCount](#pendingRequestCount)
* [**stats](#stats)
* [**title](#title)
* [**totalRequestCount](#totalRequestCount)
* [**userId](#userId)
* [**username](#username)

## Properties<!-- -->[**](#Properties)

### [**](#accessedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L814)accessedAt

**accessedAt: Date

### [**](#actId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L819)optionalactId

**actId?

<!-- -->

: string

### [**](#actRunId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L820)optionalactRunId

**actRunId?

<!-- -->

: string

### [**](#createdAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L812)createdAt

**createdAt: Date

### [**](#expireAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L815)optionalexpireAt

**expireAt?

<!-- -->

: string

### [**](#generalAccess)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L823)optionalgeneralAccess

**generalAccess?

<!-- -->

: null | STORAGE\_GENERAL\_ACCESS

### [**](#hadMultipleClients)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L821)hadMultipleClients

**hadMultipleClients: boolean

### [**](#handledRequestCount)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L817)handledRequestCount

**handledRequestCount: number

### [**](#id)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L807)id

**id: string

### [**](#modifiedAt)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L813)modifiedAt

**modifiedAt: Date

### [**](#name)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L808)optionalname

**name?

<!-- -->

: string

### [**](#pendingRequestCount)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L818)pendingRequestCount

**pendingRequestCount: number

### [**](#stats)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L822)stats

**stats: [RequestQueueStats](https://docs.apify.com/api/client/js/api/client/js/reference/interface/RequestQueueStats.md)

### [**](#title)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L809)optionaltitle

**title?

<!-- -->

: string

### [**](#totalRequestCount)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L816)totalRequestCount

**totalRequestCount: number

### [**](#userId)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L810)userId

**userId: string

### [**](#username)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/request_queue.ts#L811)optionalusername

**username?

<!-- -->

: string
