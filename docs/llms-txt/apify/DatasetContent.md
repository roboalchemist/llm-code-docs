# Source: https://docs.apify.com/sdk/js/reference/interface/DatasetContent.md

# externalDatasetContent<!-- --> \<Data>

## Index[**](#Index)

### Properties

* [**count](#count)
* [**desc](#desc)
* [**items](#items)
* [**limit](#limit)
* [**offset](#offset)
* [**total](#total)

## Properties<!-- -->[**](#Properties)

### [**](#count)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L420)externalcount

**count: number

Count of dataset entries returned in this set.

### [**](#desc)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L428)externaloptionaldesc

**desc?

<!-- -->

: boolean

Should the results be in descending order.

### [**](#items)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L426)externalitems

**items: Data\[]

Dataset entries based on chosen format parameter.

### [**](#limit)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L424)externallimit

**limit: number

Maximum number of dataset entries requested.

### [**](#offset)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L422)externaloffset

**offset: number

Position of the first returned entry in the dataset.

### [**](#total)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L418)externaltotal

**total: number

Total count of entries in the dataset.
