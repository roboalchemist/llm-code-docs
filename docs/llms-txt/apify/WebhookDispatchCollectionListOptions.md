# Source: https://docs.apify.com/api/client/js/reference/interface/WebhookDispatchCollectionListOptions.md

# WebhookDispatchCollectionListOptions<!-- -->

### Hierarchy

* PaginationOptions
  * *WebhookDispatchCollectionListOptions*

## Index[**](#Index)

### Properties

* [**chunkSize](#chunkSize)
* [**desc](#desc)
* [**limit](#limit)
* [**offset](#offset)

## Properties<!-- -->[**](#Properties)

### [**](#chunkSize)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L258)optionalinheritedchunkSize

**chunkSize?

<!-- -->

: number

Inherited from PaginationOptions.chunkSize

Maximum number of items returned in one API response. Relevant in the context of asyncIterator, the iterator will fetch results in chunks of this size from API and yield them one by one. It will stop fetching once the limit is reached or once all items from API have been fetched.

Chunk size is usually limited by API. Minimum of those two limits will be used.

### [**](#desc)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/webhook_dispatch_collection.ts#L72)optionaldesc

**desc?

<!-- -->

: boolean

### [**](#limit)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L251)optionalinheritedlimit

**limit?

<!-- -->

: number

Inherited from PaginationOptions.limit

Maximum number of entries requested.

### [**](#offset)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L249)optionalinheritedoffset

**offset?

<!-- -->

: number

Inherited from PaginationOptions.offset

Position of the first returned entry.
