# Source: https://docs.apify.com/sdk/js/reference/interface/MetamorphOptions.md

# MetamorphOptions<!-- -->

## Index[**](#Index)

### Properties

* [**build](#build)
* [**contentType](#contentType)

## Properties<!-- -->[**](#Properties)

### [**](#build)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1959)optionalbuild

**build?

<!-- -->

: string

Tag or number of the target Actor build to metamorph into (e.g. `beta` or `1.2.345`). If not provided, the run uses build tag or number from the default Actor run configuration (typically `latest`).

### [**](#contentType)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1953)optionalcontentType

**contentType?

<!-- -->

: string

Content type for the `input`. If not specified, `input` is expected to be an object that will be stringified to JSON and content type set to `application/json; charset=utf-8`. If `options.contentType` is specified, then `input` must be a `String` or `Buffer`.
