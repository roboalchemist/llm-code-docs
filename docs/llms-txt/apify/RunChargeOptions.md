# Source: https://docs.apify.com/api/client/js/reference/interface/RunChargeOptions.md

# RunChargeOptions<!-- -->

Options for charging events in a pay-per-event Actor run.

## Index[**](#Index)

### Properties

* [**count](#count)
* [**eventName](#eventName)
* [**idempotencyKey](#idempotencyKey)

## Properties<!-- -->[**](#Properties)

### [**](#count)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L531)optionalcount

**count?

<!-- -->

: number

Defaults to 1

### [**](#eventName)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L529)eventName

**eventName: string

Name of the event to charge. Must be defined in the Actor's pricing info else the API will throw.

### [**](#idempotencyKey)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/run.ts#L533)optionalidempotencyKey

**idempotencyKey?

<!-- -->

: string

Defaults to runId-eventName-timestamp
