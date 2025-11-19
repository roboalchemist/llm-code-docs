# Source: https://docs.apify.com/api/client/js/reference/interface/PaginatedList.md

# PaginatedList<!-- --> \<Data>

## Index[**](#Index)

### Properties

* [**count](#count)
* [**desc](#desc)
* [**items](#items)
* [**limit](#limit)
* [**offset](#offset)
* [**total](#total)

## Properties<!-- -->[**](#Properties)

### [**](#count)[**](https://github.com/apify/apify-client-js/blob/master/src/utils.ts#L237)count

**count: number

Count of dataset entries returned in this set.

### [**](#desc)[**](https://github.com/apify/apify-client-js/blob/master/src/utils.ts#L243)desc

**desc: boolean

Should the results be in descending order.

### [**](#items)[**](https://github.com/apify/apify-client-js/blob/master/src/utils.ts#L245)items

**items: Data\[]

Dataset entries based on chosen format parameter.

### [**](#limit)[**](https://github.com/apify/apify-client-js/blob/master/src/utils.ts#L241)limit

**limit: number

Maximum number of dataset entries requested.

### [**](#offset)[**](https://github.com/apify/apify-client-js/blob/master/src/utils.ts#L239)offset

**offset: number

Position of the first returned entry in the dataset.

### [**](#total)[**](https://github.com/apify/apify-client-js/blob/master/src/utils.ts#L235)total

**total: number

Total count of entries in the dataset.
