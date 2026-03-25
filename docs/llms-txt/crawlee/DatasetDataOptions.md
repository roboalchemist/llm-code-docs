# Source: https://crawlee.dev/js/api/core/interface/DatasetDataOptions.md

# DatasetDataOptions<!-- -->

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

### [**](#clean)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L128)optionalclean

**clean?

<!-- -->

: boolean = false

If `true` then the function returns only non-empty items and skips hidden fields (i.e. fields starting with `#` character). Note that the `clean` parameter is a shortcut for `skipHidden: true` and `skipEmpty: true` options.

### [**](#desc)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L110)optionaldesc

**desc?

<!-- -->

: boolean = false

If `true` then the objects are sorted by `createdAt` in descending order. Otherwise they are sorted in ascending order.

### [**](#fields)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L115)optionalfields

**fields?

<!-- -->

: string\[]

An array of field names that will be included in the result. If omitted, all fields are included in the results.

### [**](#limit)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L103)optionallimit

**limit?

<!-- -->

: number = 250000

Maximum number of array elements to return.

### [**](#offset)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L97)optionaloffset

**offset?

<!-- -->

: number = 0

Number of array elements that should be skipped at the start.

### [**](#skipEmpty)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L141)optionalskipEmpty

**skipEmpty?

<!-- -->

: boolean = false

If `true` then the function doesn't return empty items. Note that in this case the returned number of items might be lower than limit parameter and pagination must be done using the `limit` value.

### [**](#skipHidden)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L134)optionalskipHidden

**skipHidden?

<!-- -->

: boolean = false

If `true` then the function doesn't return hidden fields (fields starting with "#" character).

### [**](#unwind)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L121)optionalunwind

**unwind?

<!-- -->

: string

Specifies a name of the field in the result objects that will be used to unwind the resulting objects. By default, the results are returned as they are.
