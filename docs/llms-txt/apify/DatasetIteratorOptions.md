# Source: https://docs.apify.com/sdk/js/reference/interface/DatasetIteratorOptions.md

# externalDatasetIteratorOptions<!-- -->

### Hierarchy

* Omit<[DatasetDataOptions](https://docs.apify.com/sdk/js/sdk/js/reference/interface/DatasetDataOptions.md), offset | limit | clean | skipHidden | skipEmpty>
  * *DatasetIteratorOptions*

## Index[**](#Index)

### Properties

* [**desc](#desc)
* [**fields](#fields)
* [**unwind](#unwind)

## Properties<!-- -->[**](#Properties)

### [**](#desc)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L41)externaloptionalinheriteddesc

**desc?

<!-- -->

: boolean = false

Inherited from Omit.desc

If `true` then the objects are sorted by `createdAt` in descending order. Otherwise they are sorted in ascending order.

### [**](#fields)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L45)externaloptionalinheritedfields

**fields?

<!-- -->

: string\[]

Inherited from Omit.fields

An array of field names that will be included in the result. If omitted, all fields are included in the results.

### [**](#unwind)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/@crawlee/core/storages/dataset.d.ts#L50)externaloptionalinheritedunwind

**unwind?

<!-- -->

: string

Inherited from Omit.unwind

Specifies a name of the field in the result objects that will be used to unwind the resulting objects. By default, the results are returned as they are.
