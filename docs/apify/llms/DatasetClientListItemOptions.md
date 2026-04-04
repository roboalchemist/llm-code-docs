# Source: https://docs.apify.com/api/client/js/reference/interface/DatasetClientListItemOptions.md

# DatasetClientListItemOptions<!-- -->

Options for listing items from a dataset.

Provides various filtering, pagination, and transformation options to customize the output format and content of retrieved items.

### Hierarchy

* PaginationOptions

  * *DatasetClientListItemOptions*

    * [DatasetClientCreateItemsUrlOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetClientCreateItemsUrlOptions.md)
    * [DatasetClientDownloadItemsOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetClientDownloadItemsOptions.md)

## Index[**](#Index)

### Properties

* [**chunkSize](#chunkSize)
* [**clean](#clean)
* [**desc](#desc)
* [**fields](#fields)
* [**flatten](#flatten)
* [**limit](#limit)
* [**offset](#offset)
* [**omit](#omit)
* [**signature](#signature)
* [**skipEmpty](#skipEmpty)
* [**skipHidden](#skipHidden)
* [**unwind](#unwind)
* [**view](#view)

## Properties<!-- -->[**](#Properties)

### [**](#chunkSize)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L258)optionalinheritedchunkSize

**chunkSize?

<!-- -->

: number

Inherited from PaginationOptions.chunkSize

Maximum number of items returned in one API response. Relevant in the context of asyncIterator, the iterator will fetch results in chunks of this size from API and yield them one by one. It will stop fetching once the limit is reached or once all items from API have been fetched.

Chunk size is usually limited by API. Minimum of those two limits will be used.

### [**](#clean)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L460)optionalclean

**clean?

<!-- -->

: boolean

### [**](#desc)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L461)optionaldesc

**desc?

<!-- -->

: boolean

### [**](#fields)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L463)optionalfields

**fields?

<!-- -->

: string\[]

### [**](#flatten)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L462)optionalflatten

**flatten?

<!-- -->

: string\[]

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

### [**](#omit)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L464)optionalomit

**omit?

<!-- -->

: string\[]

### [**](#signature)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L469)optionalsignature

**signature?

<!-- -->

: string

### [**](#skipEmpty)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L465)optionalskipEmpty

**skipEmpty?

<!-- -->

: boolean

### [**](#skipHidden)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L466)optionalskipHidden

**skipHidden?

<!-- -->

: boolean

### [**](#unwind)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L467)optionalunwind

**unwind?

<!-- -->

: string | string\[]

### [**](#view)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L468)optionalview

**view?

<!-- -->

: string
