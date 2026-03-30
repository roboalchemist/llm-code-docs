# Source: https://crawlee.dev/js/api/core/interface/QueueOperationInfo.md

# QueueOperationInfo<!-- -->

A helper class that is used to report results from various [RequestQueue](https://crawlee.dev/js/api/core/class/RequestQueue.md) functions as well as enqueueLinks.

## Index[**](#Index)

### Properties

* [**requestId](#requestId)
* [**wasAlreadyHandled](#wasAlreadyHandled)
* [**wasAlreadyPresent](#wasAlreadyPresent)

## Properties<!-- -->[**](#Properties)

### [**](#requestId)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L15)requestId

**requestId: string

The ID of the added request

### [**](#wasAlreadyHandled)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L12)wasAlreadyHandled

**wasAlreadyHandled: boolean

Indicates if request was already marked as handled.

### [**](#wasAlreadyPresent)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L9)wasAlreadyPresent

**wasAlreadyPresent: boolean

Indicates if request was already present in the queue.
