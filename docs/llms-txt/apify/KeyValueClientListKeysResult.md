# Source: https://docs.apify.com/api/client/js/reference/interface/KeyValueClientListKeysResult.md

# KeyValueClientListKeysResult<!-- -->

Result of listing keys in a Key-Value Store.

Contains paginated list of keys with metadata and pagination information.

## Index[**](#Index)

### Properties

* [**count](#count)
* [**exclusiveStartKey](#exclusiveStartKey)
* [**isTruncated](#isTruncated)
* [**items](#items)
* [**limit](#limit)
* [**nextExclusiveStartKey](#nextExclusiveStartKey)

## Properties<!-- -->[**](#Properties)

### [**](#count)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L578)count

**count: number

### [**](#exclusiveStartKey)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L580)exclusiveStartKey

**exclusiveStartKey: string

### [**](#isTruncated)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L581)isTruncated

**isTruncated: boolean

### [**](#items)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L583)items

**items: [KeyValueListItem](https://docs.apify.com/api/client/js/api/client/js/reference/interface/KeyValueListItem.md)\[]

### [**](#limit)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L579)limit

**limit: number

### [**](#nextExclusiveStartKey)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/key_value_store.ts#L582)nextExclusiveStartKey

**nextExclusiveStartKey: string
