# Source: https://docs.apify.com/sdk/js/reference/interface/DatasetDataOptions.md

# externalDatasetDataOptions<!-- -->

## Index[**](#Index)

### Properties

* [**clean](#clean)
* [**desc](#desc)
* [**fields](#fields)
* [**limit](#limit)
* [**offset](#offset)
* [**skipEmpty](#skipEmpty)
* [**skipHidden](#skipHidden)
* [**unwind](#unwind)

## Properties<!-- -->[**](#Properties)

### [**](#clean)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L56)externaloptionalclean

**clean?

<!-- -->

: boolean = false

If `true` then the function returns only non-empty items and skips hidden fields (i.e. fields starting with `#` character). Note that the `clean` parameter is a shortcut for `skipHidden: true` and `skipEmpty: true` options.

### [**](#desc)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L41)externaloptionaldesc

**desc?

<!-- -->

: boolean = false

If `true` then the objects are sorted by `createdAt` in descending order. Otherwise they are sorted in ascending order.

### [**](#fields)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L45)externaloptionalfields

**fields?

<!-- -->

: string\[]

An array of field names that will be included in the result. If omitted, all fields are included in the results.

### [**](#limit)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L35)externaloptionallimit

**limit?

<!-- -->

: number = 250000

Maximum number of array elements to return.

### [**](#offset)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L30)externaloptionaloffset

**offset?

<!-- -->

: number = 0

Number of array elements that should be skipped at the start.

### [**](#skipEmpty)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L67)externaloptionalskipEmpty

**skipEmpty?

<!-- -->

: boolean = false

If `true` then the function doesn't return empty items. Note that in this case the returned number of items might be lower than limit parameter and pagination must be done using the `limit` value.

### [**](#skipHidden)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L61)externaloptionalskipHidden

**skipHidden?

<!-- -->

: boolean = false

If `true` then the function doesn't return hidden fields (fields starting with "#" character).

### [**](#unwind)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L50)externaloptionalunwind

**unwind?

<!-- -->

: string

Specifies a name of the field in the result objects that will be used to unwind the resulting objects. By default, the results are returned as they are.
