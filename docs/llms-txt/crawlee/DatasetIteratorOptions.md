# Source: https://crawlee.dev/js/api/core/interface/DatasetIteratorOptions.md

# DatasetIteratorOptions<!-- -->

### Hierarchy

* Omit<[DatasetDataOptions](https://crawlee.dev/js/api/core/interface/DatasetDataOptions.md), offset | limit | clean | skipHidden | skipEmpty>
  * *DatasetIteratorOptions*

## Index[**](#Index)

### Properties

* [**desc](#desc)
* [**fields](#fields)
* [**unwind](#unwind)

## Properties<!-- -->[**](#Properties)

### [**](#desc)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L110)optionalinheriteddesc

**desc?

<!-- -->

: boolean = false

Inherited from Omit.desc

If `true` then the objects are sorted by `createdAt` in descending order. Otherwise they are sorted in ascending order.

### [**](#fields)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L115)optionalinheritedfields

**fields?

<!-- -->

: string\[]

Inherited from Omit.fields

An array of field names that will be included in the result. If omitted, all fields are included in the results.

### [**](#unwind)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/dataset.ts#L121)optionalinheritedunwind

**unwind?

<!-- -->

: string

Inherited from Omit.unwind

Specifies a name of the field in the result objects that will be used to unwind the resulting objects. By default, the results are returned as they are.
