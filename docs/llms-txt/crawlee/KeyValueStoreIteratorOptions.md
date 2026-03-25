# Source: https://crawlee.dev/js/api/core/interface/KeyValueStoreIteratorOptions.md

# KeyValueStoreIteratorOptions<!-- -->

## Index[**](#Index)

### Properties

* [**collection](#collection)
* [**exclusiveStartKey](#exclusiveStartKey)
* [**prefix](#prefix)

## Properties<!-- -->[**](#Properties)

### [**](#collection)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L860)optionalcollection

**collection?

<!-- -->

: string

Collection name to use for listing keys.

### [**](#exclusiveStartKey)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L852)optionalexclusiveStartKey

**exclusiveStartKey?

<!-- -->

: string

All keys up to this one (including) are skipped from the result.

### [**](#prefix)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L856)optionalprefix

**prefix?

<!-- -->

: string

If set, only keys that start with this prefix are returned.
