# Source: https://crawlee.dev/js/api/types/interface/PaginatedList.md

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

### [**](#count)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L34)count

**count: number

Count of dataset entries returned in this set.

### [**](#desc)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L40)optionaldesc

**desc?

<!-- -->

: boolean

Should the results be in descending order.

### [**](#items)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L42)items

**items: Data\[]

Dataset entries based on chosen format parameter.

### [**](#limit)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L38)limit

**limit: number

Maximum number of dataset entries requested.

### [**](#offset)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L36)offset

**offset: number

Position of the first returned entry in the dataset.

### [**](#total)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/types/src/storages.ts#L32)total

**total: number

Total count of entries in the dataset.
