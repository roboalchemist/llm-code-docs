# Source: https://docs.apify.com/api/client/js/reference/interface/DatasetClientDownloadItemsOptions.md

# DatasetClientDownloadItemsOptions<!-- -->

Options for downloading dataset items in a specific format.

Extends [DatasetClientListItemOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetClientListItemOptions.md) with format-specific options.

### Hierarchy

* [DatasetClientListItemOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/DatasetClientListItemOptions.md)
  * *DatasetClientDownloadItemsOptions*

## Index[**](#Index)

### Properties

* [**attachment](#attachment)
* [**bom](#bom)
* [**chunkSize](#chunkSize)
* [**clean](#clean)
* [**delimiter](#delimiter)
* [**desc](#desc)
* [**fields](#fields)
* [**flatten](#flatten)
* [**limit](#limit)
* [**offset](#offset)
* [**omit](#omit)
* [**signature](#signature)
* [**skipEmpty](#skipEmpty)
* [**skipHeaderRow](#skipHeaderRow)
* [**skipHidden](#skipHidden)
* [**unwind](#unwind)
* [**view](#view)
* [**xmlRoot](#xmlRoot)
* [**xmlRow](#xmlRow)

## Properties<!-- -->[**](#Properties)

### [**](#attachment)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L502)optionalattachment

**attachment?

<!-- -->

: boolean

### [**](#bom)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L503)optionalbom

**bom?

<!-- -->

: boolean

### [**](#chunkSize)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L258)optionalinheritedchunkSize

**chunkSize?

<!-- -->

: number

Inherited from DatasetClientListItemOptions.chunkSize

Maximum number of items returned in one API response. Relevant in the context of asyncIterator, the iterator will fetch results in chunks of this size from API and yield them one by one. It will stop fetching once the limit is reached or once all items from API have been fetched.

Chunk size is usually limited by API. Minimum of those two limits will be used.

### [**](#clean)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L460)optionalinheritedclean

**clean?

<!-- -->

: boolean

Inherited from DatasetClientListItemOptions.clean

### [**](#delimiter)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L504)optionaldelimiter

**delimiter?

<!-- -->

: string

### [**](#desc)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L461)optionalinheriteddesc

**desc?

<!-- -->

: boolean

Inherited from DatasetClientListItemOptions.desc

### [**](#fields)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L463)optionalinheritedfields

**fields?

<!-- -->

: string\[]

Inherited from DatasetClientListItemOptions.fields

### [**](#flatten)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L462)optionalinheritedflatten

**flatten?

<!-- -->

: string\[]

Inherited from DatasetClientListItemOptions.flatten

### [**](#limit)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L251)optionalinheritedlimit

**limit?

<!-- -->

: number

Inherited from DatasetClientListItemOptions.limit

Maximum number of entries requested.

### [**](#offset)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/utils.ts#L249)optionalinheritedoffset

**offset?

<!-- -->

: number

Inherited from DatasetClientListItemOptions.offset

Position of the first returned entry.

### [**](#omit)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L464)optionalinheritedomit

**omit?

<!-- -->

: string\[]

Inherited from DatasetClientListItemOptions.omit

### [**](#signature)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L469)optionalinheritedsignature

**signature?

<!-- -->

: string

Inherited from DatasetClientListItemOptions.signature

### [**](#skipEmpty)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L465)optionalinheritedskipEmpty

**skipEmpty?

<!-- -->

: boolean

Inherited from DatasetClientListItemOptions.skipEmpty

### [**](#skipHeaderRow)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L505)optionalskipHeaderRow

**skipHeaderRow?

<!-- -->

: boolean

### [**](#skipHidden)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L466)optionalinheritedskipHidden

**skipHidden?

<!-- -->

: boolean

Inherited from DatasetClientListItemOptions.skipHidden

### [**](#unwind)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L467)optionalinheritedunwind

**unwind?

<!-- -->

: string | string\[]

Inherited from DatasetClientListItemOptions.unwind

### [**](#view)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L468)optionalinheritedview

**view?

<!-- -->

: string

Inherited from DatasetClientListItemOptions.view

### [**](#xmlRoot)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L506)optionalxmlRoot

**xmlRoot?

<!-- -->

: string

### [**](#xmlRow)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/dataset.ts#L507)optionalxmlRow

**xmlRow?

<!-- -->

: string
