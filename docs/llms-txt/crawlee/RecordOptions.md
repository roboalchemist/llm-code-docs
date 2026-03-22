# Source: https://crawlee.dev/js/api/core/interface/RecordOptions.md

# RecordOptions<!-- -->

## Index[**](#Index)

### Properties

* [**contentType](#contentType)
* [**doNotRetryTimeouts](#doNotRetryTimeouts)
* [**timeoutSecs](#timeoutSecs)

## Properties<!-- -->[**](#Properties)

### [**](#contentType)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L835)optionalcontentType

**contentType?

<!-- -->

: string

Specifies a custom MIME content type of the record.

### [**](#doNotRetryTimeouts)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L845)optionaldoNotRetryTimeouts

**doNotRetryTimeouts?

<!-- -->

: boolean

If set to `true`, the `set-record` API call will not be retried if it times out.

### [**](#timeoutSecs)[**](https://github.com/apify/crawlee/blob/e6451749f838744d539c81bf9d969c1cfcc9e86b/packages/core/src/storages/key_value_store.ts#L840)optionaltimeoutSecs

**timeoutSecs?

<!-- -->

: number

Specifies a custom timeout for the `set-record` API call, in seconds.
