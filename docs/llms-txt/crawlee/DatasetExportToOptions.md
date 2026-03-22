# Source: https://crawlee.dev/js/api/core/interface/DatasetExportToOptions.md

# DatasetExportToOptions<!-- -->

### Hierarchy

* [DatasetExportOptions](https://crawlee.dev/js/api/core/interface/DatasetExportOptions.md)
  * *DatasetExportToOptions*

## Index[**](#Index)

### Properties

* [**clean](#clean)
* [**collectAllKeys](#collectAllKeys)
* [**desc](#desc)
* [**fields](#fields)
* [**fromDataset](#fromDataset)
* [**skipEmpty](#skipEmpty)
* [**skipHidden](#skipHidden)
* [**toKVS](#toKVS)
* [**unwind](#unwind)

## Properties<!-- -->[**](#Properties)

### [**](#clean)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L128)optionalinheritedclean

**clean?

<!-- -->

: boolean = false

Inherited from DatasetExportOptions.clean

If `true` then the function returns only non-empty items and skips hidden fields (i.e. fields starting with `#` character). Note that the `clean` parameter is a shortcut for `skipHidden: true` and `skipEmpty: true` options.

### [**](#collectAllKeys)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L149)optionalinheritedcollectAllKeys

**collectAllKeys?

<!-- -->

: boolean

Inherited from DatasetExportOptions.collectAllKeys

If true, includes all unique keys from all dataset items in the CSV export header. If omitted or false, only keys from the first item are used.

### [**](#desc)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L110)optionalinheriteddesc

**desc?

<!-- -->

: boolean = false

Inherited from DatasetExportOptions.desc

If `true` then the objects are sorted by `createdAt` in descending order. Otherwise they are sorted in ascending order.

### [**](#fields)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L115)optionalinheritedfields

**fields?

<!-- -->

: string\[]

Inherited from DatasetExportOptions.fields

An array of field names that will be included in the result. If omitted, all fields are included in the results.

### [**](#fromDataset)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L177)optionalfromDataset

**fromDataset?

<!-- -->

: string

### [**](#skipEmpty)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L141)optionalinheritedskipEmpty

**skipEmpty?

<!-- -->

: boolean = false

Inherited from DatasetExportOptions.skipEmpty

If `true` then the function doesn't return empty items. Note that in this case the returned number of items might be lower than limit parameter and pagination must be done using the `limit` value.

### [**](#skipHidden)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L134)optionalinheritedskipHidden

**skipHidden?

<!-- -->

: boolean = false

Inherited from DatasetExportOptions.skipHidden

If `true` then the function doesn't return hidden fields (fields starting with "#" character).

### [**](#toKVS)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L178)optionaltoKVS

**toKVS?

<!-- -->

: string

### [**](#unwind)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L121)optionalinheritedunwind

**unwind?

<!-- -->

: string

Inherited from DatasetExportOptions.unwind

Specifies a name of the field in the result objects that will be used to unwind the resulting objects. By default, the results are returned as they are.
