# Source: https://docs.apify.com/api/client/js/reference/interface/ActorStandby.md

# ActorStandby<!-- -->

Configuration for Actor standby mode.

Standby mode keeps Actor containers warm and ready to process requests with minimal latency. This is useful for Actors that need to respond quickly to incoming requests.

## Index[**](#Index)

### Properties

* [**build](#build)
* [**desiredRequestsPerActorRun](#desiredRequestsPerActorRun)
* [**disableStandbyFieldsOverride](#disableStandbyFieldsOverride)
* [**idleTimeoutSecs](#idleTimeoutSecs)
* [**maxRequestsPerActorRun](#maxRequestsPerActorRun)
* [**memoryMbytes](#memoryMbytes)
* [**shouldPassActorInput](#shouldPassActorInput)

## Properties<!-- -->[**](#Properties)

### [**](#build)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L580)optionalbuild

**build?

<!-- -->

: string

### [**](#desiredRequestsPerActorRun)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L581)optionaldesiredRequestsPerActorRun

**desiredRequestsPerActorRun?

<!-- -->

: number

### [**](#disableStandbyFieldsOverride)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L582)optionaldisableStandbyFieldsOverride

**disableStandbyFieldsOverride?

<!-- -->

: boolean

### [**](#idleTimeoutSecs)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L583)optionalidleTimeoutSecs

**idleTimeoutSecs?

<!-- -->

: number

### [**](#maxRequestsPerActorRun)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L584)optionalmaxRequestsPerActorRun

**maxRequestsPerActorRun?

<!-- -->

: number

### [**](#memoryMbytes)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L585)optionalmemoryMbytes

**memoryMbytes?

<!-- -->

: number

### [**](#shouldPassActorInput)[**](https://github.com/apify/apify-client-js/blob/a8a29bacd7df19373e3300fc059110221bc37e09/src/resource_clients/actor.ts#L586)optionalshouldPassActorInput

**shouldPassActorInput?

<!-- -->

: boolean
