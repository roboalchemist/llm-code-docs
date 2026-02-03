# Source: https://docs.apify.com/api/client/js/reference/interface/StoreCollectionListOptions.md

# StoreCollectionListOptions<!-- -->

### Hierarchy

* PaginationOptions
  * *StoreCollectionListOptions*

## Index[**](#Index)

### Properties

* [**category](#category)
* [**chunkSize](#chunkSize)
* [**limit](#limit)
* [**offset](#offset)
* [**pricingModel](#pricingModel)
* [**search](#search)
* [**sortBy](#sortBy)
* [**username](#username)

## Properties<!-- -->[**](#Properties)

### [**](#category)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/store_collection.ts#L97)optionalcategory

**category?

<!-- -->

: string

### [**](#chunkSize)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L258)optionalinheritedchunkSize

**chunkSize?

<!-- -->

: number

Inherited from PaginationOptions.chunkSize

Maximum number of items returned in one API response. Relevant in the context of asyncIterator, the iterator will fetch results in chunks of this size from API and yield them one by one. It will stop fetching once the limit is reached or once all items from API have been fetched.

Chunk size is usually limited by API. Minimum of those two limits will be used.

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

### [**](#pricingModel)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/store_collection.ts#L99)optionalpricingModel

**pricingModel?

<!-- -->

: string

### [**](#search)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/store_collection.ts#L95)optionalsearch

**search?

<!-- -->

: string

### [**](#sortBy)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/store_collection.ts#L96)optionalsortBy

**sortBy?

<!-- -->

: string

### [**](#username)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/store_collection.ts#L98)optionalusername

**username?

<!-- -->

: string
