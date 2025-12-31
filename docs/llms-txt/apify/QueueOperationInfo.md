# Source: https://docs.apify.com/sdk/js/reference/interface/QueueOperationInfo.md

# externalQueueOperationInfo<!-- -->

A helper class that is used to report results from various [RequestQueue](https://docs.apify.com/sdk/js/sdk/js/reference/class/RequestQueue.md) functions as well as enqueueLinks.

## Index[**](#Index)

### Properties

* [**requestId](#requestId)
* [**wasAlreadyHandled](#wasAlreadyHandled)
* [**wasAlreadyPresent](#wasAlreadyPresent)

## Properties<!-- -->[**](#Properties)

### [**](#requestId)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/types/storages.d.ts#L12)externalrequestId

**requestId: string

The ID of the added request

### [**](#wasAlreadyHandled)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/types/storages.d.ts#L10)externalwasAlreadyHandled

**wasAlreadyHandled: boolean

Indicates if request was already marked as handled.

### [**](#wasAlreadyPresent)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/types/storages.d.ts#L8)externalwasAlreadyPresent

**wasAlreadyPresent: boolean

Indicates if request was already present in the queue.
