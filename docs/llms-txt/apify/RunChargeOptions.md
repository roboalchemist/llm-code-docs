# Source: https://docs.apify.com/api/client/js/reference/interface/RunChargeOptions.md

# RunChargeOptions<!-- -->

## Index[**](#Index)

### Properties

* [**count](#count)
* [**eventName](#eventName)
* [**idempotencyKey](#idempotencyKey)

## Properties<!-- -->[**](#Properties)

### [**](#count)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L302)optionalcount

**count?

<!-- -->

: number

Defaults to 1

### [**](#eventName)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L300)eventName

**eventName: string

Name of the event to charge. Must be defined in the Actor's pricing info else the API will throw.

### [**](#idempotencyKey)[**](https://github.com/apify/apify-client-js/blob/master/src/resource_clients/run.ts#L304)optionalidempotencyKey

**idempotencyKey?

<!-- -->

: string

Defaults to runId-eventName-timestamp
