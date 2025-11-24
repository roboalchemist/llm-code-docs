# Source: https://docs.apify.com/sdk/js/reference/interface/CallOptions.md

# CallOptions<!-- -->

### Hierarchy

* ActorCallOptions
  * *CallOptions*

## Index[**](#Index)

### Properties

* [**build](#build)
* [**contentType](#contentType)
* [**maxItems](#maxItems)
* [**memory](#memory)
* [**timeout](#timeout)
* [**token](#token)
* [**waitSecs](#waitSecs)
* [**webhooks](#webhooks)

## Properties<!-- -->[**](#Properties)

### [**](#build)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/apify-client/src/resource_clients/actor.d.ts#L137)externaloptionalinheritedbuild

**build?

<!-- -->

: string

Inherited from ActorCallOptions.build

Tag or number of the actor build to run (e.g. `beta` or `1.2.345`). If not provided, the run uses build tag or number from the default actor run configuration (typically `latest`).

### [**](#contentType)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/apify-client/src/resource_clients/actor.d.ts#L144)externaloptionalinheritedcontentType

**contentType?

<!-- -->

: string

Inherited from ActorCallOptions.contentType

Content type for the `input`. If not specified, `input` is expected to be an object that will be stringified to JSON and content type set to `application/json; charset=utf-8`. If `options.contentType` is specified, then `input` must be a `String` or `Buffer`.

### [**](#maxItems)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/apify-client/src/resource_clients/actor.d.ts#L173)externaloptionalinheritedmaxItems

**maxItems?

<!-- -->

: number

Inherited from ActorCallOptions.maxItems

Specifies maximum number of items that the actor run should return. This is used by pay per result actors to limit the maximum number of results that will be charged to customer. Value can be accessed in actor run using `ACTOR_MAX_PAID_DATASET_ITEMS` environment variable.

### [**](#memory)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/apify-client/src/resource_clients/actor.d.ts#L149)externaloptionalinheritedmemory

**memory?

<!-- -->

: number

Inherited from ActorCallOptions.memory

Memory in megabytes which will be allocated for the new actor run. If not provided, the run uses memory of the default actor run configuration.

### [**](#timeout)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/apify-client/src/resource_clients/actor.d.ts#L154)externaloptionalinheritedtimeout

**timeout?

<!-- -->

: number

Inherited from ActorCallOptions.timeout

Timeout for the actor run in seconds. Zero value means there is no timeout. If not provided, the run uses timeout of the default actor run configuration.

### [**](#token)[**](https://github.com/apify/apify-sdk-js/blob/master/packages/apify/src/actor.ts#L1895)optionaltoken

**token?

<!-- -->

: string

User API token that is used to run the Actor. By default, it is taken from the `APIFY_TOKEN` environment variable.

### [**](#waitSecs)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/apify-client/src/resource_clients/actor.d.ts#L176)externaloptionalinheritedwaitSecs

**waitSecs?

<!-- -->

: number

Inherited from ActorCallOptions.waitSecs

### [**](#webhooks)[**](https://undefined/apify/apify-sdk-js/blob/master/node_modules/apify-client/src/resource_clients/actor.d.ts#L167)externaloptionalinheritedwebhooks

**webhooks?

<!-- -->

: readonly

<!-- -->

WebhookUpdateData\[]

Inherited from ActorCallOptions.webhooks

Specifies optional webhooks associated with the actor run, which can be used to receive a notification e.g. when the actor finished or failed, see [ad hook webhooks documentation](https://docs.apify.com/webhooks/ad-hoc-webhooks) for detailed description.
