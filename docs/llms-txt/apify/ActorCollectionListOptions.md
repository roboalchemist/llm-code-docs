# Source: https://docs.apify.com/api/client/js/reference/interface/ActorCollectionListOptions.md

# ActorCollectionListOptions<!-- -->

### Hierarchy

* PaginationOptions
  * *ActorCollectionListOptions*

## Index[**](#Index)

### Properties

* [**chunkSize](#chunkSize)
* [**desc](#desc)
* [**limit](#limit)
* [**my](#my)
* [**offset](#offset)
* [**sortBy](#sortBy)

## Properties<!-- -->[**](#Properties)

### [**](#chunkSize)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L258)optionalinheritedchunkSize

**chunkSize?

<!-- -->

: number

Inherited from PaginationOptions.chunkSize

Maximum number of items returned in one API response. Relevant in the context of asyncIterator, the iterator will fetch results in chunks of this size from API and yield them one by one. It will stop fetching once the limit is reached or once all items from API have been fetched.

Chunk size is usually limited by API. Minimum of those two limits will be used.

### [**](#desc)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_collection.ts#L99)optionaldesc

**desc?

<!-- -->

: boolean

### [**](#limit)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L251)optionalinheritedlimit

**limit?

<!-- -->

: number

Inherited from PaginationOptions.limit

Maximum number of entries requested.

### [**](#my)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_collection.ts#L98)optionalmy

**my?

<!-- -->

: boolean

### [**](#offset)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L249)optionalinheritedoffset

**offset?

<!-- -->

: number

Inherited from PaginationOptions.offset

Position of the first returned entry.

### [**](#sortBy)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor_collection.ts#L100)optionalsortBy

**sortBy?

<!-- -->

: [ActorListSortBy](https://docs.apify.com/api/client/js/api/client/js/reference/enum/ActorListSortBy.md)
