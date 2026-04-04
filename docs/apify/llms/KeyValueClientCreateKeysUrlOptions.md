# Source: https://docs.apify.com/api/client/js/reference/interface/KeyValueClientCreateKeysUrlOptions.md

# KeyValueClientCreateKeysUrlOptions<!-- -->

Options for creating a public URL to list keys in a Key-Value Store.

Extends [KeyValueClientListKeysOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueClientListKeysOptions.md) with URL expiration control.

### Hierarchy

* [KeyValueClientListKeysOptions](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueClientListKeysOptions.md)
  * *KeyValueClientCreateKeysUrlOptions*

## Index[**](#Index)

### Properties

* [**collection](#collection)
* [**exclusiveStartKey](#exclusiveStartKey)
* [**expiresInSecs](#expiresInSecs)
* [**limit](#limit)
* [**prefix](#prefix)
* [**signature](#signature)

## Properties<!-- -->[**](#Properties)

### [**](#collection)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L558)optionalinheritedcollection

**collection?

<!-- -->

: string

Inherited from KeyValueClientListKeysOptions.collection

### [**](#exclusiveStartKey)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L557)optionalinheritedexclusiveStartKey

**exclusiveStartKey?

<!-- -->

: string

Inherited from KeyValueClientListKeysOptions.exclusiveStartKey

### [**](#expiresInSecs)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L569)optionalexpiresInSecs

**expiresInSecs?

<!-- -->

: number

### [**](#limit)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L556)optionalinheritedlimit

**limit?

<!-- -->

: number

Inherited from KeyValueClientListKeysOptions.limit

### [**](#prefix)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L559)optionalinheritedprefix

**prefix?

<!-- -->

: string

Inherited from KeyValueClientListKeysOptions.prefix

### [**](#signature)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L560)optionalinheritedsignature

**signature?

<!-- -->

: string

Inherited from KeyValueClientListKeysOptions.signature
