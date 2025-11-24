# Source: https://docs.apify.com/sdk/js/reference/interface/OpenStorageOptions.md

# OpenStorageOptions<!-- -->

## Index[**](#Index)

### Properties

* [**forceCloud](#forceCloud)

## Properties<!-- -->[**](#Properties)

### [**](#forceCloud)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1990)optionalforceCloud

**forceCloud?

<!-- -->

: boolean = false

If set to `true` then the cloud storage is used even if the `CRAWLEE_STORAGE_DIR` environment variable is set. This way it is possible to combine local and cloud storage.
